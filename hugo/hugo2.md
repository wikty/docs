配置文件













```

```

hugo会按照网站的源码结构来生成网站的发布结构的

```
.
└── content
    └── about
    |   └── _index.md  // <- http://1.com/about/
    ├── post
    |   ├── firstpost.md   // <- http://1.com/post/firstpost/
    |   ├── happy
    |   |   └── ness.md  // <- http://1.com/post/happy/ness/
    |   └── secondpost.md  // <- http://1.com/post/secondpost/
    └── quote
        ├── first.md       // <- http://1.com/quote/first/
        └── second.md      // <- http://1.com/quote/second/
```



front matter

为内容添加元数据，支持`TOML`（`+++`），`YAML`（`---`），`JSON`（`{}`）格式

```toml
+++
title = "spf13-vim 3.0 release and new website"
description = "spf13-vim is a cross platform distribution of vim plugins and resources for Vim."
tags = [ ".vimrc", "plugins", "spf13-vim", "vim" ]
date = "2012-04-06"
categories = [
  "Development",
  "VIM"
]
slug = "spf13-vim-3-0-release-and-new-website"
+++

content of file
```

```yaml
---
title: "spf13-vim 3.0 release and new website"
description: "spf13-vim is a cross platform distribution of vim plugins and resources for Vim."
tags: [ ".vimrc", "plugins", "spf13-vim", "vim" ]
lastmod: 2015-12-23
date: "2012-04-06"
categories:
  - "Development"
  - "VIM"
slug: "spf13-vim-3-0-release-and-new-website"
---

content of file
```

```json
{
    "title": "spf13-vim 3.0 release and new website",
    "description": "spf13-vim is a cross platform distribution of vim plugins and resources for Vim.",
    "tags": [ ".vimrc", "plugins", "spf13-vim", "vim" ],
    "date": "2012-04-06",
    "categories": [
        "Development",
        "VIM"
    ],
    "slug": "spf13-vim-3-0-release-and-new-website"
}

content of file
```

front matter中有hugo预定义的变量，也有用户自定义的变量，在模板中可以通过`.Params.variablename`来访问相应的变量（注均使用小写名字访问变量，不管变量是怎样大小写定义的）

常见变量

```
title = "the title for the content"
description = "the description for the content"
date = the date the content will sorted by
taxonomies = These will use the field name of the plural form of the index
# old published path redirect to this content
aliases = []
#  If true, the content will not be rendered unless hugo is called with --buildDrafts
draft = true
# If in the future, content will not be rendered unless hugo is called with --buildFuture
publishdate = 
#  Content already expired will not be rendered unless hugo is called with --buildExpired
expirydate =
type = the type of the content
# If true, explicitly treat the content as CJKLanguage, affect .Summary and .WordCount
isCJKLanguage = true
# It can be used to change the part of the url that is based on the filename
slug = 
# The full path to the content from the web root. It makes no assumptions about the path of the content file. It also ignores any language prefixes of the multilingual feature.
url = 
# If neither slug or url is present, the filename will be used
```





别名机制

hugo允许在front matter中指定别名，来实现别名重定向到当前页面，这个机制对网站迁移有很大好处，使得以前发布的链接重定向到迁移后的页面

```toml
+++
aliases = [
    "/posts/my-original-url/",
    "/2010/01/01/even-earlier-url.html"
]
+++
```

访问`aliases`中的任意一个链接都会重定向到当前页面

hugo别名机制，其实是通过按照别名生成静态文件来实现的，因此注意别名需要提供完整的路径名，而且别名页面会先生成，也即可能会被后续同名的页面重写，生成的别名静态文件内容样例

```
<!DOCTYPE html>
<html>
  <head>
    <title>http://mysite.tld/posts/my-original-url</title>
    <link rel="canonical" href="http://mysite.tld/posts/my-original-url"/>
    <meta http-equiv="content-type" content="text/html; charset=utf-8"/>
    <meta http-equiv="refresh" content="0; url=http://mysite.tld/posts/my-original-url"/>
  </head>
</html>
```

