## Scrapy 

Scrapy is an application framework for crawling web sites and extracting structured data which can be used for a wide range of useful applications, like data mining, information processing or historical archival.

## Scrapy Features

requests are scheduled and processed asynchronously. This means that Scrapy doesn’t need to wait for a request to be finished and processed, it can send another request or do other things in the meantime. This also means that other requests can keep going even if some request fails or an error happens while handling it.

Scrapy also gives you control over the politeness of the crawl through a few settings. You can do things like setting a download delay between each request, limiting amount of concurrent requests per domain or per IP, and even using an auto-throttling extension that tries to figure out these automatically.

Built-in support for generating feed exports in multiple formats (JSON, CSV, XML) and storing them in multiple backends (FTP, S3, local filesystem) CSS and Xpath to extract data from html

An interactive shell console (IPython aware) for trying out the CSS and XPath expressions to scrape data, very useful when writing or debugging your spiders. 

Strong extensibility support, allowing you to plug in your own functionality using signals and a well-defined
API (middlewares, extensions, and pipelines).

Wide range of built-in extensions and middlewares for handling: cookies and session handling; HTTP features like compression, authentication, caching; user-agent spoofing; robots.txt; crawl depth restrict;

A Telnet console for hooking into a Python console running inside your Scrapy process, to introspect and debug your crawler

Plus other goodies like reusable spiders to crawl sites from Sitemaps and XML/CSV feeds, a media pipeline
for automatically downloading images (or any other media) associated with the scraped items, a caching DNS resolver, and much more!

## Spider Structure

They must subclass scrapy.Spider and define the initial requests to make, optionally how to follow links in the pages, and how to parse the downloaded page content to extract data

The parse() method usually parses the response, extracting the scraped data as dicts and also finding new
URLs to follow and creating new requests (Request) from them.

The best way to learn how to extract data with Scrapy is trying selectors using the shell Scrapy shell

1. You start by generating the initial Requests to crawl the first URLs, and specify a callback function to be called with the response downloaded from those requests
2. In the callback function, you parse the response (web page) and return either dicts with extracted data, Item objects, Request objects, or an iterable of these objects. Those Requests will also contain a callback (maybe the same) and will then be downloaded by Scrapy and then their response handled by the specified callback
3. Finally, the items returned from the spider will be typically persisted to a database (in some Item Pipeline) or written to a file using Feed exports

## Following Links

What you see here is Scrapy’s mechanism of following links: when you yield a Request in a callback method, Scrapy will schedule that request to be sent and register a callback method to be executed when that request finishes.

Using this, you can build complex crawlers that follow links according to rules you define, and extract different kinds of data depending on the page it’s visiting.

As yet another example spider that leverages the mechanism of following links, check out the CrawlSpider class for a generic spider that implements a small rules engine that you can use to write your crawlers on top of it.

By default, Scrapy filters out duplicated requests to URLs already visited, avoiding the problem of hitting servers too much because of a programming mistake. This can be configured by the setting DUPEFILTER_CLASS

In some cases you may be interested in passing arguments to those callback functions so you can receive the arguments later, in the second callback. You can use the Request.meta attribute for that.

### Link Extractors

Link extractors are objects whose only purpose is to extract links from web pages

The only public method that every link extractor has is extract_links, which receives a Response object and returns a list of scrapy.link.Link objects. Link extractors are meant to be instantiated once and their extract_links method called several times with different responses to extract links to follow.

Built-in link extractors is from scrapy.linkextractors import LinkExtractor

## Extracting Data

```
# selector list object
response.css()
# selector list object
response.xpath()
# extract
response.xpath().extract()
response.xpath().extract_first()
response.xpath().re(r'(\w+) to (\w+)')
```

A Scrapy spider typically generates many dictionaries containing the data extracted from the page. To do that, we use the yield Python keyword in the callback

## Arrange Data

### Item

The main goal in scraping is to extract structured data from unstructured sources, typically, web pages. Scrapy spiders can return the extracted data as Python dicts. While convenient and familiar, Python dicts lack structure: it is easy to make a typo in a field name or return inconsistent data, especially in a larger project with many spiders.

To define common output data format Scrapy provides the Item class. Item objects are simple containers used to collect the scraped data. They provide a dictionary-like API with a convenient syntax for declaring their available fields.

```
import scrapy
class Product(scrapy.Item):
  # Field objects are used to specify metadata for each field.
  name = scrapy.Field()
  price = scrapy.Field()
  stock = scrapy.Field()
  last_updated = scrapy.Field(serializer=str)

# instance
product = Product(name='Desktop PC', price=1000)
product = Product({'name': 'Laptop PC', 'price': 1500})
# access field
product.keys()
product.items()
product['name']
product.get('lala', 'unknown field')
# It’s important to note that the Field objects used to declare the item do not stay assigned as class attributes. Instead, they can be accessed through the Item.fields attribute
if 'last_updated' in product.fields
# set field
product['last_updated'] = 'today'
```

