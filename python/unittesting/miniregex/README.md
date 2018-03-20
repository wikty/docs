简介

本程序核心代码摘录自[《代码之美》][1]第一章中 Rob Pike 开发的正则匹配程序。该正则匹配程序短小精炼，包含了正则表达式中的核心语法，可以很好的展示正则表达式的基本思想。

语法

| 语法   | 含义                 |
| ---- | ------------------ |
| .    | 匹配任意单个字符           |
| *    | 匹配前一个字符零次或多次（非贪婪的） |
| ^    | 匹配字符串开头            |
| $    | 匹配字符串结尾            |
| c    | 匹配该字符 c            |

样例

`abb*` 将匹配 `ab` , `abb` , `abbb`

`a.c` 将匹配 `abc` , `adc`

`a.*` 将匹配 `a` , `ab` , `abcde`

`^a.c` 将匹配 `abc` ，不能匹配 `dabc`

`a.c$` 将匹配 `abc` ，不能匹配 `abcd`

[1]: https://book.douban.com/subject/3224524/	"Beautiful Code"