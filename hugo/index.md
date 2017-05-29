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

### data

data 目录用来存放一些数据文件。不同于内容文档，数据文件并不会被转换为网页，而是为内容文档提供数据。当你觉得塞在内容文档头部的信息太多时，可以考虑将其迁移到数据文件中，或者当我们想要在网站展示大量的数据时，也可以考虑将它们存放在该目录下，把数据文件单独放在一起，方便管理。

数据文件可以使用 `YAML` , `JSON` , `TOML` 格式来保存，并且数据目录中的数据会以键值对的形式被保存在模板变量 `.Site.Data` 中，这样就可以将这些数据渲染到模板文件中了。

注：数据以键值对形式保存在模板变量中，键由数据文件所在目录名、文件名以及变量名来决定，比如定义在数据文件 `data/author/en/fiction.toml` 中的变量 `names` ，最终在模板中通过 `.Site.Data.author.en.fiction.names` 来引用。

### layouts

存放自定义的模板文件，在生成网站时该目录下的模板文件会替代主题目录中同名模板文件发挥作用。该目录下的子目录保存着不同用途的模板，具体来说有以下几类子目录

* 跟内容类型同名的目录

  ​

* 跟 Section 同名的目录

* 目录 `_default`

* 目录 `section`

#### static

存放自定义的图片、 CSS 以及 Javascript 等资源文件，在生成网站时该目录中的内容会被原样复制到静态网站目录中，该目录结构如何组织完全取决于自己，一般来说通常会创建 `js` 、`css` 、 `img` 子目录用来存放相应的资源文件。

#### themes

存放主题文件夹，Hugo 社区提供了丰富的主题资源以供用户选择，我们可以下载喜欢的主题放在该目录下，在生成网站时可以使用下载好的主题。主题资源一般来说会含有模板文件以及相关图片等资源文件。Hugo 支持用户从多个粒度对主题进行自定义，即可以把主题的部分内容替换为自定义的内容。

### 内容类型

不同内容类型的文档会使用不同的元数据和模板文件。Hugo 支持用户自定义内容类型并提供了命令 `hugo new` 来创建特定内容类型的文档。

让我们更进一步来看到底什么是内容类型或者说到底为什么内容要区分类型？我们在生活中每天可以接触到很多很多电子化的内容，比如：朋友圈、微博、个人博客、微视频等，这些显然是不同的内容，需要用不一样的元数据来描述这些内容，像个人博客可能会用标题、作者、日期等元数据来描述一篇博客，而微视频则可能还要指定视频时间长度以及尺寸信息，并且博客跟视频的展现方式肯定是不同的，需要使用不同的模板来展示它们，这样来看 Hugo 允许用户为网站定义多种内容类型就合情合理了。

Hugo 是如何决定一个内容文档的类型呢？在 Hugo 中我们将内容目录中的子目录称为 Section，默认情况下位于某个 Section 下的所有内容文档具有同一内容类型，且内容类型跟所在 Section 同名。并且 Hugo 还提供了用来创建特定类型文档的命令，`hugo new post/first-post.md` 命令创建的文档位于`content/post` 目录且文档的内容类型为 `post`  ，打开新建的文档可以看到 Hugo 已经自动为文档添加了相应的头部内容。此外 Section 和 内容类型的这种默认关联可以通过在内容文档头部指定 `type` 来改变，使用 `type` 可以显式的为当前文档指定内容类型。

内容类型又是怎样定义的呢？之前有提到每个内容类型都有特定的元数据和模板文件，因此要创建新的内容类型本质上就是定义新的元数据以及创建新的模板文件，假设我们要定义名称为 `post` 的内容类型，具体来说需要做以下几件事情

* 创建文档原型

  在文档原型定义目录 `archetypes` 中创建文件 `post.md` ，该文件头部指定的元数据就是内容类型 `post` 的元数据。

* 创建单页模板

  首先需要在 `layouts` 目录下创建 `post` 以存放相应内容类型的模板文件，然后创建 `layouts/post/single.html` 模板文件，用来定义该内容类型的单页显示方式。

* 创建列表模板

  创建 `layouts/post/list.html` 模板文件，用来定义 `post` 内容类型的列表显示方式。

* 创建其它模板

  Hugo 不限制内容的呈现方式，除了常见的单页以及列表外，用户可以在模板目录中创建任何模板来自定义内容的显示方式

如果你觉得创建一个内容类型太麻烦了。没关系，上面为内容类型创建文档原型以及各种模板文件都不是必须的，没有创建这些东西，照样可以从逻辑上把内容区分为各种类型，而且同内容类型关联的文档原型以及模板文件都是支持回退的，即找不到对应内容类型的原型以及模板文件时，Hugo 会自动使用默认原型和模板文件。

### 组织内容目录

内容目录 `content` 中的文件是最终用来生成网站的数据来源，我们可以在该目录下嵌套任意层级的子目录来组织内容文档，Hugo 会假定作者对内容目录的组织有自己的意图，所以生成网站的结构同内容目录的结构是对应的，比如下面的内容目录结构

```
└── content
    └── about
    |   └── _index.md
    ├── post
    |   ├── firstpost.md
    |   ├── happy
    |   |   └── ness.md
    |   └── secondpost.md
    └── quote
        ├── first.md
        └── second.md
```

最终生成的网页结构为

```
/about/
/post/firstpost/
/post/happy/ness/
/post/secondpost/
/quote/first/
/quoter/second/
```

除了让 Hugo 根据内容目录结构来自动构造网站结构外，还可以通过在内容文档头部指定某些参数来控制文档最终将被安排在网站的哪个位置。下面列举了一些控制文档生成位置的参数，它们的优先级依次升高，也即后面参数可以覆盖前面参数的影响：

* `slug` 默认情况下生成的网页文件跟内容文档同名，如果指定了 `slug` ，则生成的网页文件使用它来作为文件名
* section 根据内容文档所在 section 来决定生成网页的位置，该参数不能通过文档头部指定，而是由内容文档在磁盘的位置决定
* `type` 用来指定内容文档的类型
* `url` 用URL来指定最终生成页面的位置