### ItemLoader

Item Loaders provide a convenient mechanism for populating scraped Items. Even though Items can be populated using their own dictionary-like API, Item Loaders provide a much more convenient API for populating them from a scraping process, by automating some common tasks like parsing the raw extracted data before assigning it.

In other words, Items provide the container of scraped data, while Item Loaders provide the mechanism for populating that container.

Item Loaders are designed to provide a flexible, efficient and easy mechanism for extending and overriding different field parsing rules, either by spider, or by source format (HTML, XML, etc) without becoming a nightmare to maintain.

you start collecting values into the Item Loader, typically using Selectors. You can add more than one value to the same item field; the Item Loader will know how to “join” those values later using a proper processing function.

```
from scrapy.loader import ItemLoader
from myproject.items import Product
def parse(self, response):
  l = ItemLoader(item=Product(), response=response)
  l.add_xpath('name', '//div[@class="product_name"]') # add name
  l.add_xpath('name', '//div[@class="product_title"]') # add name again
  l.add_xpath('price', '//p[@id="price"]')
  l.add_css('stock', 'p#stock]')
  l.add_value('last_updated', 'today') # you can also use literal values
  return l.load_item() # populate and return item
```

An Item Loader contains one input processor and one output processor for **each (item) field**. The input processor processes the extracted data as soon as it’s received (through the add_xpath(), add_css() or add_value() methods) and the result of the input processor is collected and kept inside the ItemLoader. 

After collecting all data, the ItemLoader.load_item() method is called to populate and get the populated Item object. That’s when the output processor is called with the data previously collected (and processed using the input processor). The result of the output processor is the final value that gets assigned to the item.

input/output processor are just callable objects, must accept only one positional argument, which will be an  iterator. the output of them can be anything, The result of input processors will be appended to an internal list (in the Loader) containing the collected values (for that field). The result of the output processors is the value that will be finally assigned to the item

```
# declare input/output processors in ItemLoader
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join
class ProductLoader(ItemLoader):
  default_output_processor = TakeFirst()
  name_in = MapCompose(unicode.title)
  name_out = Join()
  price_in = MapCompose(unicode.strip)
```

```
# declare input/output processors in Item Field
import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags
def filter_price(value):
if value.isdigit():
return value
class Product(scrapy.Item):
  name = scrapy.Field(
  input_processor=MapCompose(remove_tags),
  output_processor=Join(),
  )
  price = scrapy.Field(
  input_processor=MapCompose(remove_tags, filter_price),
  output_processor=TakeFirst(),
  )
```

The Item Loader Context is a dict of arbitrary key/values which is shared among all input and output processors in the Item Loader. It can be passed when declaring, instantiating or using Item Loader. They are used to modify the behaviour of the input/output processors.

```
# processor declare with loader_context argument
# so the Item Loader passes the currently active context when calling it
def parse_length(text, loader_context):
  unit = loader_context.get('unit', 'm')
  # ... length parsing code goes here ...
  return parsed_length
```

```
# set ItemLoader's context
loader = ItemLoader(product)
loader.context['unit'] = 'cm'
# or
loader = ItemLoader(product, unit='cm')
# or
class ProductLoader(ItemLoader):
  length_out = MapCompose(parse_length, unit='cm')
```

When parsing related values from a subsection of a document, it can be useful to create nested loaders

```
loader = ItemLoader(item=Item())
# load stuff not in the footer
footer_loader = loader.nested_xpath('//footer')
footer_loader.add_xpath('social', 'a[@class = "social"]/@href')
footer_loader.add_xpath('email', 'a[@class = "email"]/@href')
# no need to call footer_loader.load_item()
loader.load_item()
```

Item Loaders are designed to ease the maintenance burden of parsing rules, without losing flexibility and, at the same time, providing a convenient mechanism for extending and overriding them.

extending Item Loaders can be very helpful is when you have multiple source formats, for example
XML and HTML. In the XML version you may want to remove CDATA occurrences

```
from scrapy.loader.processors import MapCompose
from myproject.ItemLoaders import ProductLoader
from myproject.utils.xml import remove_cdata
class XmlProductLoader(ProductLoader):
  name_in = MapCompose(remove_cdata, ProductLoader.name_in)
```

As for output processors, it is more common to declare them in the field metadata, as they usually depend only on the field and not on each specific site parsing rule (as input processors do).

### built-in processors

scrapy.loader.processors.Identity

The simplest processor, which doesn’t do anything. It returns the original values unchanged

