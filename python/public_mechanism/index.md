---
title: "python module and package public API"
author: "Xiao Wenbin"
date: 2014-07-10T15:48:08-04:00
draft: true
tags: ["python"]
---

#Python中用于公开package和module的API的机制#

所谓公开API，即指可以通过`from X import *`导入对象，有一种说法是这样做会弄脏当前的名称空间，你唯一应该遵从的原则是，如果有效就使用它，在有的情况下，这样做是很方便的，例如：当程序处于开发阶段时，你并不能确定提供给外部使用的接口是什么，这时通过导入全部对象是个不错的办法，还有就是当你想要了一个模块的结构时，导入全部对象也很方便

##定义公开API的机制##

在**module**中以一个下划线开头命名的对象是非公开API，并且可以使用`__all__`机制（后面会有介绍）来指定公开哪些特定API

在**package**中，是通过在package directory的`__init__.py`文件中定义`__all__`指定公开哪些特定模块的

##`__all__`机制##

该机制其实是一个白名单机制，`__all__`被赋于一个含有字符串元素的列表，其中的字符串中罗列除了具有公开性的API，在module的`__all__`紧跟在`import`语句的后面定义，其中的字符串对应的是该module中可以公开的对象名称字符串，并且`__all__`中定义的公开性优先于*"以一个下划线开头的对象名是非公开的"规则*，在package中的`__init__.py`定义的`__all__`中的字符串是没有后缀的模块文件名或者package中的子package名称

##若干用法示例##

1. 导入当前模块的别的模块不被暴露

        # This file is mytest.py

        import os

        import sys

        __all__ = ['test',]

        def test():

            print('this is a test function')

        # When you execute `from mytest import *`, you cannot get os and sys objects

2. package中指定可公开模块

        # package directory struct

        package/

                |-- __init__.py

                |-- module1.py

                |-- module2.py

                |-- subpackage/

                               |-- __init__.py

                               |-- submodule.py

        # In package/__init__.py

        __all__ = ['module1', 'subpackage']