在 Hugo 中顶级内容层级被叫做 Section，上面样例含有三个 Section 分别是 about 和 post  以及 quote ，Section的逻辑含义就是将网站内容划分为几大块，可以看成网站内容的大类别。

同时 Hugo 支持 Section 与文档内容类型的关联，也即在某个 Section 创建的内容文档默认都是跟该 Section 同名的内容类型，如果想要改变这种默认的关联，可以在文档头部通过 `type` 来为文档指定内容类型。

此外 Hugo 会为每个 Section 自动创建一个页面用来展示该 Section 所有文章的列表，如果不满意 Hugo 自动为 Section 创建的展示页面可以在该 Section 目录中创建文件 `_index.md` 来自定义该页面的内容和文档头，并可以自定义模板文件 `/layouts/section/your-section-name.html` 来决定如何显示该 Section 的展示页面。

### 模板变量

如果说模板是待填充的网页，则模板变量是用来填充模板的内容。Hugo 内置了许多可以在模板中访问的变量，这些变量可以分为以下几种类型

* 网站变量

  通过网站变量，我们可以访问网站级别的配置和数据。

  ```
  .Site.BaseURL 			配置文件中为网站指定的 basse URL
  .Site.RSSLink 			网站的 RSS 链接
  .Site.Taxonomies 		网站所有的分类标签
  .Site.Pages				网站所有页面（仅含当前语言）
  .Site.AllPages			网站所有页面（含多语言）
  .Site.Params			配置文件中通过 params 定义的网站参数
  .Site.Sections			网站所有 Section（也即网站的顶级目录）
  .Site.Title				配置文件中为网站指定的 title
  .Site.Author			配置文件中为网站指定的 author
  .Site.Copyright			配置文件中为网站指定的 copyright
  .Site.LastChange		网站最后更新时间，格式跟内容文档头部 date 保持一致
  .Site.Data				网站自定义数据文件的访问接口
  .Site.RegularPages		网站中所有常规页面
  .Site.Files				网站所有源文件
  .Site.Menus				网站所有菜单
  .Site.LanguageCode		配置文件中为网站指定的 language code
  .Site.DisqusShortname	配置文件中为网站指定的 disqus 评论id
  .Site.GoogleAnalytics   配置文件中为网站指定的 google analytics tracking code
  .Site.Permalinks		配置文件中为网站指定的 permalink format
  .Site.BuildDrafts		配置文件中为网站指定的 build drafts
  .Site.IsMultiLingual	网站是否支持多语言
  .Site.Language			配置文件中指定的 language
  ```

* 页面变量

  通过页面变量，我们可以访问内容文档级别的配置和数据。

  ```
  .Title					内容文档的标题
  .Content				内容文档的内容
  .Date					内容文档的日期
  .PublishDate			页面发布日期
  .FuzzyWordCount			内容的近似字数
  .WordCount				内容的字数
  .Type					内容文档的内容类型
  .URL					页面的相对 URL
  .UniqueID				内容文档路径的md5值
  .Weidht					内容文档中定义的排序权重
  .Kind					页面类型
  .Params					内容文档头部定义的任意元数据都可以通过 .Params 来访问（不同定义如何命名，均以字母小写的名字访问）
  						补充：网站变量中也有 .Site.Params 来定义网站参数，一般来说页面参数比网站参数更具体，
  						可以使用模板函数 $.Param "header_image" 来访问网站和页面的同名参数
  .IsHome					页面是否为首页
  .IsPage					是否为常规内容页面
  .Next					下一个页面（根据页面发布日期）
  .Prev					上一个页面（根据页面发布日期）
  .NextInSection			当天Section中的下一个页面（根据页面分布日期）
  .PrevInSection			当天Section中的上一个页面（根据页面分布日期）
  .TableOfContents		页面目录
  .Permalink				页面的永久链接
  .RelPermalink			页面永久链接的相对路径
  .RawContent				页面的 Markdown 内容，当想要在网站中集成https://github.com/gnab/remark时，就需要提取页面的 Markdown 内容了
  .ReadingTime			页面大概需要花费的阅读时间
  .Section				页面所在 Section
  .Summary				页面摘要
  .Truncated				摘要是否截断页面
  .Description			描述
  .Keywords				关键词
  .LinkTitle				链接到当前页面时使用的 title
  .ExpiryDate				页面失效日期
  .Draft					页面是否为草稿
  .IsTranslated			页面是否有多语言版本
  .Translations			页面的多语言页面
  .Lang					语言
  .Language				语言对象
  ```

* 文件变量

  当页面的生成来源于内容文档时，可以访问内容文档文件相关信息。

  ```
  .File.Path				内容文档的相对路径，比如：content/posts/first.en.md
  .File.Dir				内容文档所在目录
  .File.LogicalName		内容文档文件名，比如：first.en.md
  .File.TranslationBaseName 内容文档根文件名，比如：first
  .File.Ext				内容文档扩展名，比如：md
  .File.Lang				内容文档的语言
  ```

* Hugo 变量

  ```
  .Hugo.Generator			Hugo 版本号的 meta tag，例如：<meta name="generator" content="Hugo 0.15" />
  .Hugo.Version			Hugo 二进制程序版本号
  ```

模板变量的作用域问题

单页模板、Section 列表模板以及 Taxonomy 列表模板均可以访问网站变量和页面变量，此外Taxonomy 列表模板可以访问代表其自身的 `.Data.Singular` 变量。

### 模板角色

模板文件混杂了 HTML 代码和模板标识符，用来设计网页布局的。Hugo 支持 Go 语言的 HTML 模板库来对网站进行布局规划，虽然模板文件本质上没有不同，可 Hugo 结合常用网站布局结构的需要将模板分为了几种角色，下面将依次介绍这些模板角色

也即页面类型

page home section taxonomy or taxonomy Term 

rss sitemap robotsTXT 404

#### 首页模板

