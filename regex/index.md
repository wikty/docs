---
date: 2017/12/31
---

[TOC]



# Regular Expression



## Introduction

### 应用背景

日常工作中我们需要处理许多数据，比如文本、表格、图片等数据。不同的数据有其自身的特点，同时也有各种便利的软件可用，比如 Excel 用来处理表格数据、Photoshop 用来处理图片数据。在所有的数据中，文本数据也许是最为基本和常见的数据类别，高效的处理文本数据极为必要，而在文本数据的处理中最常见的任务莫过于字符串的查找、替换等。本文介绍的正则表达式，可以轻松的完成这些任务。

### 简介及原理

正则表达式是一种规范化、轻量级的描述性编程语言，常用来定义搜索模式（也即字符串集合）并结合各种工具或函数库来实现对文本内容进行查找、替换以及分割等处理。正则语法有多种变体，而且不同函数库和工具还对正则语言进行了扩充，但本文主要介绍其中较为主流的基于 Perl 的正则语法（参见 [PCRE](https://www.wikiwand.com/en/Perl_Compatible_Regular_Expressions)）。

先来常规的文本搜索过程：一般我们会在 Word 等文字处理软件中打开搜索功能，输入内容对全文（或部分）进行查找，我们输入的内容会被精确的在文本中匹配出来。在本文中我们将全文内容称为字符串（源字符串），而要查找的内容称为子串（目标字符串），所以搜索过程其实就是在源字符串中查找一个目标字符串。更具体来说，可以假设存在一个搜索指针，搜索时指针会从源字符串开头移到结尾处，并会在每个位置跟目标字符串进行匹配测试。

利用正则表达式进行搜索，跟上面不同的地方在于：正则表达式代表字符串集合（多个字符串），因此允许用户指定复杂的搜索模式，而不是简单的纯文本匹配。比如：`Jim` , `Tim`, `Pim` 三个词可以用正则更紧凑的表示为 `[JTP]im`。

## Components

正则表达式是一种描述性语言，有两类字符组成：

* 普通字符（literal character）

  所有字符都可以出现在正则表达式中，并且大部分字符在表达式中的意义就是指代它们自己。


* 元字符（meta character）

  有少数字符像`$`, `|`, `.`, `+` 等这些在正则表达式中并不指代它们自己而是有特殊含义。通常它们用来指代一类字符或者改变正则表达式的意义，所以被称为元字符。

除了以上两类组成正则表达式的字符外，一些函数库和工具还允许通过参数配置来影响正则匹配过程，比如匹配时是否忽略大小写等。这些配置参数也可以看成是正则表达式的组成部分。一个正则表达式就是用这些字符混合组成的。

## Basic Syntax

元字符按照用途可以分为以下几种：

* 位置约束（Anchor）
* 字符通配（Wildcard）
* 字符类别（CharClass）
* 字符集合（CharSet）
* 计量（Quantifier）
* 或（VerticalBar）
* 分组（Parentheses）
* 转义（Backslash）

### 位置约束

指定正则表达式要匹配源字符串中哪里的位置。

| Name   | Syntax | Description                              |
| ------ | ------ | ---------------------------------------- |
| Caret  | `^`    | 正则表达式匹配字符串**开始**位置。具体效果会受到正则配置参数 MULTILINE 的影响。 |
| Dollar | `$`    | 正则表达式匹配字符串**结尾**位置。具体效果会受到正则配置参数 MULTILINE 的影响。 |

### 字符通配

指代任意字符，使得正则表达式书写更加紧凑。

| Name | Syntax | Description                              |
| ---- | ------ | ---------------------------------------- |
| Dot  | `.`    | 匹配除了换行符号以外的所有字符。要同时允许匹配换行，需要开启正则配置参数 DOTALL。 |

### 字符类别

指代某类字符，比如字母类、数字类等。

| Name      | Syntax | Description                              |
| --------- | ------ | ---------------------------------------- |
| CharClass | 见下面介绍  | 不同版本的正则表达式中表示字符类别的方法可能存在差异，下面介绍的以 Python 中的正则为准。 |

* 数字类：`\d` 默认等价于 `[0-9]` ，若开启 UNICODE 则扩充该集合。补集为 `\D`。
* 空白类：`\s` 默认等价于 `[\t\n\r\f\v]`，若开启 UNICODE 扩充该集合。补集为 `\S`。
* 单词类：`\w` 默认等价于 `[0-9a-zA-Z_]`，若开启 LOCALE 和 UNICODE 扩充集合。补集为 `\W`。
* 边界类：`\b` 用来表示 `\w` 和 `\W` 或开头之间的字符，即不属于单词的字符。补集为 `\B`。

注：字符类别会受到语言本地化以及字符集编码影响，参见正则配置 LOCALE 和 UNICODE。

### 字符集合

定义一个字符集合，指代集合中的任意字符。

| Name    | Syntax  | Description                              |
| ------- | ------- | ---------------------------------------- |
| CharSet | `[...]` | `[]` 充当字符集合的定界符，匹配定义于其中的任意字符。注：此处 `...` 代指一个省略的正则语法，后文也会这样表示。 |

如何定义字符集合呢？

* 直接罗列字符。
* 使用字符范围语法，例如 `[0-9]` 表示从 0 到 9 这 10 个字符。
* 补集语法。在集合中第一字符如果是 `^`，则表示补集，例如 `[^0-9]` 表示除 0 到 9 这 10 个字符以外的所有字符。
* 字符类别，比如 `\d`, `\w` 等。
* 具有特殊含义的元字符在字符集合中没有特殊含义，比如 `[*+]` 仅仅表示匹配 * 或者 + 字符。
* 字符集合中定义字符 `-` 和 `]` 时，需要转义。因为 `-` 在字符范围语法中使用到，如果要在字符集合中包含它，需要将其放在第一个或者使用 `\` 对其转义。`]` 字符表示字符集合结束定界符，因此在使用时也需要放在第一个或者进行转义。

### 计量

用于定义紧跟在其前面匹配项可以出现的次数，这里要注意紧跟在前面的配置项可以是一个字符，也可以是一个分组。

| Name       | Syntax          | Description                              |
| ---------- | --------------- | ---------------------------------------- |
| Star       | `*`             | 匹配项出现 **0** 次或任意多次，尽可能多的匹配，即匹配是贪婪的。      |
| Plus       | `+`             | 匹配项出现 **1** 次或任意多次，尽可能多的匹配，即匹配是贪婪的。      |
| Question   | `?`             | 匹配项出现 **0** 次或 **1** 次，尽可能多的匹配，即匹配是贪婪的。  |
| Range      | `{m}`           | 匹配项**仅**出现 m 次。                          |
| Range      | `{m,n}`         | 匹配项出现次数为 **m** 次到 **n** 次，尽可能多的匹配，即匹配是贪婪的。 |
| Range      | `{,n}` 或 `{m,}` | `{m,n}` 省去上界或者下界次数。                      |
| Non-Greedy | 计量字符后置 `?`      | 上述各种计量字符 `*`, `+`, `{m}`, `{m,n}` 以及 `?` 都是贪婪匹配的。如果想要关闭这种贪婪特性，可以在后面紧跟 `?` 字符。 例如：字符串 `<a> b <c>` 使用 `<*>`将整个被匹配，而使用 `<*?>` 则仅匹配其中的 `<a>` 。 |

### 或

A|B, where A and B can be arbitrary REs, creates a regular expression that will match either A or B. An arbitrary number of REs can be separated by the '|' in this way. This can be used inside groups (see below) as well. As the target string is scanned, REs separated by '|' are tried from left to right. When one pattern completely matches, that branch is accepted. This means that once A matches, B will not be tested further, even if it would produce a longer overall match. In other words, the '|' operator is never greedy. To match a literal '|', use `\|`, or enclose it inside a character class, as in `[|]`.

### 分组

将要匹配的内容分成若干组，便于后期对匹配内容的提取以及后续匹配时引用前面的匹配

Matches whatever regular expression is inside the parentheses, and indicates the start and end of a group; the contents of a group can be retrieved after a match has been performed, and can be matched later in the string with the \number special sequence. To match the literals '(' or ')', use \( or \), or enclose them inside a character class: `[(][)]`.

### 转义

使用转义字符 `\` 来对某些字符进行转义。转义的常见情形如下：

* 元字符转义使其失去元字符的特殊含义，比如：`*` 进行转义后 `\*` 将不再具有计量的意义。
* 分组号，`\number` 只能指定 1 到 99，三位整数有可能被当成十六进制数字
* 开头：`\A`
* 结尾：`\Z`
* 十六进制：三位数字转义表示十六进制字符

注：Python 中提供了 `re.escape` 函数来对一个字符串中含有的正则元字符进行转义。

## Advanced Syntax

以 `(?...)` 模式出现的就是扩展语法，其中 `...` 代表具体是怎样的扩展语法

### 正则配置

`(?flag)` 

其中 flag 可以是 i, L, m, s, u, x 中的任意一个或多个，分别对应大小写、本地语言、多行、点匹配换行、unicode 以及 verbose 。改变正则的匹配模式，它应该是正则表达式中第一个非空白 non-whitespace 匹配的语法

### 非捕获版本的分组

`(?:...)`

A non-capturing version of regular parentheses. Matches whatever regular expression is inside the parentheses, but the substring matched by the group cannot be retrieved after performing a match or referenced later in the pattern.

### 命名分组

`(?P<name>...)`

类似普通分组。支持嵌套。

当前正则表达式中可以引用，语法为 `(?P=name)` 和 `\1`

匹配结果中引用，m.group('name') 和 m.group(1)

替换字符串时引用，regex.sub('\g<name>')  和 regex.sub('\g<1>') 和  regex.sub('\1')

### 引用命名分组

`(?P=name)`

A backreference to a named group; it matches whatever text was matched by the earlier group named name. 比如匹配引号，`(?P<quote>['"]).*?(?P=quote)`

### 正则注释

`(?#...)`

### 前向正断言

`(?=...)`

前向正断言lookahead assertion：只有接下来的字符串满足该条件时，才会进行匹配。如果不满足的话，也不会影响后续的匹配。所谓前向是指原字符串中未进行匹配测试的字符串方向，所谓断言是指仅仅用来测试并不消耗原字符串。

例如：`(xiao (?=wen)|wen)` 既可以匹配 `iao wen bin` 中的 wen

### 前向负断言

`(?!...)`

前向负断言negative lookahead assertion：只有接下来的字符串不满足该条件时，才会进行匹配。同样不成立时，也不会影响后续的匹配。

### 后向正断言

`(?<=...)`

后向正断言positive lookbehind assertion：只有之前的字符串满足该条件时，才会进行匹配。不会消耗字符串。

所谓后向就是沿原字符串已经匹配过的方向来进行断言测试。例如：`(?<=-)\w+` 只会匹配 `chicken-egg` 中的一个 `egg`

### 后向负断言

`(?<!...)`

后向负断言negative lookbehind assertion

### 分组条件匹配 

`(?(id/name)yes-pattern|no-pattern)`

分组条件匹配：如果分组 id/name 存在，则匹配 yes-pattern，否则匹配 no-pattern，并且其中的 `|no-pattern` 可以省略。例如：`(<)?(\w+@\w+(?:\.\w+)+)(?(1)>)` 可以匹配 `xiao@gmail.com` 或者 `<xiao@gmail.com>`



## 正则配置参数

* DOTALL 

控制 `.` 是否匹配任意字符，包括换行。默认 `.` 匹配除换行以外的任意字符。

Make the '.' special character match any character at all, including a newline; without this flag, '.' will match anything except a newline.

* MULTILINE 

控制 `^` 和 `$` 匹配字符串开头和结尾的行为。默认将输入的字符串作为一整个字符串来匹配，开启该模式后会将其中每个换行间隔的当成字符串

When specified, the pattern character '^' matches at the beginning of the string and at the beginning of each line (immediately following each newline); and the pattern character '$' matches at the end of the string and at the end of each line (immediately preceding each newline).

* IGNORECASE 

匹配时是否忽略大小写

Perform case-insensitive matching; expressions like [A-Z] will match lowercase letters, too. This is not affected by the current locale. To get this effect on non-ASCII Unicode characters such as ü and Ü, add the UNICODE flag.

* LOCALE 

本地语言支持

Make \w, \W, \b, \B, \s and \S dependent on the current locale.

* UNICODE  

unicode 字符支持

Make the \w, \W, \b, \B, \d, \D, \s and \S sequences dependent on the Unicode character properties database.

* VERBOSE 

支持 verbose 模式，即正则中夹杂注释说明

This flag allows you to write regular expressions that look nicer and are more readable by allowing you to visually separate logical sections of the pattern and add comments. Whitespace within the pattern is ignored, except when in a character class, or when preceded by an unescaped backslash, or within tokens like `*?`, `(?:` or `(?P<...>`. When a line contains a `#` that is not in a character class and is not preceded by an unescaped backslash, all characters from the leftmost such `#` through the end of the line are ignored.

## 正则表达式的局限

正则表达式可以匹配任意字符串吗？并不能。

假设存在如下字符串：`He said: "The first program of "Hello World" is bug free".`。我们现在试图用正则表达式匹配其中的 `"Hello Word"` 可以做到吗？

先来看 `".*"`，将会匹配 `"The first program of "Hello World" is bug free"` 这条语句。再来看非贪心的 `".*?"`，将会匹配 `"The first program of "`。

不论是贪心还是非贪心都无法匹配到我们的目标，这其实是正则表达式的一个典型局限性：无法对嵌套递归内容进行匹配。

注：这里强调的是正则语法本身无法匹配递归内容，但许多编程语言和工具提供了其它途径来匹配这种情况。



## Python Regex

Python 和 正则对某些字符的二次转义问题，建议在 Python 中使用 raw string 来书写正则语法

search 查找字符串中第一次出现的匹配子串

match 从开头匹配

split 根据匹配子串进行分割字符串

findall 找到字符串中所有被匹配的子串

sub 替换匹配的子串

escape 对字符串中含有的正则元字符进行转义

以上所有查找替换等都会得到一个匹配对象，该对象含有位置信息等



## Examples

### 变量名

在许多程序设计语言中都对变量名的命名有限制，最常见的限制是：变量名只能含有大小写字母、数字以下划线并且只能以下划线或大小写字母开头。

用于匹配变量名的正则表达式为：`^[a-zA-Z_][0-9a-zA-Z_]*`

### 成对符号

这里成对符号是泛指引号、书名号等成对的符号。具体来说成对的符号又可以分为两类：前后一致的，比如英文的单引号和双引号等；前后不一致的，比如中文引号、书名号以及英文小中大括号等。

先来看如何匹配前后一致成对符号，以双引号为例：`(?P<quote>").*?(?P=quote)`。



再来看如何匹配前后不一致的成对符号，以书名号为例：`(?P<bookmark>[《]).*?(?P=bookmark)`







