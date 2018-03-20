---
title: Markdown简介
author: Xiao Wenbin
date: 2016/10/29
category: markdown
---

**Markdown** is created by [Daring Fireball](http://daringfireball.net/), the original guideline is [here](http://daringfireball.net/projects/markdown/syntax). Its syntax, however, varies between different parsers or editors.

## 哲学

> Markdown is intended to be as easy-to-read and easy-to-write as is feasible.
>
> Readability, however, is emphasized above all else. A Markdown-formatted document should be publishable as-is, as plain text, without looking like it’s been marked up with tags or formatting instructions.
>
> Markdown’s syntax is comprised entirely of punctuation characters, which punctuation characters have been carefully chosen so as to look like what they mean. E.g., asterisks around a word actually look like *emphasis*. Markdown lists look like, well, lists.

可读性最重要

## Markdown 和 HTML

Markdown文档中可以直接插入大多数HTML标签。HTML的区段标签（如：`<span><cite><del>`等）甚至可以直接插入到Markdown的段落、列表等语法中。同时某些HTML区块标签的插入存在一些限制（如： `<div><table><pre><p>` 等），必须在前后加上空行与其它内容隔开，还要求它们的开始标签与结尾标签不能用制表符或空格来缩进。

在HTML区块标签内的Markdown语法将不会被处理，但在 HTML 区段标签间的Markdown格式语法却会被处理。

> Markdown’s syntax is intended for one purpose: to be used as a format for *writing* for the web.
>
> Markdown is not a replacement for HTML, or even close to it. Its syntax is very small, corresponding only to a very small subset of HTML tags. The idea is *not* to create a syntax that makes it easier to insert HTML tags. In my opinion, HTML tags are already easy to insert. The idea for Markdown is to make it easy to read, write, and edit prose. HTML is a *publishing* format; Markdown is a *writing* format. Thus, Markdown’s formatting syntax only addresses issues that can be conveyed in plain text.
>
> For any markup that is not covered by Markdown’s syntax, you simply use HTML itself. There’s no need to preface it or delimit it to indicate that you’re switching from Markdown to HTML; you just use the tags.

Markdown 是一种针对 web 的书写格式，而 HTML 则是针对 web 的发布格式，二者完全不同。Markdown 的设计初衷是，使得编辑、阅读纯文本文档变得简单，而不是要取代 HTML 或者替代 HTML 的部分子集。

至于说 Markdown 文档将以任何形式发布，则是另外一回事，不过一般会以 HTML 形式发布，这就需要用到 Markdown 到 HTML 的转换工具了。

Markdown 语法仅仅解决可以通过纯文本来表达的问题。在无法用 Markdown 来进行表达时，允许创作者自由的使用原生的 HTML。既保证了纯文本的简洁性，又结合了 HTML 丰富的表现力。

不过对于 block-level HTML elements — e.g. `<div>`,`<table>`, `<pre>`, `<p>`, etc. 插入它们时，一定要将它们更前后的内容用空行来分隔开，并且开始标记和结束标记不能被缩进。同时要注意，位于 block-level HTML  标记内的 Markdown 语法将不被解析，Note that Markdown formatting syntax is not processed within block-level HTML tags.

不过对于 Span-level HTML tags — e.g. `<span>`, `<cite>`, or `<del>` — can be used anywhere in a Markdown paragraph, list item, or header. 它们可以用在文档中任何地方。并且位于 span-level HTML 标记内的 Markdown 语法可以被解析。

## 用 Markdown 写 HTML 更方便

HTML 由于给标记和实体字符的冲突，要对内容中出现的 < 和 & 转义处理：In HTML, there are two characters that demand special treatment: `<`and `&`. Left angle brackets are used to start tags; ampersands are used to denote HTML entities. If you want to use them as literal characters, you must escape them as entities, e.g. `&lt;`, and `&amp;`. 如果没有转义的话，一般会引起 HTML 解析错误。

Markdown 解析器对 < 和 & 的处理，是智能的，可以判断 < 和 & 是 HTML 的语法部分，还是正文中出现的，如果是正文中出现的话，就自动将其替换为 `&lt;` 和 `&amp;`，如果是语法部分则保持不变。

This makes it easy to use Markdown to write about HTML code. (As opposed to raw HTML, which is a terrible format for writing about HTML syntax, because every single `<` and `&` in your example code needs to be escaped.)

## markdown 转义

markdown 的元字符可以使用 `\` 进行转义，这样的话，即使语法规则符合，也不会被 Markdown 引擎解析

# 块元素 Block Elements

跟周围的内容用空行间隔开

## 段落 Paragraphs

一个 Markdown 段落是由一个或多个连续的文本行组成，它的前后要有一个以上的空行（空行定义为看起来是空的，便会被视为空行。比方说，若某一行只包含空格和制表符，则该行也会被视为空行）。并且在Markdown中段落从行首开始，不要用空格或制表符来缩进。如果在行尾结束时添加两个空格再敲回车，则Markdown转换为 html 文档时会在该段落后插入`<br/>`元素进行强制换行。  

要注意的是 HTML 在显示时，会将换行以及多个空白都显示为一个空格符，因此 Markdown 中多个连续的文本行并不意味着最终得到的 HTML 也是多行，除非使用上面介绍的强制换行或者用空白行隔开为多个 Markdown 段落。

Markdown’s email-style [blockquoting](https://daringfireball.net/projects/markdown/syntax#blockquote) and multi-paragraph [list items](https://daringfireball.net/projects/markdown/syntax#list)work best — and look better — when you format them with hard breaks.

## 标题 Headers

Markdown 支持两种风格的标题：一种是在标题内容后面一行用不少于一个 `=` 或 `-` 符号来标注，其中 `=` 表示一级标题，`-` 表示二级标题；另外一种风格是在行首用 1~6 个 `#` 来分别表示 6 个级别的标题，如果为了看起来美观可以在标题结尾添加任意数量的 `#` 字符，此外 `#` 和标题内容之间可以用空格隔开，也可以不隔开。



## 块引用 Blockquotes

在引用内容的每行前面添加 `>`，并且引用内容又可以被段落语法解析，也即如果引用内容有被空白行隔开的话，最终会形成多个段落。

此外还支持每个段落（多个连续的文本行）仅使用一个 `>`

连续书写的多个引用，最终会被转换为同一个引用中的多个段落。

引用支持嵌套

支持在引用中写其他的 Markdown 语法：Blockquotes can contain other Markdown elements, including headers, lists, and code blocks:



> 生命的意义在于不断的去探索、去寻找
>
> > 还可以嵌套引用
>
> ### 引用中可以使用标题语法
>
> * 列表项1
> * 列表项2
>
> 引用中使用区块代码语法：
>
> ```python
> def test():
> 	pass
> ```



## 列表 Lists

无序和有序列表

无序使用 `*`, `-`, `+`

有序使用数字和点号，如 `1.`

有序列表中列表项的输出顺序跟数字序标无关，跟书写顺序相关。It’s important to note that the actual numbers you use to mark the list have no effect on the HTML output Markdown produces. 

列表符号前后的空白：List markers typically start at the left margin, but may be indented by up to three spaces. List markers must be followed by one or more spaces or a tab.

对于多行内容，列表支持悬挂式缩进，在最终转换时会自动移除多余的空白：

```
悬挂式缩进列表（更美观）
*   Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
    Aliquam hendrerit mi posuere lectus. Vestibulum enim wisi,
    viverra nec, fringilla in, laoreet vitae, risus.
*   Donec sit amet nisl. Aliquam semper ipsum sit amet velit.
    Suspendisse id sem consectetuer libero luctus adipiscing.
没有缩进也可以
*   Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
Aliquam hendrerit mi posuere lectus. Vestibulum enim wisi,
viverra nec, fringilla in, laoreet vitae, risus.
*   Donec sit amet nisl. Aliquam semper ipsum sit amet velit.
Suspendisse id sem consectetuer libero luctus adipiscing.
```

对于多个段落，后续段落必须缩进 4 个空格或是 1 个制表符，同样一个段落中的多行内容，缩进不缩进都可以

列表项中可以嵌套，块引用和代码块，在缩进 8 个空格或是 2 个制表符后，在使用相应的语法：

```
*   A list item with a blockquote:

    > This is a blockquote
    > inside a list item.

*   A list item with a code block:

        <code goes here>
```



* 列表项目标记通常放在最左边，但是其实也可以缩进，最多 3 个空格，项目标记后面一定要接着至少一个空格或制表符
* 如果列表项目间用空行分开，则在转换为HTML时项目内容会用`<p>`标签包起来
* 列表是可以嵌套的
  * 嵌套列表项1
  * 嵌套列表项2


* 列表项目可以包含多个段落，且段落必须缩进 4 个空格或是 1 个制表符

  列表项中的一个段落

  列表项中的另一个段落

* 如果要在列表项目内包含引用，那引用标记`^`就需要缩进4 个空格或是 1 个制表符

  > 包含在列表项目中的引用内容



* 如果要在列表项目内包含代码区块，该区块就需要缩进 8 个空格或是 2 个制表符

        <代码写在这里>




## 代码区块 Code Blocks

Pre-formatted code blocks are used for writing about programming or markup source code. Rather than forming normal paragraphs, the lines of a code block are interpreted literally. Markdown wraps a code block in both `<pre>` and `<code>` tags.

下面是代码区块： indent every line of the block by at least 4 spaces or 1 tab. A code block continues until it reaches a line that is not indented (or the end of the article).

    程序文档等内容通常会有已经排版好的格式，我们不希望以一般段落格式去展示它们，而是希望以原来看到的排版方式来呈现。
    代码区块转换为HTML时，会被<pre>和<code>标签来把代码区块的内容包起来

可以很容易的在代码块中书写 HTML：代码块中的 `&` `<` `>` 将被转换为 HTML 实体

Within a code block, ampersands (`&`) and angle brackets (`<` and `>`) are automatically converted into HTML entities. This makes it very easy to include example HTML source code using Markdown

可以很容易的在代码块中书写 Markdown：代码块中的 markdown 语法不会被解析

Regular Markdown syntax is not processed within code blocks. E.g., asterisks are just literal asterisks within a code block. This means it’s also easy to use Markdown to write about Markdown’s own syntax.

## 分割线 horizontal rules

三个及以上的 `*` 或 `-` 或 `_`



---



# 行内元素 span elements





## 链接

Markdown supports two style of links: *inline* and *reference*. In both styles, the link text is delimited by [square brackets].

### inline link

要建立一个行内式的链接，只要在方块括号后面紧接着圆括号并插入网址链接即可，如果你还想要加上链接的 title 文字，再用双引号把 title文字包起来加在尾部即可，例如：[点击](http://www.baidu.com/ "必应搜索") 访问必应官网。

If you’re referring to a local resource on the same server, you can use relative paths:

```
See my [About](/about/) page for details.  
```

如果是要链接到本机目录的话，可以使用相对路径地址，例如：[点击](/about.html)查看个人信息主页。

### reference link

此外还以使用引用式链接，即将链接内容和链接的使用分开来写，如果同一链接在文档中出现多次，显然引用式只需要在文档中插入一次链接内容，这样更加方便。引用式链接的使用语法跟行内式链接稍有不同，引用式链接的定义可以出现在文档中任意位置：一般选择放在被引用段落后或者文档尾部。

```
This is [an example][id] reference-style link.
This is [an example] [id] reference-style link.
[id]: http://example.com/  "Optional Title Here"

```

- link id 可以有字母、数字、空格以及标点，不区分大小写
- Square brackets containing the link identifier (optionally indented from the left margin using up to three spaces);
- followed by a colon;
- followed by one or more spaces (or tabs);
- followed by the URL for the link;
- optionally followed by a title attribute for the link, enclosed in double or single quotes, or enclosed in parentheses.

The link URL may, optionally, be surrounded by angle brackets:

```
[id]: <http://example.com/>  "Optional Title Here"
```

You can put the title attribute on the next line and use extra spaces or tabs for padding, which tends to look better with longer URLs:

```
[id]: http://example.com/longish/path/to/resource/here
    "Optional Title Here"
```

The *implicit link name* shortcut allows you to omit the name of the link, in which case the link text itself is used as the name. Just use an empty set of square brackets — e.g., to link the word “Google” to the google.com web site, you could simply write:

```
Visit [Daring Fireball][] for more information.
```

And then define the link:

```
[Daring Fireball]: http://daringfireball.net/
```

引用链接是文档可读性更强

The point of reference-style links is not that they’re easier to write. The point is that with reference-style links, your document source is vastly more readable.

下面是一个参考式链接的范例：

我比较喜欢[Google][1]，[Yahoo][2]，[MSN][3]等网站。

[1]: http://google.com/        "Google"
[2]: http://search.yahoo.com/  "Yahoo Search"
[3]: http://search.msn.com/    "MSN Search"

链接插入的简写语法：<http://example.com>

## 强调 Emphasis

Markdown treats asterisks (`*`) and underscores (`_`) as indicators of emphasis. Text wrapped with one `*` or `_` will be wrapped with an HTML `<em>` tag; double `*`’s or `_`’s will be wrapped with an HTML`<strong>` tag.

Emphasis can be used in the middle of a word:

```
un*frigging*believable

```

But if you surround an `*` or `_` with spaces, it’ll be treated as a literal asterisk or underscore. 不能和被强调的内容用空白隔开。

使用 `\` 对元字符转义



*single asterisks*

_single underscores_

**double asterisks**

__double underscores__

## 行内代码 code span

To indicate a span of code, wrap it with backtick quotes.

To include a literal backtick character within a code span, you can use multiple backticks as the opening and closing delimiters, 为了使得开始和尾部可以包含 backtick quote，允许空白，The backtick delimiters surrounding a code span may include spaces — one after the opening, one before the closing. This allows you to place literal backtick characters at the beginning or end of a code span:

```
A single backtick in a code span: `` ` ``

A backtick-delimited string in a code span: `` `foo` ``
```

代码行内的 `&` `<` `>` 会被自动转换为 HTML实体



`printf()` 是最常见的C语言函数之一



## 图片 Images

跟链接类似支持：inline 和 reference 两种风格语法

![Alt text](/path/to/img.jpg "Optional title")

![Alt text][id]

[id]: url/to/image  "Optional title attribute"

添加的文件将作为 `<img>` 元素的 `alt` 属性，用单引号会双引号包括

到目前为止， Markdown 还没有办法指定图片的宽高，如需要的话，可以使用HTML的 `<img>` 标签。



# Misc

## link shortcut

Markdown supports a shortcut style for creating “automatic” links for URLs and email addresses: simply surround the URL or email address with angle brackets.

```
<http://example.com/>
```

```
<a href="http://example.com/">http://example.com/</a>
```

电子邮件地址的自动链接的工作方式与此类似，但Markdown还会执行一些随机化的十进制和十六进制实体编码，以帮助屏蔽地址收集spambots的地址。

## backslash escape

Markdown allows you to use backslash escapes to generate literal characters which would otherwise have special meaning in Markdown’s formatting syntax.

Markdown provides backslash escapes for the following characters:

```
\   backslash
`   backtick
*   asterisk
_   underscore
{}  curly braces
[]  square brackets
()  parentheses
#   hash mark
+   plus sign
-   minus sign (hyphen)
.   dot
!   exclamation mark
```