Hugo 使用首页模板（homepage template）来渲染网站首页。一般来说网站首页同其它页面具有不一样的风格，因此需要专门为其使用特定的模板进行渲染。Hugo 在生成网站时，通常会依次从下面路径中查找首页模板，将找到的第一个文件作为首页模板：

- /layouts/index.html
- /layouts/_default/list.html
- /layouts/_default/single.html
- /themes/`THEME`/layouts/index.html
- /themes/`THEME`/layouts/_default/list.html
- /themes/`THEME`/layouts/_default/single.html

也即默认首页模板是 `index.html` ，当该文件不存在时，依次使用 `list.html` 和 `single.html` 来充当首页模板。另外首页模板中可以通过模板变量 `.Data.Pages` 来访问网站中所有内容文档，通常我们会遍历该变量在首页创建一个文档展示列表，不过Hugo 不会对模板的创建有任何限制，如何定义首页模板完全取决于自己。

#### 单页模板

Hugo 使用单页模板（single template）来渲染内容文档。换句话说，内容文档的内容将嵌入单页模板设计好的网页结构中，以此生成网页。那么当生成静态网站时，Hugo 会使用哪个单页模板来渲染内容文档呢？Hugo 会依次从下面路径列表中查找可用的单页模板，将找到的第一个单页模板文件作为当前内容文档的渲染模板：

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

其中 `TYPE` 表示内容文档的类型名称，`SECTION` 表示内容文档的 Section ，`THEME` 表示主题名称，`LAYOUT` 表示内容文档指定的模板名。`TYPE` 和 `LAYOUT` 可分别通过内容文档头部的 `type` （默认跟所在 Section 同名）和 `layout` （默认为单页模板）进行设置 ，`SECTION` 则由内容文档磁盘路径对应的 Section 决定。

可以看出 Hugo 默认会先从 `TYPE` 和 `SECTION` 这些模板目录中查找文档指定的布局 `LAYOUT` ，再查找相应的单页模板，然后再从网站源默认的布局目录 `_default` 中查找单页模板，最后会查找当前主题的相关布局目录，可见 Hugo 奉行的准则是：先精确查找，再回退默认。

在单页模板中可以访问网站变量和页面变量以及模板函数，通常我们会将内容文档的内容嵌入到单页模板中，有时也许还想为模板创建一个侧变量用来显示相关信息等，怎样定义单页模板完全取决于自己。

一般情况下，当我们为网站添加过主题之后，主题都会有单页模板的，如果想要覆盖主题中定义的单页模板，可以在网站源的模板目录下面创建相应的单页模板，或者直接创建单页模板 `layouts/_default/single.html` 作为内容文档未找到单页模板时的默认模板。

#### 内容视图

Hugo 使用内容视图（content views）来以不同于单页模板的方式展示内容文档。比如有时，我们只想要展示文档摘要或者文档列表项而非整个文档，内容视图在此时就特别有用了。

内容视图也是普通的模板文件，Hugo 查找内容视图时会根据当前文档的内容类型进行查找，也就是说同名的内容视图对不同内容类型渲染效果是不同的。Hugo 会依次从以下路径列表中查找可用的内容视图，将找到的第一个模板文件来作为渲染模板

- /layouts/`TYPE`/`VIEW`.html
- /layouts/_default/`VIEW`.html
- /themes/`THEME`/layouts/`TYPE`/`VIEW`.html
- /themes/`THEME`/layouts/_default/`view`.html

假定我们要为内容类型 `post` 和 `project` 分别创建内容视图 `li.html`  ，则对应的模板文件路径为：`/layouts/post/li.html` 和 `/layouts/project/li.html` 。如果我们在网站首页使用如下代码罗列所有文档

```
{{ range .Data.Pages }}
{{ .Render "li"}}
{{ end }}
```

其中 `{{ .Render "li" }}` 表示引用当前内容文档对应内容视图 `li.html` （`post` 和 `project` 使用各自的内容视图文件），在内容视图 `li.html` 中可以访问任何页面变量，下面是 `li.html` 示例

```html
<li>
<a href="{{ .Permalink }}">{{ .Title }}</a>
<div class="meta">{{ .Date.Format "Mon, Jan 2, 2006" }}</div>
</li>
```

#### 列表模板

Hugo 使用列表模板（list template）渲染多个被罗列的内容文档，比如：分类标签页面和 Section 页面通常需要罗列逻辑上从属于该类别的所有文档。值得注意的是，不同于单页文档总是被内容文档填充，列表模板一般却不会被内容文档填充（下文会介绍什么情况下列表模板也会填充内容文档）。

Hugo 中列表模板常见的应用场景有：Section 列表页、Taxonomy 列表页、Section RSS 以及 Taxonomy RSS等（注：网站首页虽然也是列表页，可因其特殊性，需要使用特定的模板渲染）。这些页面渲染后的 URL 路径分别如下

* Section 列表页

   `baseURL/SECTION/` ，例如：`http://1.com/post/` 

* Taxonomy 列表页

  `baseURL/PLURAL/TERM/` ，例如：`http://1.com/tags/python/` 

* Section RSS

  `baseURL/SECTION/index.html` ，例如：`http://1.com/post/index.html` 

* Taxonomy RSS

   `baseURL/PLURAL/TERM/index.html` ，例如：`http://1.com/tags/python/` 

此外，Hugo 会依次从路径列表中查找可用的列表模板，将找到的第一个列表模板文件来作为渲染模板。以上介绍的常见列表页面的查找路径如下

* Section 列表
  - /layouts/section/`SECTION`.html
  - /layouts/_default/section.html
  - /layouts/_default/list.html
  - /themes/`THEME`/layouts/section/`SECTION`.html
  - /themes/`THEME`/layouts/_default/section.html
  - /themes/`THEME`/layouts/_default/list.html
* Taxonomy 列表

  - /layouts/taxonomy/`SINGULAR`.html
  - /layouts/_default/taxonomy.html
  - /layouts/_default/list.html
  - /themes/`THEME`/layouts/taxonomy/`SINGULAR`.html
  - /themes/`THEME`/layouts/_default/taxonomy.html
  - /themes/`THEME`/layouts/_default/list.html
