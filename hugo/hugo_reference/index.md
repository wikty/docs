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

- 文档路径参数

  `ref` 和 `relref` 均需要输入一个文档路径参数，该路径是相对于内容目录 `content` 的路径。此外还可以直接输入文档名，但当不同 Section 中含有相同文档名时就会产生二义性，因此建议使用相对于 `content` 的路径名。

- 锚点参数

  `ref` 和 `relref` 还可接受锚点参数，锚点可以是当前文档内的，也可以是其它文档中的，值得注意的是 Hugo 在生成含有锚点的链接时自动添加了一个随机后缀，后面会解析为什么要添加后缀。

- 相对链接和绝对链接地址

  到底该使用 `ref` 还是 `relref` 呢？二者的区别就在于生成的链接是否含有网站的 baseURL ，不含 baseURL 的好处在于，当 baseURL 改变时网站不需要重新生成，这样看来 `relref` 可移植性更好。

前面一直提到文档锚点的引用，那么文档锚点是怎么来的，是 Hugo 自动生成的，还是我们自定义的呢？其实在 Hugo 将 Markdown 文档转换为网页时，自动为 Markdown 文档内的标题级内容生成了锚点以供引用，并且 Hugo 还保证了锚点在文档内以及整个站点内的唯一性。

那么 Markdown 文档中标题级内容是如何转化为锚点的呢？假设标题内容为：Hugo: A Fast & Modern Static Web Engine，最终被转换成锚点 `hugo-a-fast-modern-static-web-engine` 。标题到锚点转换过程为：先将其转换为小写内容，再将非字母数字字符用连字符替换，并将多余的连字符去除。除了让 Hugo 自动将标题内容转为锚点，Hugo 还支持文档作者为标题指定固定的锚点，比如这样定义标题内容：`# Hugo: A Fast & Modern Static Web Engine {#hugo-main}` ，然后 Hugo 在生成站点时就会为该标题生成锚点 `hugo-main` 。此外当页面中出现相同锚点时，Hugo 会自动外这些锚点添加后缀 `-1` 、`-2` 等。

此外[官网介绍](http://gohugo.io/extras/crossreferences/)，为了确保标题锚点全站的唯一性，Hugo 会根据内容文档的路径为其生成一个独一无二的标识串，并在为锚点生成链接时会添加该文档标识作为锚点后缀。另外提到列表页为了避免锚点冲突也使用到了文档唯一标识串。这两点有些不太懂，为何要确保全站锚点唯一性，列表页又为何会出现锚点冲突的情况？留待以后填坑，，，