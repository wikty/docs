## Pandoc
[Pandoc](http://pandoc.org/index.html) 是及其强大的文件转换工具，可以在常见文件格式之间完成任意转换

可以从这里[下载](https://github.com/jgm/pandoc/releases/download/1.19/pandoc-1.19-windows.msi)，另外转换PDF需要安装[LaTeX](http://miktex.org/)

## Pandoc扩展Markdown语法

### 脚注

* 注脚语法

  ```markdown
  这是一个脚注参考[^1]，这是另外一个脚注参考[^longnote]

  [^1]: 这是脚注内容。

  [^longnote]: 这是含有多个块内容的脚注。

      紧跟在脚注之后缩进一个tab的段落被认为属于前面的脚注。缩进的段落可以只缩进第一行，或者缩进段落的每一行内容。

          属于前面注脚的代码需要缩进两个tab

  这里的内容并没有缩进，所以不属于前面的注脚了
  ```

### 表格

* 表格标题

  ```markdown
     Left     Right
  -------     ------
       12     12
      123     123
        1     1

  Table: 这里是表格标题。
  ```

  以`Table:`或者`:`开头的段落且放在表格之前或者之后的段落会被当做表格标题

* 简单表格语法

  ```markdown
    右对齐     左对齐     居中    表头太长则默认对齐
  -------     ------ ----------   -------
       12     12        12            12
      123     123       123          123
        1     1          1             1

  Table:  这是表格标题
  ```

  表格对齐方式取决于表头内容相对于下方虚线的位置。如果表头内容右对齐于下方虚线，则该列内容右对齐，其它对齐情形与此类似。

  表格用一个空白行表示表格结束。表头行内容可以省去，这样可以创建无表头表格，无表头表格对齐方式取决于单元格内容相对于虚线的对齐方式。

* 多行表格语法

  ```markdown
  Table: 表格标题也可以是
  多行的

  -------------------------------------------------------------
    居中对齐   默认对齐          右对齐 左对齐
    多行表头   多行表头        多行表头 多行表头
  ----------- ------- --------------- -------------------------
     第一       行               12.0  多行
                                       的内容，后面紧跟空白行
                                       用来分隔表格行

     第二    	行                5.0 多行
     								   的内容
  -------------------------------------------------------------


  下面是无表头表格，且该表格只有一行内容

  ----------- ------- --------------- -------------------------
     第一       行               12.0  即使仅含有一个表格行，后面
     									用来分隔表格行的空行也要有
                                       
  -------------------------------------------------------------
  Table: 无表头
  ```

  表格需要一行虚线表示表格的开始；表格行需要用空白行来间隔；表格需要一行虚线和一个空白行表示表格的结束。所谓多行表格指的是单元格内容可以分布在多个行上，但是要注意内容不能跨越到单元格之外。

* 格框表格

  ```markdown
  : 表格标题

  +---------------+---------------+--------------------+
  | Fruit         | Price         | Advantages         |
  +:==============+===============+:==================:+
  | Bananas       | $1.34         | - built-in wrapper |
  |               |               | - bright color     |
  +---------------+---------------+--------------------+
  | Oranges       | $2.10         | - cures scurvy     |
  |               |               | - tasty            |
  +---------------+---------------+--------------------+

  : 无表头

  +--------------:+:--------------+:------------------:+
  | Right         | Left          | Centered           |
  +---------------+---------------+--------------------+
  ```

  表头行和表体内容使用一行等号间隔开，表格开始和结束行以及其它行间隔使用`+---+---+`隔开；列内容使用`|`间隔；单元格中可插入其它markdown语法（段落，代码块，列表等），但不支持跨越单元格。对齐方式通过为表头下面间隔符两端添加`:`来控制，哪边添加`:`则向哪边对齐，两边都添加了则居中对齐。

* 管道表格

  ```markdown
  | Right | Left | Default | Center |
  |------:|:-----|---------|:------:|
  |   12  |  12  |    12   |    12  |
  |  123  |  123 |   123   |   123  |
  |    1  |    1 |     1   |     1  |

  : 表格标题
  ```

  表格两端的`|`是可选的，但用来间隔列内容的`|`是必须有的；对齐方式由表头下面间隔符两端添加`:`来控制，哪边有`:`则向哪边对齐，两边都有则居中对齐；表头行不能省略，要想创建无表头表格，将表头单元格留空即可。表格列使用`|`间隔开，已经很好的可以区分列内容了，因此在书写时不需要可以对齐列内容。单元格内容只允许单行段落，不支持其它markdown语法，当内容太长时，生成的表格会自动换行。

### 列表

* 有序列表语法

  ```markdown
  下面是markdown标准有序列表语法：
  以数字开始紧接着一个英文句号，再接一个空格，然后是列表项内容。
  而且数字顺序跟列表最终生成的数字标号无关，最终生成的列表依次按照1,2,3...标号

  1. one
  2. two
  3. three

  pandoc扩展的有序列表语法：
  将#作为替代数字的符号，生成的列表同上

  #. one
  #. two
  #. three

  此外支持大小写英文字母和罗马数字作为列表项标号

  i. roman one
  ii. roman two
  iii. roman three

  A.  句号后留有两个空格
  B.  句号后留有两个空格
  C.  句号后留有两个空格

  此外还支持括号，右括号来代替英文句号间隔列表项内容

  1) one
  2) two
  3) three

  (1) one
  (2) two
  (3) three
  ```

* 定义列表语法

  ```
  机器学习*可以用行内markdown语法*

  : 定义1第一段内容，也可以用~作为定义的开始

  		第二段内容，缩进两个tab在定义中插入代码
  	
  	定义的第三段内容

  : 定义2第一段内容
  第一段内容的第二行

  	定义的第二段内容

  专业词汇
  ~ 更加紧凑的定义语法
  ```

* ​







## Pandoc制作演示文稿

[基于Web的演示文稿](https://en.wikipedia.org/wiki/Web-based_slideshow)比那些通过PowerPoint等软件生成的演示文稿更加灵活，可以让作者将更多精力放在文档内容而不是样式上，而且转换而成的Web演示文稿（Web Slide）是由HTML+Javascript+CSS等内容构成的，可以在任何浏览器上打开。

目前Pandoc支持五种方式生成Web Slide：[S5](http://meyerweb.com/eric/tools/s5/)，[DZSlides](http://paulrouget.com/dzslides/)，[Slidy](https://www.w3.org/Talks/Tools/Slidy2/Overview.html#(1))，[Slideous](http://goessner.net/articles/slideous/)，[reveal.js](https://github.com/hakimel/reveal.js)。其实五种生成方式对应了五种Web Slide解决方案，不同方案演示文稿的表现能力各不相同，下文将着重介绍reveal.js。

我们只需要编写纯文本格式文档，然后就可以使用Pandoc将其转换为富有表现形式的Web Slide。用来制作Slide的文档可以使用任何一种Pandoc支持的标记语言（Markdown、org-mode、reST、Textile等）来编辑。下文中将以Markdown为例。

```
% Nonsense Stuff
% John Doe
% March 22, 2005

# In the morning

## Getting up

- Turn off alarm
- Get out of bed

## Breakfast

- Eat eggs
- Drink coffee

# In the evening

## Dinner

- Eat spaghetti
- Drink wine

------------------

![picture of spaghetti](images/spaghetti.jpg)

## Going to sleep

- Get in bed
- Count sheep
```



### Pandoc使用方法

Pandoc是一个命令行工具，所以我们需要在命令行环境中使用它

#### 检查是否安装成功

查看版本信息

	pandoc --version [Enter]

#### 命令行中的转换实验

命令行中输入markdown转为html

1. 命令行中输入：`pandoc [Enter]`
2. 光标在下一行闪动，表示可以在此输入内容，可以输入一些markdown内容，然后输入`[Crtl+Z][Enter]`来表示输入结束
3. 可以看到刚刚输入的markdown内容被转换为html内容，在命令行中输出了

命令行中输入html转为markdown

1. 命令行中输入：`pandoc -f html -t markdown [Enter]`
2. 光标在下一行闪动，同刚刚命令一样，可以在命令行中输入内容，转换后在命令行中输出，但这次输入的命令含有参数，其中`-f html`表示输入内容格式为html，`-t markdown`表示输出内容格式为markdown，也就是说这次我们希望将输入的html内容转换为markdown内容在命令行中输出，因此输入一些html内容，再输入`[Crtl+Z][Enter]`表示结束，然后在命令行中可以看到markdown内容输出
3. 其实pandoc的默认参数是`-f markdown -t html`，所以命令`pandoc [Enter]`和命令`pandoc -f markdown -t html [Enter]`是等价的

#### 文件转换

转换markdown文件为html内容并直接在命令行中输出

	pandoc test.md

markdown文件转换为html文件

	pandoc test.md -o your-filename-for-html-document.html

markdown文件转换为html文件，如果html文件不完整的话，会添加额外内容使其完整

	pandoc test.md -s -o your-filename-for-new-document.html

markdown文件转换为LaTex文件

	pandoc test.md -f markdown -t latex -s -o your-filename-for-new-document.tex

根据后缀名自动识别输入和输出格式

	pandoc test.md -s -o your-filename-for-new-document.tex

#### 制作中文PDF文档存在若干问题

1. 首先markdown文档需要保存在UTF-8编码格式，不然生成pdf时会报告编码错误
2. pandoc默认的LaTeX引擎是pdflatex，不支持中文，需要修改引擎为xelatex，`--latex-engine=xelatex`
3. 此时生成的pdf文档里的中文不显示，因为生成pdf时字体不支持中文，需要指定系统上的字体（查看系统字体`fc-list`），`-V mainfont="SimSun"`
4. 此时生成的文档文字越界，使用别人的[模板](https://github.com/tzengyuxio/pages/tree/gh-pages/pandoc)，并将模板中字体替换为系统上支持的字体
5. 最后命令如下：`pandoc test.md -o outfile.pdf --latex-engine=xelatex -template=pm-template.latex`

[参考文章](http://www.cnblogs.com/loongfee/p/3223957.html)





	

文档开头三行包含元信息：标题，作者，日期

可以直接在文本中嵌入HTML，用于显示Markdown等标记语言不支持的表格，或控制字体大小，以及进行其他更加复杂的排版。当然，如果用到的HTML标签过多，这不是Markdown这些轻量级标记语言的错，也许是做幻灯片的方式出了问题。因为演示本身要传达的是内容，复杂的排版没有任何意义。

目前Pandoc内置了对五种HTML幻灯片框架的支持：

* DZSlides
* Slidy
* S5
* Slideous
* reveal.js

当然，你实际上可以使用任何喜欢的幻灯片框架（比如Google I/O HTML5 slide template），只要让Pandoc在渲染HTML时使用你指定的模板即可。甚至你可以定义自己的模板，如果你知道如何写CSS去定义页面外观、如何写JavaScript让<div>元素动起来，或者已经有了一个不错的HTML幻灯片模板，你就可以直接让Pandoc把Markdown转换成纯HTML片段，用来嵌到自己的模板里

DZSlides内置于Pandoc的模板，支持键盘操作→/←翻页，PgUp/PgDn，Home/End，Pandoc生成的DZSlides幻灯片中自包含了所需CSS和JavaScript，无需依赖任何外部文件。

	pandoc slides.md -o slides.html -t dzslides -s

若要对模板的样式进行调整，可以用--template指定自定义模板。默认的模板为default.dzslides，因此上述命令等效于：

	pandoc slides.md -o slides.html -t dzslides --template default.dzslides

可以从这里<https://github.com/jgm/pandoc-templates>找到原来的模板，自行修改后替换掉原先的模板。其余幻灯片框架与此相仿，以后不再赘述。

HTML Slidy是W3C开发的一个极简主义HTML幻灯片模板，没有任何多余的样式，支持鼠标单击翻页，键盘操作→/←，PgUp/PgDn，Home/End。

采用默认模板渲染一个独立的Slidy幻灯片：

	pandoc slides.md -o slides.html -t slidy -s

或指定自定义模板：

	pandoc slides.md -o slides.html -t slidy --template default.slidy

Pandoc生成的Slidy HTML依赖于<http://www.w3.org/Talks/Tools/Slidy2/styles/slidy.css>和<http://www.w3.org/Talks/Tools/Slidy2/scripts/slidy.js>这两个外部文件。若不想依赖<http://www.w3.org/>，可以将它们保存为本地文件。

S5（Simple Standards-Based Slide Show System）是一个公有领域的HTML幻灯片规范。它支持鼠标单击翻页，键盘操作→/←，PgUp/PgDn，Home/End。

为了使用S5作为幻灯片框架，需要从[这里](http://meyerweb.com/eric/tools/s5/)下载S5。解压之后把S5文件夹中的ui/default拷贝到幻灯片所在路径下，改名为s5/default即可。

渲染幻灯片：

	pandoc slides.md -o slides.html -t s5 -s

Slideous是另一个有些年头的HTML幻灯片框架。支持鼠标单击翻页，键盘操作→/←，PgUp/PgDn，Home/End。

下载<http://goessner.net/download/prj/slideous/slideous.js>和<http://goessner.net/download/prj/slideous/slideous.css>这两个文件，放到本地目录slideous/下即可。

渲染幻灯片：

	pandoc slides.md -o slides.html -t slideous -s

reveal.js这东西已经红得不能更红了，最近开始火起来的WYSIWYG在线幻灯片工具slid.es也是基于它。

reveal.js的设计风格（字体、HTML5/CSS3效果）比起前面几个框架更加现代，所以如果没有特别的理由（旧浏览器兼容性）的话，reveal.js果然还是最应该推荐的一个。

虽说reveal.js本身就提供对Markdown语法的支持，不过Pandoc的好处很明显，那就是一条命令解决问题，不需要用户接触任何HTML。

首先需要从GitHub上获取<https://github.com/hakimel/reveal.js>，将reveal.js同名的文件夹放在幻灯片所在目录下即可

渲染幻灯片：

	pandoc slides.md -o slides.html -t revealjs -s

除了默认的外观主题以外，reveal.js还提供了多个主题可供选择，

	pandoc slides.md -o slides.html -t revealjs -s -V theme=beige

* default：（默认）深灰色背景，白色文字
* beige：米色背景，深色文字
* sky：天蓝色背景，白色细文字
* night：黑色背景，白色粗文字
* serif：浅色背景，灰色衬线文字
* simple：白色背景，黑色文字
* solarized：奶油色背景，深青色文字

LaTeX Beamer虽然不是HTML，Pandoc也可以用来将Markdown文件渲染成LaTeX beamer样式的PDF幻灯片。如需要打印而不是演示时特别有用。

	pandoc slides.md -o slides.pdf -t beamer

幻灯片级别（Slide level）

在前文的例子里看到，

	# In the morning

	## Getting up

	- Turn off alarm
	- Get out of bed

1级标题In the morning后面紧跟2级标题Getting up，而2级标题Getting up后面的内容是显示在幻灯片上的主体内容，因此这里的Slide level为2。这意味着每个2级标题生成一张幻灯片。高于2级的标题（1级标题）生成一张独立的仅包含标题的幻灯片，而低于2级的标题（3级标题）将存在于上一级标题的幻灯片中，不单独生成新的幻灯片。

可以使用--slide-level选项覆盖默认的Slide level。

在reveal.js模板下，由于幻灯片的滚动方向可以是二维的（键盘→←↑↓），所以1级标题渲染为水平方向的幻灯片，2级标题渲染为竖直方向的幻灯片。

“华丽丽的分割线”：

	------------------

用来强制生成新的幻灯片。
渐进显示

生成幻灯片时加入-i选项，用于控制列表的显示效果（逐条渐入）。

$ pandoc slides.md -o slides.html -t slidy -s -i

两段文字显示之间的人为停顿，用如下分割线：

. . .

TeX公式

可以直接插入TeX公式：

$e^x = \sum_{n=0}^\infty \frac{x^n}{n!} = \lim_{n\rightarrow\infty} (1+x/n)^n$

MathML的渲染效果为：

ex=∑n=0∞xnn!=limn→∞(1+x/n)n

控制TeX公式渲染方式的选项有--mathml，--webtex，--mathjax和--latexmathml。（Chrome和Firefox均支持MathML）
代码高亮风格

控制代码高亮风格的选项有：

    --highlight-style pygments
    --highlight-style kate
    --highlight-style monochrome
    --highlight-style espresso
    --highlight-style haddock
    --highlight-style tango
    --highlight-style zenburn

自定义CSS

你当然可以通过修改相应模板文件夹下的CSS来实现自定义外观，不过也可以使用--css指定任何现成的CSS文件。

提示板

首先，提示板的功能仅适用于reveal.js。

其次，由于浏览器的本地安全策略，需使用该功能的幻灯片必须在HTTP服务器上运行。

在Markdown中插入标签<div class="notes">的小抄：

	<div class="notes">
		This is my note.
	
		- It can contain markdown
		- like this list
	
	</div>

使用键盘s键打开提示板。当然，这个提示板是用来给演讲者自己看的，是不用mirror到外接投影仪的。


#### 更多文档

命令中查看帮助文档：`pandoc --help`

官网查看[帮助文档](http://pandoc.org/MANUAL.html)