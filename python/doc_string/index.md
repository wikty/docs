---
title: "Python Docstring"
author: "Xiao Wenbin"
date: 2014-07-10T15:48:08-04:00
draft: true
tags: ["python"]
---



#Docstring 的语义#

参见 [PEP 257](https://www.python.org/dev/peps/pep-0257/)

该 PEP 从高层抽象角度介绍 Docstring 约定以及语义 semantics（what they should contain, and how to say it.），并不介绍 Docstring 中具体使用了什么标记语言的语法 syntax 规则。

## 什么是 Docstring

A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition. Such a docstring becomes the `__doc__`special attribute of that object.

All modules should normally have docstrings, and all functions and classes exported by a module should also have docstrings. Public methods (including the `__init__` constructor) should also have docstrings. A package may be documented in the module docstring of the `__init__.py` file in the package directory.



在定义module，class，function，method时的第一个语句并且是字符串常量语句就称其为Docstring，该字符串常量会在代码运行时成为所在对象的`__doc__`属性，它的主要用途在于为代码的使用者提供文档帮助

package中定义Docstring，其定义方法有些不同，是将Docstring放在package directory的`__init__.py`文件中的



Q&A

它是什么？定义于特定位置的字符串常量。

它定义在哪里，是给谁用的？特定位置指的是模块、类、函数、方法以及包的 `__init__.py` 中的第一语句中定义的字符串常量。

它的作用是什么，包含些什么内容？用于为代码提供文档啊

如何在运行时访问它？通过对象 `__doc__` 属性

不在这些指定位置的字符串常量也有可能成为 Docstring 吗？只有这些指定位置的字符串常量会被 Python 解释器加载到对象的 `__doc__` 属性，其它地方定义的也可能被其它软件工具解释为 Docstring，主要有两类：

1. String literals occurring immediately after a simple assignment at the top level of a module, class, or `__init__` method are called "attribute docstrings".
2. String literals occurring immediately after another docstring are called "additional docstrings".
3. Please see [PEP 258](https://legacy.python.org/dev/peps/pep-0258), "Docutils Design Specification" [[2\]](https://legacy.python.org/dev/peps/pep-0257/#id5), for a detailed description of attribute and additional docstrings.



## Docstring 约定

从逻辑上讲只要符合上面描述的都是Docstring，但在实际使用中出于可读性的考虑，会对Docstring的使用范围以及书写风格和内容有些约定，遵从约定不仅使得你的代码更具可读性而且某些工具可能会依赖约定工作，所以本文大量篇幅介绍的不是*Docstring是什么*而是*Docstring的约定有哪些*

**注：**约定的目的是为了提高可读性，如果你的风格更具可读性则没有必要遵从约定，或者如果你在维护陈旧的代码（没有使用约定的风格），为了遵从约定而丢失一致性也是不可取的，记住，约定只是为了让代码更可读





##在哪里使用Docstring##

按照约定需要添加Docstring的地方有：所有的package，所有的module，在module中所有被导出（exported）的function和class，class中的公开（public）method和`__init__()`

**注：**总的来说就是只有公开的对象（即可被使用，调用的对象）才需要添加Docstring，以便使用者了解对象的接口，对于那些不公开（私有）的对象没有必要写Docstring，但是建议在写Docstring的地方写上注释



##定义Docstring所用语法##

For consistency, always use `"""triple double quotes"""` around docstrings. Use `r"""raw triple double quotes"""` if you use any backslashes in your docstrings. For Unicode docstrings, use `u"""Unicode triple-quoted strings"""`.

1. 普通形式

        """使用三个双引号包裹Docstring内容"""

2. raw形式

        r"""如果内容中使用了\n，则用该形式"""

3. unicode形式

        u"""如果内容中有unicode字符，则用形式"""

虽然字符串常量可以使用 `"` 和 `'` 来作为定界符，但建议总是使用 `"""` 语法来声明 Docstring 字符串常量，即使对于单行的 Docstring 也是这样，一来便于以后扩展，二来为了一致性



## Docstring 类别

从形式上来划分的话，有单行、多行 Docstring

从应用对象上来划分的话，有用于 package, module, class, function, method 等

### 单行Docstring

顾名思义Docstring内容仅定义在一行之内

**示例：**

```
def kos_root():
    """Return the pathname of the KOS root directory."""
    global _kos_root
    if _kos_root: 
    	return _kos_root
    return None
```


**注：**

1. 虽然 `"""` 语法是用来定界多行字符串的，但即使 Docstring 只有一行字符串，也应该坚持使用它，以便于以后的扩展

2. 开始和结束引号均在同一行，字符串开始结尾均无空白

3. Docstring 内容应该是以句号结尾的短句

4. 单行文档字符串不应当被当成函数签名（参数介绍）来使用，下面这样不可取

   ```
   def function(a, b):
       """function(a, b) -> list"""
   ```


### 多行Docstring

多行 Docstring 的组成：summary line + a blank line + description lines

Multi-line docstrings consist of a summary line just like a one-line docstring, followed by a blank line, followed by a more elaborate description.

The summary line may be on the same line as the opening quotes or on the next line. The entire docstring is indented the same as the quotes at its first line.

### class 的 Docstring

class 的 Docstring 应该跟后面的 method 代码间隔一个空行

Insert a blank line after all docstrings (one-line or multi-line) that document a class -- generally speaking, the class's methods are separated from each other by a single blank line, and the docstring needs to be offset from the first method by a blank line.

class 的 Docstring 应该对该类含有的公共方法以及属性进行简介，类中的各个公开方法有各自定义的 Docstring 对其进行详细的描述。类中打算被子类重写的接口应该单独给予说明。

The docstring for a class should summarize its behavior and list the public methods and instance variables. If the class is intended to be subclassed, and has an additional interface for subclasses, this interface should be listed separately (in the docstring). The class constructor should be documented in the docstring for its `__init__` method. Individual methods should be documented by their own docstring.

class 如何继承自另外一个父类，应该简要介绍跟父类的差别，并且如果重写了父类的方法应该用 `override` 标注，如果扩展了父类的方法，应该用 `extend` 标注。

If a class subclasses another class and its behavior is mostly inherited from that class, its docstring should mention this and summarize the differences. Use the verb "override" to indicate that a subclass method replaces a superclass method and does not call the superclass method; use the verb "extend" to indicate that a subclass method calls the superclass method (in addition to its own behavior).

classDocstring的内容主要介绍它的功能，公开方法，实例属性，如果class中含有将被子类重写的接口则应该列出，class的构造说明写入`__init__()`的Docstring，如果class是一个子类，则应该说明与父类的不同之处，使用*overrid*描述那些被重写的方法，使用*extend*描述那些子类调用父类方法的情况

### script 的 Docstring

脚本即可以运行的模块，脚本的 Docstring 应该起到类似 `--help` 的作用

The docstring of a script (a stand-alone program) should be usable as its "usage" message, printed when the script is invoked with incorrect or missing arguments (or perhaps with a "-h" option, for "help"). Such a docstring should document the script's function and command line syntax, environment variables, and files. Usage messages can be fairly elaborate (several screens full) and should be sufficient for a new user to use the command properly, as well as a complete quick reference to all options and arguments for the sophisticated user.

为脚本编写的Docstring应该阐明脚本的用法，就像命令行中使用的--help参数实现的功能一样，即有简单的使用方法又涵盖所有的脚本用法和参数

### package/module 的 Docstring

模块的 Docstring 应该对公开的类、函数以及异常等予以简要介绍，每行介绍一个

The docstring for a module should generally list the classes, exceptions and functions (and any other objects) that are exported by the module, with a one-line summary of each. (These summaries generally give less detail than the summary line in the object's docstring.) 

包的 Docstring 应该对公开的子包和模块，简要介绍

The docstring for a package (i.e., the docstring of the package's `__init__.py` module) should also list the modules and subpackages exported by the package.



module的Docstring通常用于列出其中含有的class，function，exception以及变量等被module导出对象的信息，每行内容简单介绍一个对象

package的Docstring写入package directory文件`__init__.py`文件中，每行内容简单介绍一个module或sub-package

### function/method 的 Docstring

函数和方法的 Docstring 应该用于介绍函数的行为、参数、返回值、副作用、会抛出的异常以及使用限制等等。哪些参数是可选的，是否接受关键字参数，都应该语义说明。

The docstring for a function or method should summarize its behavior and document its arguments, return value(s), side effects, exceptions raised, and restrictions on when it can be called (all if applicable). Optional arguments should be indicated. It should be documented whether keyword arguments are part of the interface.

如果function，method中的代码是用很多空行分隔开成块的代码段，则Docstring前后个添加一个空行，形成块状的感觉

function，method中的Docstring主要简单介绍它的功能，参数，返回值，副作用，会引发的异常，指出可选参数和关键字参数

### arguments 的 Docstring

函数和方法中参数的介绍，要注意保持大小写一致，每个参数单独列为一行介绍

Python is case sensitive and the argument names can be used for keyword arguments, so the docstring should document the correct argument names. It is best to list each argument on a separate line. For example:

    def complex(real=0.0, imag=0.0):
        """Form a complex number.
    
        Keyword arguments:
        real -- the real part (default 0.0)
        imag -- the imaginary part (default 0.0)
        """
        if imag == 0.0 and real == 0.0:
            return complex_zero

## Docstring 缩进和空白行的处理

Docstring 处理工具（比如 [Docutils](http://www.tibsnjoan.co.uk/docutils.html) 之类的）对 Docstring 中空白和缩进的处理

Blank lines should be removed from the beginning and end of the docstring.

Any heading and tailing blanks in the first line of the docstring is insignificant and removed.

The second and further lines of the docstring will be stripped a uniform amount of indentation that is equal to the minimum indentation of all non-blank lines after the first line.

处理逻辑是：与开始引号在同一行的内容移除开头的空白，余下所有行，找出最小缩进量的行，并对所有行移除该最小缩进量，再除去所有空白行，下面是取自[PEP文档](http://legacy.python.org/dev/peps/pep-0257/#handling-docstring-indentation)的缩进处理逻辑对应的python代码：

```

def trim(docstring):

    if not docstring:

        return ''

    # Convert tabs to spaces (following the normal Python rules)

    # and split into a list of lines:

    lines = docstring.expandtabs().splitlines()

    # Determine minimum indentation (first line doesn't count):

    indent = sys.maxint

    for line in lines[1:]:

        stripped = line.lstrip()

        if stripped:

            indent = min(indent, len(line) - len(stripped))

    # Remove indentation (first line is special):

    trimmed = [lines[0].strip()]

    if indent < sys.maxint:

        for line in lines[1:]:

            trimmed.append(line[indent:].rstrip())

    # Strip off trailing and leading blank lines:

    while trimmed and not trimmed[-1]:

        trimmed.pop()

    while trimmed and not trimmed[0]:

        trimmed.pop(0)

    # Return a single string:

    return '\n'.join(trimmed)
```
由此可见下面这两种写法是一样的：

```
def foo():

    """A multi-line.

    docstring
    """

def bar():
    """
    A multi-line.
    
    docstring
    """
```

推荐使用第一种，毕竟第一行 Docstring 之前的空白是无意义的。



# Docstring 的语法

这一小节承接上面，继续了解，如何来书写 Docstring（用什么语法规则），进而可以实现语义的表达。

单纯文本的 Docstring 有时没办法表示文档中某些丰富的语义，比如：如何指定哪部分内容是对参数的介绍？，人们自然而然的为 Docstring 引入了语法规则，并且不同的开发者使用了不同的语法规则，本节将要介绍的是基于[reStructuredText markup](http://docutils.sourceforge.net/rst.html) 标记语言的 Docstring 语法规则（参见 [PEP 257](https://www.python.org/dev/peps/pep-0287/)），项目文档生成工具  [Sphinx](http://sphinx-doc.org/) 也是基于该标记语言的，这也是该标记语言书写 Docstring 的优势之一。

Nor is it an attempt to deprecate pure plaintext docstrings, which are always going to be legitimate. The reStructuredText markup is an alternative for those who want more expressive docstrings.

样例：

```
"""
This is a reST style.

:param param1: this is a first param
:param param2: this is a second param
:returns: this is a description of what is returned
:raises keyError: raises an exception
"""
```



## 其它常用 Docstring 语法规则

### Epytest

```
"""
This is a javadoc style.

@param param1: this is a first param
@param param2: this is a second param
@return: this is a description of what is returned
@raise keyError: raises an exception
"""
```

### Google

```
"""
This is an example of Google style.

Args:
    param1: This is the first param.
    param2: This is a second param.

Returns:
    This is a description of what is returned.

Raises:
    KeyError: Raises an exception.
"""
```

### Numpydoc

```
"""
My numpydoc description of a kind
of very exhautive numpydoc format docstring.

Parameters
----------
first : array_like
    the 1st param name `first`
second :
    the 2nd param
third : {'value', 'other'}, optional
    the 3rd param, by default 'value'

Returns
-------
string
    a value in a string

Raises
------
KeyError
    when a key error
OtherError
    when an other error
"""
```