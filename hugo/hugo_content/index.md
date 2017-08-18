### content

该目录顾名思义是用来存放内容文档的目录。Hugo 假设你对该目录的组织是有特定意图的，因此在生成网站时，Hugo 会按照该目录的结构来规划网站的目录组织结构，也即除了内容文档外（内容文档需要被转换为 HTML 文件），其余文件以及目录结构都被原样复制到生成的网站目录中。

默认情况下，目录组织结构决定内容文档的类型。由于在生成网站时，网站会按照该目录下的第一级子目录来将内容划分为几个部分，所以该目录下的第一级子目录被称为 Section，而且默认某个子目录中的内容文档类型名跟该子目录名相同，比如位于 `content/post/content.md` 的内容文档，其类型为 `post` 。可见对该目录下第一级子目录的划分，等价于对内容文档的类型进行划分，不过内容文档的类型除了由所在目录决定外，还可以通过在头部指定字段 `type` 来决定。其实在 Hugo 中 Section 和 文档类型这两个概念是独立的，但由于位于同一个 Section 目录的内容文档通常具有相同的类型，所以在大多数情况下可以不对它们进行区分。

在 Hugo 中内容文档类型的概念很重要。内容目录中的第一级子目录名代表了相应的文档类型；使用命令新建内容文档时，会根据文档类型来使用相应的原型（先在目录 `archetypes` 中查找有无同名原型，没有的话就使用默认原型）；渲染内容文档时，会根据文档类型来使用相应的模板（先在目录 `layouts` 中查找有无同名模板目录，没有的话就使用默认模板）。



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

- `slug` 默认情况下生成的网页文件跟内容文档同名，如果指定了 `slug` ，则生成的网页文件使用它来作为文件名
- section 根据内容文档所在 section 来决定生成网页的位置，该参数不能通过文档头部指定，而是由内容文档在磁盘的位置决定
- `type` 用来指定内容文档的类型
- `url` 用URL来指定最终生成页面的位置

在 Hugo 中顶级内容层级被叫做 Section，上面样例含有三个 Section 分别是 about 和 post  以及 quote ，Section的逻辑含义就是将网站内容划分为几大块，可以看成网站内容的大类别。

同时 Hugo 支持 Section 与文档内容类型的关联，也即在某个 Section 创建的内容文档默认都是跟该 Section 同名的内容类型，如果想要改变这种默认的关联，可以在文档头部通过 `type` 来为文档指定内容类型。

此外 Hugo 会为每个 Section 自动创建一个页面用来展示该 Section 所有文章的列表，如果不满意 Hugo 自动为 Section 创建的展示页面可以在该 Section 目录中创建文件 `_index.md` 来自定义该页面的内容和文档头，并可以自定义模板文件 `/layouts/section/your-section-name.html` 来决定如何显示该 Section 的展示页面。



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