可以在`layouts`创建文件`alias.html`自定义别名静态文件内容（可以访问变量`Premalink`和`Page`）



组织网站结构

Hugo相信你对内容组织是有一定目的的，因此会按照跟你对内容相同的组织方式来组织发布网站的内容，内容的顶级结构称作Section，hugo会自动为每个Section生成一个list用来列举其中的所有内容。默认一个Section中的内容都使用相同的内容类型，如果要改变某个内容的类型，需要在相应的front matter中的通过type指定

Hugo believes that you organize your content with a purpose. The same structure
that works to organize your source content is used to organize the rendered
site. Following this pattern Hugouses the top level of your content organization as **the Section**.

Hugo will automatically create pages for each section root that list all
of the content in that section

The following example site uses two sections, “post” and “quote”.

```
.
└── content
    ├── post
    |   ├── firstpost.md       // <- http://1.com/post/firstpost/
    |   ├── happy
    |   |   └── ness.md        // <- http://1.com/post/happy/ness/
    |   └── secondpost.md      // <- http://1.com/post/secondpost/
    └── quote
        ├── first.md           // <- http://1.com/quote/first/
        └── second.md          // <- http://1.com/quote/second/
```

内容类型

hugo支持不同内容类型，每个内容类型会使用不同的元数据以及模板，我们通过命令`hugo new your-type/my-newest-post.md`来创建基于不同内容类型的内容文本，正常情况下使用该命令时，hugo默认会将为创建的文本生成front matter内容（含有`title`，`date`等），为了创建符合自己需求的内容文本模板，就需要自定义内容类型，这样在使用`hugo new your-type/some.md`时将会具有自定的front matter

使用`hugo new my-content-type/post-name`命令时，hugo自动识别出内容文本要使用的内容类型名为`my-content-type`，当然也可以通过参数`--kind`来指定内容类型名

hugo使用哪个内容类型：首先查看目录`archetypes`下有没有跟命令行指定名称一致的文件，如果没有的话，就看有没有`archetypes/default.md`文件，如果没有的话，看是否使用了主题，如果还是没有的话，就使用hugo内置的类型（添加元数据title, date, draft）

hugo假设你的网站按照section组织并且每个section有相应的内容类型，然后section中的每个内容将会继承所在section的内容类型或者通过front matter 的`type`来改变

创建新的内容类型

在目录`layouts`中创建类型目录，例如：类型post对应的目录为`layouts/post/`

在类型目录下创建single模板，例如：`layouts/post/single.html`

在目录`layouts/section/`创建list模板，例如：`layouts/section/list.html`

创建视图模板，放置在`layouts/post/`目录下

创建archetype，在目录`archetypes/`下创建`archetypes/post.md`



内容类型定义文件

假设内容打算按照`categories`和`tags`来组织，为此想要在每个新创建的内容文件中添加这些front matter信息，因此创建文件`archetypes/default.md`

```toml
+++
tags: ["x", "y"]
categories = ["x", "y"]
+++
```

然后在执行`hugo new post/my-new-post.md`，将会在内容文本中生成下面的头信息

```toml
+++
title = "my new post"
date = "2015-01-12T19:20:04-07:00"
tags = ["x", "y"]
categories = ["x", "y"]
+++
```

上面的例子假设网站只含有一种内容类型的，创建的所有内容文本将会使用该default类型，下面将介绍创建其它的内容类型

创建文件`archetypes/musician.md`，添加一下内容

```toml
+++
name = ""
bio = ""
genre = ""
+++
```

然后使用内容类型`musician`创建内容文本：`hugo new musician/test.md`，将生成内容文本`content/musician/test.md`，并且含有一下front matter

```
+++
title = "mozart"
date = "2015-08-24T13:04:37+02:00"
name = ""
bio = ""
genre = ""
+++
```

此外注意的是，以上格式都是`TOML`的，可以通过站点配置文件中的`MetaDataFormat`来改变格式的



内容排序