* Section RSS

  - /layouts/section/`SECTION`.rss.xml
  - /layouts/_default/rss.xml
  - /themes/`THEME`/layouts/section/`SECTION`.rss.xml
  - /themes/`THEME`/layouts/_default/rss.xml
* Taxonomy RSS
  - /layouts/taxonomy/`SINGULAR`.rss.xml
  - /layouts/_default/rss.xml
  - /themes/`THEME`/layouts/taxonomy/`SINGULAR`.rss.xml
  - /themes/`THEME`/layouts/_default/rss.xml


从上面模板的查找路径可以看出，Hugo 首先会查找为特定 `SECTION` 和 `TAXONOMY` 定义的模板文件，如果查找失败，会再查找 Section 和 Taxonomy 通用的模板文件，如果还是找不到就使用 `layouts/_defaults/list.html` 和 `layouts/_defaults/rss.xml` 。

既然知道了列表模板的用途，也知道了模板文件的查找路径，那么列表模板文件中该写些什么呢？列表文件也是一个普通的模板文件，在模板中可以使用任何 Go 内置模板函数，还可以访问网站模板变量和页面模板变量（用于 Taxonomy 的模板还可以访问代表当前分类的变量 `.Data.Singular` ）。根据列表模板的用途一般来说会在模板中为内容文档创建一个展示列表，此外也许希望对这个内容文档分类或者剔除某些文档，利用简洁而强大的 Go 模板方法可以自定义任何复杂的列表页面。下面是一个用于 Section 的列表模板示例

```html
{{ partial "header.html" . }}
{{ partial "subheader.html" . }}

<section id="main">
  <div>
   <h1 id="title">{{ .Title }}</h1>
        <ul id="list">
            {{ range .Data.Pages }}
                {{ .Render "li"}}
            {{ end }}
        </ul>
  </div>
</section>

{{ partial "footer.html" . }}
```

#### 分类模板

Hugo 使用分类模板（taxonomy terms template）来渲染当前分类下的所有标签。

要注意同Taxonomy 列表页相区分，Taxonomy 列表页用来罗列属于某个标签下所有的内容文档，优先查找模`/layouts/taxonomy/SINGULAR.html` 作为该标签列表页的模板，且将页面渲染于 `baseURL/PLURAL/TERM/` 。而分类模板页面是用来罗列当前分类下所有标签的，优先查找 `/layouts/taxonomy/SINGULAR.terms.html` 作为页面模板，且渲染于 `baseURL/PLURAL/` 。

Hugo 会依次从路径列表中查找可用的模板，将找到的第一个模板文件来作为渲染模板

* /layouts/taxonomy/`SINGULAR`.terms.html
* /layouts/_default/terms.html
* /themes/`THEME`/layouts/taxonomy/`SINGULAR`.terms.html
* /themes/`THEME`/layouts/_default/terms.html

如果以上模板都不存在，Hugo 就不会渲染分类标签页面。换句话说，分类标签页面的渲染也不一定必须单独使用一个模板文件，我们可以在页面侧边栏之类的地方来渲染分类标签（比如：侧边栏实现一个标签云）。

分类模板中除了可以访问网站变量和页面变量外，还有一些关于分类标签的变量可供我们使用：

```
.Data.Singular						分类的单数名称，比如：tag
.Data.Plural						分类的复数名称，比如：tags
.Data.Pages							属于当前分类的所有页面
.Data.Terms							属于当前分类的所有标签
.Data.Terms.Alphabetical			属于当前分类的所有标签（字母序）
.Data.Terms.ByCount					属于当前分类的所有标签（根据标签下文档数量排序）
```

下面是一个示例分类模板，该模板罗列出了当前分类下的所有标签，并给出了标签下所有文档的链接

```html
{{ partial "header.html" . }}
{{ partial "subheader.html" . }}

<section id="main">
  <div>
    <h1 id="title">{{ .Title }}</h1>

    {{ $data := .Data }}
    {{ range $key,$value := .Data.Terms.ByCount }}
    <h2><a href="{{ .Site.LanguagePrefix }}/{{ $data.Plural }}/{{ $value.Name | urlize }}">{{ $value.Name }}</a> {{ $value.Count }}</h2>
    <ul>
    {{ range $value.Pages.ByDate }}
      <li><a href="{{ .Permalink }}">{{ .Title }}</a></li>
    {{ end }}
    </ul>
    {{ end }}
  </div>
</section>

{{ partial "footer.html" . }}
```

#### 片段模板

Hugo 使用片段模板（partial template）作为其它模板文件的原材料，比如首页模板、单页模板、列表模板等这些模板通常会使用片段模板来创建。这里之所以将片段模板比作原材料，是因为片段模板通常包含了其它模板中的公共部分，反过来说，我们应该将多个模板中的公共内容分离出来创建片段模板文件，然后可以在其它模板中引用该片段文件。使用片段模板的好处在于，不需要重复定义相同的模板内容，而且片段模板十分有利于主题资源的开发，主题中应该将那些想要让用户覆盖的模板内容单独作为一个片段模板，这样主题的使用者只需要定义相同的片段模板就可以对主题片段模板进行替换，片段模板文件是比普通模板文件更加细粒度的模板内容容器。

如何创建片段模板呢？Hugo 默认将模板目录 `/layouts/partials/` 及其子目录中的模板文件看作片段模板，片段模板的内容如同普通模板一样可以访问各种模板变量和模板函数，不过片段模板可以访问到的模板变量取决于引用该模板时传入了怎样的变量进来（后面会有讲，如何引用片段模板以及如何传递变量到片段模板）。在网站中最为常见的片段模板也许就是网页头和网页脚，因为网页头和网页脚在网站大多数页面中都是相同的，将其分离于片段模板中是明智的选择，假设我们创建了 `/layouts/partials/header.html` 和 `/layouts/partials/footer.html` 片段模板文件，它们的内容分别为

