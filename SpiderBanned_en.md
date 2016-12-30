# Anti-crawling strategy

1. IP restrictions based on access frequency/quantity

	Real users and crawlers visit web site with different frequency. In general, crawlers have two features: most of the accesses are concentrated in a short time and accesses are time-periodic. Crawleres' features of the frequency of access are very different from normal users, so it can easily be identified as crawler. Similarly the site will be based on access quantity to detect crawler, if a visitor make a amount of traffic in a long time, the site will generate a verification window to verify the visitors.

2. Check HTTP request header

	Real users use browsers to request web pages, the HTTP request header is generated by browsers. Corresponding, crawlers' HTTP header is generate by themself, there is a large difference with the HTTP header generated by browsers. In general, sites detect HTTP header(e.g, User-Agent and Refer) to identify crawlers.

3. Dynamically web content

	In the Web 2.0 era, many web pages' rendering mode migrates from the back-end rendering to the front-end asynchronous loading. In other words, the content of web page is dynamically loading while user interaction with it, rather than loaded at the beginning of access the web page. To crawl those web pages, crawlers must have the ability to run javascript code in web pages to dynamically load content.

4. Frequently change the page structure

	The way of crawlers to obtain web pages' content is parsing the structure of HTML documents to get the content. So crawlers will not work when the structure of web page is changed.

# Anti-anti-crawling strategy

1. Let down the speed of crawler
2. Use the Tor network proxy
3. Use the headless browser Phantomjs, Zombiejs and so on
4. Build ourself dynamic IP proxy pool
5. Buy Crawler Cloud Service
6. Anti-banned tips

## Let down crawler speed

This solution is a compromise, on the one hand we want to quickly crawl a lot of pages, on the other hand we do not want to be blocked by sites. We can test the maximum limit  frequency of access to the site, and then to access the at the maximum limit frequency.

Sites not only to limit the frequency of access, the amount of traffic is also limited. When the amount of traffic has exceeded, crawlers will be responded to by a verification code window. We can use the machine learning method to complete the verification code identification work.

In short, this solution can partially solve blocked issues, but lower speed crawling will heavily affect the efficiency of production.

## Use the Tor network proxy

Tor network can be seen as a complex IP proxy pool. Crawlers' HTTP requests will go through the Tor network to the destination web site. In other words, crawlers make a request with a dynamic IP, so do not worry about being blocked by the site. 

In short, because Tor network is blocked in China, the access to Tor network is unstable in sometimes.

## Using headless browser Phantomjs/Zombiejs

Some sites use front-end javascript code to dynamically load the page content, so crawlers need to be able to run the javascript to dynamically load pages. In order to do that, project must use browser core Phantomjs, Zombiejs and so on.

In short, this solution is only to solve the problem of front-end asynchronous loading of the page content, has no effect to blocked issues.

## Build ourself dynamic IP proxy pool

We need to collect free IP proxy from the Internet, and  to verify the availability of IP in real-time.

In short, this solution is perfect, but it will take a lot of time to build the dynamic IP proxy system. Moreover, the free Ip proxy are usually less stable.

## Buy Crawler Cloud Services

Crawler cloud services are generally distributed deployment, and they have a complex mechanism to avoid be banned.

In short, Crawler cloud service [crawlera](https://crawlera.com/) is a good choice, integrating it into the crawler framework scrapy is very simple.

## Anti-banned tips

1. Dynamic switch User-Agent
2. Disable cookies
3. Delay the download, random sleep between each request a few seconds

# Conclusion

I recommend temporarily using the tor network or the crawler cloud service, while building our own dynamic IP proxy system.