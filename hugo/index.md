---
title: Hugo 简介
author: Xiao Wenbin
date: 2017/03/30
category: hugo
---

# 介绍

[Hugo][1] 是一款静态网站生成工具。如果你之前使用过 [Jekyll][2] ，那么一定不会对这类工具感到陌生。简单来说静态网站生成工具允许你以不同于传统博客系统（比如：[WordPress][3] ）的模式书写/发布内容，你可以用 [Markdown][4] 之类的文本标记语言撰写内容，然后由静态网站生成工具负责将内容发布为网站形式。这里之所以说生成的网站是静态的，是由于网站内容在生成那一刻就是固定不变的了，不会像一般网站那样通过用户交互来动态生成网站内容。博客、文章以及技术文档等内容本来就是很少变化的，跟用户也没有交互性，因此这类站点很适合用静态网站生成工具来生成。

静态网站生成工具的巨大优势在于：*书写语言灵活性带来内容创作的自由*。首先，Markdown 等标记语言本来就是通过简单格式标记符来撰写文档的利器，使得内容创作者将精力集中在内容本身而不是内容的显示格式上；其次，用 Markdown 等标记语言书写的文档不仅仅可以通过静态网站生成工具发布为网站形式，利用像 [Pandoc][5] 这类文档转换工具可以将其转换为 PDF 、Word 等格式进行发布。也即使用 Markdown 等标记语言创作的内容是数据源，可以使用各种发布工具将内容发布为丰富多样的格式。更进一步来说使用标记语言来创作内容，使得内容创作过程和内容展示发布过程独立开来。

为什么选择 Hugo 而不是 Jekyll ：Hugo 简单易用、安装方便而且网站生成速度快。我是一个懒惰而且懒惰的人，以上两点足够成为我拥抱 Hugo 的理由。

# 初识 Hugo

## 安装

Hugo 支持各种操作系统而且安装十分简单，只需下载一个安装程序就可以使用了，可以点击[这里][6]前往下载地址，记得要下载跟自己操作系统对应的版本。此外还需要参照[官网][7]进行一些很简单的设置，比如 Windows 用户需要将下载好的程序移动到合适的位置并将其重命名为 `hugo.exe` ，然后再添加程序路径到系统环境变量 PATH 中。

注：Hugo 是一款基于命令行的工具，下文中涉及到 Hugo 的命令都是在命令行中执行的

## 术语

为了方便理解下文内容，先来介绍几个术语：

- 源目录

  用来生成静态网站的数据来源，该目录中存放了撰写的文章、生成网站时的配置文件以及所有一切相关数据。

- 内容文档

  我们把撰写文章的文档称为内容文档，该文档含有用 Markdown 等标记语言书写的文章内容以及一些用来描述文档的头部信息。

- 文档元数据

  文档头部用来描述文档的信息叫做元数据，元数据一般包含：文章标题、编辑时间以及作者等跟文档相关的信息。这些文档头的元数据通常又被叫做 [Front Matter][8] 。

- 草稿文档

  草稿文档就是还在撰写，没有完成的文档，默认草稿文档是不会被发布出去的。

- 网站主题

  内容文档仅仅是内容，在转换为静态网站时，通常我们会希望网页具有丰富多样表现形式，比如是否为网页添加侧边栏、是否进行分页显示以及网站首页要呈现怎样的内容等，关于内容的表现形式统统由主题来控制，而且 Hugo 允许我们使用不同主题来生成不同风格的网站。同时 Hugo 还提供了丰富的[主题资源][9]，供我们使用。

- 模板文件

  在将内容文档转换为网页的时候，是按照主题或者自定义的某种约定进行转换的，用来约定内容文档如何转换为网页的文件就叫做模板文件，模板文件主要用来定义网页结构，其实可以将模板文件看成是待填充的网页样板。网站主题其实就是由很多资源（包括：CSS 、Javascript 和图片等）以及模板文件构成的。

- 网站生成

  使用 Hugo 将网站源目录中的内容文档和主题资源等数据转换为静态网站。

- 网站预览

  Hugo 提供了本地预览网站功能，使得我们可以在将网站发布出去之前，在本地预览网站效果。