```html
<!DOCTYPE html>
<html class="no-js" lang="en-US" prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb#">
<head>
    <meta charset="utf-8">

    {{ partial "meta.html" . }}

    <base href="{{ .Site.BaseURL }}">
    <title> {{ .Title }} : spf13.com </title>
    <link rel="canonical" href="{{ .Permalink }}">
    {{ if .RSSLink }}<link href="{{ .RSSLink }}" rel="alternate" type="application/rss+xml" title="{{ .Title }}" />{{ end }}

    {{ partial "head_includes.html" . }}
</head>
<body lang="en">
```

和

```html
<footer>
  <div>
    <p>
    &copy; 2013-14 Steve Francia.
    <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons Attribution">Some rights reserved</a>;
    please attribute properly and link back. Hosted by <a href="http://servergrove.com">ServerGrove</a>.
    </p>
  </div>
</footer>
<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-XYSYXYSY-X']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script');
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' :
        'http://www') + '.google-analytics.com/ga.js';
    ga.setAttribute('async', 'true');
    document.documentElement.firstChild.appendChild(ga);
  })();

</script>
</body>
</html>
```

以上模板内容除了常规的 HTML 代码外，还出现了像 `{{ partial "meta.html" . }}` 这样的模板语句，这条语句在这里的作用是引用片段模板 `meta.html` 到当前模板文件中（即 `header.html` 片段模板文件），就是说 Hugo 允许我们在片段模板中再次引用片段模板。

下面让我们研究一下，如何引用一个片段模板文件，引用片段模板的语法为：`{{ partial "path/to/file.html" variables }}` ，其中 `path/to/file.html` 表示被引用的片段模板文件相对于 `/layouts/partials/` 目录的路径，比如想要引用 `/layouts/partials/post/sidebar.html` ，则对应的引用路径为 `post/sidebar.html` 。其中 `variables` 表示要传入片段模板的变量（片段模板除了这些传入的变量，是无法访问其它变量的），通常我们会将代表当前模板内所有变量的 `.` 作为 `variables` 传入片段模板中。

有没有想过，很多模板引用相同的片段模板文件，在生成网页时，这些片段模板是不是在每个引用模板中都要重新渲染一次呢？有没有办法减少片段模板的渲染次数，毕竟片段模板生成的网页片段除了根据传入变量不同会有改变外，基本的网页结构是相似的。如果想要让 Hugo 提升片段模板的渲染效率（Hugo 会自动缓存已经渲染好的片段模板供后续使用），可以在引用模板文件时用 `partialCached` 来代替 `partial` ，并且 Hugo 还支持用户按照类别缓存片段模板，比如： `{{ partialCached "footer.html" . .Section }}` 的意思是，为每个 Section 渲染一次 `footer.html` 模板。



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



## Hugo配置

Hugo会在工作目录查找关于网站生成的配置文件`config.toml`，`config.yaml`，`config.json`。 这三个文件都可以用来为配置文件，只是配置信息的格式不同而已。

## Hugo工作目录结构

### 样例

```
.
├── config.toml
├── archetypes
|   └── default.md
├── content
|   ├── post
|   |   ├── firstpost.md
|   |   └── secondpost.md
|   └── quote
|   |   ├── first.md
|   |   └── second.md
├── data
├── i18n
├── layouts
|   ├── _default
|   |   ├── single.html
|   |   └── list.html
|   ├── partials
|   |   ├── header.html
|   |   └── footer.html
|   ├── taxonomies
|   |   ├── category.html
|   |   ├── post.html
|   |   ├── quote.html
|   |   └── tag.html
|   ├── post
|   |   ├── li.html
|   |   ├── single.html
|   |   └── summary.html
|   ├── quote
|   |   ├── li.html
|   |   ├── single.html
|   |   └── summary.html
|   ├── shortcodes
|   |   ├── img.html
|   |   ├── vimeo.html
|   |   └── youtube.html
|   ├── index.html
|   └── sitemap.xml
├── themes
|   ├── hyde
|   └── doc
└── static
    ├── css
    └── js
```

Hugo内容文档按照Sections以及Taxonomies来组织的，在该样例含有`post`和`quote`两个Section，Taxonomies含有`categories`和`tags`两种。

虽然Hugo会为分类，部分等结构创建首页，但是为这些首页添加自定义内容以及fontematter，需要在相应的目录下创建`_index.md`文件https://www.gohugo.io/content/using-index-md/

```
└── content
    ├── _index.md
    ├── categories
    │   ├── _index.md
    │   └── photo
    │       └── _index.md
    ├── post
    │   ├── _index.md
    │   └── firstpost.md
    └── tags
        ├── _index.md
        └── hugo
            └── _index.md
```



## 深入 Hugo

### 文档排序

当在列表页面展示多篇文档时，就涉及到文档先后顺序的问题了。Hugo 中文档默认是以元信息 `weight` 来排序，当文档未指定 `weight` 时，就以元信息 `date` 来排序，如果这两项都没有指定的话，列表页面看到的文档就是无序的。

不过除了上面 `weight` 和 `date` 外，Hugo 还支持我们以更多方式来排序列表页面，我们需要在列表模板文件中使用以下一些模板变量来控制文档的排序

* 按照元信息权重和日期排序（默认排序方式）

  ```
  {{ range .Data.Pages }}
  <li>
  <a href="{{ .Permalink }}">{{ .Title }}</a>
  <div class="meta">{{ .Date.Format "Mon, Jan 2, 2006" }}</div>
  </li>
  {{ end }}
  ```

* 按照元信息日期排序

  ```
  {{ range .Data.Pages.ByDate }}
    <!-- ... -->
  {{ end }}
  ```

* 按照发布日期排序

  ```
  {{ range .Data.Pages.ByPublishDate }}
    <!-- ... -->
  {{ end }}
  ```

* 按照失效日期排序

  ```
  {{ range .Data.Pages.ByExpiryDate }}
    <!-- ... -->
  {{ end }}
  ```

* 按照修改日期排序

  ```
  {{ range .Data.Pages.ByLastmod }}
    <!-- ... -->
  {{ end }}
  ```

* 按照文档内容长度排序

  ```
  {{ range .Data.Pages.ByLength }}
    <!-- ... -->
  {{ end }}
  ```

