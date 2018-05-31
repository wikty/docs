## 网络应用

### Requests

Python的urllib2标准模块涵盖了所需的大多数HTTP功能，但它的API却是支离破碎的。它构建在一个和现今完全不同的时期——以及为了一个不一样的网络。一个简单的任务便需要耗费它大量的工作(即使重写函数也无济于事)。

Requests将所有Python HTTP相关的功能剥离了出来，并与网络服务无缝衔接。Requests无需再在URL中添加查询语句或格式编码的POST数据。而集成在Requests中urllib3，则实现了持久连接和HTTP连接池的完全自动化。

### ZeroMQ

ØMQ(也被称作ZeroMQ, 0MQ 或 ZMQ)是一种高性能异步消息传递库，旨在应用于可扩展分布的或并发的应用。它提供一个消息队列，但与面向消息的中间件不同，ØMQ系统可在不依赖专用消息代理的情况下运行。ØMQ旨在设计成为类似于socket风格的API。

### RabbitMQ

RabbitMQ是一种使用了高级消息队列协议(AMQP)的开源消息代理软件。RabbitMQ服务由Erlang编程语言写成，并构建在开放电信平台框架上，应用于集群和故障转移。与该代理交互的客户端库支持所有主流编程语言。



## 命令行应用

命令行应用，也被称为 [控制台应用](http://en.wikipedia.org/wiki/Console_application) 是面向如 [shell](http://en.wikipedia.org/wiki/Shell_(computing)) 之类文本接口的计算机程序。 命令行应用通常接收一些输入作为参数，这些参数（arguments）通常被称为参数（parameters）或子命令 ，而选项（options）则被称为flags或switches。

### Clint

[clint](https://pypi.python.org/pypi/clint/) 是一个Python模块，它包含了很多 对命令行应用开发有用的工具。它支持诸如CLI着色以及缩进，简洁而强大的列打印， 基于进度条的迭代以及参数控制的特性。

### Click

[click](http://click.pocoo.org/) 是一个以尽可能少的代码，用组合方式创建命令行接口的Python包。 命令行接口创建工具（“Command-line Interface Creation Kit”, Click）高度可配置，但也有开箱即用的默认值设置。

### docopt

[docopt](http://docopt.org/) 是一个轻量级，高度Pythonic风格的包，它支持 简单而直觉地创建命令行接口，它是通过解析POSIX-style的用法指示文本实现的。

### Plac

[Plac](https://pypi.python.org/pypi/plac) Python标准库 [argparse](http://docs.python.org/2/library/argparse.html) 的简单封装， 它隐藏了大量声明接口的细节：参数解析器是被推断的，其优于写命令明确处理。 这个模块的面向是不想太复杂的用户，程序员，系统管理员，科学家以及只是想 写个只运行一次的脚本的人们，使用这个命令行接口的理由是它可以快速实现并且简单。

### Cliff

[Cliff](http://docs.openstack.org/developer/cliff/) 是一个建立命令行程序的框架。 它使用setuptools入口点（entry points）来提供子命令，输出格式化，以及其他的扩展。这个框架 可以用来创建多层命令程序，如subversion与git，其主程序要进行一些简单的参数解析然后调用 一个子命令干活。

### Cement

[Cement](http://builtoncement.com/) 是一个高级的CLI应用程序框架。 其目标是为简单和复杂的命令行应用程序引入标准和功能完整的平台，并支持快速开发需求，而不会牺牲质量。 Cement是灵活的，它的用例范围涵盖了从微框架的简单到巨型框架的复杂。



## 图形界面应用

### Qt

[Qt](http://qt-project.org/) 是跨平台应用框架，它被广泛用于借GUI开发软件，但是也可用于非GUI应用。

### Toga

[Toga](https://toga.readthedocs.io/en/latest/) 是一个原生Python和操作系统的 跨平台GUI工具包。Toga由一个具有共享接口的基础组件库组成，以简化与平台无关的GUI开发。

Toga适用于Mac OS、Windows、Linux（GTK）以及Android和iOS等移动平台。

### Tk

Tkinter是Tcl/Tk上的面向对象层。 **它的优势是包括Python标准库，能够使编程更加方便，兼容性更强。**

不管是Tk还是Tkinter，在大多数Unix平台，以及Windows和Macintosh系统都可用。 从8.0发布版本开始，Tk在所有平台上使本身的样式和感觉更赞。

在 [TkDocs](http://www.tkdocs.com/tutorial/index.html) 中有一个非常好的多语言Tk教程， 所有例子使用Python。更多信息可以看 [Python 维基百科](http://wiki.python.org/moin/TkInter).

### wxPython

wxPython是Python语言编写的GUI工具包。Python编写人员能够使简单容易地使用健壮，高功能的图形用户接口编程。 把流行的wxWidgets包在跨平台GUI库中，从而作为Python的扩展模块，这用C++编写。

### PyjamasDesktop (pyjs Desktop)

PyjamasDesktop是Pyjamas的端口。PyjamasDesktop是桌面应用工具集，并且是跨平台框架 （在发布的v0.6版本之后，PyjamasDesktop是Pyjamas (Pyjs)的一部分）。简而言之， 它允许完全一样的Python网页应用资源代码能够如独立的桌面应用执行。

### PyQt

PyQt提供Qt框架的Python绑定（见如下）

[http://www.riverbankcomputing.co.uk/software/pyqt/download](http://www.riverbankcomputing.co.uk/software/pyqt/download)

### Kivy

[Kivy](http://kivy.org/) 是一个Python库，该库用于开发多点触控的媒体应用。 当代码需要重复利用并且可部署时，它能够实现快速简单的交互设计，并且加速成形。

Kivy使用Python编写，并且基于OpenGL，除此，它支持不同的输入设备， 例如鼠标、双鼠标、WiiMote、WM_TOUCH、HIDtouch和苹果的产品等等。

Kivy由社区积极开发，并且免费使用。它适用于所有主要的平台（Linux，OSX, Windows, Android）



## Web 应用

### 开发框架 - 应用的开发工具

广义地说，Web框架包含一系列库和一个主要的处理器（handler），这样您就能够构建自己的代码来实现Web应用 （比如说一个交互式的网站）。大多数web框架包含模式和工具，至少实现以下功能：

- URL路由（URL Routing）

  将输入的HTTP请求匹配到特定的Python代码用来调用

- 请求和响应对象（Request and Response Objects）

  封装来自或发送给用户浏览器的信息

- 模板引擎（Template Engine）

  能够将实现应用的Python代码逻辑和其要产生输出的HTML（或其他）分离开

- Web服务器开发（Development Web Server）

  在开发机上运行HTTP服务器，从而快速开发；当文件更新时自动更新服务端代码。

#### Django

[Django](http://www.djangoproject.com/) 是一个功能齐备的web应用框架。它是创建面向内容网站的极佳选择。 通过提供众多工具和模式，Django使得快速构建复杂的、有数据库支持的web应用成为可能， 同时鼓励使用它作为编写代码的最佳实践。

Django拥有非常庞大和活跃的社区。此外，许多预构建的 [可重用模块](http://djangopackages.com/) 可以原样合并到新工程中，或者定制成符合需求的样子。

#### Flask

[Flask](http://flask.pocoo.org/) 是一款针对Python的“微型框架”，它是构建更小应用、API和web服务的极佳选择。 使用Flask构建应用，除了一些函数附上路由，它和写标准Python模块很相似。它真的很赞。

Flask不会提供一切您可能需要的内容，而是实现了web应用框架中最常用的核心组件，比如说URL路由、请求和响应对象和模板等。

作为Flask的用户，由您来决定选择和集成其他您可能用到的组件。比如说数据库访问或者表单生成和验证就不是Flask内置的功能。

#### Tornado

[Tornado](http://www.tornadoweb.org/) 是一个面向Python的异步web框架，它有自己的事件。 这就使得它，举个例子，可以原生地支持WebSockets。编写良好的Tornado应用具有卓越的性能特性。



### 模板系统 - 构建应用的骨架 

多数WSGI应用响应HTTP请求，从而服务于HTML或其他标记语言中的内容。关注点分离的概念建议我们使用模板， 而不是直接由Python生成文本内容。模板引擎管理一系列的模板文件，其系统的层次性和包容性避免了不必要的重复。 模板引擎负责渲染（产生）实际内容，用由应用生成的动态内容填充静态内容。

由于模板文件有时是由设计师或者前端开发者编写，处理不断增长的复杂度会变得困难。

一些通用的良好实践应用到了部分应用中，情景包括传递动态内容到模板引擎和模板自身中。

- 模板文件只应传递需要渲染的动态内容。避免传递附加的“以防万一”的内容： 需要时添加遗漏的变量比移除可能不用的变量要来的容易。
- 许多模板引擎允许在模板中编写复杂语句或者赋值，也有许多允许一些Python代码 在模板中等价编写。这种便利会导致复杂度不可控地增加，也使得查找bug变得更加 困难。
- 我们常常需要混合JavaScript模板和HTML模板。一种聪明的做法是孤立出HTML 模板传递部分变量内容到JavaScript代码中的部分。

#### Jinja2

[Jinja2](http://jinja.pocoo.org/) 是一个很受欢迎的模板引擎。

它使用基于文本的模板语言，因此可以用于生成任何类型的标记，而不仅仅是HTML。 它允许自定义过滤器，标签，测试和全局变量。 它具有Django模板系统的许多改进。

#### Chameleon

[Chameleon](https://chameleon.readthedocs.io/) 页面模板是使用 [模板属性语言（Template Attribute Language, TAL）](https://en.wikipedia.io/wiki/Template_Attribute_Language)、 [TAL表达语法（TAL Expression Syntax,TALES）](https://chameleon.readthedocs.io/en/latest/reference.html#expressions-tales) 和 [宏扩展TAL（Macro Expansion TAL, Metal）](https://chameleon.readthedocs.io/en/latest/reference.html#macros-metal) 语法的HTML/XML模板引擎实现。

页面模板是在文档结构中添加特定元素属性和文本标记。使用一系列简单语言概念，您能够控制文档流程、元素重复、文本替换和翻译。 由于使用了基于属性的语法，未渲染的页面模板是合法的HTML，它可以在浏览器中查看，甚至能够在WYSIWYG编辑器中编辑。 这使得设计者和原型构建者之间在浏览器是中静态文件上的往复合作变得更加简单。

#### Mako

[Mako](http://www.makotemplates.org/) 是一种模板语言，为了最大的性能，它编译为了Python。 它的语法和API借鉴了其他模板语言，如Django和Jinja2中最好的部分。它 是包括 [Pylons 和 Pyramid](http://www.pylonsproject.org/) 在内的web框架所使用的默认模板语言。



### 服务器 - 应用的运行工具

Python应用的主体托管于WSGI服务器（比如说 [Gunicorn](http://pythonguidecn.readthedocs.io/zh/latest/scenarios/web.html#gunicorn-ref)） 或是直接或间接在轻量级web服务器（比如说 [nginx](http://pythonguidecn.readthedocs.io/zh/latest/scenarios/web.html#nginx-ref)）之后。

WSGI服务器为Python应用服务，它能更好的处理诸如静态文件服务、请求路由、DDoS保护和基本认证的任务。

#### Python 应用和 Web 服务器交互

web 服务器和 Python 应用之间的交互是通过 WSGI 协议实现的：

Web服务网关接口（Web Server Gateway Interface，简称“WSGI”）是一种在Web服务器 和Python Web应用程序或框架之间的标准接口。通过标准化Web服务器和Python web应用程序 或框架之间的行为和通信，WSGI使得编写可移植的的Python web代码变为可能，使其能够部署在任何 :ref:` 符合WSGI的web服务器 <wsgi-servers-ref>` 上。WSGI记录在 [**PEP 3333**](https://www.python.org/dev/peps/pep-3333)。

#### Python 应用和 WSGI 服务器交互

当然也可以直接使用 WSGI 服务器来运行 Python 应用：

* Gunicorn

  [Gunicorn](http://gunicorn.org/) （Green Unicorn，绿色独角兽）是一个纯Python WSGI服务器， 用来支持Python应用。Gunicorn是如今新Python web应用程序的推荐选择。

* Waitress

  [Waitress](https://waitress.readthedocs.io/) 是一个纯Python WSGI服务器，声称具备“非常可接受的性能”。 它的文档不是很详细，但它确实提供了一些很好的而Gunicorn没有的功能（例如HTTP请求缓冲）。

  Waitress在Python Web开发社区中越来越受欢迎。

* uWSGI

  [uWSGI](https://uwsgi-docs.readthedocs.io/) 用来构建全栈式的主机服务。除了进程管理、进程监控和其他功能外， uWSGI也能作为一个应用服务器，适用于多种编程语言和协议 - 包括Python和WSIG。 uWSGI既能当作独立的web路由器来运行，也能运行在一个完整web服务器（比如Nginx或Apache）之后。 对于后者，web服务器可以基于 [uwsgi 协议](https://uwsgi-docs.readthedocs.io/en/latest/Protocol.html) 配置uWSGI和应用的操作。uWSGI的web服务器支持允许动态配置Python、传递环境变量以及进一步优化。




## 数据库

### DB-API

Python数据库API（DB-API）定义了一个Python数据库访问模块的标准接口。它的文档在 [**PEP 249**](https://www.python.org/dev/peps/pep-0249) 可以查看。 几乎所有Python数据库模块，诸如 sqlite3， psycopg 以及 mysql-python 都遵循这个接口。

### SQLAlchemy

[SQLAlchemy](http://www.sqlalchemy.org/) 是一个流行的数据库工具。不像很多 数据库库，它不仅提供一个ORM层，而且还有一个通用API来编写避免SQL的数据库无关代码。

### Records

[Records](https://github.com/kennethreitz/records) 是极简SQL库，旨在将原始SQL查询发送到各种数据库。 数据可以以编程方式使用，也可以导出到一些有用的数据格式。

### Django ORM

Django ORM 是 [Django](http://www.djangoproject.com/) 用来进行数据库访问的接口。

它的思想建立在 [models](https://docs.djangoproject.com/en/dev/#the-model-layer) ， 之上。这是一个致力于简化Python中数据操作的抽象层。

### peewee

[peewee](http://docs.peewee-orm.com/en/latest/) 是另一个ORM，它致力于轻量级和支持Python2.6+与3.2+默认支持的 SQLite，MySQL以及Postgres

### PonyORM

[PonyORM](http://ponyorm.com/) 是一个ORM，它使用与众不同的方法查询数据库，有别于 使用类似SQL的语言或者布尔表达式，它使用Python的生成器达到目的。而且还有一个图形化 schema编辑器生成PonyORM实体。





## 爬虫

Web站点使用HTML描述，这意味着每个web页面是一个结构化的文档。有时从中 获取数据同时保持它的结构是有用的。web站点不总是以容易处理的格式， 如 `csv` 或者 `json` 提供它们的数据。

这正是web抓取出场的时机。Web抓取是使用计算机程序将web页面数据进行收集 并整理成所需格式,同时保存其结构的实践。

### Scrapy

爬虫开发框架

### Requests

跟网站进行复杂的网络交互，并提供了从页面提取数据的函数

### Libxml

[lxml](http://lxml.de/) 是一个优美的扩展库，用来快速解析XML以及HTML文档 即使所处理的标签非常混乱。



## 图像处理

多数图像处理与操作技术可以被两个库有效完成，它们是Python Imaging Library (PIL)与 OpenSource Computer Vision (OpenCV)。

### PIL/Pillow

[Python Imaging Library](http://www.pythonware.com/products/pil/) ，或者叫PIL，简略来说， 是Python图像操作的核心库。不幸的是，它的开发陷入了停滞，最后一次更新是2009年。

对您而言幸运的是，存在一个活跃的PIL开发分支，叫做 [Pillow](http://python-pillow.github.io/) 它很容易安装，运行在各个操作系统上，而且支持Python3。

这里有一些Pillow库的例子： [Pillow 教程](https://pillow.readthedocs.io/en/3.0.x/handbook/tutorial.html)。

### OpenCV

OpenSource Computer Vision,其更广为人知的名字是OpenCv，是一个在图像操作与处理上 比PIL更先进的库。它可以在很多语言上被执行并被广泛使用。

在Python中，使用OpenCV进行图像处理是通过使用 `cv2` 与 `NumPy` 模块进行的。 [OpenCV 安装指南](http://docs.opencv.org/2.4/doc/tutorials/introduction/table_of_content_introduction/table_of_content_introduction.html#table-of-content-introduction) 可以指导您如何为您自己的项目进行配置。

更多的OpenCV在Python运行例子在这里可以找到： [collection of tutorials](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html).



## 运维

http://pythonguidecn.readthedocs.io/zh/latest/scenarios/admin.html



## 科学计算

由于科学计算对高性能的要求，Python中相关操作经常借用外部库，通常是 以更快的语言（如C，或者FORTRAN来进行矩阵操作）写的。其主要的库有 [Numpy](http://numpy.scipy.org/), [Scipy](http://scipy.org/) 以及 [Matplotlib](http://matplotlib.sourceforge.net/)。关于这些库的细节超出了本指南的范围。不过， 关于Python的科学计算生态的综合介绍可以在这里找到 [Python Scientific Lecture Notes](http://scipy-lectures.github.com/)。

### Python 的科学发行版

安装这些科学计算Python包可能会有些麻烦，因为它们中很多是用Python的C扩展实现的， 这就意味着需要编译。这一节列举了各种科学计算Python发行版，它们提供了预编译编译 且易于安装的科学计算Python包。

#### windows 平台

很多人在Windows平台上做科学计算，然而众所周知的是，其中很多科学计算包在该平台上 难以构建和安装。不过， [Christoph Gohlke](http://www.lfd.uci.edu/~gohlke/pythonlibs/) 将一系列有用的Python包编译成了Windows的二进制文件，其数量还在不断增长。如果您在 Windows上工作，您也许想要看看。

#### Anaconda

[Continuum Analytics](http://continuum.io/) 提供了 [Anaconda Python Distribution](https://store.continuum.io/cshop/anaconda)，它 拥有所有常见的Python科学包，也包括与数据分析和大数据相关的包。Anaconda是免费的 而Continuum销售一些专有的额外组件。学术研究者可以获取这些组件的免费许可。

#### Canopy

[Canopy](https://www.enthought.com/products/canopy/) 是另一个Python科学发布版，由 [Enthought](https://www.enthought.com/) 提供。其受限制的 ‘Canopy Express’ 版本 是免费提供的，但是Enthought负责完整版。学术研究者可以获取到免费许可。



### IPython

[IPython](http://ipython.org/) 是一个加强版Python解释器，它提供了科学工作者 感兴趣的特性。其中，inline mode 允许将图像绘制到终端中（基于Qt）。 进一步的，notebook 模式支持文学化编程（literate programming， 译者注：作者这里可能是指其富文本性不是那个编程范式）与可重现性（reproducible， 译者注：作者可能是指每段程序可以单独重新计算的特性），它产生了一个基于web的 python 笔记本。这个笔记本允许您保存一些代码块，伴随着它们的计算结果以及增强的 注释（HTML,LaTex,Markdown）。这个笔记本可以被共享并以各种文件格式导出。

### NumPy

[NumPy](http://numpy.scipy.org/) 是一个用C和FORTRAN写的底层库，它提供一些高层 数学函数。NumPy通过多维数组和操作这些数组的函数巧妙地解决了Python运行算法较慢的问题。 任何算法只要被写成数组中的函数，就可以运行得很快。

NumPy是SciPy项目中的一部分，它被发布为一个独立的库，这样对于只需基本功能的人来说， 就不用安装SciPy的其余部分。

NumPy兼容Python 2.4-2.7.2以及3.1+。

### Numba

[Numba](http://numba.pydata.org/) 是一个针对NumPy的Python编译器（即时编译器,JIT） 它通过特殊的装饰器，将标注过的Python（以及NumPy）代码编译到LLVM（Low Level Virtual Machine，底层虚拟机）中。简单地说，Python使用一种机制，用LLVM将Python代码编译为 能够在运行时执行的本地代码。

### SciPy

[SciPy](http://scipy.org/) 是基于NumPy并提供了更多的数学函数的库。 SciPy使用NumPy数组作为基本数据结构，并提供完成各种常见科学编程任务的模块， 包括线性代数，积分（微积分），常微分方程求解以及信号过程。

### Matplotlib

[Matplotlib](http://matplotlib.sourceforge.net/) 是一个可以灵活绘图的库，它 能够创建2D、3D交互式图形，并能保存成具有稿件质量（manuscript-quality）的图表。 其API很像 [MATLAB](http://www.mathworks.com/products/matlab/)，这使得MATLAB用户 很容易转移到Python。在 [matplotlib gallery](http://matplotlib.sourceforge.net/gallery.html) 中可以找到很多例子以及实现它们的源代码（可以在此基础上再创造）。

### Pandas

[Pandas](http://pandas.pydata.org/) 是一个基于NumPy的数据处理库，它提供了 许多有用的函数能轻松地对数据进行访问、索引、合并以及归类。其主要数据结构（DataFrame） 与R统计学包十分相近；也就是，使用名称索引的异构数据（heterogeneous data）表、时间序列操作以及对数据的自动对准（auto-alignment）。

### Rpy2

[Rpy2](http://rpy2.bitbucket.org/) 是一个对R统计学包的Python绑定， 它能够让Python执行R函数，并在两个环境中交换数据。Rpy2是 对 [Rpy](http://rpy.sourceforge.net/rpy.html) 绑定的面向对象实现。

### PsychoPy

[PsychoPy](http://www.psychopy.org/) 是面向认知科学家的库，它允许创建 认知心理学和神经科学实验（译者注：指的是那种您坐在电脑前，给您一个刺激测 您反应的实验，基本上就是个UI）。这个库能够处理刺激表示、实验设计脚本以及 数据收集。



## C/C++ 交互

### CFFI

[CFFI](https://cffi.readthedocs.io/en/latest/) 通过CPython和PyPy给出了和 C语言交互的简单使用机制。它支持两种模式：一种是内联的ABI兼容模式(示例如下)， 它允许您动态加载和运行可执行模块的函数(本质上与LoadLibrary和dlopen拥有相同的功能)； 另一种为API模式，它允许您构建C语言扩展模块。

### ctypes

[ctypes](https://docs.python.org/3/library/ctypes.html) 是CPython中与C/C++ 交互的事实上的库。它不仅能完全访问大多数主流操作系统(比如：Windows上的Kernel32， *nix上的libc)的纯C接口，并且支持对动态库的加载和交互，如DLL和运行时共享对象。 它同时涵盖许多可和系统API交互的类型，并允许您以相对简单的方式定义自己的复杂类型， 如struct和union，并在需要时允许您作出如填充、对齐这样的修改。对它的使用可能稍显复杂， 但与 [struct](https://docs.python.org/3.5/library/struct.html) 模块配合使用， 可通过纯C(++)方法让您从根本上控制您的数据类型转换成更有用的东西。

### SWIG 

[SWIG](http://www.swig.org/) 并不仅仅应用于Python(它支持多种脚本语言)， 它是生成解释性语言和C/C++头文件绑定的工具。它极易使用：使用者只需简单的定义接口文件 （详见相关指南和文档），包含必要的C/C++头文件，并对它们运行生成工具。但它也有其局限性， 目前，它与C++部分新特性间仍存在问题，而模板重码的工作多少有些冗繁。只需少量的工作， 它便能提供诸多作用，并展现Python的许多特性。同时，您可以简单的扩展SWIG生成的绑定 （在接口文件中）来重载操作符和内建函数，也可以有效的重新转换C++异常， 使其可被Python所捕获。

### Boost.Python

[Boost.Python](http://www.boost.org/doc/libs/1_59_0/libs/python/doc/) 需要一些手动工作来展现C++对象的功能，但它可提供SWIG拥有的所有特性。同时， 它可提供在C++中访问Python对象的封装，也可提取SWIG封装的对象， 甚至可在C++代码中嵌入部分Python。