- 网站发布

  将生成的静态网站发布到互联网中，允许别人通过互联网来访问自己生成的静态网站。

## 开始搭建网站

按照下面步骤一步步来搭建一个静态网站：

1. 创建网站源目录

   ```shell
   $ hugo new site your-folder-name
   ```

   `your-folder-name` 应该替换为自己指定的网站源码目录名称（可以是相对路径或者绝对路径）。网站源目录结构如下

   ```
   your-folder-name
    ├─config.toml
    ├─archetypes
    ├─content
    ├─data
    ├─layouts
    ├─static
    └─themes
   ```

   现在暂时不需要担心这么多目录到底用来干嘛的，只要记住我们平时使用最多的就是目录 `content` ，该目录用来存放我们编写的内容文档。

   注：接下来大多数命令都需要在网站源目录中运行，如果没有特殊强调，假定你已经将命令行切换到了源目录。

2. 添加内容文档

   ```shell
   $ hugo new post/first-article.md
   ```

   此时可以在目录 `your-folder-name/content/post` 中发现新建的文件 `first-article.md`，这是一个普通的 Markdown 文档，是我们写作的起点。这里之所以使用 Hugo 命令而不是自己创建 Markdown 文档，是因为通过 Hugo 命令创建的文档会含有一些文档元数据，打开该文档可以看到如下内容：

   ```toml
   +++
   date = "2016-02-14T16:11:58+05:30"
   draft = true
   title = "First Article"

   +++
   ```

   这些元数据主要用来声明文档创建时间、标题等信息，我们可以修改这些这些元数据，此外我们也可以添加其它信息到头部，后续会有讲到。上面元数据中有一项 `draft=true` 表示当前文档是草稿，新创建的文档默认是草稿文档，在生成静态网站时是不会被发布的。

   现在可以在文档头部信息之后为该文档追加一些内容，以便后续生成静态网站时可以看到文档的内容。

3. 草稿更改为可发布文档

   可以直接将内容文档头部的 `draft=true` 改为 `draft=false` ，或者使用 Hugo 命令来完成

   ```shell
   $ hugo undraft content/post/first-article.md
   ```

4. 添加网站主题

   存放在 `content` 目录中文档的仅仅只是写作的内容数据，至于这些书写的内容在发布成为网站后如何排版、如何组织则由 Hugo 主题来决定的（没有主题是无法发布内容的）， Hugo 拥有丰富的主题资源，可以在 Hugo [主题网站][9]预览各种主题，然后挑选喜欢的主题安装到网站源目录的主题目录下（可以安装任意多个主题）

   主题的安装，可直接从主题网站下载，然后解压到网站源目录中的主题目录下，也可以通过 Git 来安装。通过Git 安装主题的好处在于，以后更新主题时会比较方便，Git 安装主题方法如下

   ```shell
   # 切换到网站源目录的主题目录下
   $ cd themes
   # 这里使用了主题https://github.com/Zenithar/hugo-theme-bleak.git
   # 想要使用哪个主题完全取决于自己的喜好
   $ git clone https://github.com/Zenithar/hugo-theme-bleak.git
   ```

5. 本地预览

   在最终生成文档的发布内容之前，通常我们会先在本地预览发布效果，Hugo 集成了本地预览的功能，运行以下命令，然后可以使用浏览器打开网址：http://localhost:1313/ ，就可以看到预览效果

   ```shell
   # 指定以主题hugo-theme-bleak运行预览，主题hugo-theme-bleak是上文安装过的
   $ hugo server --theme=hugo-theme-bleak
   # 如果想要预览草稿文档，需要运行命令
   $ hugo server --theme=hugo-theme-bleak --buildDrafts
   ```

6. 网站生成

   ```shell
   # 指定以主题hugo-theme-bleak生成网站内容
   $ hugo server --theme=hugo-theme-bleak
   # 强制发布草稿
   $ hugo server --theme=hugo-theme-bleak --buildDrafts
   ```

   此时在网站源目录下生成了一个 `public` 目录，该目录中存放了刚刚生成的静态网站，如果想要在别的目录中存放静态网站可以运行命令

   ```shell
   $ hugo server --theme=hugo-theme-bleak -d other-dir-name
   ```