scrapy.loader.processors.TakeFirst

Returns the first non-null/non-empty value from the values received, so it’s typically used as an output processor to single-valued fields

scrapy.loader.processors.Join(separator=u’ ‘)

Returns the values joined with the separator given in the constructor

scrapy.loader.processors.Compose

A processor which is constructed from the composition of the given functions. This means that each input value of this processor is passed to the first function, and the result of that function is passed to the second function, and so on, until the last function returns the output value of this processor. By default, stop process on None value. This behaviour can be changed by passing keyword argument stop_on_none=False

input value for next function depend on current function's result

scrapy.loader.processors.MapCompose

A processor which is constructed from the composition of the given functions

The functions can also return None in which case the output of that function is ignored for further processing over the chain

Difference with Compose:
MapCompose: iterate input argument to apply function, and collect function result to construct a new iteratable to pass next function. This processor provides a convenient way to compose functions that only work with single values (instead of iterables).

```
from scrapy.loader.processors import Compose, MapCompose
proc1 = Compose(lambda v: v[0], str.upper)
proc1(['hello', 'world']) # HELLO

def filter_world(x):
    return None if x == 'world' else x
proc2 = MapCompose(filter_world, unicode.upper)
proc2([u'hello', u'world', u'this', u'is', u'scrapy']) # [u'HELLO, u'THIS', u'IS', u'SCRAPY']
```

scrapy.loader.processors.SelectJmes

```
# process json data
proc_json_list = Compose(json.loads, MapCompose(SelectJmes('foo')))
```

## Item Pipeline

After an item has been scraped by a spider, it is sent to the Item Pipeline which processes it through several components that are executed sequentially.

Each item pipeline component (sometimes referred as just “Item Pipeline”) is a Python class that implements a simple method. They receive an item and perform an action over it, also deciding if the item should continue through the pipeline or be dropped and no longer processed.

typical usage:

* cleansing HTML data
* validating scraped data (checking that the items contain certain fields)
* checking for duplicates(and droping them)
* storing the scraped item in a database

Each item pipeline component is a Python class that must implement process_item(self, item, spider) method

this method should return a dict with data, return an Item, raise scrapy.exceptions.DropItem exception

open_spider(self, spider)

This method is called when the spider is opened

close_spider(self, spider)

This method is called when the spider is closed

from_crawler(cls, crawler)

If present, this classmethod is called to create a pipeline instance from a Crawler. It must return a new instance of the pipeline. Crawler object provides access to all Scrapy core components like settings and signals; it is a way for pipeline to access them and hook its functionality into Scrapy

```
# validation and dropping
from scrapy.exceptions import DropItem
class PricePipeline(object):
	vat_factor = 1.15
	def process_item(self, item, spider):
		if item['price']:
			if item['price_excludes_vat']:
				item['price'] = item['price'] * self.vat_factor
			return item
		else:
			raise DropItem("Missing price in %s" % item)
```

```
# write items to a JSON file
# If you really want to store all scraped items into a JSON file you should use the Feed exports.
import json
class JsonWriterPipeline(object):
	def open_spider(self, spider):
		self.file = open('items.jl', 'wb')
	def close_spider(self, spider):
		self.file.close()
	def process_item(self, item, spider):
		line = json.dumps(dict(item)) + "\n"
		self.file.write(line)
		return item
```

```
# Write items to MongoDB
import pymongo
class MongoPipeline(object):
	collection_name = 'scrapy_items'
	def __init__(self, mongo_uri, mongo_db):
		self.mongo_uri = mongo_uri
		self.mongo_db = mongo_db
	@classmethod
	def from_crawler(cls, crawler):
		return cls(
			mongo_uri=crawler.settings.get('MONGO_URI'),
			mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
		)
	def open_spider(self, spider):
		self.client = pymongo.MongoClient(self.mongo_uri)
		self.db = self.client[self.mongo_db]
	def close_spider(self, spider):
		self.client.close()
	def process_item(self, item, spider):
		self.db[self.collection_name].insert(dict(item))
		return item
```

```
# deferred write screenshot filename into item
import scrapy
import hashlib
from urllib.parse import quote
class ScreenshotPipeline(object):
	"""Pipeline that uses Splash to render screenshot of every Scrapy item."""
	SPLASH_URL = "http://localhost:8050/render.png?url={}"
	def process_item(self, item, spider):
		encoded_item_url = quote(item["url"])
		screenshot_url = self.SPLASH_URL.format(encoded_item_url)
		request = scrapy.Request(screenshot_url)
		dfd = spider.crawler.engine.download(request, spider)
		dfd.addBoth(self.return_item, item)
		return dfd
	def return_item(self, response, item):
		if response.status != 200:
			# Error happened, return item.
			return item
		# Save screenshot to file, filename will be hash of url.
		url = item["url"]
		url_hash = hashlib.md5(url.encode("utf8")).hexdigest()
		filename = "{}.png".format(url_hash)
		with open(filename, "wb") as f:
			f.write(response.body)
		# Store filename in item.
		item["screenshot_filename"] = filename
		return item
```

