---
date: 2017/07/04
---

## 字符串函数

 获取字符串长度：strlen

去除字符串两端的空白字符（或者其他字符）：trim, ltrim, rtrim, chop

用一个字符串分割另一个字符串： explode

使用一个字符串中任意字符分割另一个字符串：strtok

使用正则表达式分割字符串：split

用一个字符串将一维数组的值连接为字符串： implode, join

返回字符的 ASCII 码值：ord

返回 ASCII 码值指定的字符：chr

返回字符串的子串：substr

返回字符串出现某个子串的前半部分或后半部分：strstr, stristr

替换字符串的子串：substr_replace, str_replace, preg_replace

计算子串出现的次数：substr_count

比较两个字符串指定位置子串的大小：substr_compare

用一个字符表来替换字符串中某些字符：strtr, strchr

大小写转换：strtoupper, strtolower, ucwords, ucfirst, lcfirst

字符集中的字符在字符串中首次出现的序列长度：strspn

不在字符集中的字符在字符串中首次出现的序列长度：strcspn

查找字符串中子串首次出现的位置：strpos, stripos, strrpos, strripos

在字符串中查找一组字符的任何一个字符，并返回此字符之后的内容：strpbrk

查找指定字符在字符串中的最后一次出现：strrchr

反转字符串：strrev

打断字符串为指定数量的字串：wordwrap

统计字符串中单词，字等信息：str_word_count, count_chars

字符串按长度分割成为数组：str_split, chunk_split

随机打乱一个字符串：str_shuffle

重复一个字符串：str_repeat

填充字符串为指定长度：str_pad

对字符串执行 ROT13 转换：str_rot13

计算一个字符串的循环冗余码：crc32

字符串比较：strcmp, strcasecmp, strncmp, strncasecmp, strnatcmp, strnatcasecmp, strcoll

转义和去转义处理字符串：addcslashes, addslashes, stripslashes, stripcslashes

从字符串中去除 HTML 和 PHP 标记：strip_tags

HTML 实体编码解码：htmlspecialchars, htmlentities, htmlspecialchars_decode, html_entity_decode, quotemeta

将 CSV 字符串解析为数组：str_getcsv

格式化输入输出字符串：sscanf, sprintf, printf, fprintf, vprintf, vsprintf, vfprintf

计算字符串之间的各类相似度：soundex, levenshtein, metaphone, similar_text

摘要加密函数：sha1, md5, sha1_file, md5_file, crypt

二进制字符串到十六进制：bin2hex, hex2bin

网络安全传输安全编解码：convert_uuencode, convert_uudecode

## URL 处理函数

使用 MIME base64 对数据进行编码：

解码 MIME base64 编码的数据：

编码 URL 字符串：urlencode, rawurlencode

解码 URL 字符串：urldecode, rawurldecode

编码查询字符串：http_build_query

解析 URL 的各个部分：parse_url

获取 HTTP 请求头：get_headers

提取所有的 meta 标签 content 属性：get_meta_tags