hugo将按照内容文本front matter中的`weight`，`date`，`title`依次排序

为内容指定weight

```toml
+++
weight = 4
title = "Three"
date = "2012-04-06"
+++
```



内容摘要

hugo自动生成摘要内容（将文章中所有html除去后的前70个字作为摘要）并将其保存在`.Summary`变量供模板使用

用户可以通过在内容中放置`<!--more-->`，这样位于该分隔符前面的内容会作为`.Summary`变量供模板使用

此外如果生成摘要时，以及包含了内容文本所有内容，模板变量`.Truncated`值为`false`，利用这一点可以摘要试图中根据条件判断是否显示Read More..链接

```
{{ range first 10 .Data.Pages }}
  <div class="summary">
    <h4><a href="{{ .RelPermalink }}">{{ .Title }}</a></h4>
    {{ .Summary }}
  </div>
  {{ if .Truncated }}
  <div class="read-more-link">
    <a href="{{ .RelPermalink }}">Read More…</a>
  </div>
  {{ end }}
{{ end }}
```



多语言支持

https://www.gohugo.io/content/multilingual/



主题

hugo并没有搭载默认主题，要渲染网站需要从https://themes.gohugo.io/下载自己喜欢的主题才行

使用git或者手动下载主题文件夹，放置在`themes`目录下，然后通过命令行`--theme`或者网站配置文件中的`theme`来为网站指定主题

对主题定制化

hugo允许用户在working directory中同名文件重写主题的模板和静态文件，也即一般我们会下载一个主题文件夹到`themes`目录中，然后在working directory目录中编写自己的某些模板和静态文件来替换主题提供的文件

假设主题含有较低版本的JQuery静态文件，位置为`/themes/themename/static/js/jquery.min.js`，你只需要将较新版本的JQuery文件放置在`/static/js/jquery.min.js`即可替换主题的JQuery文件

替换模板文件，因为hugo在查找模板文件时，先会查找working directory，然后才查找主题目录，因此可以方便的用working directory的模板重写主题同名模板，`/themes/themename/layouts/_default/single.html`将被`/layouts/_default/single.html`重写

替换内容类型，如果主题`archetypes`中定义了内容类型不能满足你的需求，可以在working directory目录的`archetypes`目录中定义同名内容类型

创建主题

命令：`hugo new theme theme-name`



模板

hugo主要模板有： single, list, homepage, partial templates, content views, taxonomy terms, rss, sitemap, 404, alias





Go模板语法

简单来说Go模板就是含有模板函数和模板变量的HTML文件

* 模板变量和函数访问语法

  ```
  # 直接在模板中输出变量foo
  {{ .Title }}
  # 调用函数add，并将结果返回到模板中
  # 注：传入函数的参数用空格分隔开
  {{ add 1 2 }}
  # 使用dot语法访问成员
  {{ .Params.bar }}
  ```

  ​

* 自定义变量

  ```
  # 除了访问模板预先定义的变量外，还可以自定义变量
  {{ foo := "hello" }}
  # 访问自定义变量的语法跟访问预先定义变量的语法一样
  {{ foo }}
  ```

  ​

* 表达式分组

  ```
  # 使用括号对表达式分组
  {{ if or (isset .Params "foo") (isset .Params "bar") }} hello word!
  {{ end }}
  ```

  ​

* 包含子模板

  ```
  # 第一个参数指定模板路径
  # template在layouts目录下查找模板；partial在layouts/partials目录下查找模板
  # 第二个参数指定子模板可以访问的变量
  # 指定dot将当前上下文环境传递到子模板
  {{ template "partials/header.html" . }}
  {{ partial "header.html" . }}
  ```

  ​

* 迭代

  ```
  # range 可以用来迭代字典和数组
  # 并且在range内部上限文环境变成了正在迭代的元素
  {{ range seq 5 }}
  	{{ . }}
  {{ end }}
  {{ range $e := seq 5 }}
  	{{ $e }}
  {{ end }}
  {{ range $i, $e := seq 5 }}
  	{{ $i }}
  	{{ $e }}
  {{ end }}
  ```

  ​

