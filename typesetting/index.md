https://yihui.name/cn/2017/04/space/

习惯在中文中的英文单词和数字前后空格，除非前后是标点符号，显然这是沿用了纯英文写作的习惯。其实也有点受 CTeX 的影响。默认情况下，CTeX 文档用 `xelatex` 编译出来的 PDF 中，中文里的英文单词前后会自动空格。

中英文之间加入空格的一个好处体现在网页排版中。如今还没有任何浏览器真的很好支持中英文混排时的断行问题。空格对浏览器来说是一个重要的断行提示。要是没有空格，英文单词可能会紧紧贴在中文上，导致它处在页面边缘时会连带着上一行的一个中文字符被断到下一行去，例如：

```
假装这是很长很长很长很长很长的一句话sentence。

```

英文前没有空格的时候可能会被这样断行：

```
| 假装这是很长很长很长 |
| 很长很长很长的一句　 |
| 话sentence。

```

而不是你预期的这样：

```
| 假装这是很长很长很长 |
| 很长很长很长的一句话 |
| sentence。

```

方块字都对不齐，人生还有什么意义。

断行问题在 CSS 中有几种可能的设定，但没有任何一种选项真的适合中英文混排。上面的例子显示的是默认的断句换行效果。

https://yihui.name/cn/2017/05/pangu/

因为看到有人评论我的老文章，我跑去瞄了一眼那文章，不看不要紧，看了就失去了活下去的勇气。我大约从 2015 年开始患上[空格强迫症](https://yihui.name/cn/2017/04/space/)，那之前的文章里中英文之间都没有空格，通体不舒畅，于是心想着能不能写个 JS 脚本自动添加空格。

这种轮子大概也轮不到我区区一个 R 码畜来造，放狗一搜，早有人做了，名叫“盘古” [pangu.js](https://github.com/vinta/pangu.js)。于是操起键盘就把它[加到](https://github.com/rbind/yihui/commit/6de91d0a)我的旧文章页面中了。正常加载办法应该是[如此这般](https://yihui.name/cn/2017/04/do-this/)：

```
<script src="https://cdn.bootcss.com/pangu/3.3.0/pangu.min.js">
</script>

<script>
  pangu.spacingPage();
</script>

```

然而我怎么可能让这 7K 的“巨型”脚本阻挡我的页面载入？必须异步加载，否则会浪费十毫秒的加载时间。于是用高射炮打蚊子（不支持 IE 8 及更低版本的 IE，但我会在乎 IE 吗）：

```
<script>
(function(u, c) {
  var d = document, t = 'script', o = d.createElement(t),
      s = d.getElementsByTagName(t)[0];
  o.src = u;
  if (c) { o.addEventListener('load', function(e) { c(e); }); }
  s.parentNode.insertBefore(o, s);
})('//cdn.bootcss.com/pangu/3.3.0/pangu.min.js', function() {
  pangu.spacingPage();
});
</script>

```

我这是何苦来哉。