* 按照文档标题排序

  ```
  {{ range .Data.Pages.ByTitle }}
    <!-- ... -->
  {{ end }}
  ```

* 按照链接标题排序

  ```
  {{ range .Data.Pages.ByLinkTitle }}
    <!-- ... -->
  {{ end }}
  ```

* 按照其它元信息排序

  ```
  {{ range (.Date.Pages.ByParam "author.last_name") }}
    <!-- ... -->
  {{ end }}
  ```

* 反转排序（以上所有排序都可反转）

  ```
  {{ range .Data.Pages.ByTitle.Reverse }}
    <!-- ... -->
  {{ end }}
  ```

除此之外，文档还可以按照分类进行排序，而分类标签本身可以按照标签字母序来排序

```
<ul>
{{ $data := .Data }}
{{ range $key, $value := .Data.Taxonomy.Alphabetical }}
<li><a href="{{ .Site.LanguagePrefix }}/{{ $data.Plural }}/{{ $value.Name | urlize }}"> {{ $value.Name }} </a> {{ $value.Count }} </li>
{{ end }}
</ul>
```

或者按照关联到该分类标签的文档数量排序（即按照分类的热门程度排序）

```
<ul>
{{ $data := .Data }}
{{ range $key, $value := .Data.Taxonomy.ByCount }}
<li><a href="{{ .Site.LanguagePrefix }}/{{ $data.Plural }}/{{ $value.Name | urlize }}"> {{ $value.Name }} </a> {{ $value.Count }} </li>
{{ end }}
</ul>

```

属于某个分类的文档默认按照 `weight` 和 `date` 来排序，并且支持为文档指定分类排序时的权重，这样可以调整文档在分类中的顺序，这个功能通过文档中指定元数据 `taxonomyname_weight` 来实现，其中 `taxonomyname` 代表分类名。

### 文档分组

当在列表页面展示多篇文档时，Hugo 支持我们根据文档类型、日期或者 Section 来分组显示文档。

* 按照 Section 分组

  ```
  {{ range .Data.Pages.GroupBy "Section" }}
  <h3>{{ .Key }}</h3>
  <ul>
      {{ range .Pages }}
      <li>
      <a href="{{ .Permalink }}">{{ .Title }}</a>
      <div class="meta">{{ .Date.Format "Mon, Jan 2, 2006" }}</div>
      </li>
      {{ end }}
  </ul>
  {{ end }}
  ```

* 按照日期分组

  ```
  {{ range .Data.Pages.GroupByDate "2006-01" }}
    <!-- ... -->
  {{ end }}
  ```

* 按照发布日期分组

  ```
  {{ range .Data.Pages.GroupByPublishDate "2006-01" }}
    <!-- ... -->
  {{ end }}
  ```

* 按照其它元信息分组

  ```
  {{ range .Data.Pages.GroupByParam "param_key" }}
    <!-- ... -->
  {{ end }}
  ```

* 反转分组排序

  ```
  {{ range (.Data.Pages.GroupByDate "2006-01").Reverse }}
    <!-- 利用模板函数Reverse来反转 -->
  {{ end }}

  {{ range .Data.Pages.GroupByDate "2006-01" "desc" }}
    <!-- 或者直接指定排序方向 -->
  {{ end }}
  ```

* 组内文档排序

  ```
  {{ range .Data.Pages.GroupByDate "2006-01" "asc" }}
  <h3>{{ .Key }}</h3>
  <ul>
      {{ range .Pages.ByTitle }}
      <!-- 可以按照之前介绍排序文档的各种方法来排序组内文档 -->
      {{ end }}
  </ul>
  {{ end }}
  ```

### 文档过滤

有时候也许想要排除某些文档在列表页面显示，Hugo 支持我们在列表页面限制文档显示数量以及限制显示的文档种类。

* 限制文档显示数量

  ```
  {{ range first 10 .Data.Pages }}
      <!-- 利用模板函数first，只显示排在前面的10篇文档 -->
      {{ .Render "summary" }}
  {{ end }}
  ```

* 根据条件过滤某些文档

  ```
  {{ range where .Data.Pages "Section" "post" }}
     <!-- 利用模板函数where，只筛选显示Section为post的文档 -->
     {{ .Content }}
  {{ end }}

  {{ range first 5 (where .Data.Pages "Section" "post") }}
     <!-- 同时使用where和first -->
     {{ .Content }}
  {{ end }}
  ```

### 文档摘要

Hugo 默认会截取文档前70个词作为文档摘要，并将摘要内容存放在模板页面变量 `.Summary` ，同时提供模板变量 `.Truncated` 来记录截取的摘要是否包含了文档的全部内容。同时 Hugo 还支持我们在内容文档中明确指定将哪些内容作为该文档的摘要，具体来说需要在文档中插入一行 `<!--more-->` 来标识位于该行之前的内容作为摘要，同理 Hugo 会将摘要存放在模板页面变量 `.Summary` ，并用模板变量 `.Truncated` 标识摘要是否包含了文档全部内容。

利用文档的摘要功能可以实现“阅读更多...”这样的功能，示例如下

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

### 引用文档

在书写文档时，经常要插入其它文档的链接或者插入当前文档某个位置的链接（即锚点）。Hugo 提供了两种 shortcode 用来在 Markdown 内容中插入引用链接：`ref` 和 `relref` ，其中 `relref` 插入被引用文档相对于当前文档的链接地址，而 `ref` 则插入被引用文档的完整链接地址。

使用示例如下

```
{{< ref "#anchor-in-current-document" >}}
{{< relref "#anchor-in-current-document" >}}
{{< ref "blog/about.md" >}}
{{< relref "blog/about.md" >}}
{{< ref "blog/about.md#anchor-in-other-document" >}}
{{< relref "blog/about.md#anchor-in-other-document" >}}
```

上面插入的代码最终会被 Hugo 顺次转换为

