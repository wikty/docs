---
title: "Python Docstring"
author: "Xiao Wenbin"
date: 2014-07-10T15:48:08-04:00
draft: true
tags: ["python"]
---

#Python Docstring#

在定义module，class，function，method时的第一个语句并且是字符串常量语句就称其为Docstring，该字符串常量会在代码运行时成为所在对象的`__doc__`属性，它的主要用途在于为代码的使用者提供文档帮助

**注：**上面没有提及package中定义Docstring，其定义方法有些不同，是将Docstring放在package directory的`__init__.py`文件中的

##关于Docstring的约定##

从逻辑上讲只要符合上面描述的都是Docstring，但在实际使用中出于可读性的考虑，会对Docstring的使用范围以及书写风格和内容有些约定，遵从约定不仅使得你的代码更具可读性而且某些工具可能会依赖约定工作，所以本文大量篇幅介绍的不是*Docstring是什么*而是*Docstring的约定有哪些*

**注：**约定的目的是为了提高可读性，如果你的风格更具可读性则没有必要遵从约定，或者如果你在维护陈旧的代码（没有使用约定的风格），为了遵从约定而丢失一致性也是不可取的，记住，约定只是为了让代码更可读

##在哪里使用Docstring##

按照约定需要添加Docstring的地方有：所有的package，所有的module，在module中所有被导出（exported）的function和class，class中的公开（public）method和`__init__()`

**注：**总的来说就是只有公开的对象（即可被使用，调用的对象）才需要添加Docstring，以便使用者了解对象的接口，对于那些不公开（私有）的对象没有必要写Docstring，但是建议在写Docstring的地方写上注释

##定义Docstring所用语法##

1. 普通形式

        """使用三个双引号包裹Docstring内容"""

2. raw形式

        r"""如果内容中使用了\n，则用该形式"""

3. unicode形式

        u"""如果内容中有unicode字符，则用形式"""

##单行Docstring##

顾名思义Docstring内容仅定义在一行之内

**示例：**

    def test():

        """ """

        pass

**注：**

1. 开始和结束引号均在同一行

2. Docstring应该描述对象怎么使用，而不是对象做了什么

3. class的Docstring不能用单行Docstring，即便内容仅仅一行也要用多行Docstring

##多行Docstring##

对于多行Docstring有一些书写风格和内容的约定

1. Docstring内容可以从开始引号后面直接写或者从开始引号换行后写起，例：

        def foo():

            """A multi-line

            docstring

            """

        def bar():

            """

            A multi-line

            docstring

            """

2. 所有行要同开始引号的缩进相同，从上面的例子可以看出

3. function，method中的Docstring主要简单介绍它的功能，参数，返回值，副作用，会引发的异常，指出可选参数和关键字参数

3. class的Docstring要求开始引号后和结束引号前都要有换行，并且Docstring的前后要各用一个空行与其他内容隔开，Docstring的内容主要介绍它的功能，公开方法，实例属性，如果class中含有将被子类重写的接口则应该列出，class的构造说明写入`__init__()`的Docstring，如果class是一个子类，则应该说明与父类的不同之处，使用*overrid*描述那些被重写的方法，使用*extend*描述那些子类调用父类方法的情况

4. 如果function，method中的代码是用很多空行分隔开成块的代码段，则Docstring前后个添加一个空行，形成块状的感觉

5. 为脚本编写的Docstring应该阐明脚本的用法，就像命令行中使用的--help参数实现的功能一样，即有简单的使用方法又涵盖所有的脚本用法和参数

7. module的Docstring通常用于列出其中含有的class，function，exception以及变量等被module导出对象的信息，每行内容简单介绍一个对象

6. package的Docstring写入package directory文件`__init__.py`文件中，每行内容简单介绍一个module或sub-package

##对多行字符串缩进的处理##

处理逻辑是：与开始引号在同一行的内容移除开头的空白，余下所有行，找出最小缩进量的行，并对所有行移除该最小缩进量，再除去所有空白行，这时才是你通过`__doc__`访问的内容，也就是说不论你的Docstring内容是紧跟开始引号后的，还是在下一行中开始的，最终得到的结果是一样的，下面是取自[PEP文档](http://legacy.python.org/dev/peps/pep-0257/#handling-docstring-indentation)的缩进处理逻辑对应的python代码：

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
