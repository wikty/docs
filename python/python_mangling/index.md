---
title: "python name mangling mechanism"
author: "Xiao Wenbin"
date: 2014-07-11T15:48:08-04:00
draft: true
tags: ["python"]
---

#Name Mangling#

#副标题：python中对class的private支持#

这是在各类计算机语言中广泛使用的用于避免名称冲突的机制，通过添加更多的语义信息到变量名中来实现避免名称冲突，python也提供了这种机制，主要是通过避免子类重写父类某些属性，来支持python类中private的实现

##预备知识##

1. **类的private属性**，在C++和Java中你可以明确的声明一个某成员是private的，private成员的意义在于：该成员只能够从类中访问，也就是说，一方面，使用该类的用户不能从外部直接访问该成员，另一方面，private成员是不会被该类的子类继承的，同时也表明子类不能够重写父类的private成员（没有继承过来何谈重写），也就是说子类中定义的同名成员仅仅是子类的成员而已跟父类无关

2. **多态**，从C++观点来看，不同子类对父类的某个接口进行了不同的逻辑实现，这样对象在运行时由于属于不同的子类就会表现出不同的行为，这种现象称其为多态

3. **python类成员的特殊性**，从C++观点来看，python中所有的类成员都是public的（即都可从外部访问且都可被子类继承）并且都是virtual（即都可子类被重写）

##python为什么要提供Name Mangling机制##

python对class没有提供强制的private机制（即强制属性私有化，只能在class内访问的机制），也就是说父类中的一切属性都会被子类继承重写，假设这样一个情形，父类中有方法：`show()`和`tick()`，并且`show()`中调用了`tick()`，子类中重写了方法`tick()`，这时子类的实例化对象调用`show()`的效果跟父类中定义的`show()`是不同的（因为被调用到的`tick()`逻辑发生了变化），至此，对上述现象有两种解读：一，如果父类期望方法`tick()`被子类重写，那么上面的现象就是多态，二，如果父类只是将`tick()`当作自己使用的方法并不期望被子类重写呢，那么上面的现象就是一个错误，Name Mangling机制正是针对第二种情况的解决方案，其目的就是避免子类重写父类不期望子类重写的属性

##python中Name Mangling语法##

class中以两个下划线开头且至多以一个下划线结尾的属性将被进行mangling处理

##mangling处理，到底干了什么##

**原理：**在python解释器从源码构造class对象时，凡是符合mangling语法的属性都被重命名，例如：类MyClass中的`__my`属性被重命名为`_MyClass__my`，就为属性添加前缀：一个下划线加当前类名，并且在类中凡是引用到该属性的地方都进行了替换

**示例1：**对属性重命名

    # Class Define

    class MyClass(object):

        def __init__(self, x, y):

            self.x = x

            self.y = y

        # Notice: 这个方法将被mangling处理

        def __cal(self):

            self.total = self.x + self.y  # 加法

        def show(self):

            self.__cal() # 这里也会进行mangling处理

            print(self.total)

    # In Python Interpeter, you should import MyClass first

    >>>MyClass.__cal

    Traceback (most recent call last):

    File "<stdin>", line 1, in <module>

    AttributeError: type object 'MyClass' has no attribute '__cal'

    # 因为属性__cal已经转换为_MyClass__cal所以上面报错，执行下面的则不会报错

    >>>MyClass._MyClass__cal

**示例2：**子类'不能'重写父类的mangling属性

    # 定义一个继承自上面MyClass类的子类

    class DerivedMyClass(MyClass):

        # 定义一个跟父类同名的方法，其实该方法并不会重写父类方法

        # 因为该方法mangling后为_DerivedMyClass__cal，而父类

        # 同名方法mangling后为_MyClass__cal，因为经过mangling

        # 处理后方法名是不同的，所以子类是不能重写父类的__cal方法的，

        # 其实通过mangling机制实现对private支持并不是强制的，因为

        # 你还是可以在子类通过重写父类方法_MyClass__cal来打破私有

        # 限制，可以看出python类的设计思想是：假设用户是明智的

        def __cal(self):

            self.total = self.x * self.y  # 乘法

    # In Python interpeter, you should import MyClass and DerivedMyClass first

    >>>d = DerivedMyClass(5, 7)

    >>>d.show()

    12 # 结果是使用父类的__cal的加法计算的，而不是子类__cal的乘法计算的

**示例3：**如果一个方法既具有私有性又具有公有性

    # Class Define

    class MyClass(object):

        def __init__(self, x, y):

            self.x = x

            self.y = y

        # 注意：方法名由__cal变成了cal

        # 这样使得子类中可以重写方法cal

        # 同时父类中仍可使用不被重写的cal逻辑

        def cal(self):

            self.total = self.x + self.y

        def show(self):

            self.__cal()

            print(self.total)

        __cal = cal # 通过赋值重用方法
