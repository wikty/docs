# 项目目录

```
project_dir/
	.git/
	googlemaps/
		googlemaps.py
	test/
		test_googlemaps.py
	doc/
		index.rst
		html/
			index.html
	README.txt
	LICENSE.txt
	setup.py
	MANIFEST.in
```

# 项目结构化

我们对于“结构化”的定义是您关注于怎样使您的项目最好地满足它的对象性，我们 需要去考虑如何更好地利用Python的特性来创造简洁、高效的代码。在实践层面， “结构化”意味着通过编写简洁的代码，并且正如文件系统中文件和目录的组织一样， 代码应该使逻辑和依赖清晰。

哪个函数应该深入到哪个模块？数据在项目中如何流转？什么功能和函数应该组合 或独立？要解决这些问题，您可以开始做个一计划，大体来说，即是您的最终产品 看起来会是怎样的。

### 项目目录结构/仓库目录

在一个健康的开发周期中，代码风格，API设计和自动化是非常关键的。同样的，对于工程的 [架构](http://www.amazon.com/gp/product/1257638017/ref=as_li_ss_tl?ie=UTF8&tag=bookforkind-20&linkCode=as2&camp=1789&creative=39095&creativeASIN=1257638017) ,仓库的结构也是关键的一部分。

当一个潜在的用户和贡献者登录到您的仓库页面时，他们会看到这些:

- 工程的名字
- 工程的描述
- 一系列的文件

只有当他们滚动到目录下方时才会看到您工程的README。

如果您的仓库的目录是一团糟，没有清晰的结构，他们可能要到处寻找才能找到您写的漂亮的文档。

> 为您的渴望的事业而奋斗，而不是仅仅只为您现在的工作而工作。

当然，第一印象并不是一切。但是，您和您的同事会和这个仓库并肩战斗很长时间，会熟悉它的每一个角落和细节。拥有良好的布局，事半功倍。

样例

```
README.rst
LICENSE
setup.py
requirements.txt
sample/__init__.py
sample/core.py
sample/helpers.py
docs/conf.py
docs/index.rst
tests/test_basic.py
tests/test_advanced.py
```

具体介绍

1. sample 目录

   您的模块包是这个仓库的核心，它不应该隐藏起来，放在其他目录:

   ```
   ./sample/

   ```

   如果您的模块只有一个文件，那么您可以直接将这个文件放在仓库的根目录下:

   ```
   ./sample.py
   ```

2. LICENSE

   除了源代码本身以外，这个毫无疑问是您仓库最重要的一部分。在这个文件中要有完整的许可说明和授权。

   如果您不太清楚您应该使用哪种许可方式，请查看 [choosealicense.com](http://choosealicense.com/).

   当然，您也可以在发布您的代码时不做任何许可说明，但是这显然阻碍潜在的用户使用您的代码。

3. setup.py

   打包和发布管理，跟模块包在同一目录，应该放在仓库根目录下

4. requirements.txt

   记录项目对第三方库依赖关系的文件，它应该指明完整工程的所有依赖包: 测试, 编译和文档生成。

   如果您的工程没有任何开发依赖，或者您喜欢通过 `setup.py` 来设置，那么这个文件不是必须的。

5. docs 目录

   包的参考文档

6. tests 目录

   包的相关测试代码

   最开始，一组测试例子只是放在一个文件当中:

   ```
   ./test_sample.py

   ```

   当测试例子逐步增加时，您会把它放到一个目录里面，像下面这样:

   ```
   tests/test_basic.py
   tests/test_advanced.py
   ```

7. Makefile / manage.py 等

   常规的管理任务（可选的）。

   如果您看看我的项目或者其他开源项目，您都会发现有一个Makefile。为什么？这些项目也不是用C写的啊。。。简而言之，make对于定义常规的管理任务是非常有用的工具。

   样例 Makefile:

   ```
   init:
       pip install -r requirements.txt

   test:
       py.test tests

   PHONY: init test

   ```

   一些其他的常规管理脚本（比如 `manage.py` 或者 `fabfile.py`），也放在仓库的根目录下。



如何解决测试代码中需要导入包的模块？

当然，这些测试例子需要导入您的包来进行测试，有几种方式来处理:

- 将您的包安装到site-packages中。
- 通过简单直接的路径设置来解决导入的问题。

我极力推荐后者。如果使用 `setup.py develop` 来测试一个持续更新的代码库，需要为每一个版本的代码库设置一个独立的测试环境.太麻烦了。

可以先创建一个包含上下文环境的文件 tests/context.py。 file:

```
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sample

```

然后，在每一个测试文件中，导入:

```
from .context import sample

```

这样就能够像期待的那样工作，而不用采用安装的方式。

一些人会说应该把您的测试例子放到您的模块里面 – 我不同意。这样会增加您用户使用的复杂度；而且添加测试模块将导致需要额外的依赖和运行环境。



创建 django 项目时，应该避免在仓库目录进行嵌套

在进入一个新的仓库后，通常都这样操作：

```
$ django-admin.py startproject samplesite

```

这样的操作生成的仓库结构是这样的:

```
README.rst
samplesite/manage.py
samplesite/samplesite/settings.py
samplesite/samplesite/wsgi.py
samplesite/samplesite/sampleapp/models.py 
```

可以看到显然仓库目录下的项目代码有了两层嵌套结构

应该这样来做：

```
$ django-admin.py startproject samplesite .

```

注意末尾的 “`.`“。

生成的结构是这样的:

```
README.rst
manage.py
samplesite/settings.py
samplesite/wsgi.py
samplesite/sampleapp/models.py
```

### 软件架构和 Python 模块、包

得益于Python提供的导入与管理模块的方式，结构化Python项目变得相对简单。 这里说的简单，指的是结构化过程没有太多约束限制而且模块导入功能容易掌握。 因而您只剩下架构性的工作，包括设计、实现项目各个模块，并整理清他们之间 的交互关系。



Python 代码中文件即模块，目录即包



#### 模块

Python模块是最主要的抽象层之一，并且很可能是最自然的一个。抽象层允许将代码分为 不同部分，每个部分包含相关的数据与功能。

例如在项目中，一层控制用户操作相关接口，另一层处理底层数据操作。最自然分开这两 层的方式是，在一份文件里重组所有功能接口，并将所有底层操作封装到另一个文件中。 这种情况下，接口文件需要导入封装底层操作的文件，可通过 `import` 和 `from ...import` 语句完成。一旦您使用 import 语句，就可以使用这个模块。 既可以是内置的模块包括 os 和 sys，也可以是已经安装的第三方的模块，或者项目 内部的模块。

为遵守风格指南中的规定，模块名称要短、使用小写，并避免使用特殊符号，比如点(.) 和问号(?)。如 `my.spam.py` 这样的名字是必须不能用的！该方式命名将妨碍 Python的模块查找功能。就 my.spam.py 来说，Python 认为需要在 `my` 文件夹 中找到 `spam.py` 文件，实际并不是这样。这个例子 [example](http://docs.python.org/tutorial/modules.html#packages) 展示了点表示 法应该如何在Python文件中使用。如果愿意您可以将模块命名为 `my_spam.py`， 不过并不推荐在模块名中使用下划线。但是，在模块名称中使用其他字符（空格或连字号） 将阻止导入（-是减法运算符），因此请尽量保持模块名称简单，以无需分开单词。 最重要的是，不要使用下划线命名空间，而是使用子模块。

```
# OK
import library.plugin.foo
# not OK
import library.foo_plugin

```

除了以上的命名限制外，Python文件成为模块没有其他特殊的要求，但为了合理地使用这 个观念并避免问题，您需要理解import的原理机制。具体来说，`import modu` 语句将 寻找合适的文件，即调用目录下的 `modu.py` 文件（如果该文件存在）。如果没有 找到这份文件，Python解释器递归地在 “PYTHONPATH” 环境变量中查找该文件，如果仍没 有找到，将抛出ImportError异常。

一旦找到 `modu.py`，Python解释器将在隔离的作用域内执行这个模块。所有顶层 语句都会被执行，包括其他的引用。方法与类的定义将会存储到模块的字典中。然后，这个 模块的变量、方法和类通过命名空间暴露给调用方，这是Python中特别有用和强大的核心概念。

在很多其他语言中，`include file` 指令被预处理器用来获取文件里的所有代码并‘复制’ 到调用方的代码中。Python则不一样：include代码被独立放在模块命名空间里，这意味着您 一般不需要担心include的代码可能造成不好的影响，例如重载同名方法。

也可以使用import语句的特殊形式 `from modu import *` 模拟更标准的行为。但 `import *`通常 被认为是不好的做法。**使用** `from modu import *` **的代码较难阅读而且依赖独立性不足**。 使用 `from modu import func` 能精确定位您想导入的方法并将其放到全局命名空间中。 比 `from modu import *` 要好些，因为它明确地指明往全局命名空间中导入了什么方法，它和 `import modu` 相比唯一的优点是之后使用方法时可以少打点儿字。

**差**

```
[...]
from modu import *
[...]
x = sqrt(4)  # sqrt是模块modu的一部分么？或是内建函数么？上文定义了么？

```

**稍好**

```
from modu import sqrt
[...]
x = sqrt(4)  # 如果在import语句与这条语句之间，sqrt没有被重复定义，它也许是模块modu的一部分。

```

**最好的做法**

```
import modu
[...]
x = modu.sqrt(4)  # sqrt显然是属于模块modu的。

```

在 [代码风格](http://pythonguidecn.readthedocs.io/zh/latest/writing/style.html#code-style) 章节中提到，可读性是Python最主要的特性之一。可读性意味着避免 无用且重复的文本和混乱的结构，因而需要花费一些努力以实现一定程度的简洁。但不能 过份简洁而导致简短晦涩。除了简单的单文件项目外，其他项目需要能够明确指出类和方法 的出处，例如使用 `modu.func` 语句，这将显著提升代码的可读性和易理解性。

#### 包

Python提供非常简单的包管理系统，即简单地将模块管理机制扩展到一个目录上(目录扩 展为包)。

任意包含 `__init__.py` 文件的目录都被认为是一个Python包。导入一个包里不同 模块的方式和普通的导入模块方式相似，特别的地方是 `__init__.py` 文件将集合 所有包范围内的定义。

`pack/` 目录下的 `modu.py` 文件通过 `import pack.modu` 语句导入。 该语句会在 `pack` 目录下寻找 `__init__.py` 文件，并执行其中所有顶层 语句。以上操作之后，`modu.py` 内定义的所有变量、方法和类在pack.modu命名空 间中均可看到。

一个常见的问题是往 `__init__.py` 中加了过多代码，随着项目的复杂度增长， 目录结构越来越深，子包和更深嵌套的子包可能会出现。在这种情况下，导入多层嵌套 的子包中的某个部件需要执行所有通过路径里碰到的 `__init__.py` 文件。如果 包内的模块和子包没有代码共享的需求，使用空白的 `__init__.py` 文件是正常 甚至好的做法。

最后，导入深层嵌套的包可用这个方便的语法：`import very.deep.module as mod`。 该语法允许使用 mod 替代冗长的 `very.deep.module`。



#### 不良的架构设计

容易结构化的项目同样意味着它的结构化容易做得糟糕。糟糕结构的特征包括：

- 多重且混乱的循环依赖关系：假如在 `furn.py` 内的Table与Chair类需要 导入 `workers.py` 中的Carpenter类以回答类似 `table.isdoneby()` 的问题，并且Carpenter类需要引入Table和Chair类以回答 `carpenter.whatdo()` 这类问题，这就是一种循环依赖的情况。在这种情况下,您得借助一些不怎么靠谱的 小技巧，比如在方法或函数内部使用import语句。
- 隐含耦合：Table类实现代码中每一个改变都会打破20个不相关的测试用例，由于它 影响了Carpenter类的代码，这要求谨慎地操作以适应改变。这样的情况意味着 Carpenter类代码中包含了太多关于Table类的假设关联（或相反）。
- 大量使用全局变量或上下文：如果Table和Carpenter类使用不仅能被修改而且能被 不同引用修改的全局变量，而不是明确地传递 `(height, width, type, wood)` 变量。您就需要彻底检查全局变量的所有入口，来理解到为什么一个长方形桌子变 成了正方形，最后发现远程的模板代码修改了这份上下文，弄错了桌子尺寸规格的 定义。
- 面条式代码 (Spaghetti code) ：多页嵌套的if语句与for循环，包含大量复制-粘贴 的过程代码，且没有合适的分割——这样的代码被称为面条式代码。Python中有意思 的缩进排版(最具争议的特性之一)使面条式代码很难维持。所以好消息是您也许不 会经常看到这种面条式代码。
- Python中更可能出现混沌代码：这类代码包含上百段相似的逻辑碎片，通常是缺乏 合适结构的类或对象，如果您始终弄不清手头上的任务应该使用FurnitureTable， AssetTable还是Table，甚至TableNew，也许您已经陷入了混沌代码中



# 项目构建流程

## 项目托管

项目需要托管在一个网站上，这样人们才可以下载、学习使用并留下反馈。现在有许多流行的免费开源项目托管网站：

- Bitbucket: [http://bitbucket.org/](http://bitbucket.org/)
- CodePlex: [http://www.codeplex.com/](http://www.codeplex.com/)
- Freepository: [https://freepository.com/](https://freepository.com/)
- GitHub: [http://github.com/](http://github.com/)
- Gitorious: [http://gitorious.org/](http://gitorious.org/)
- Google Code: [http://code.google.com/projecthosting/](http://code.google.com/projecthosting/)
- Launchpad: [https://launchpad.net/](https://launchpad.net/)
- Sourceforge: [http://www.sourceforge.net/](http://www.sourceforge.net/)
- Tuxfamily: [http://www.tuxfamily.org/](http://www.tuxfamily.org/)

Your code needs a home on the Internet: a website where people can download your software, learn how to use it, and provide feedback. There are several websites that will host your open-source project for free; some popular choices are listed below. The basic requirements are web page hosting, a version control system, and a user feedback system. Feedback mechanisms include bug trackers, forums, and mailing lists. If you’re not sure which host to use, Sourceforge is one of the oldest and best-known hosts; I’ll be using Sourceforge in the examples below.

为你的项目起个名字

You’ll need a project name in order to register. Your project’s name is important, but don’t spend too much time obsessing over it. It’s worth doing a quick search on [Google](http://www.google.com/), [The Python Package Index](http://pypi.python.org/) and [freshmeat](http://www.freshmeat.net/) to see if someone else already has a software product by that name. If it’s something totally unrelated, it’s probably not a problem (but watch out for trademarks). If your name is taken, consider tacking on “Py” or “Python” or a clever [Monty Python](http://en.wikipedia.org/wiki/Monty_Python) reference.

> Note
>
> Your project name or “short name” may be taken on your host; this may affect the URL of your project’s homepage and detract from its “findability.” Your project’s actual name doesn’t have to match the project name you use on your host, but it helps. Decide whether that’s important; if so, consider whether you want to change your project’s name, live with a mismatched host project name, or find another hosting service that has your name available.
>
> Note
>
> You *can* set up a project on your own website and host things yourself, but it’s more work.

Sign up for an account on your chosen host. Register your project, and take a few minutes to fill in your project’s metadata. Including a brief description, category, tags or keywords, programming language, etc. will make your software easier for people to find and grok. (If your host requires you to choose a license for your software up front, have a look at the [licensing](http://infinitemonkeycorps.net/docs/pph/#id9) section.)



## 项目版本控制

使用一个版本控制工具来管理你的项目

### Create a Repository

You will need to set up a version control system (VCS; also called a revision control or source code mangagement system) to hold your code on the Internet. This is practically what it means to be an open source project: anybody can easily download your code at any time. It also has the practical benefit of keeping backup copies of every version of your code you check in.

Subversion is probably the most widely-known VCS, and something of a lowest common denominator. It’s a good default choice, supported by many project hosts, and available on all platforms. I’ll be using Subversion for the examples in this article, but feel free to choose one of the newer, sexier VCSes below. They are all functionally identical for the basics, and most have facilities to import from or export to Subversion if you decide you want to change later.

Note that your choice of project host may limit your choice of VCS, or vice versa.

Create a SVN (or git, or hg, or bzr, or...) repository at your project host’s website.

### Back Up Your Code

Backing up is always a good idea; we’ll just make a quick tarball in case something gets hosed.

> Note
>
> I’m using Unix command lines and pathnames in this document, but the concepts easily map to other operating systems.

In what follows, I’m going to assume your Python source currently lives at `*/path/to/googlemaps/googlemaps.py*`. You’ll need to replace `*/path/to/*` with the appropriate path on your system, and everywhere you see `*googlemaps*`, replace it with the appropriate name for your project. Now, about that tarball:

> `$ cd */path/to/*`
>
> `$ tar czvf *googlemaps*.tgz *googlemaps/*`

While you’re at it, you should clean out your source directory, remove any compiled/binary files (such as `*.pyc`), clean out any hidden settings files or directories (you have a backup!), and remove anything sensitive or private; everything in there is about to be shared with the world.

Now we’ll move your code directory aside for the new one we’re about to create:

> `$ mv *googlemaps*/ *googlemaps*-backup/`

### Check out the repository

Your host should give you a URL or command to check out the repository. Here’s what it looks like for **svn** from Sourceforge:

> `$ cd */path/to/googlemaps*`
>
> `$ svn co https://*googlemaps*.svn.sourceforge.net/svnroot/*googlemaps* *googlemaps*`

This should give you a new `googlemaps` directory containing a hidden `.svn` directory (or whatever VCS you’re using).

### Copy your code into your working repo copy

Your new `googlemaps` directory will soon contain other things besides source code (remember: it’s a *project* now!), so we are going to make a new subdirectory for your code. Source files go in a subdirectory with the same name as the project or package.

> `$ svn mkdir */path/to/googlemaps/googlemaps*` (note the **svn**!)
>
> `$ cp -a */path/to/googlemaps*-backup/* */path/to/googlemaps*/`

### Add your code to the repository

> `$ cd */path/to/googlemaps/*`
>
> `$ svn add *`

### Commit your changes

> `$ svn commit -m "Initial import."`

That’s it. The master copy of the code now lives on your project host’s servers.. You’ll do all of your coding in this new working directory on your machine, and periodically commit changes to the server. If you’re new to version control, refer to the appropriate link below, but basically: you’ll need to tell your VCS whenever you’re adding, moving, or deleting a file from your source. Here are the basics for **svn**:

> **svn stat** - Show what’s added or changed
>
> **svn commit** - Save a snapshot of your code to the repo
>
> **svn add** - Put a new file under version control
>
> **svn mv** - Tell svn when you’re moving a file (use instead of **/bin/mv**)
>
> **svn rm** - Tell svn you’re removing a file (use instead of **/bin/rm**)
>
> **svn mkdir** - Create a new directory in your working copy (use instead of **/bin/mkdir**)
>
> **svn update** - Download any changes from the repo into your working copy

### 常用的几种版本控制工具

- Bazaar (bzr): [http://bazaar-vcs.org/](http://bazaar-vcs.org/)
- Git (git): [http://git-scm.com/](http://git-scm.com/)
- Mercurial (hg): [http://mercurial.selenic.com/wiki/](http://mercurial.selenic.com/wiki/)
- Subversion (svn): [http://subversion.tigris.org/](http://subversion.tigris.org/)



## 高质量的编码

高质量编码既是一门艺术，也是一门科学。有各种原则指导如何写出高质量代码，同时也有各种工具来量化高质量。

Writing good code is a journey. [The Pragmatic Programmer](http://www.pragprog.com/the-pragmatic-programmer) by Andrew Hunt and David Thomas is a good first step. [Code Complete](http://cc2e.com/) by Steve McConnell is another. A good sense of design and implementation can be learned, but you still have to use it. Probably the single biggest driver of open source code quality is knowing that other hackers will be looking at and using your code. Write code for other humans to read: your peers, your clients, your potential employers... your open source projects become a part of your reputation, your resume. Invest the effort to write good code. (Did I mention it will save you time and grief in the long run?)

Writing good code is an art. Aesthetics are subjective, but in Python, there is a generally accepted standard for formatting your code: [PEP 8](http://python.org/dev/peps/pep-0008/). Read it. There is a tool, [pep8](http://pypi.python.org/pypi/pep8/), for checking your code against it.

Writing good code is a science. There are (semi-) objective means of measuring code quality. First, your code should work, which we can verify with [unit testing](http://infinitemonkeycorps.net/docs/pph/#id5). Second, your code should look and [smell](http://en.wikipedia.org/wiki/Code_smell) good, which we can check with [Pylint](http://www.logilab.org/857).

### Python 2 和 Python 3 兼容

The Python world is starting to make a leisurely transition to [Python 3](http://docs.python.org/dev/3.0/whatsnew/3.0.html), which is not backwards compatible with Python 2. You can prepare your code for the future by running your [unit tests](http://infinitemonkeycorps.net/docs/pph/#unittesting) under Python 2.6+ with the `-3` switch:

> `$ python -3 test/test_mymodule.py`

This will warn you about things that will change in Python 3. If you really want to make sure your code works in Python 3, use the [2to3](http://docs.python.org/library/2to3.html)tool to translate your code to Python 3, then install Python 3 (keep your Python 2!) and run your unit tests under it. Don’t try to maintain both versions; just keep running your 2.x source through **2to3**.

Quality code is the most important part of an open source project. Once your package is set up, this is where you should spend most of your time.

### 代码质量检测工具

- Pylint, [lint](http://en.wikipedia.org/wiki/Lint_(software)) for Python: [http://www.logilab.org/857](http://www.logilab.org/857)
- PEP 8, Style Guide for Python Code: [http://python.org/dev/peps/pep-0008/](http://python.org/dev/peps/pep-0008/)
- pep8, code formatting checker: [http://pypi.python.org/pypi/pep8/](http://pypi.python.org/pypi/pep8/)
- Pyntch, a static type checker (for a dynamic language!): [http://www.unixuser.org/~euske/python/pyntch/index.html](http://www.unixuser.org/~euske/python/pyntch/index.html)
- PyFlakes, a fast lint-like tool for Python: [http://divmod.org/trac/wiki/DivmodPyflakes](http://divmod.org/trac/wiki/DivmodPyflakes)
- PyChecker, a Python source code checking tool: [http://pychecker.sourceforge.net/](http://pychecker.sourceforge.net/)
- PyMetrics, code statistics including cyclomatic complexity: [http://sourceforge.net/projects/pymetrics/](http://sourceforge.net/projects/pymetrics/)
- 2to3, Automated Python 2 to 3 code translation: [http://docs.python.org/library/2to3.html](http://docs.python.org/library/2to3.html)

### Pylint 简介

> `$ sudo easy_install pylint`
>
> `$ pylint mymodule.py`

Pylint warns you about many potential problems with your code. The first you’ll probably notice are naming conventions. The short of it is that pretty much all identifiers should be `lowercase_with_underscores`, with the exception of `ClassNames` and `ExceptionNames`, which are CamelCased (and exception names should generally end with Error). “Constants” are `UPPER_CASE_UNDERSCORE`.`_private_identifiers` can be prefixed with a leading underscore, but for modules, there’s a better way: list all public classes, functions, and data as strings in a global list called `__all__`:

```
__all__ = ['GoogleMaps', 'GoogleMapsError']
```

A quick advice rundown: One- and two-character variable names are generally too short to be meaningful. Indent with 4 spaces. Put whitespace around operators and after commas. Give everything a docstring. Don’t shadow variables. Use `is` to compare with `None`, `True`, and `False`. Make your own exceptions subclass `Exception`. Limit `try` clauses to the bare minimum amount of code; catch the most specific exception possible (i.e., not `Exception`). Keep it simple. Last but very first: don’t use global variables.

Look at and learn about the warnings Pylint produces. Know when to ignore them; it can produce false positives. If Pylint complains and you are really sure that your code is safe, indicate to Pylint (and anyone reading your code) that you know what you’re doing:

```
def fetch_json(query_url, params={}, headers={}):       # pylint: disable-msg=W0102
    ...
```

Try for a Pylint score of at least 8. Personally, I try to fix or shush all messages except those about long line length in code (I do keep docstrings trimmed for people using the interactive help).



## 单元测试

测试驱动开发

A good way to check whether your code works is to try it. A great way is to try it automatically, every time it changes. That’s the premise of [unit testing](http://en.wikipedia.org/wiki/Unit_testing): write code to test your code, so that it’s easy, so that you’ll do it often. In this context, unit means module, class, or function; we test each unit of functionality separately, so we have more confidence everything will work when we put it all together.

Python 中几种流行的单元测试工具

### doctest

Python has two standard unit testing modules, `doctest` and `unittest` (it’s that important!). `doctest` is a fantastic way to kill two birds with one stone: demonstrating how to use your code by example, and making sure it gives the answers you expect. You can literally run your code in an interactive session, check if its working, and then paste the session into a docstring:

```
def local_search(self, query, numresults=_LOCAL_RESULTS_PER_PAGE, **kwargs):
    """
    Searches Google Local for the string `query` and returns a
    dictionary of the results.

    >>> gmaps = GoogleMaps()
    >>> local = gmaps.local_search('sushi san francisco, ca')
    >>> result = local['responseData']['results'][0]
    >>> print result['titleNoFormatting']
    Sushi Groove
    """

```

Then, by putting this in your main routine:

```
if __name__ == "__main__":
    import doctest
    doctest.testmod()

```

`doctest` will automatically pull the code out of your docstring, run it, and compare the output to that present in the docstring whenever your module is run as a script.

Writing examples is an important part of [good documentation](http://infinitemonkeycorps.net/docs/pph/documentation) anyway, and with `doctest` it takes almost no extra effort to turn those docs into tests.

### unittest

`unittest` is Python’s standard “heavyweight” unit testing framework. It’s a bit more flexible and a bit more powerful that `doctest`, but it takes a bit more doing to use. Here is the same test using `unittest`:

```
import unittest
from googlemaps import GoogleMaps

class Test(unittest.TestCase):
    """Unit tests for googlemaps."""

    def test_local_search(self):
        """Test googlemaps local_search()."""
        gmaps = GoogleMaps(GMAPS_API_KEY, referrer_url='http://www.google.com/')
        local = gmaps.local_search('sushi san francisco, ca')
        result = local['responseData']['results'][0]
        self.assertEqual(result['titleNoFormatting'], 'Sushi Groove')

if __name__ == "__main__":
    unittest.main()

```

This would go in a file called `test/test_googlemaps.py`, and this is a general rule: tests go in a directory called `test` at the root level of your package, and are named `test_*modulename*.py`. All of the tests for module modulename go in this file, and this file tests all of the functionality in modulename.

Even if you are only using doctests, you should still have a `test/test_*modulename*.py` that runs your doctests:

```
import unittest
import doctest

import googlemaps

class Test(unittest.TestCase):
    """Unit tests for googlemaps."""

    def test_doctests(self):
        """Run googlemaps doctests"""
        doctest.testmod(googlemaps)

if __name__ == "__main__":
    unittest.main()

```

This is because `unittest` is the standard for Python unit testing, and many tools, IDEs, and people expect to find and interface with `unittest` tests in the standard place.

Since the test modules are in a separate directory from your code, you may need to add your module’s parent directory to your **PYTHONPATH** in order to run them:

> `$ cd */path/to/googlemaps*`
>
> `$ export PYTHONPATH=$PYTHONPATH:/path/to/*googlemaps*/*googlemaps*`
>
> `$ python test/test_*googlemaps*.py`

### nose

Finally, there is one more popular unit testing framework for Python (it’s that important!), [nose](http://somethingaboutorange.com/mrl/projects/nose/). `nose` helps simplify and extend the builtin `unittest` framework (it can, for example, automagically find your test code and setup your **PYTHONPATH** for you), but it is not included with the standard Python distribution.

In conclusion: Write unit tests. Run them. Often. It will make you feel MUCH more confident about releasing your code to the world.

### 单元测试相关资源

- unittest, Python’s builtin unit testing framework: [http://docs.python.org/library/unittest.html](http://docs.python.org/library/unittest.html)
- doctest, Test interactive Python examples in docstrings: [http://docs.python.org/library/doctest.html](http://docs.python.org/library/doctest.html)
- nose, “is nicer testing for python”: [http://somethingaboutorange.com/mrl/projects/nose/](http://somethingaboutorange.com/mrl/projects/nose/)
- coverage.py, test coverage measurement: [http://nedbatchelder.com/code/coverage/](http://nedbatchelder.com/code/coverage/)
- Python Testing Tools Taxonomy, including web app and GUI testing tools: [http://pycheesecake.org/wiki/PythonTestingToolsTaxonomy](http://pycheesecake.org/wiki/PythonTestingToolsTaxonomy)

## 项目文档

Good documentation is important for showing others how to use your code as well as for keeping *you* straight on what it’s supposed to do. With the `doctest` module, you can even use it to test your code. Python makes it easy to insert documentation right into the code with [docstrings](http://docs.python.org/tutorial/controlflow.html#documentation-strings); they often even do triple-duty as comments. With just a little extra formatting in your docstrings, you can automatically produce beautiful web or print documentation for your project.

I even suggest writing the documentation *before* writing the code (or at least concurrently). This is a great way to employ user-centered design. You are going to have to explain how to use your code at some point; what design would be the easiest to explain? I’d wager that design would also be in the running for “easy to implement, test and maintain” as well. Writing up the docs first will let you figure out how it all works together before committing to the code.

This works just as well if a module is written by you, for you as a component of a higher-level program. Ask yourself: if I were looking for a module to do XYZ, what would I want it to look like? How would I want to use it? What would I want to know first? What examples would I like to see? Have compassion on yourself: write good documentation (and code) for *you*. Write out the docs for this awesome hypothetical module, see if it “coheres,” then fill in the code.

### Use reStructuredText in docstrings

The Python community is gravitating toward [reStructuredText](http://docutils.sourceforge.net/rst.html) for docstring markup; it’s the equivalent of Javadoc for Python. It’s easy to write and read:

```
def reverse_geocode(self, lat, lng, sensor='false', oe='utf8', ll='', spn='', gl=''):
    """
    Converts a (latitude, longitude) pair to an address.

    Interesting bits:

    >>> gmaps = GoogleMaps()
    >>> reverse = gmaps.reverse_geocode(38.887563, -77.019929)
    >>> address = reverse['Placemark'][0]['address']
    >>> print address
    200 6th St SW, Washington, DC 20024, USA
    >>> accuracy = reverse['Placemark'][0]['AddressDetails']['Accuracy']
    >>> print accuracy
    8

    :param lat: latitude
    :type lat: float
    :param lng: longitude
    :type lng: float
    :return: `Reverse geocoder return value`_ dictionary giving closest
        address(es) to `(lat, lng)`
    :rtype: dict
    :raises GoogleMapsError: If the coordinates could not be reverse geocoded.

    Keyword arguments and return value are identical to those of :meth:`geocode()`.

    .. _`Reverse geocoder return value`:
        http://code.google.com/apis/maps/documentation/geocoding/index.html#ReverseGeocoding

    """

```

It can automatically generate HTML like this:

> - `GoogleMaps.``reverse_geocode`(*lat*, *lng*, *sensor='false'*, *oe='utf8'*, *ll=''*, *spn=''*, *gl=''*)
>
>   Converts a (latitude, longitude) pair to an address.Interesting bits:`>>> gmaps = GoogleMaps()>>> reverse = gmaps.reverse_geocode(38.887563, -77.019929)>>> address = reverse['Placemark'][0]['address']>>> print address200 6th St SW, Washington, DC 20024, USA>>> accuracy = reverse['Placemark'][0]['AddressDetails']['Accuracy']>>> print accuracy8`Parameters:*lat* (float) – latitude*lng* (float) – longitudeReturns:[Reverse geocoder return value](http://code.google.com/apis/maps/documentation/geocoding/index.html#ReverseGeocoding) dictionary giving closest address(es) to (lat, lng)Return type:dictRaises GoogleMapsError: If the coordinates could not be reverse geocoded.Keyword arguments and return value are identical to those of `geocode()`.

Take-home points:

- Normal docstring formatting conventions apply: see [PEP 257](http://www.python.org/dev/peps/pep-0257/).
- Identifier references go in `backticks`.
- `:param lat: latutide` documents parameters
- `:type lat: float` documents parameter types
- `:return: dictionary giving closest addresses...` documents return values
- `:rtype: dict` documents return type
- `:raises GoogleMapsError: If coordinates could not...` documents exceptions raised
- `>>>` starts a doctest and is automatically formatted as code; code can also be indicated by indenting four spaces or preceding with `::` and a blank line
- Link to other methods, functions, classes, modules with `:meth:`*mymethod*``, `:func:`*myfunc*``, `:class:`*myclass*``, and `:mod:`*mymodule*``.
- Hyperlink names go in backticks with a trailing underscore: ``Google`_`, and targets can be defined anywhere with `.. _Google:http://www.google.com/`.
- See the [reStructuredText](http://docutils.sourceforge.net/rst.html) documentation for much more.

### Generate docs with Sphinx

The documentation above, and the present Howto, were rendered with [Sphinx](http://sphinx.pocoo.org/). Sphinx is the official document processor for Python itself and many Python projects. You’ve probably seen its handiwork at [http://docs.python.org/](http://docs.python.org/). Setting up Sphinx to automatically generate documentation for your module is easy. First tell your VCS to create a `doc/` directory under your project root (this is the the standard place for documentation), and then run **sphinx-quickstart**:

> `$ cd */path/to/googlemaps*`
>
> `$ svn mkdir doc`
>
> `$ cd doc`
>
> `$ sudo easy_install sphinx`
>
> `$ sphinx-quickstart`

Answer the questions (the defaults are fine, except be sure to say ‘yes’ to the autodoc extension). Then, edit the generated `index.rst`file to add this:

> `.. automodule:: *googlemaps*`

This is the place to put any extra documentation that’s not in your docstrings. Be sure to put `index.rst` and Sphinx’ `conf.py` under version control:

> `$ svn add index.rst conf.py`

You can generate your documentation by running **sphinx-build** in the `doc/` directory:

> `$ sphinx-build . html/`

(You will need to have `*/path/to/googlemaps/googlemaps*` in your **PYTHONPATH** for this to work.)

This will put the HTML documentation in `doc/html/`. Sphinx generates very nice documentation. Open it up with your web browser and look at it. It will encourage you to write better documentation if you see that you’re making something beautiful as you write.

### README

In addition to the docstrings in your code and the resulting HTML documentation, you should create a `README.txt` file in the top level of your directory structure. Put it under version control. Your `README.txt` should contain the following:

- Name, version, and release date of the package
- Brief description of the package
- Any dependencies or required versions of Python
- How to install the package (ideally just `easy_install *packagename*`)
- How to run the program(s), if your package contains scripts
- Package author and contact information
- Copyright and [licensing](http://infinitemonkeycorps.net/docs/pph/#id9) terms
- Pointer to full documentation

Some people like to break a few of these out into separate files (`INSTALL`, `AUTHORS`, `ANNOUNCE`...), but personally I prefer to keep it simple.

If you already have this information in your docstrings or somewhere else, by all means, [don’t repeat yourself](http://en.wikipedia.org/wiki/Don%27t_repeat_yourself): either use Sphinx, which can also produce plain (reStructured) text, or whip up a script to pull out the information and write your `README.txt` for you. You can extract the docstring from any module, class, or function with, e.g., `*mymodule*.__doc__`. Here’s how to make Sphinx output plain (reStructured) text to the `text/` directory:

> `$ sphinx-build -b text . text/`

### 文档相关资源

- PEP 257, Docstring Conventions: [http://www.python.org/dev/peps/pep-0257/](http://www.python.org/dev/peps/pep-0257/)
- reStructuredText markup: [http://docutils.sourceforge.net/rst.html](http://docutils.sourceforge.net/rst.html)
- Sphinx, Python Documentation Generator: [http://sphinx.pocoo.org/](http://sphinx.pocoo.org/)

## 项目许可证

You will need to decide on a license for your code. Popular open-source licenses include the GPL and LGPL, BSD, MIT/X11, Apache, Eclipse, and Mozilla. There are several resources listed below to help guide you in choosing a license. Your choice has implications for who can use your code under what circumstances, including which other open source projects can incorporate it. Your choice of license may also have implications for your choice of project host, since some hosts only permit software under some licenses. Take the time to learn a bit about licensing, and decide how you would like your code to be used.

Once you have chosen a license, you can find the complete text at the [Open Source Initiative](http://www.opensource.org/licenses). Read through the text to ensure you agree with its terms. Copy the complete text into a file called `LICENSE.txt` at the top level of your project (and put it under version control). Then, you will need to put a copyright notice in a comment at the top of each source file, and a brief statment of the licensing terms including where to find the license. You do not have to include the full license directly in your source; see the resources below for suggestions. If you have considerable documentation, consider licensing the documentation itself under one of the available [free documentation licenses](http://www.dreamsongs.com/IHE/IHE-50.html).

### 相关资源

- Open Source Licenses at OSI: [http://www.opensource.org/licenses](http://www.opensource.org/licenses)
- Open Source Licenses on Wikipedia: [http://en.wikipedia.org/wiki/Open_source_license](http://en.wikipedia.org/wiki/Open_source_license)
- zooko Quick Reference for Choosing a Free Software License: [http://zooko.com/licence_quick_ref.html](http://zooko.com/licence_quick_ref.html)
- KDE Open Source License Comparison: [http://developer.kde.org/documentation/licensing/licenses_summary.html](http://developer.kde.org/documentation/licensing/licenses_summary.html)
- New Media Rights’ Open Source Licensing Guide: [http://www.newmediarights.org/open_source/new_media_rights_open_source_licensing_guide](http://www.newmediarights.org/open_source/new_media_rights_open_source_licensing_guide)
- Groklaw - Understanding Open Source Software: [http://www.groklaw.net/article.php?story=20031231092027900](http://www.groklaw.net/article.php?story=20031231092027900)
- Innovation Happens Elsewhere’s Licenses for Docmentation: [http://www.dreamsongs.com/IHE/IHE-50.html](http://www.dreamsongs.com/IHE/IHE-50.html)
- Creative Commons ‘Choose a License’ (for documentation): [http://creativecommons.org/choose/](http://creativecommons.org/choose/)
- Free Software Foundation’s Various Licenses and Comments About Them: [http://www.gnu.org/philosophy/license-list.html](http://www.gnu.org/philosophy/license-list.html)

为项目添加许可证，是为了别人可以更好的利用你的代码，这里有很多 [开源许可](http://opensource.org/licenses/alphabetical) 可以选择。

一般来说，这些许可大致分为两类：

1. 许可更关注用户随意使用软件的自由（较宽松的自由软件开源许可，如 MIT、 BSD，以及 Apache）。
2. 许可更关注确保代码 — 包括对其任意的修改和分发 — 的自由（较不宽松的 自由软件许可，如GPL 和 LGPL）。

后者相较而言不太宽松，它们不允许他人在软件中添加代码，也不允许分发软件 包括对其源代码的更改。

为了帮助您选择用于项目的许可，这里有一个 [许可选择器](http://choosealicense.com/)， **可供使用**。

**较宽松：**

- PSFL (Python Software Foundation License) – 用于贡献给Python
- MIT / BSD / ISC
  - MIT (X11)
  - New BSD
  - ISC
- Apache

**较不宽松:**

- LGPL
- GPL
  - GPLv2
  - GPLv3

关于许可中使用软件时什么能做、不能做、必须做的解释，这里 [tl;drLegal](https://tldrlegal.com/) 有很好的概述。

## 项目打包

Packaging takes the files in your carefully crafted directory layout and bundles them up for easy download and use by others. The standard way to do this in Python is with [distutils](http://docs.python.org/distutils/index.html). Creating a simple file, `setup.py`, will give you your own **easy_install**-able package.

### setup.py

Here is an example `setup.py`:

```
from distutils.core import setup
import sys

sys.path.append('googlemaps')
import googlemaps


setup(name='googlemaps',
      version='1.0',
      author='John Kleint',
      author_email='py-googlemaps-general@lists.sourceforge.net',
      url='http://sourceforge.net/projects/py-googlemaps/',
      download_url='https://sourceforge.net/projects/py-googlemaps/files/',
      description='Easy geocoding, reverse geocoding, driving directions, and local search in Python via Google.',
      long_description=googlemaps.GoogleMaps.__doc__,
      package_dir={'': 'googlemaps'},
      py_modules=['googlemaps'],
      provides=['googlemaps'],
      keywords='google maps local search ajax api geocode geocoding directions navigation json',
      license='Lesser Affero General Public License v3',
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 2',
                   'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
                   'License :: OSI Approved :: GNU Affero General Public License v3',
                   'Topic :: Internet',
                   'Topic :: Internet :: WWW/HTTP',
                   'Topic :: Scientific/Engineering :: GIS',
                  ],
     )

```

Don’t worry if you don’t have a `download_url` yet. Notice that we import our own module in order to pull in the `__doc__` string for the `long_description`; you are free to use whatever text is appropriate. If you have a package instead of a module, you’d replace `py_modules` with `packages` and remove the `package_dir`. You can find the list of `classifiers` at PyPI’s list of [trove classifiers](http://pypi.python.org/pypi?%3Aaction=list_classifiers). If your code depends on other third-party packages/modules, you can specify those with a `required` keyword argument.

This covers our code, but we need one more file to pull in the documentation: `MANIFEST.in` in the package root:

```
recursive-include doc/html *
prune doc/html/.doctrees/
exclude doc/html/.buildinfo
include LICENSE.txt
```

Now, to build your package, you just run **setup.py sdist**:

> `$ python setup.py sdist`

If all goes well, this will create a tarball in `dist/*googlemaps*-1.0.tar.gz`. Let’s make sure there are no problems installing it and verify the presence of important files with **cheesecake_index**:

> `$ sudo easy_install cheesecake`
>
> `$ cheesecake_index --path=dist/*googlemaps*-1.0.tar.gz`

Ensure at the minimum that your package is able to be installed. Notice that the cheesecake index includes Pylint as one component, so you’re already ahead of the game. Personally I think the score is weighted a bit heavily toward installability and documentation, but a relative [cheesecake index](http://pycheesecake.org/#algorithm-for-computing-the-cheesecake-index) of at least 70% seems like a reasonable target.

### 相关资源

- distutils, the standard Python Distribution Utilities: [http://docs.python.org/distutils/index.html](http://docs.python.org/distutils/index.html)
- setuptools, an enhanced, extended distutils and home of **easy_install**: [http://peak.telecommunity.com/DevCenter/setuptools](http://peak.telecommunity.com/DevCenter/setuptools)
- Cheesecake, package “kwalitee” checker: [http://pycheesecake.org/](http://pycheesecake.org/)
- PyPI’s list of trove classifiers: [http://pypi.python.org/pypi?%3Aaction=list_classifiers](http://pypi.python.org/pypi?%3Aaction=list_classifiers)

## 项目发布

Now that we’ve built the “golden master” in `dist/*googlemaps*-1.0.tar.gz`, it’s time to upload it. Your project host should have instructions for uploading files for release; most hosts let you do this via the web, SCP/SFTP, or FTP. Once you’ve uploaded the package, upload the documentation in `docs/html` to your project’s website (don’t forget the subdirectories). Take a moment to update your project’s metadata with things that may have changed, such as the license. If your program has a GUI, take a few screenshots and add them to your project metadata and/or web page.

Copy the URL where your file can be downloaded (the page containing the link is fine), and put it in the `download_url` argument of your `setup.py`.

### PyPI

You’ll likely want to register your package with the [Python Package Index](http://pypi.python.org/pypi). This enables people to automatically download and install your package with [easy_install](http://peak.telecommunity.com/DevCenter/EasyInstall) or [pip](http://pip.openplans.org/). You will need to sign up for a PyPI account (it’s free). You can do this either on the PyPI website, or via the command line and have your password mailed to you. Either way:

> `$ python setup.py sdist register upload`

This will build your packages, prompt you for your username/password, register your package (and its metadata) with PyPI, and then upload your package to PyPI. Uploading your package itself is not strictly necessary, but it may make it easier to find.

While you’re at it, you can also create a Windows installer to make it easy for Windows users to get your package:

> `$ python setup.py bdist_wininst upload`

This will create a file `dist/*googlemaps*-1.0.win32.exe` that you can also upload to your project host. (Note that Python 2.6 has a bug that may give the installer the wrong name, but you can simply rename it.)

Visit your project’s PyPI page at `http://pypi.python.org/pypi/*projectname*/`; you’ll notice that your `setup.py` `long_description` text has become the text of the web page. PyPI understands [reStructuredText](http://docutils.sourceforge.net/rst.html), so go ahead and tweak your `long_description` to your liking. Remeber that `sphinx-build -b text . text/` will “flatten” your documentation to reStructuredText, if you want to put the whole thing on PyPI. You can re-register a revised project without changing the version number. You can also edit your project’s metadata via the PyPI website.

- PyPI, the Python Package Index: [http://pypi.python.org/pypi](http://pypi.python.org/pypi)
- Registering with the Package Index: [http://docs.python.org/distutils/packageindex.html](http://docs.python.org/distutils/packageindex.html)
- Easy Install, automatically download and install Python packages: [http://peak.telecommunity.com/DevCenter/EasyInstall](http://peak.telecommunity.com/DevCenter/EasyInstall)
- pip, “pip installs packages”: [http://pip.openplans.org/](http://pip.openplans.org/)
- freshmeat.net, Open source project index: [http://freshmeat.net/](http://freshmeat.net/)

### Epilogue

Congratulations on the release of your Python package! Your code may grow from these humble beginnings, but it has a good foundation, and you are now familiar with the mechanics of open source Python projects. In parting, I woluld be remiss not to mention a great resource on all aspects of the open-source project lifecycle, the free book [Producing Open Source Software](http://www.producingoss.com/), by Karl Fogel. Best of luck. And...

> *Always look on the bright side of life...*
>
> *Always look on the bright side of life...*





[^1]: http://infinitemonkeycorps.net/docs/pph/
[^2]: http://pythonguidecn.readthedocs.io/zh/latest/writing/structure.html