* 条件判断

  ```
  # if
  {{ if isset .Params "title" }}<h4>{{ index .Params "title" }}</h4>{{ end }}
  # if ... else
  {{ if isset .Params "alt" }}
      {{ index .Params "alt" }}
  {{else}}
      {{ index .Params "caption" }}
  {{ end }}
  # if ... else if
  {{ if isset .Params "alt" }}
      {{ index .Params "alt" }}
  {{ else if isset .Params "caption" }}
      {{ index .Params "caption" }}
  {{ end }}
  # and, or
  {{ if and (or (isset .Params "title") (isset .Params "caption")) (isset .Params "attr")}}
  # with
  # 当变量测试为false时，直接跳过with语句
  # 当变量测试为true时，with内部的上下文环境表示当前变量
  {{ with .Params.title }}<h4>{{ . }}</h4>{{ end }}
  ```

  ​

* 管道

  ```
  # 通过管道将多个操作连接在一起，就像流水线一样不断处理数据
  {{ (seq 1 5) | shuffle }} # {{ shuffle (seq 1 5) }}
  {{ index .Params "disqus_url" | html }}
  {{ if isset .Params "caption" | or isset .Params "title" | or isset .Params "attr" }}
  Stuff Here
  {{ end }}
  ```

  ​

* 上下文环境

  ```
  # 上下文环境用来表示当前变量作用域，使用dot语法引用当前上下文环境
  {{ . }}
  # 在顶级模板（就是不被任何模板包含的模板）中上下文环境表示整个页面的作用域
  # 在with或者迭代中，上下文环境表示当前被处理的元素，在这些情形下无法使用dot语法访问页面作用域
  # 访问页面作用域的若干方案
  # 1. 自定义全局变量
  {{ $title := .Site.Title }}
  {{ range .Params.tags }}
    <li>
      <a href="{{ $baseURL }}/tags/{{ . | urlize }}">{{ . }}</a>
      - {{ $title }}
    </li>
  {{ end }}
  2. 使用$访问页面作用域
  {{ range .Params.tags }}
    <li>
      <a href="{{ $baseURL }}/tags/{{ . | urlize }}">{{ . }}</a>
      - {{ $.Site.Title }}
    </li>
  {{ end }}
  ```

  ​

* 访问配置参数

  ```
  # 网站配置文件中的params配置项
  {{ .Site.Params.Author }}
  # 当前文件front matter中的配置项
  {{ if not .Params.notoc }}
      <div id="toc" class="well col-md-4 col-sm-6">
      {{ .TableOfContents }}
      </div>
  {{ end }}
  ```

  ​

* d

* ​


* ​


### 模板变量



### 常用模板函数