7. 网站发布

   生成的网站只有发布到互联网后，别人才能浏览。可以将网站发布到 GitHub ，也可以发布到自己的服务器上。当然对于大多数人而言发布到 GitHub 是首选，因为它是免费的而且操作也很简单。

   * 发布到GitHub

     首次发布到GitHub

     ```shell
     # 首先你需要在GitHub上创建一个仓库，具体方法参见GitHub官网
     # 然后在网站源目录中运行以下命令
     $ cd public
     $ git init
     $ git remote add origin git@github.com:<github-username>/your-repo-name.git
     $ git checkout -b gh-pages
     $ git add --all
     $ git commit -m "message about this commit"
     $ git push -f origin gh-pages
     ```

     后续发布到GitHub

     ```shell
     # 网站源目录下运行以下命令
     $ cd your-folder-name/public
     $ git add --all
     $ git commit -m "message about this commit"
     $ git push -f origin gh-pages
     ```

   * 发布到自己的服务器

     Hugo 程序使用 Go 语言编写，天生具有多线程的优势，可以在自己的服务器上使用 Hugo 来作为静态网站的 Web Server，当然也可以选择其它 Web Server 来托管自己的静态网站。要使 Hugo 作为 Web Server，需要运行以下命令

     ```shell
     $ hugo server --baseURL=http://yoursite.org/ \
                   --port=80 \
                   --appendPort=false \
                   --bind=87.245.198.50
     ```

     其中 `--bind` 指定监听服务器上哪块网卡，`0.0.0.0` 表示监听所有网卡；运行上述命令后Hugo 会实时监测文档内容改变并根据文档内容来响应请求，为了优化性能，可以通过传递参数 `--disableLiveReload=true` 来关闭该功能。

8. 网站后续更新

   后续对网站的更新流程大概是这样的：

   * 撰写内容文档
   * 本地预览效果
   * 生成网站
   * 发布网站

# 探寻 Hugo

通过初识 Hugo ，我们已经可以搭建一个简单的网站了，可是 Hugo 的能力不止于此，如果可以深入理解 Hugo 的一些原理和概念，就可以帮助我们灵活的使用 Hugo，创建出功能丰富的静态网站。下面将依次介绍一些 Hugo 中常用概念以帮助我们更好的理解 Hugo 是怎样生成静态网站的。

## 源目录

之前有介绍，源目录就是用来生成静态网站的数据来源，该目录中存放了撰写的文章、生成网站时的配置文件以及所有一切相关数据。简单来说，源目录就是使用命令 `hugo new site your-folder-name` 创建的那个目录，是 Hugo 生成静态站点时的资源输入，而且是唯一的资源输入。所有书写的内容文档以及下载的主题文档都存放在该目录下，在生成静态网站内容时，Hugo 会自动将该目录下的文件转换为静态网页文件并正确的组织网页之间的结构。

以下是典型的源目录结构示例，后续将对各个子目录以及文件用途进行详细说明。

```
├─archetypes
├─content
├─data
├─layouts
├─static
├─themes
└─config.toml 
```

### archetypes

archetypes 的意思是“原型”，这里原型是指内容文档原型，要理解什么是内容文档原型，先来看之前我们是如何创建内容文档的，使用命令 `hugo new post/first-article.md` 创建了新的内容文档，而且该文档包含一个头部，用来描述关于文档的一些信息，比如： `title` 、 `date` 等，这样可以省去我们自己定义头部的麻烦。那么使用该命令创建内容文档时，Hugo 又是怎样决定应该为新文档添加哪些头部信息呢，又或者能不能添加不同于默认头部信息的元数据到新建的文档中呢？

这就涉及到了原型的概念，可以认为每个新建的内容文档都来自于一个模板文档，这个预先规定了头部信息的模板文档就是所谓的原型，当我们安装了 Hugo 之后使用 `hugo new path/to/content` 命令新建的文档是依照 Hugo 内置的默认原型来创建的，因为这个内置原型预定义了 `title` 、 `date` 以及 `draft` 头部信息，所以我们新建的文档会含有这些头部信息。文档原型和内容文档类型的概念是一一对应的，可以认为属于某个原型的内容文档是同一类型的。