```
# A filter that looks for duplicate items, and drops those items that were already processed.
from scrapy.exceptions import DorpItem
class DuplicatesPipeline(object):
	def __init__(self):
		self.ids_seen = set()
	def process_item(self, item, spider):
		if item['id'] in self.ids_seen:
			raise DropItem("Duplicate item found: %s" % item)
		else:
			self.ids_seen.add(item['id'])
		return item
```

To activate an Item Pipeline component you must add its class to the ITEM_PIPELINES setting, items go through from lower valued to higher valued classes. It’s customary to define these numbers in the 0-1000 range

## Storing Data& Feed Exports

One of the most frequently required features when implementing scrapers is being able to store the scraped data properly and, quite often, that means generating an “export file” with the scraped data (commonly called “export feed”) to be consumed by other systems.

Scrapy provides this functionality out of the box with the Feed Exports, which allows you to generate a feed with the scraped items, using multiple serialization formats and storage backends.

The simplest way to store the scraped data is by using Feed exports

```
# For historic reasons, Scrapy appends to a given file instead of overwriting its contents. If you run this command twice without removing the file before the second time, you’ll end up with a broken JSON file

scrapy crawl quotes -o quotes.json
# The JSON Lines format is useful because it’s stream-like, you can easily append new records to it. It doesn’t have the same problem of JSON when you run twice. Also, as each record is a separate line, you can process big files without having to fit everything in memory, there are tools like JQ https://stedolan.github.io/jq/ to help doing that at the command-line.

scrapy crawl quotes -o quotes.jl
```

In small projects (like the one in this tutorial), that should be enough. However, if you want to perform more complex things with the scraped items, you can write an Item Pipeline

### built-in serialization formats

json, json lines, xml, csv, pickle, marshal

### built-in storage backends 

Local filesystem, ftp, s3, standard output and so on

The feed exports supports multiple storage backend types which are defined by the URI scheme(FEED_URI)

```
# FEED_URI examples
# %(name)s -> will be replaced by spider name
# %(time)s -> will replaced by timestamp
# %(attrname)s -> will be replaced by spider.attrname
file:///tmp/export.csv
ftp://user:password@ftp.example.com/scraping/feeds/%(name)s/%(time)s.json
s3://mybucket/path/to/export.csv
```

### settings about feed exports

FEED_URI is required to enable feed export

FEED_FORMAT serialization format for the feed: json, jsonlines, xml, pickle, csv,marshal

FEED_EXPORT_ENCODING encoding for the feed

FEED_STORAGES 

FEED_EXPORTERS

## Request and Response

### request pass arguments into callback

```
def parse_page1(self, response):
	request = scrapy.Request('http://example.com', callback=self.parse_page2)
	request.meta['last_url'] = response.url
	yield request

def parse_page2(self, response):
	yield {
      	'last_url': response.meta['last_url']
	}
```

### catch exceptions in request processing

```
import scrapy
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError
class ErrbackSpider(scrapy.Spider):
    name = "errback_example"
    start_urls = [
      "http://www.httpbin.org/", # HTTP 200 expected
      "http://www.httpbin.org/status/404", # Not found error
      "http://www.httpbin.org/status/500", # server issue
      "http://www.httpbin.org:12345/", # non-responding host, timeout expected
      "http://www.httphttpbinbin.org/", # DNS error expected
    ]
    def start_requests(self):
    	for u in self.start_urls:
    		yield scrapy.Request(u, callback=self.parse_httpbin, errback=self.errback_httpbin, dont_filter=True)
    def parse_httpbin(self, response):
    	self.logger.info('Got successful response from {}'.format(response.url))
    	# do something useful here...
    def errback_httpbin(self, failure):
        # log all failures
        self.logger.error(repr(failure))
        # in case you want to do something special for some errors,
		# you may need the failure's type:
		if failure.check(HttpError):
			# these exceptions come from HttpError spider middleware
			# you can get the non-200 response
			response = failure.value.response
			self.logger.error('HttpError on %s', response.url)
		elif failure.check(DNSLookupError):
			# this is the original request
			request = failure.request
			self.logger.error('DNSLookupError on %s', request.url)
		elif failure.check(TimeoutError, TCPTimedOutError):
			request = failure.request
			self.logger.error('TimeoutError on %s', request.url)
```

### request.meta special keys