```
# default
# 为没有设置的值提供默认值
{{ index .Params "foo" | default "default-value" }}
{{ default "default-value" (index .Params "foo") }}
# delimit
# 将数组或者字典值通过指定的分隔符拼接为字符串
# 可选的第三个参数用来指定最后两个值使用的分隔符
{{ delimit .Params.tags ", " }} # tag1, tag2, tag3
{{ delimit .Params.tags ", " " and " }} # tag1, tag2 and tag3
# dict
# 创建一个字典对象，常用于模板向partial传递参数
{{partial "foo" (dict "key1" "value2" "key2" "value2" "content" .)}}
# slice
# 创建数组
{{ delimit (slice "foo" "bar" "buzz") ", " }}
# shuffle
# 返回打乱顺序的数组
{{ shuffle (slice "foo" "bar" "buzz") }}
# echoParam
# 如果参数存在就输出它
{{ echoParam .Params "foo" }}
# eq
# 判断值相等
{{ if eq .Section "blog" }}Blog{{ end }}
# first
# 提取数组前N个元素
{{ range first 10 .Data.Pages }}{{ end }}
# last
# 提取数组后N个元素
{{ range last 10 .Data.Pages }}{{ end }}
# after
# 提取数组第N个之后的元素，同first结合可以提取数组中间任意部分的元素
{{ range after 10 .Data.Pages }}{{ end }}
# jsonify
# 将字典转换为json字符串
{{ dict("title" .Title "content" .Plain) | jsonify }}
# getenv
# 返回系统环境变量的值
{{ getenv "HOME" }}
# in
# 判断某个值是否在数组或字符串中
{{ if in .Params.tags "Git" }}Follow me on GitHub!{{ end }}
{{ if in "this string contains a substring" "substring" }}Substring found!{{ end }}
# intersect
# 返回两个数组中的公共部分
# 可以利用博客共有的tags做相似性博客推荐
<ul>
{{ $page_link := .Permalink }}
{{ $tags := .Params.tags }}
{{ range .Site.Pages }}
    {{ $page := . }}
    {{ $has_common_tags := intersect $tags .Params.tags | len | lt 0 }}
    {{ if and $has_common_tags (ne $page_link $page.Permalink) }}
        <li><a href="{{ $page.Permalink }}">{{ $page.Title }}</a></li>
    {{ end }}
{{ end }}
</ul>
# isset
# 判断值是否设置
{{ if isset .Params "foo" }}{{ index .Params "foo" }}{{ end }}
# seq
# 创建整数序列，语法同Linux的seq
{{ seq 3 }} # 1 2 3
{{ seq 1 2 4 }} # 1 3
{{ seq -3 }} # -1 -2 -3
{{ seq 1 4 }} # 1 2 3 4
{{ seq 1 -2 }} # 1 0 -1 -2
# sort
# 返回排序后的数组或者字典值
# 可选的第二个参数指定按照什么排序，第三个参数指定升序还是降序
{{ range sort .Params.tags }}{{ . }} {{ end }}
{{ range sort .Site.Params.authors "lastName" "desc" }}{{ .lastName }} {{ end }}
# where
# 过滤数组，仅返回匹配指定条件的元素
# 支持各种条件运算符eq, ne, ge, gt, le, lt, in, not in, intersect
{{ range where .Data.Pages "Section" "post" }}
   {{ .Content }}
{{ end }}
{{ range where .Data.Pages "Section" "!=" "post" }}
   {{ .Content }}
{{ end }}
{{ range where .Site.Pages ".Params.tags" "intersect" .Params.tags }}
  {{ if ne .Permalink $.Permalink }}
    {{ .Render "summary" }}
  {{ end }}
{{ end }}
{{ range first 5 (where .Data.Pages "Section" "post") }}
   {{ .Content }}
{{ end }}
{{ range where .Data.Pages ".Params.specialpost" "!=" nil }}
   {{ .Content }}
{{ end }}
# readDir
# 读取目录返回为数组
{{ range (readDir ".") }}{{ .Name }}{{ end }}
# readFile
# 读取文件并返回文件内容为字符串
{{readFile "README.txt"}}
# imageConfig
# 获取图像信息
{{ with (imageConfig "favicon.ico") }}
favicon.ico: {{.Width}} x {{.Height}}
{{ end }}
# 数学函数
{{ add 1 2 }}
{{ sub 3 2 }}
{{ mul 2 3 }}
{{ div 4 2 }}
{{ mod 6 3 }}
{{ modBool 6 3 }}
# int
# 字符串转为整数
{{ int "233" }}
# printf
{{ printf "formatted %.2f" 3.1416 }}
# chomp
# 移除尾部的换行符
{{chomp "<p>Blockhead</p>\n"}}
# dateFormat
# 日期格式化
{{ dateFormat "Monday, Jan 2, 2006" "2015-01-21" }} # Wednesday, Jan 21, 2015
# emojify
# 生成emoji表情字符
# 可用emoji表情参见：https://www.webpagefx.com/tools/emoji-cheat-sheet/
{{ "I :heart: Hugo" | emojify }}
# highlight
# 代码高亮
{{< highlight html >}}
<body></body>
{{< /highlight >}}
# htmlEscape
# 转义html元字符：<, >, &, ', "
{{ htmlEscape "Hugo & Caddy > Wordpress & Apache" }}
# htmlUnescape
# 对转义的html元字符解码
{{ htmlUnescape "Hugo &amp; Caddy &gt; Wordpress &amp; Apache" }}
# humanize
# 返回数据适合人阅读的格式
{{humanize "my-first-post"}} # "My first post"
{{humanize "myCamelPost"}} # "My camel post"
{{humanize "52"}} # "52nd"
{{humanize 103}} # "103rd"
# lower
# 小写转换
{{ lower "TestTest" }}
{{ upper "test" }}
# markdownify
{{ .Title | markdownify }}
# plainify
# 除去字符串中的html标签
{{ "<b>BatMan</b>" | plainify }}
# pluralize
# 将英文单词转为复数形式
{{ "box" | pluralize }}
# 英文单词的单数形式
{{ "cats" | singularize }}
# findRE
# 利用正则表达式从文本中找出匹配字符串并作为数组返回
# 可选的第二个参数用来指定返回的匹配个数
{{ findRE "<h2.*?>(.|\n)*?</h2>" .Content }}
# 利用findRE找到h2标题构建文章目录
{{ $headers := findRE "<h2.*?>(.|\n)*?</h2>" .Content }}

{{ if ge (len $headers) 1 }}
    <ul>
    {{ range $headers }}
        <li>
            <a href="#{{ . | plainify | urlize }}">
                {{ . | plainify }}
            </a>
        </li>
    {{ end }}
    </ul>
{{ end }}
# replace
# 字符串替换
{{ replace "I'm item" "item" "new item" }}
# replaceRE
# 使用正则语法进行字符串替换
{{ replaceRE "^https?://([^/]+).*" "$1" "http://gohugo.io/docs" }}
# safeHTML
# 声明字符串不需要过滤html标签，也不需要转化html元字符
{{ "<em>test</em>" }} # &lt;em&gt;test&lt;/em&gt;
{{ "<em>test</em>" | safeHTML }} # <em>test</em>
# safeHTMLAttr
# 声明参数不需要过滤html标签，也不需要转化html元字符
{{ printf "href=%q" .URL | safeHTMLAttr }}
# safeCSS
# 声明字符串含有CSS代码，不要进行过滤
<p style="{{ .Params.style | safeCSS }}">…</p>
# safeJS
# 声明字符串含有JS代码，不要进行过滤
<script>var form_{{ .Params.hash | safeJS }};…</script>
# slicestr
# 截取子字符串
# 第二个可选参数指定子字符串结束位置
{{slicestr "BatMan" 3}}
{{slicestr "BatMan" 0 3}}
# truncate
# 截断字符串
{{ "this is a text" | truncate 10 " ..." }} # this is a ...
{{ "<em>Keep my HTML</em>" | safeHTML | truncate 10 }} # <em>Keep my …</em>
{{ "With [Markdown](#markdown) inside." | markdownify | truncate 10 }} # With <a href='#markdown'>Markdown …</a>
# split
# 字符串切割为数组
{{split "tag1,tag2,tag3" "," }}
# string
# 转换为字符串
{{ string 12 }}
# substr
# 提取子字符串
{{substr "BatMan" 0 -3}} # omit last three chars, return Bat
{{substr "BatMan" 3 3}} # start is 3, and length is 3, return Man
# hasPrefix
# 测试字符串前缀是否匹配
{{ hasPrefix "Hugo" "Hu" }}
# title
# 将字符串转换为title风格
{{ title "hello world" }}
# trim
# 将字符串首尾所有指定字符移除后返回
{{ trim "++Batman--" "+-" }} # Batman
# countwords
# 统计单词数
{{ "hello world" | countwords }}
# countrunes
# 中日韩统计字数
{{ "Hello, 世界" | countrunes }}
# md5
# 计算数据的md5值
# 当使用avatar头像服务时尤其有用
<img src="https://www.gravatar.com/avatar/{{ md5 "your@email.com" }}?s=100&d=identicon">
# sha1
# 计算数据的sha1值
{{ sha1 "hello" }}
# sha256
# 计算数据的sha1值
{{ sha256 "hello" }}
# 时间
{{ time "2016-05-28" }}
{{ (time "2016-05-28").YearDay }}
{{ mul 1000 (time "2016-05-28T10:30:00.00+10:00").Unix }} # unix milliseconds
{{ now }}
# base64编码解码
{{ "Hello world" | base64Encode }}
{{ "SGVsbG8gd29ybGQ=" | base64Decode }}
# apply
# 对数组或字典应用一个函数并生成新的数组或字典
# 第二个参数是要应用的函数字符串，第二个之后的参数是传递给应用函数的参数
{{ apply .Params.names "urlize" "." }}
# 假设现在想要创建一个tag list页面
# tag link页面如下
<a class="post-tag post-tag-{{ . | urlize }}" href="/tags/{{ . | urlize }}">{{ . }}</a>
# tag list页面如下
{{ with .Params.tags }}
<div class="tags-list">
  Tags:
  {{ $sort := sort . }}
  {{ $links := apply $sort "partial" "post/tag/link" "." }}
  {{ $clean := apply $links "chomp" "." }}
  {{ delimit $clean ", " }}
</div>
{{ end }}
# .Render
# 使用指定模板渲染数组中的内容
# 下面使用了模板layouts/_default/summary.html
{{ range .Data.Pages }}
    {{ .Render "summary"}}
{{ end }}
# urlize
# 将字符串转换为适合在url中使用的形式
<a href="/tags/{{ . | urlize }}">{{ . }}</a>
# safeURL
# 声明直接输出，不要进行URL过滤
{{ "http://www.google.com" | safeURL }}
# querify
# 将键值对转换为url中的查询字符串
<a href="https://www.google.com?{{ (querify "q" "test" "page" 3) | safeURL }}">Search</a>
# absURL, relURL
# 基于配置的baseURL来生成绝对URL和相对URL
# 假设baseURL为http://mysite.com/hugo/
{{ "mystyle.css" | absURL }} # “http://mysite.com/hugo/mystyle.css"
{{ "mystyle.css" | relURL }} # “/hugo/mystyle.css”
{{ "http://extrenal.org" | absURL }} # http://extrenal.org
```

