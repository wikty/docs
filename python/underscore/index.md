---
title: "the underscore in python"
author: "Xiao Wenbin"
date: 2014-07-10T15:48:08-04:00
draft: true
tags: ["python"]
---

#Python中的下划线含有特殊的意义#

python中的下划线是宠儿，因为在python中有如此多的特性跟下划线关联了起来，从变量到名称空间，以及接口设计都与下划线相关

##在解释器中的下划线##

缓存了最近一次函数调用返回的结果

##magic对象##

如果对象的名称是以两个下划线开头并以两个下划线结尾的，说明该对象是magic对象，你可以将它看成是python中的hook，常见的magic对象有，magic模块：`__builtins__`, `__future__`，magic全局变量：`__all__`, magic方法：`__init__`等

**注：**更多详细内容，请看[magic方法](/python/2014/07/11/python-magic)

##在模块中的下划线##

一个以下划线开头的模块全局变量对象是non-public的，也就是说通过`import *`语句是无法导入该对象的

**注：**上面提到的用于定义non-public对象的方法，此外还可使用[`__all__`机制](/python/2014/07/10/python-public-mechanism)来指定哪些对象是public的

##在类中的下划线##

以两个下划线开头并以至多一个下划线结尾的类的属性名将会被[mangling处理](/python/2014/11/python-mangling)，你可以将其看成是类的private

以一个下划线开头的属性是非公开的（仅仅是一种命名约定，没有强制实现不允许外部访问），你可将此类属性看成是protected

##防止与python保留字冲突##

为了防止对象名同python保留字的冲突，当对象名要使用python保留字时，你需要额外在对象名尾部添加一个下划线，例如：`class`作为对象名是不合法的，但是`class_`作为对象名就是合法的了
