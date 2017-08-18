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

- 高亮

  用来高亮文档中的代码片段，用法样例如下

  ```
  {{< highlight python >}}
  def pt(txt):
  	print(txt)
  {{< /highlight >}}
  ```

- 图片

  用来扩展 Markdown 中插入图片的语法，该 shortcode 插入的图片支持自定义 CSS 类、添加链接和 caption 等高级功能，用法样例如下

  ```
  {{< figure src="/media/spf13.jpg" title="Steve Francia" link="" caption="" class="" attr="" attrlink="" alt="" >}}
  ```

- 文档引用

  用来在文档中引用其它文档或者当前文档内部某个锚点，用法样例如下

  ```
  [Who]({{< ref "about.md#who" >}})
  [Who]({{< relref "about.md#who" >}})
  ```

  只需给出被引用文档的相对路径，Hugo 会自动将其替换为相应文档的永久链接，`ref` 和 `relref` 的不同之处在于，后者会给出相对路径链接，而前者给出绝对路径链接。

- Twitter 推文

  用来在内容中插入一条 tweet ，推文的链接是这样的： [https://twitter.com/spf13/status/666616452582129664](https://twitter.com/spf13/status/666616452582129664) ，插入这条推文的 shortcode 如下

  ```
  {{< tweet 666616452582129664 >}}
  ```

- YouTube 视频

  用来在内容中插入 YouTube 视频，YouTube 视频资源链接是这样的： [https://www.youtube.com/watch?v=w7Ft2ymGmfc](https://www.youtube.com/watch?v=w7Ft2ymGmfc) ，插入该视频的 shortcode 如下

  ```
  {{< youtube w7Ft2ymGmfc >}}
  ```

  或者开启自动播放

  ```
  {{< youtube id="w7Ft2ymGmfc" autoplay="true" >}}
  ```

- Vimeo 视频

  同插入 YouTube 视频类似，假设资源链接为：[https://vimeo.com/channels/staffpicks/146022717](https://vimeo.com/channels/staffpicks/146022717) ，则插入语法如下

  ```
  {{< vimeo 146022717 >}}
  ```

- GitHub 代码片段

  用来在文档中插入 GitHub 上创建的代码片段，假设代码片段链接为：[https://gist.github.com/username/id](https://gist.github.com/username/id) ，则插入语法如下

  ```
  {{< gist username id >}}
  ```

- Speaker Deck 演示文稿

  [Speaker Deck](https://speakerdeck.com/) 是一个允许我们共享演示文稿的地方，我们可以将共享在其上的演示文稿插入到内容文档中，在 Speaker Deck 上点击分享后会生成一段 HTML 代码，假设其中的 `data-id="123456"` ，那么在文档中可以使用如下语法插入该演示文稿

  ```
  {{< speakerdeck 123456 >}}
  ```

- Instagram 图片

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

- 高亮

  ```
  {{ .Get 0 | highlight .Inner  }}
  ```

- 图片

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

- YouTube 视频

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