---
title: "python __init__.py file"
author: "Xiao Wenbin"
date: 2014-07-10T15:48:08-04:00
draft: true
tags: ["python"]
---

#Python initialize file#

最为基本的初始化文件仅仅作为一个package的标志出现，同时初始化文件是控制包名称空间的重要机制，体现了软件设计中的接口暴露思想，通过初始话文件来决定将哪些接口暴露给使用者，这对软件架构设计是至关重要的，因为符合封装好变化，使得软件具有持久的生命力

##预先储备知识##

1 . **namespace**

    我们知道python源码中定义了各种各样的对象，当解释器读入python源码后依照源码的定义在内存中构造相应的对象，并将对象以package，module，class，function，variable这些单元按照层次树状结构组织起来，而用于记录对象的这种组织关系树的就是namespace，你可以将namesapce看成是一个类似dict类型的数据结构，并且该结构是层次嵌套的dict，由顶层到底层依次是package => module => class(=> attribute), function(=> variable), variable，你之所以可以代码中引用各种对象，都是因为有namespace的缘故，才能够找到它们，此外namespace的层次树状结构保证了不同分支中可以出现相同的对象名称，避免了命名冲突问题

2. **module**

    module对象的构造源是一个python源文件，该文件中定义的global variables，constants，class，function都将映射到module对象的属性

3. **package**

    package对象对应的构造源是一个python源目录（且该目录中必须有`__init__.py`文件），该对象属性引用的自然是定义在该目录中的modules

##`__init__.py`文件有什么特殊意义##

含有`__init__.py`文件的目录在python中被当成package对象的构造源，也就是说该目录将会映射成为一个package对象，如果目录中没有该文件那么该目录对python而言仅仅只是一个普通的文件目录而已，python之所以有这样的规定，原因在于避免将特殊名称的普通目录（例：该目录名为string）误当成package目录进行导入，这样你的普通目录就可以随意的命名了（即便同python要导入的package同名，只要不含初始化文件就仅仅是普通文件目录而已）

**一个package目录示例：**

    package/

            |-- __init__.py

            |-- module1.py

            |-- module2.py

            |-- subpackage/

                           |-- __init__.py

                           |-- submodule1.py

##`__init__.py`文件中的内容##

1. 因为只要python源目录中有该文件就会被标识package目录，所以最简单的情形是该文件中不含任何内容

2. 其实该文件中可以写入一些初始化package的代码

    1. **导入语句**，将某对象导入到package对象中，这样当使用该对象时可从package导入，以上面的package目录结构为例，假设module1.py中定义类MyClass，当你要使用该类时，导入语句为：`from package.module1 import MyClass`，但是如果在`__init__.py`中写入：`from module1 import MyClass`后，每当要使用该类时，只需：`from package import MyClass` 或者直接通过package引用 `package.MyClass`，也就是说在`__init__.py`中凡是通过导入语句引入的对象都直接位于package对象的名称空间下

    2. **公开模块**，通过在`__init__.py`中写入`__all__`语句可以指定package中的公开模块（就是可以通过`from X import *`导入的模块）有哪些，具体的用法参见[公开API机制](/python/2014/07/10/python-public-mechanism)

    3. 就如果module定义的顶级代码一样，任何写入`__init__.py`文件的代码都会被执行（在导入package中的某个对象时会依次执行路径上的每个`__init__.py`中的代码）

##`__init__.py`中的`import`语句体现了接口设计思想##

1. 没有任何`import`语句

    这样确保了干净的package名称空间，使用package的用户精确的通过dot语法，按照package目录结构导入所需对象，还是上面的例子，要使用MyClass：`from package.module1 import MyClass`

2. 仅`import`关键，常用，重要的对象

    这样虽然弄脏了package的名称空间，但是在使用被导入对象时直接从package导入即可，方便了不少，`__init__.py`中的导入语句：`from module1 import MyClass`，package用户使用MyClass时：`from package import MyClass`，此外这样做的好处还有，当package作者对package进行重构时（比如package目录结构的调整），只要被导入对象名称没变就不会影响package的使用者，这样在一定程度上将packge的变化与依赖package的用户隔离开了
