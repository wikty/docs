



## 源目录结构

源目录就是使用命令`hugo new site myblog`创建的那个目录，该目录用来存放静态站点内容，是Hugo生成静态站点时的资源输入，而且是唯一的资源输入目录。所有书写的内容文档以及下载的主题文档都存放在该目录下，在生成静态网站内容时，Hugo会自动将该目录下的文件转换为静态网页文件并正确的组织网站结构。

典型源目录结构示例

```
├─archetypes
├─content
├─data
├─i18n
├─layouts
├─static
├─themes
└─config.toml 
```

下面依次对源目录下面的子目录以及文件进行介绍

### archetypes

archetypes的意思是“原型”，这里原型是指内容文档原型。

Hugo允许我们通过命令`hugo new path/to/my/content`来创建新的内容文档，这些文档一般会包含一个头部，用来描述关于文档的一些信息，比如：`title`、`date`等，这样可以省去我们自己定义头部的麻烦。在使用命令创建内容文档时，Hugo是怎样决定应该为新文档添加哪些头部信息呢？

这就涉及到了原型的概念，可以认为每个新建的内容文档都来自于一个模板文档，这个预先规定了头部信息的模板文档就是所谓的原型，当我们安装了Hugo之后使用`hugo new path/to/content`命令新建的文档是依照Hugo内置的默认原型来创建的，因为这个内置原型预定义了`title`、`date`以及`draft`头部信息，所以我们新建的文档会含有这些头部信息。

除了使用Hugo内置的原型外，Hugo还支持用户自定义原型。这就是目录`archetypes`的用途，该目录下用来存放用户自定义的各种原型文档。

### content

content顾名思义是用来存放内容文档的目录

### data

data目录用来存放一些数据文件。当我们想要在网站展示大量的数据时，可以将这些数据存放在该目录下



## Hugo配置

Hugo可以自动识别工作目录中的内容文档以及主题文件来生成静态网站内容，大多情况下Hugo就像你期望那样工作。此外，Hugo还允许你通过配置来控制网站生成过程、定义网站全局参数等。Hugo既可以通过操作系统中以`HUGO_`为前缀的环境变量名来配置，也可以通过位于工作目录中的文件`config.toml`、`config.yaml`或者`config.json`来配置，Hugo会依次查找这三个配置文件，将找到的第一个文件作为配置文件（这三种文件在配置Hugo的功效上是等价的，仅仅只是文件内容格式不同而已）。

下面是一个`config.yaml`配置文件样例

```yaml
baseURL: "http://yoursite.example.com/"
title: "My Blog"
contentDir: "content"
layoutDir: "layouts"
publishDir: "public"
buildDrafts: false
params:
  AuthorName: "Your Name"
  Hobby:
    - "foo"
    - "bar"
  SidebarRecentLimit: 5
```

配置文件中主要含Hugo内置配置项以及用户自定义配置项两类。像上文配置文件中`baseURL`、`contentDir`、`layoutDir `、`publishDir`、`buildDrafts`等这些都是Hugo内置的配置项，这些配置项Hugo都是给它们添加默认值，除非你要修改这些默认值，一般情况下这些配置项保持Hugo的默认值即可，是不需要出现在你的配置文件中的。此外某些时候可能想要添加自定义配置项，比如上文中`AuthorName`、`Hobby`、`SidebarRecentLimit`都是用户自定义的全局参数，这些参数可以在主题模板文件中访问，以此来控制网站的生成过程。

常用Hugo内置配置项样例