### 模板变量

#### Site Variables



#### Page Variables



#### Page Params



#### Param method





#### File Variables



#### Hugo Variables 



### 模板种类

#### Single

single是hugo用来渲染一个内容文件的主要视图，hugo会使用一系列判断规则决定哪一个single模板来作为当前内容文件的渲染视图，具体来说hugo会依次从以下位置查找single模板文件直到找到：

- /layouts/`TYPE`/`LAYOUT`.html
- /layouts/`SECTION`/`LAYOUT`.html
- /layouts/`TYPE`/single.html
- /layouts/`SECTION`/single.html
- /layouts/_default/single.html
- /themes/`THEME`/layouts/`TYPE`/`LAYOUT`.html
- /themes/`THEME`/layouts/`SECTION`/`LAYOUT`.html
- /themes/`THEME`/layouts/`TYPE`/single.html
- /themes/`THEME`/layouts/`SECTION`/single.html
- /themes/`THEME`/layouts/_default/single.html

也即先从布局文件夹`layouts`查找，再从主体文件夹`themes`查找；并且先查找有没有符合当前内容类型`TYPE`的模板，再查找有没有符合当前章节类型`SECTION`的模板；另外如果指定要使用某个布局的话，就优先使用`LAYOUT.html`而不是`single.html`；当所有模板都没有查找到时，将会使用模板`layouts/_default/single.html`

注：章节类型根据内容文件所在文件夹来决定的；内容类型和布局可以分别通过内容文件front matter中的`type`和`layout`来设置





#### List

#### Homepage

#### Partial Template

#### Content View

#### Taxonomy Term

#### RSS

#### Sitemap

#### 404

#### Alias