```
#anchor-in-current-document:aj24jd83
#anchor-in-current-document:aj24jd83
baseURL/blog/about/
/blog/about/
baseURL/blog/about/#anchor-in-other-document:83jdfoi33
/blog/about/#anchor-in-other-document:83jdfoi33
```

这里有几点需要注意

* 文档路径参数

  `ref` 和 `relref` 均需要输入一个文档路径参数，该路径是相对于内容目录 `content` 的路径。此外还可以直接输入文档名，但当不同 Section 中含有相同文档名时就会产生二义性，因此建议使用相对于 `content` 的路径名。

* 锚点参数

  `ref` 和 `relref` 还可接受锚点参数，锚点可以是当前文档内的，也可以是其它文档中的，值得注意的是 Hugo 在生成含有锚点的链接时自动添加了一个随机后缀，后面会解析为什么要添加后缀。

* 相对链接和绝对链接地址

  到底该使用 `ref` 还是 `relref` 呢？二者的区别就在于生成的链接是否含有网站的 baseURL ，不含 baseURL 的好处在于，当 baseURL 改变时网站不需要重新生成，这样看来 `relref` 可移植性更好。

前面一直提到文档锚点的引用，那么文档锚点是怎么来的，是 Hugo 自动生成的，还是我们自定义的呢？其实在 Hugo 将 Markdown 文档转换为网页时，自动为 Markdown 文档内的标题级内容生成了锚点以供引用，并且 Hugo 还保证了锚点在文档内以及整个站点内的唯一性。

那么 Markdown 文档中标题级内容是如何转化为锚点的呢？假设标题内容为：Hugo: A Fast & Modern Static Web Engine，最终被转换成锚点 `hugo-a-fast-modern-static-web-engine` 。标题到锚点转换过程为：先将其转换为小写内容，再将非字母数字字符用连字符替换，并将多余的连字符去除。除了让 Hugo 自动将标题内容转为锚点，Hugo 还支持文档作者为标题指定固定的锚点，比如这样定义标题内容：`# Hugo: A Fast & Modern Static Web Engine {#hugo-main}` ，然后 Hugo 在生成站点时就会为该标题生成锚点 `hugo-main` 。此外当页面中出现相同锚点时，Hugo 会自动外这些锚点添加后缀 `-1` 、`-2` 等。