proxy, dont_retry, dont_redirect, and so on

### request subclass FromRequest

```
# Using FormRequest to send data via HTTP POST
return [FormRequest(url="http://www.example.com/post/action", formdata={'name': 'John Doe', 'age': '27'}, callback=self.after_post)]
```

```
# Using FormRequest.from_response() to simulate a user login
import scrapy
class LoginSpider(scrapy.Spider):
	name = 'example.com'
	start_urls = ['http://www.example.com/users/login.php']
	def parse(self, response):
		return scrapy.FormRequest.from_response(
			response,
			formdata={'username': 'john', 'password': 'secret'},
			callback=self.after_login)
	def after_login(self, response):
		# check login succeed before going on
		if "authentication failed" in response.body:
			self.logger.error("Login failed")
			return
```

## Control Spider

You can provide command line arguments to your spiders by using the -a option when running them

```
scrapy crawl quotes -o quotes-humor.json -a tag=humor
```

These arguments are passed to the Spider’s \__init__ method and become spider attributes by default. In this example, the value provided for the tag argument will be available via self.tag inside quotes spider, you can override \__init__ method to change this. The default \__init__ method will take any spider arguments and copy them to the spider as attributes

Keep in mind that spider arguments are only strings. The spider will not do any parsing on its own.

## Project Root Dir Difference

You use the scrapy tool from inside your projects to control and manage them

Some Scrapy commands (like crawl) must be run from inside a Scrapy project.

Also keep in mind that some commands may have slightly different behaviours when running them from inside projects. For example, the fetch command will use spider-overridden behaviours (such as the user_agent attribute to override the user-agent) if the url being fetched is associated with some specific spider. This is intentional, as the fetch command is meant to be used to check how spiders are downloading pages.

## Built-in Spiders

### scrapy.Spider

This is the simplest spider, and the one from which every other spider must inherit (including spiders that come bundled with Scrapy, as well as spiders that you write yourself). It doesn’t provide any special functionality. It just provides a default start_requests() implementation which sends requests from the start_urls spider attribute and calls the spider’s method parse for each of the resulting responses.

**attributes and methods**

name

A string which defines the name for this spider. The spider name is how the spider is located (and instantiated) by Scrapy, so it must be unique. If the spider scrapes a single domain, a common practice is to name the spider after the domain, with or without the TLD. So, for example, a spider that crawls mywebsite.com would often be called mywebsite

allowed_domains

An optional list of strings containing domains that this spider is allowed to crawl

start_urls

A list of URLs where the spider will begin to crawl from, when no particular URLs are specified

custom_settings

A dictionary of settings that will be overridden from the project wide configuration when running this
spider. It must be defined as a class attribute since the settings are updated before instantiation.

crawler

This attribute is set by the from_crawler() class method after initializating the class, and links to the
Crawler object to which this spider instance is bound.

settings

Configuration for running this spider after initializating the spider class. This is a Settings instance

logger

Python logger created with the Spider’s name.

from_crawler(crawler, *args, **kwargs)

This is the class method used by Scrapy to create your spiders. You probably won’t need to override this directly because the default implementation acts as a proxy to the \__init__() method, calling it with the given arguments args and named arguments kwargs.

start_requests()

This method must return an iterable with the first Requests to crawl for this spider.

make_requests_from_url(url)

A method that receives a URL and returns a Request object (or a list of Request objects) to scrape.

parse(response)

This is the default callback used by Scrapy to process downloaded responses, when their requests don’t
specify a callback.

closed(reason)

Called when the spider closes

### scrapy.spiders.CrawlSpider

This is the most commonly used spider for crawling regular websites, as it provides a convenient mechanism for following links by defining a set of rules. It may not be the best suited for your particular web sites or project, but it’s generic enough for several cases, so you can start from it and override it as needed for more custom functionality, or just implement your own spider.

**attributes and methods**

rules

Which is a list of one (or more) Rule objects. Each Rule defines a certain behaviour for crawling the
site. If multiple rules match the same link, the first one will be used

parse_start_url(response)

This method is called for the start_urls responses. It allows to parse the initial responses and must return
either an Item object, a Request object, or an iterable containing any of them.

```
class MySpider(CrawlSpider):
name = 'example.com'
allowed_domains = ['example.com']
start_urls = ['http://www.example.com']
rules = (
# Extract links matching 'category.php' (but not matching 'subsection.php')
# and follow links from them (since no callback means follow=True by default).
Rule(LinkExtractor(allow=('category\.php', ), deny=('subsection\.php', ))),
# Extract links matching 'item.php' and parse them with the spider's method parse_item
Rule(LinkExtractor(allow=('item\.php', )), callback='parse_item'),
)
```

###  scrapy.spiders.XMLFeedSpider

