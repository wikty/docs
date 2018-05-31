# 文本编辑工具

## vim

使用缩进和换行均符合 [**PEP 8**](https://www.python.org/dev/peps/pep-0008)要求的默认设置，修改 `~/.vimrc`，添加如下内容：

```
set textwidth=79  " lines longer than 79 columns will be broken
set shiftwidth=4  " operation >> indents 4 columns; << unindents 4 columns
set tabstop=4     " a hard TAB displays as 4 columns
set expandtab     " insert spaces when hitting TABs
set softtabstop=4 " insert/delete 4 spaces when hitting a TAB/BACKSPACE
set shiftround    " round indent to multiple of 'shiftwidth'
set autoindent    " align the new line indent with the previous line
```

### 相关插件

如果您还使用 Vim编辑其他语言，有一个叫做 [indent](http://www.vim.org/scripts/script.php?script_id=974) 的便捷插件可以让这个设置只为Python源文件服务。



还有一个方便的语法插件叫做 [syntax](http://www.vim.org/scripts/script.php?script_id=790) ，改进了Vim 6.1中的语法文件。



这些插件使您拥有一个基本的环境进行Python开发。要最有效的使用Vim，您应该时常检查代码的 语法错误和是否符合PEP8。幸运的是， [pycodestyle](https://pypi.python.org/pypi/pycodestyle/) 和 [Pyflakes](http://pypi.python.org/pypi/pyflakes/) 将会帮您做这些。



对于PEP8检查和pyflakes，您可以安装 [vim-flake8](https://github.com/nvie/vim-flake8) 。然后您就可以在Vim中把 `Flake8` 映射到任何热键或您想要的行为上。这个插件将会在屏幕下方显示出错误，并且提供一个简单的 方式跳转到相关行。在保存文件的时候调用这个功能会是非常方便的。要这么做， 就把下面一行加入到您的 `.vimrc`:

```
autocmd BufWritePost *.py call Flake8()
```



如果您已经在使用 [syntastic](https://github.com/scrooloose/syntastic) ，您可以设置它来运行Pyflakes，并在quickfix窗口中显示错误 和警告。一个这样做并还会在状态栏中显示状态和警告信息的样例是:

```
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*
let g:syntastic_auto_loc_list=1
let g:syntastic_loc_list_height=5
```



[Python-mode](https://github.com/klen/python-mode) 是一个在Vim中使用Python的综合解决方案。 它拥有：

- 任意组合的异步Python代码检查（ `pylint` 、 `pyflakes` 、 `pycodestyle` 、 `mccabe`）
- 使用Rope进行代码重构和补全
- Python快速折叠
- 支持virtualenv
- 搜索Python文档，运行Python代码
- 自动修复 [pycodestyle](https://pypi.python.org/pypi/pycodestyle/) 错误



[SuperTab](http://www.vim.org/scripts/script.php?script_id=1643) 是一个小的Vim插件，通过使用 `<Tab>` 或任何其他定制的按键， 能够使代码补全变得更方便。



## Emacs

Emacs是另一个强大的文本编辑器。它是完全可编程的（lisp），但要正确的工作要花些功夫。 如果您已经是一名Emacs的用户了，在EmacsWiki上的 [Python Programming in Emacs](http://emacswiki.org/emacs/PythonProgrammingInEmacs)将会是好的开始。



## TextMate

[TextMate](http://macromates.com/) 将苹果操作系统技术带入了文本编辑器的世界。 通过桥接UNIX和GUI，TextMate将两者中最好的部分带给了脚本专家和新手用户。



## Sublime Text

[Sublime Text](http://www.sublimetext.com/) 是一款高级的，用来编写代码、标记和 文章的文本编辑器。您将会爱上漂亮的用户界面、非凡的特性和惊人的表现。

Sublime Text对编写Python代码支持极佳，而且它使用Python写其插件API。它也拥有大量 各式各样的插件， [其中一些](https://github.com/SublimeLinter/SublimeLinter) 允许编辑器内的PEP8检查和代码提示。



## Atome

[Atom](https://atom.io/) 是一款21世纪的可删减的（hackable）文本编辑器。它基于我们 所喜欢的编辑器的任何优秀特性，并构建于atom-shell上。

Atom是web原生的（HTML、CSS、JS），专注于模块化的设计和简单的插件开发。它自带本地包管理 和大量的包。Python开发所推荐的插件是 [Linter](https://github.com/AtomLinter/Linter) 和 [linter-flake8](https://github.com/AtomLinter/linter-flake8) 的组合。



# IDE

## PyCharm

[PyCharm](http://www.jetbrains.com/pycharm/) 由JetBrains公司开发，此公司还以 IntelliJ IDEA闻名。它们都共享着相同的基础代码，PyCharm中大多数特性能通过免费的 [Python 插件](https://plugins.jetbrains.com/plugin/?idea&pluginId=631) 带入到IntelliJ中。PyCharm由两个版本：专业版（Professional Edition）（30天试用）和 拥有相对少特性的社区版（Community Edition）（Apache 2.0 License）。

## Visual Studio

[用于Visual Studio的Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) 是一款用于 [Visual Studio Code IDE](https://code.visualstudio.com/) 的扩展。 它是一个免费的、轻量的、开源的IDE，支持Mac、Windows和Linux。它以诸如Node.js和Python等 开源技术构建，具有如Intellisense（自动补全）、本地和远程调试、linting（代码检查）等 引人注目的特性。

## Enthought Canopy

[Enthought Canopy](https://www.enthought.com/products/canopy/) 是一款专门面向科学家 和工程师的Python IDE，它预装了为数据分析而用的库。

## Eclipse

Eclipse中进行Python开发最流行的插件是Aptana的 [PyDev](http://pydev.org/) 。

## Spyder

[Spyder](https://github.com/spyder-ide/spyder) 是一款专门面向和Python科学库 （即 [Scipy](http://www.scipy.org/) ）打交道的IDE。它集成了 [pyflakes](http://pypi.python.org/pypi/pyflakes/) 、[pylint](http://www.logilab.org/857) 和 [rope](https://github.com/python-rope/rope) 。

Spyder是开源的（免费的），提供了代码补全、语法高亮、类和函数浏览器，以及对象检查的功能。

## Eric

[Eric](http://eric-ide.python-projects.org/) 是一款功能齐全的Python IDE， 提供源代码自动补全、语法高亮、对版本控制系统的支持、对Python 3的支持、集成的web浏览器、 Python Shell、集成的调试器和灵活的插件系统等功能。它基于Qt GUI工具集，使用Python编写， 集成了Scintilla编辑器控制。Eric是一款超过10年活跃开发的开源软件工程（GPLv3许可）。

## IDLE

[IDLE](http://docs.python.org/library/idle.html#idle) 是一个集成的开发环境，它是Python标准库的一部分。 它完全由Python编写，并使用Tkinter GUI工具集。尽管IDLE不适用于作为成熟的Python开发工具， 但它对尝试小的Python代码和对Python不同特性的实验非常有帮助。

## IPython

[IPython](http://ipython.org/) 提供一个丰富的工具集来帮助您最大限度地和Python交互。 它主要的组件有：

- 强大的Python shell（终端和基于Qt）。
- 一个基于网络的笔记本，拥有相同的核心特性，但是支持富媒体、文本、代码、数学表达式和内联绘图。
- 支持交互式的数据可视化和GUI工具集的使用。
- 灵活、嵌入的解释器载入到您的工程工程中。
- 支持高级可交互的并行计算的工具。

```
$ pip install ipython

```

下载和安装带有所有可选依赖（notebook、qtconsol、tests和其他功能）的IPython

```
$ pip install ipython[all]
```

## BPython

[bpython](http://bpython-interpreter.org/) 在类Unix操作系统中可替代Python解释器的接口。 它有以下特性：

- 内联的语法高亮。
- 行内输入时的自动补全建议。
- 任何Python函数的期望参数列表。
- 从内存中pop出代码的最后一行并重新运行（re-evaluate）的“倒带”功能.
- 将输入的代码发送到pastebin。
- 将输入的代码保存到一个文件中。
- 自动缩进。
- 支持Python 3。

[ptpython](https://github.com/jonathanslenders/ptpython/) 是一个构建在 [prompt_toolkit](http://github.com/jonathanslenders/python-prompt-toolkit) 库顶部的REPL。它被视作是 [BPython](http://bpython-interpreter.org/) 的替代。