此外[官网介绍](http://gohugo.io/extras/crossreferences/)，为了确保标题锚点全站的唯一性，Hugo 会根据内容文档的路径为其生成一个独一无二的标识串，并在为锚点生成链接时会添加该文档标识作为锚点后缀。另外提到列表页为了避免锚点冲突也使用到了文档唯一标识串。这两点有些不太懂，为何要确保全站锚点唯一性，列表页又为何会出现锚点冲突的情况？留待以后填坑，，，

### Shortcode

用 Markdown 这类标记语言书写文档，将文档的渲染交给模板处理，使得我们在书写文档时只要将精力集中在内容而非内容的展示效果上，相信这是我们使用 Markdown 这类标记语言的主要原因。可这种简洁性带来的负面效果是，有时内容本身就是复杂的，需要以 Markdown 不支持的格式嵌入到文档中，通常的解决方案是，直接将 HTML 代码嵌入文档来支持相应的格式，可是这样显然又背离了 Markdown 语言的简洁性。而 Hugo 中的 shortcode 正是为此而生的，既使内容保持了 Markdown 的简洁性，又可以允许我们在文档中嵌入一些 Markdown 不支持的高级格式。简单来说，shortcode 是一些我们可以直接插入内容文档中的助记符，在 Hugo 生成网站时，会将这些助记符替换为相应的 HTML 代码片段。这样的好处在于，HTML 片段托管给 Hugo 管理，只在文档中插入 shortcode，使得跟内容无关的 HTML 格式代码被剥离出来，便于以后对格式的修改更新。

#### 插入内容文档的语法

内容文档中插入 shortcode 的语法如下

```
{{% shortcodename parameters %}}
```

其中 `shortcodename` 指相应 shortcode 的名字，`parameters` 指为该 shortcode 输入的参数，参数允许以位置参数或命名参数的形式输入，参数之间用空格间隔，如果参数本身含有空格则需要为其添加双引号。

有的 shortcode 是含有关闭标记的

```
{{% shortcodename parameters %}} something {{% /shortcodename %}}
```

其中 `{{% /shortcodename %}}` 表示关闭标记，可以看出比开始标记多了一个斜杠。

除了上面这种 shortcode 语法外，还有另外一种常见 shortcode 语法

```
{{< shortcodename parameters >}} something {{< /shortcodename >}}
```

其中用 `<` 和 `>` 替换了前面的 `%` ，二者的不同在于，使用 `%` 语法则 shortcode 内部的内容（就是那个 `something` ）会被 Markdown 处理器处理，也即内部的 Markdown 语法会被解析为相应的 HTML ，而使用 `<` 和 `>` 语法时，内部内容不被 Markdown 处理器解析。

#### Hugo 内置 shortcode

Hugo 预先定义了一些较为常用的 shortcode ，下面一一介绍如何使用以及在什么情形下使用这些 shortcodes

* 高亮

  用来高亮文档中的代码片段，用法样例如下

  ```
  {{< highlight python >}}
  def pt(txt):
  	print(txt)
  {{< /highlight >}}
  ```

* 图片

  用来扩展 Markdown 中插入图片的语法，该 shortcode 插入的图片支持自定义 CSS 类、添加链接和 caption 等高级功能，用法样例如下

  ```
  {{< figure src="/media/spf13.jpg" title="Steve Francia" link="" caption="" class="" attr="" attrlink="" alt="" >}}
  ```

* 文档引用

  用来在文档中引用其它文档或者当前文档内部某个锚点，用法样例如下

  ```
  [Who]({{< ref "about.md#who" >}})
  [Who]({{< relref "about.md#who" >}})
  ```

  只需给出被引用文档的相对路径，Hugo 会自动将其替换为相应文档的永久链接，`ref` 和 `relref` 的不同之处在于，后者会给出相对路径链接，而前者给出绝对路径链接。

* Twitter 推文

  用来在内容中插入一条 tweet ，推文的链接是这样的： [https://twitter.com/spf13/status/666616452582129664](https://twitter.com/spf13/status/666616452582129664) ，插入这条推文的 shortcode 如下

  ```
  {{< tweet 666616452582129664 >}}
  ```

* YouTube 视频

  用来在内容中插入 YouTube 视频，YouTube 视频资源链接是这样的： [https://www.youtube.com/watch?v=w7Ft2ymGmfc](https://www.youtube.com/watch?v=w7Ft2ymGmfc) ，插入该视频的 shortcode 如下

  ```
  {{< youtube w7Ft2ymGmfc >}}
  ```

  或者开启自动播放

  ```
  {{< youtube id="w7Ft2ymGmfc" autoplay="true" >}}
  ```

* Vimeo 视频

  同插入 YouTube 视频类似，假设资源链接为：[https://vimeo.com/channels/staffpicks/146022717](https://vimeo.com/channels/staffpicks/146022717) ，则插入语法如下

  ```
  {{< vimeo 146022717 >}}
  ```

* GitHub 代码片段

  用来在文档中插入 GitHub 上创建的代码片段，假设代码片段链接为：[https://gist.github.com/username/id](https://gist.github.com/username/id) ，则插入语法如下

  ```
  {{< gist username id >}}
  ```

* Speaker Deck 演示文稿

  [Speaker Deck](https://speakerdeck.com/) 是一个允许我们共享演示文稿的地方，我们可以将共享在其上的演示文稿插入到内容文档中，在 Speaker Deck 上点击分享后会生成一段 HTML 代码，假设其中的 `data-id="123456"` ，那么在文档中可以使用如下语法插入该演示文稿

  ```
  {{< speakerdeck 123456 >}}
  ```

* Instagram 图片

  插入 Instagram 上的图片，假设某张图片链接为：[https://www.instagram.com/p/BMokmydjG-M/](https://www.instagram.com/p/BMokmydjG-M/) ，则插入该图片的语法为

  ```
  {{< instagram BMokmydjG-M >}}
  ```

  或

  ```
  {{< instagram BMokmydjG-M hidecaption >}}
  ```

#### 自定义 shortcode

shortcode 本质就是将助记符关联的 HTML 片段插入到文档中，Hugo 支持自定义 shortcode ，需要做的十分简单，只要在模板目录 `layouts/shortcodes/` 中创建模板文件即可，模板文件名即为 shortcode 的名称。

先来看几个 Hugo 内置 shortcode 对应的模板文件内容（内置 shortcode 并不存在相应的模板文件）

* 高亮

  ```
  {{ .Get 0 | highlight .Inner  }}
  ```

* 图片

  ```
  <figure {{ with .Get "class" }}class="{{.}}"{{ end }}>
      {{ with .Get "link"}}<a href="{{.}}">{{ end }}
          <img src="{{ .Get "src" }}" {{ if or (.Get "alt") (.Get "caption") }}alt="{{ with .Get "alt"}}{{.}}{{else}}{{ .Get "caption" }}{{ end }}"{{ end }} />
      {{ if .Get "link"}}</a>{{ end }}
      {{ if or (or (.Get "title") (.Get "caption")) (.Get "attr")}}
      <figcaption>{{ if isset .Params "title" }}
          <h4>{{ .Get "title" }}</h4>{{ end }}
          {{ if or (.Get "caption") (.Get "attr")}}<p>
          {{ .Get "caption" }}
          {{ with .Get "attrlink"}}<a href="{{.}}"> {{ end }}
              {{ .Get "attr" }}
          {{ if .Get "attrlink"}}</a> {{ end }}
          </p> {{ end }}
      </figcaption>
      {{ end }}
  </figure>
  ```

* YouTube 视频

  ```
  <div class="embed video-player">
  <iframe class="youtube-player" type="text/html" width="640" height="385" src="http://www.youtube.com/embed/{{ index .Params 0 }}" allowfullscreen frameborder="0">
  </iframe>
  </div>
  ```

可以看出用来定义 shortcode 的模板文件跟普通的模板文件没有差别，基本就是 HTML 代码跟模板变量的混合体，不过 shortcode 模板除了可以访问常规模板变量外，还可以额外访问几个变量和方法

```
{{ .Get 0 }}					获取位置参数
{{ .Get "name" }}				获取命名参数
{{ with .Get "class"}} <p class="{{.}}"> haha! </p>{{ end }}
.Inner							位于 shortcode 开闭之间的内容
.Params							输入的参数列表
.IsNamedParams					判断 shortcode 输入的是位置参数还是命名参数
.Parent							shortcode 支持继承，该变量表示父 shortcode
.Page							所有的页面变量在 shortcode 都可用
```

### 自定义404页面

使用 Hugo 创建404页面十分简单，创建模板文件 `/layouts/404.html` ，Hugo 生成网站时在网站根目录就会有一个 `404.html` 文件，至于如何在用户访问错误时展示404页面则取决于网站部署在了哪里。

404模板示例

```html
{{ partial "header.html" . }}
{{ partial "subheader.html" . }}

<section id="main">
  <div>
   <h1 id="title">{{ .Title }}</h1>
  </div>
</section>

{{ partial "footer.html" . }}
```

网站部署在 GitHub 时，用户访问错误会自动重定向到404页面。如果网站是部署到自己服务器上的，则需要配置服务器在访问错误时加载404页面。对于 Apache 服务器，需要在网站根目录创建 `.htaccess` 并写入 `ErrorDocument 404 /404.html` 。对于 Nginx 服务器，需要在服务器配置文件 `nginx.conf` 中写入 `error_page 404 = /404.html;` 。

### 模板调试

模板编写中错误在所难免，可以使用模板函数 `printf` 调试模板变量，下面是几个常见调试样例

```
{{ printf "%#v" . }}
{{ printf "%#v" $.Site }}
{{ printf "%#v" .Permalink }}
{{ range .Data.Pages }}
    {{/* The context, ".", is now a Page */}}
    {{ printf "%#v" . }}
{{ end }}
```

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