###  scrapy.spiders.CSVFeedSpider

### scrapy.spiders.SitemapSpider

## Downloading Files and Images

Scrapy provides reusable item pipelines for downloading files attached to a particular item. 

Both pipelines implement these features:

* Avoid re-downloading media that was downloaded recently
*  Specifying where to store the media (filesystem directory, Amazon S3 bucket)

The Images Pipeline has a few extra functions for processing images:

* Convert all downloaded images to a common format (JPG) and mode (RGB)
* Thumbnail generation
* Check images width/height to make sure they meet a minimum constraint

### FilesPipeline

1. in a spider, put the urls into item file_urls field
2. item is returned, and pass to item pipeline
3. item reach FilesPipeline, item['file_urls'] are scheduled for downloading
4. when files are downloaded, item['files'] will be populated with results. This field is a list of dict about downloaded files information, same order file_urls
5. you should declare file_urls and files field in your Item definition

override default fileds

```
FILES_URLS_FIELD = 'field_name_for_your_files_urls'
FILES_RESULT_FIELD = 'field_name_for_your_processed_files'
```

file expiration

```
# 120 days of delay for files expiration
FILES_EXPIRES = 120
```

### ImagesPipeline

put image urls into image_urls field, and image information populated into images field

The advantage of using the ImagesPipeline for image files is that you can configure some extra functions like generating thumbnails and filtering the images based on their size

The Images Pipeline uses Pillow for thumbnailing and normalizing images to JPEG/RGB format, so you need to install this library in order to use it

override fileds

```
IMAGES_URLS_FIELD = 'field_name_for_your_images_urls'
IMAGES_RESULT_FIELD = 'field_name_for_your_processed_images'
```

image expiration

```
# 30 days of delay for images expiration
IMAGES_EXPIRES = 30
```

Thumbnail generation for images

```
IMAGES_THUMBS = {
  'small': (50, 50),
  'big': (270, 270),
}
# image will be store into directory
<IMAGES_STORE>/full/<image_id>.jpg
<IMAGES_STORE>/thumbs/big/<image_id>.jpg
<IMAGES_STORE>/thumbs/small/<image_id>.jpg
```

Filtering out small images

```
IMAGES_MIN_HEIGHT = 110
IMAGES_MIN_WIDTH = 110
```

### Enabling media pipeline

```
# enable image pipeline
ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}
# enable file pipeline
ITEM_PIPELINES = {'scrapy.pipelines.files.FilesPipeline': 1}

# configure the target storage filesystem
FILES_STORE = '/path/to/valid/dir'
IMAGES_STORE = '/path/to/valid/dir'
# configure the target storage Amazon S3 bucket
IMAGES_STORE = 's3://bucket/images'
```

## Settings

### Settings precedence

1. Command line options (most precedence)

   ```
   scrapy crawl myspider -s LOG_FILE=scrapy.log
   scrapy crawl myspider --set LOG_FILE=scrapy.log
   ```

2. Settings per-spider

   ```
   class MySpider(scrapy.Spider):
       name = 'myspider'
       # class attributes custom_settings
       custom_settings = {
       'SOME_SETTING': 'some value',
       }
   ```

3. Project settings module, settings.py for your project

4. Default settings per-command

5. Default global settings (less precedence), scrapy.settings.default_settings

### Access settings

In a spider, the settings are available through self.settings. but settings attribute is set in the base Spider class after the spider is initialized. If you want to use the settings before the initialization (e.g., in your spider’s \__init__() method), you’ll need to override the from_crawler() method.

```
def parse(self, response):
  print("Existing settings: %s" % self.settings.attributes.keys())
```



Settings can be accessed through the scrapy.crawler.Crawler.settings attribute of the Crawler that is
passed to from_crawler method in extensions, middlewares and item pipelines.

```
class MyExtension(object):
    def __init__(self, log_is_enabled=False):
    	if log_is_enabled:
    		print("log is enabled!")
    @classmethod
    def from_crawler(cls, crawler):
    	settings = crawler.settings
    	return cls(settings.getbool('LOG_ENABLED'))
```

access settings by from scrapy.utils.project import get_project_settings

## Logging

LOG_FILE

LOG_LEVEL

```
# in a spider
self.logger.error()
self.logger.info()
```

## Send email

```
from scrapy.mail import MailSender
mailer = MailSender()
mailer.send(to=["someone@example.com"], subject="Some subject", body="Some body", cc=["another@example.com"])
```

MAIL_FROM

MAIL_PORT

MAIL_HOST

## Telnet console

Scrapy comes with a built-in telnet console for inspecting and controlling a Scrapy running process. The telnet console is just a regular python shell running inside the Scrapy process, so you can do literally anything from it.