除了使用 Hugo 内置的原型外，Hugo 还支持用户自定义原型。这就是目录 `archetypes` 的用途，该目录下用来存放用户自定义的各种原型文档。

下面演示如何创建以及使用文档原型

1. 创建原型文档

   在目录 `archetypes` 下创建文件 `post.md` ，并在文件中添加以下内容

   ```toml
   +++
   tags = [""]
   categories = [""]
   +++
   ```

   注：这里使用了 `TOML` 格式定义元数据，可以通过修改网站配置文件中的 `MetaDataFormat` ，来设置网站全局的元数据格式（可选格式有：`toml`、`yaml` 以及 `json`）。

2. 使用原型来创建内容文档

   ```shell
   hugo new post/my-new-post.md
   ```

   可以看到新创建的内容文档头部除了 Hugo 内置的 `title` 和 `date` 外，还有 `tags` 和 `categories` 元数据。

3. 原型的选取

   在运行新建内容文档的命令 `hugo new path/to/content.md` 时，Hugo 是如何决定该使用哪个原型的呢？Hugo 会根据新建内容文档的路径，来判断文档类型，然后使用相应的原型来创建该文档，比如：路径 `post/my-first-post.md` 会被识别为 `post` 类型的文档，相应的会使用 `archetypes/post.md` 来作为 该文档的原型。如果没有找到相应的原型，就会使用 `archetypes/default.md` 来作为原型，如果该原型也找不到就使用 Hugo 内置的原型。除了让 Hugo 根据路径来判断文档类型外，还可以在创建内容文档时，通过 `--kind` 来指定文档的类型。

   除了使用自定义的原型外，还可以使用主题中定义的原型，不过要使用主题原型来创建文档，必须事先在网站配置文件中将网站主题指定为该主题。

### content

该目录顾名思义是用来存放内容文档的目录。Hugo 假设你对该目录的组织是有特定意图的，因此在生成网站时，Hugo 会按照该目录的结构来规划网站的目录组织结构，也即除了内容文档外（内容文档需要被转换为 HTML 文件），其余文件以及目录结构都被原样复制到生成的网站目录中。

默认情况下，目录组织结构决定内容文档的类型。由于在生成网站时，网站会按照该目录下的第一级子目录来将内容划分为几个部分，所以该目录下的第一级子目录被称为 Section，而且默认某个子目录中的内容文档类型名跟该子目录名相同，比如位于 `content/post/content.md` 的内容文档，其类型为 `post` 。可见对该目录下第一级子目录的划分，等价于对内容文档的类型进行划分，不过内容文档的类型除了由所在目录决定外，还可以通过在头部指定字段 `type` 来决定。其实在 Hugo 中 Section 和 文档类型这两个概念是独立的，但由于位于同一个 Section 目录的内容文档通常具有相同的类型，所以在大多数情况下可以不对它们进行区分。

在 Hugo 中内容文档类型的概念很重要。内容目录中的第一级子目录名代表了相应的文档类型；使用命令新建内容文档时，会根据文档类型来使用相应的原型（先在目录 `archetypes` 中查找有无同名原型，没有的话就使用默认原型）；渲染内容文档时，会根据文档类型来使用相应的模板（先在目录 `layouts` 中查找有无同名模板目录，没有的话就使用默认模板）。





















### 输出格式

Hugo 不仅仅可以用来构建静态网站和 RSS 订阅，只需要添加一些配置，就可以将网站源目录转换为电子书等格式。

[1]: https://www.gohugo.io/	"Hugo Site"
[2]: http://jekyllrb.com/	"Jekyll Site"
[3]: https://wordpress.org/	"WordPress Site"
[4]: http://daringfireball.net/projects/markdown/syntax	"Markdown "
[5]: http://pandoc.org/	"Pandoc Site"
[6]: https://github.com/spf13/hugo/releases	"Hugo Download"
[7]: https://www.gohugo.io/overview/installing/	"Hugo Install Tutorial"
[8]: https://gohugo.io/content/front-matter/	"Front Matter"
[9]: https://themes.gohugo.io/	"Hugo Themes"