## Debugging Spiders

myspider

```
import scrapy
from myproject.items import MyItem
class MySpider(scrapy.Spider):
	name = 'myspider'
    start_urls = (
    'http://example.com/page1',
    'http://example.com/page2',
    )
	def parse(self, response):
		# collect `item_urls`
		for item_url in item_urls:
			yield scrapy.Request(item_url, self.parse_item)
	def parse_item(self, response):
        item = MyItem()
        # populate `item` fields
        # and extract item_details_url
        yield scrapy.Request(item_details_url, self.parse_details, meta={'item': item})
    def parse_details(self, response):
        item = response.meta['item']
        # populate more
```

parse command

```
scrapy parse --spider=myspider -c parse_item -d 2 --verbose <item_url>
```

invoke scrapy shell in the spider

```
def parse_details(self, response):
    item = response.meta.get('item', None)
    if item:
    	# populate more `item` fields
    	return item
    else:
    	scrapy.shell.inspect_response(response, self)
```

open in browser

```
def parse_details(self, response):
	if "item name" not in response.body:
		scrapy.utils.response.open_in_browser(response)
```

loggine

```
def parse_details(self, response):
	if "item name" not in response.body:
		self.logger.warning('No item received for %s', response.url)
```

## AutoThrottle

This is an extension for automatically throttling crawling speed based on load of both the Scrapy server and the website you are crawling

Design goals

1. be nicer to sites instead of using default download delay of zero
2. automatically adjust scrapy to the optimum crawling speed, so the user doesn’t have to tune the download delays to find the optimum one. The user only needs to specify the maximum concurrent requests it allows, and the extension does the rest.

## Deploy spiders

Running Scrapy spiders in your local machine is very convenient for the (early) development stage, but not so much when you need to execute long-running spiders or move spiders to run in production continuously

Popular choices for deploying Scrapy spiders are: Scrapyd, Scrapy Cloud

## Crawl Jobs

Sometimes, for big sites, it’s desirable to pause crawls and be able to resume them later.

Scrapy supports this functionality out of the box by providing the following facilities:

* a scheduler that persists scheduled requests on disk
* a duplicates filter that persists visited requests on disk
* an extension that keeps some spider state (key/value pairs) persistent between batches

To enable persistence support you just need to define a job directory through the JOBDIR setting. This directory will be for storing all required data to keep the state of a single job (ie. a spider run). It’s important to note that this directory must not be shared by different spiders, or even different jobs/runs of the same spider, as it’s meant to be used for storing the state of a single job.

```
# start crawl job
scrapy crawl somespider -s JOBDIR=crawls/somespider-1
# stop crawl job
scrapy crawl somespider -s JOBDIR=crawls/somespider-1
```

access spider state data

```
def parse_item(self, response):
	# parse item here
	self.state['items_count'] = self.state.get('items_count', 0) + 1
```

Cookies may expire. So, if you don’t resume your spider quickly the requests scheduled may no longer work. This won’t be an issue if you spider doesn’t rely on cookies.

Requests must be serializable by the pickle module, in order for persistence to work, so you should make sure that your requests are serializable. The most common issue here is to use lambda functions on request callbacks that can’t be persisted.

## Scrapy archtiect

### data flow

![](dataflow.png)



## Scrapy Usage

```
# That will create a Scrapy project under the project_dir directory. If project_dir wasn’t specified, project_dir will be the same as myproject
scrapy startproject myproject [project_dir]
```

```
# create a new spider for current project
scrapy genspider [-t template] <name> <domain>
```

```
# Downloads the given URL using the Scrapy downloader and writes the contents to standard output
# this command can be used to “see” how your spider would fetch a certain page.
scrapy fetch <url>
```

```
# Opens the given URL in a browser, as your Scrapy spider would “see” it. Sometimes spiders see pages differently from regular users, so this can be used to check what the spider “sees” and confirm it’s what you expect
scrapy view <url>
```

```
scrapy crawl spidername
```

```
# Remember to always enclose urls in quotes when running Scrapy shell from command-line, otherwise urls containing arguments (ie. & character) will not work
# windows double quote
# linux single quote
scrapy shell 'http://quotes.toscrape.com/page/1/'
# shell also works for local files.
scrapy shell ./path/to/file.html
scrapy shell ../other/path/to/file.html
scrapy shell /absolute/path/to/file.html
scrapy shell file:///absolute/path/to/file.html
# open shell in your spider
from scrapy.shell import inspect_response
def parse(self, response):
  # We want to inspect one specific response.
  if ".org" in response.url:
    # break spider and go to scrapy shell
    inspect_response(response, self)
    # continue run the reset of spider
```

```
# Fetches the given URL and parses it with the spider that handles it, using the method passed with the --callback option, or parse if not given.
scrapy parse <url> [options]
```

```
# Get the value of a Scrapy setting.
scrapy settings [options]
```

```
# Run a spider self-contained in a Python file, without having to create a project.
scrapy runspider <spider_file.py>
```

```
# Run a quick benchmark test
scrapy bench
```

You can also add your custom project commands by using the COMMANDS_MODULE setting. See the Scrapy commands in scrapy/commands for examples on how to implement your commands.

## Common Practices

### Run Scrapy from a script

spider not contains in project

```
import scrapy
from scrapy.crawler import CrawlerProcess

class MySpider(scrapy.Spider):
	# MySpider Definition

class MySpider1(scrapy.Spider):
	# MySpider Definition

process = CrawlerProcess({
	'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})
process.crawl(MySpider)
process.crawl(MySpider1)# running multiple spiders in the same process
process.start() # the script will block here until the crawling is finished
```

inside a scrapy project

```
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
process = CrawlerProcess(get_project_settings())
# 'followall' is the name of one of the spiders of the project.
process.crawl('followall', domain='scrapinghub.com')
process.start() # the script will block here until the crawling is finished
```

run multiple crawlers in the same Twisted reactor

```
from twisted.internet import reactor
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

class MySpider(scrapy.Spider):
	# Your spider definition

class MySpider1(scrapy.Spider):
	# Your spider definition

configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
runner = CrawlerRunner()
d = runner.crawl(MySpider)
d.addBoth(lambda _: reactor.stop()) # manually stop the reactor after MySpider has finished running
reactor.run() # the script will block here until the crawling is finished

runner.crawl(MySpider)
runner.crawl(MySpider1)
d = runner.join()
d.addBoth(lambda _: reactor.stop()) # manually stop the reactor after MySpider has finished running
reactor.run() # the script will block here until the crawling is finished

from twisted.internet import reactor, defer
@defer.inlineCallbacks
def crawl():
    yield runner.crawl(MySpider1)
    yield runner.crawl(MySpider2)
    reactor.stop()
crawl()
reactor.run() # the script will block here until the last crawl call is finished
```

### Distributed crawls

If you have many spiders, the obvious way to distribute the load is to setup many Scrapyd instances and distribute spider runs among those.

If you instead want to run a single (big) spider through many machines, what you usually do is partition the urls to crawl and send them to each separate spider

### Setup your own DNS

If you have multiple crawling processes and single central DNS, it can act like DoS attack on the DNS server resulting to slow down of entire network or even blocking your machines. To avoid this setup your own DNS server with local cache and upstream to some large DNS like OpenDNS or Verizon.        

### Avoiding getting banned

rotate your user agent from a pool of well-known ones from browsers

disable cookies (see COOKIES_ENABLED) as some sites may use cookies to spot bot behaviour

use download delays (2 or higher). See DOWNLOAD_DELAY setting

if possible, use Google cache to fetch pages, instead of hitting the sites directly

use a pool of rotating IPs. For example, the free Tor project or paid services like ProxyMesh. An open source alterantive is scrapoxy, a super proxy that you can attach your own proxies to.

use a highly distributed downloader that circumvents bans internally, so you can just focus on parsing clean pages. One example of such downloaders is Crawlera

## Using Firefox for scraping

### Caveats with inspecting the live browser DOM

Since Firefox add-ons operate on a live browser DOM, what you’ll actually see when inspecting the page source is not the original HTML, but a modified one after applying some browser clean up and executing Javascript code. Firefox, in particular, is known for adding <tbody> elements to tables. Scrapy, on the other hand, does not modify the original page HTML, so you won’t be able to extract any data if you use <tbody> in your XPath expressions.

Therefore, you should keep in mind the following things when working with Firefox and XPath:

* Disable Firefox Javascript while inspecting the DOM looking for XPaths to be used in Scrapy
* Never use full XPath paths, use relative and clever ones based on attributes (such as id, class, width, etc) or any identifying features like contains(@href, 'image').
* Never include <tbody> elements in your XPath expressions unless you really know what you’re doing

### Useful Firefox add-ons for scraping

[Firebug](http://getfirebug.com/) its Inspect Element feature comes very handy when you need to construct the XPaths for extracting data

[Xpath finder ](https://addons.mozilla.org/en-US/firefox/addon/xpath-finder)allows you to test XPath expressions directly on the pages

[Tamper Data ](Firebug also allows to view HTTP headers, but not to modify them)allows you to view and modify the HTTP request headers sent by Firefox. Firebug also allows to view HTTP headers, but not to modify them

[Firecookie](https://addons.mozilla.org/en-US/firefox/addon/firecookie/) makes it easier to view and manage cookies.

