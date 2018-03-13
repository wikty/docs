---
title: "python magic method"
author: "Xiao Wenbin"
date: 2014-07-11T15:48:08-04:00
draft: true
tags: ["python"]
---

#Python Magic Method#

如果python没有对class提供magic method支持，从逻辑上讲class就仅仅是函数的集合，而有了magic method后class才真正的面向对象的，magic method使得class中很多功能被自动调用，隐藏了高级功能的实现细节，并且使得class与python的各种特性结合成为了可能，从这点上看，也许你可将magic method看成hook，有了这些hook使用自定义类的方式可以像内置类型一样

##magic method是什么##

如果从实现层次来考虑，instance是由数据属性和方法属性构成的对象，当你要使用它的功能时只要调用相应的方法属性即可，但是你有没有想过，instance的某些功能你并不希望自己显式的去调用它，而是希望有某种机制可以根据具体情况自动调用这些功能，这里所说的功能包括：当创建instance时希望初始化函数可以被自动调用，当instance间进行比较时（通常要把实例转换为某种格式再进行比较，比如：字符串）希望转换函数可以被自动调用等等，那自动调用是如何实现的？解释器又是如何知道什么情况下该调用哪个方法的？这是通过约定来实现的，是解释器和class编写者之间的约定，解释器中已经写好规则根据不同的情况调用特定的方法，并且对这些方法的名称进行了约定（比如：初始化时调用`__init__()`，转换为迭代器时调用`__iter__()`），相当于解释器为每种特定的功能提供了接口，而将接口的实现交给了class编写者来完成，而这些约定的方法就是magic method，正是有了这套机制才使得python class十分强大

##下面将一一介绍各个常见的magic method##

1. `__new__(cls, [...])`

    该方法是在类实例化时被调用的第一个方法（对，第一个被调用的不是`__init__()`方法），传入该方法的参数为：当前类以及实例化类时传入的参数，该方法需要返回一个类的实例，也就是说该方法**用于控制实例的创建过程**，通常你是不需要重写该方法的，除非你打算派生一个不可变类型（`str`,`unicode`,`int`,`tuple`）

    **示例：**从一个不可变类型派生子类

        class Word(str):

            def __new__(cls, word):

                if ' ' in word:

                    word = word[:word.index(' ')]

                return str.__new__(cls, word) # 返回一个新的实例

2. `__init__(self, [...])`

    该方法**用于实例的初始化**，传入该方法的参数：当前实例对象以及实例化类时传入的参数，该方法不返回任何东西，该方法是你经常重写的，通常都是一些将传入参数绑定到实例对象的语句，例如：`self.x = x`

3. `__del__(self)`

    该方法**用于对象释放之类的清理工作**，比如：用于关闭实例中打开的文件和套接字

4. 比较运算的方法：`__cmp__(self, other)`

    该方法在**实例对象进行比较时会被调用**，比较结果取决于该方法的返回值，当`self < other `时，应该返回负数，当`self == other`时，应该返回零，当`self > other`时，应该返回正数，可以看到其实该方法涵盖了所有比较操作符的逻辑，只要定义了该方法所有比较运算符都可以用于实例对象间的比较了，但是也许有时你需要明确的定义某个特定的比较操作*并且python3中废弃了\_\_cmp\_\_()方法*，这时请定义具体的比较操作：

        __eq__(self, other)  # self == other

        __ne__(self, other)  # self ！= other

        __lt__(self, other)  # self < other

        __le__(self, other)  # self <= other

        __gt__(self, other)  # self > other  

        __ge__(self, other)  # self >= other

    **注：**上面的方法通过返回True或False表示比较的结果，你只需要定义了`__eq__()`和`__gt__()`或`__lt__()`中的一个方法并对类使用装饰器`@functools.total_ordering`，就会自动为类添加余下的比较方法

5. 数值运算的方法：

        __pos__(self)  # 取正，+9

        __neg__(self)  # 取负，-9

        __abs__(self)  # 取绝对值，abs(9)

        __invert__(self)  # 比特位取反，~9

        __add__(self, other)  # 相加，7+8

        __sub__(self, other)  # 相减，7-8

        __mul__(self, other)  # 相乘，7*8

        __floordiv__(self, other)  # 除法取到最近整数，17.0 // 5 => 3.0

        __div__(self, other)  # 除法，17 / 5 => 3, 17.3 / 5 => 3.46

        __truediv__(self, other)  # 浮点除法

        __mod__(self, other)  # 取模，17 % 5 => 2

        __divmod__(self, other)  # 除法和取模，相当于内建函数divmod(7, 5) => (1, 2)

        __pow__(self, other)  # 指数运算，3 ** 2 => 9

        __lshift__(self, other)  # 左移，5 << 2

        __rshift__(self, other)  # 右移，5 >> 2

        __and__(self, other)  # 与，7 & 8

        __or__(self, other)  # 或，7 | 8

        __xor__(self, other)  # 异或，7 ^ 9

        __iadd__(self, other)  # 自增，self += other

        __isub__(self, other)  # 自减，self -= other

        __imul__(self, other)  # 自乘，self *= other

        __ifloordiv__(self, other)  # 自除并取到最近整数，self //= other

        __idiv__(self, other)  # 自除，self /= other

        __itruediv__(self, other)  # 浮点自除

        __imod__(self, other)  # 自取模，self %= other

        __ipow__(self, other)  # 自指数运算，self **= other

        __ilshift__(self, other)  # 自左移，self <<= other

        __irshift__(self, other)  # 自右移，self >>= other

        __iand__(self, other)  # 自与，self &= other

        __ior__(self, other)  # 自或，self |= other

        __ixor__(self, other)  # 自异或，self ^= other

    **注：**上面的二元运算都将self当成左操作数，如果你希望self是右操作数的话，有相应的magic method，就是将上面方法前面添加字母r，比如：`__floordiv__(self, other)`对应的运算是`self // other`，而`__rfloordiv__(self, other)`对应的运算则是`other // self`

6. 类型转换的方法：

        __int__(self)  # 被内建函数int()调用

        __long__(self)  # 被内建函数long()调用

        __float__(self)  # 被内建函数float()调用

        __complex__(self)  # 被内建函数complex()调用

        __oct__(self)  # 被内建函数oct()调用，转换为以零开头的八进制

        __hex__(self)  # 被内建函数hex()调用，转换为以0x开头的十六进制

        __index__(self)  # 当对象用在切片索引时该方法被调用，期望返回整数

        __trunc__(self)  # 当使用math.trunc(obj)时该方法被调用，期望返回整数且从数轴趋向零点

        __coerce__(self, other)  # 被内建函数coerce(x, y)调用，将self, other转化为相同类型的数值

7. 线性化：

        __str__(self)  # 被内建函数str()调用，期望返回人类可读字符串

        __repr__(self)  # 被内建函数repr()调用，期望返回机器可读字符串

        __unicode__(self)  # 被内建函数unicode()调用，期望返回人类可读的unicode字符串

        __hash__(self)  # 被内建函数hash()调用，期望返回整数序

        __nonzero__(self)  # 被内建函数bool()调用，期望返回表示对象是否为空的True或False

8. 属性访问

        __getattr__(self, name)  # 当访问对象中不存在的属性时被调用，你可以在该方法中编写错误处理代码或者返回一个默认值或者触发异常AttributeError，一切随你

        __setattr__(self, name, value)  # 当为对象添加新属性或者给属性赋值时被调用，该方法用于处理属性更新的具体逻辑

        __delattr__(self, name)  # 当del对象属性时被调用，该方法用于处理属性移除的逻辑

        __getattribute__(self, name) # 这是在new style class中添加的，每当访问对象的属性之前就被调用（不论属性是否存在）

    **注：**对`__setattr__()`实现有一个常见的错误：

        # Bad

        class MyClass(object):

            def __setattr__(self, name, value):

                self.name = value # 错误就在这里，本来对对象的属性赋值导致__setattr__被调用，但是在__setattr__又有一个赋值语句，这将会引起递归调用，千万要小心

        # Good

        class MyClass(object):

            def __setattr__(self, name, value):

                self.__dict__[name] = value  # 关键在这里

        class MyClass(object):

            def __setattr__(self, name, value):

                super(MyClass, self).__setattr__(name, value)  # 关键在这里

    **注：**对`__getattribute__()`也容易犯错

        # Bad

        class MyClass(object):

            def __getattribute__(self, name):

                if name == 'author':

                    return 'xiaowenbin'

                else:

                    return self.__dict__[name] # 此处将会无限递归，因为访问__dict__[name]意味着再次调用__getattribute__方法

        # Good

        class MyClass(object):

            def __getattribute__(self, name):

                if name == 'author':

                    return 'xiaowenbin'

                else:

                    return object.__getattribute__(self, name)  # 关键在这里

9. 使自定义类具有序列，容器对象的访问接口

        __len__(self)  # 被内建函数len()调用

        __getitem__(self, key)  # 当访问某key时（obj[key]）时被调用，错出时根据情况返回KeyError或TypeError

        __setitem__(self, key, value)  # 当为某key赋值时（obj[key] = value）被调用

        __delitem__(self, key)  # 当del某key时被调用，当key不存在时返回AttributeError

        __iter__(self)  # 被for语句或被内置函数iter()调用，期望返回一个迭代器对象（即具有next()方法的对象）

        __reversed__(self)  # 被内置函数reversed()调用，期望返回对象的逆序

        __contains__(self, item)  # 被in, not in语句调用，期望根据item是否存在于对象中返回True或False

        __concat__(self, other) # 当序列间使用+进行连接时被调用

    **注：**这里对实现类似序列，容器对象有若干规定：

    1. 不可变序列，容器类型（str, tuple)仅仅且必须实现接口`__len__`和`__getitem__()`

    2. 可变序列，容器类型（list, dict等）除了上面接口外还要实现`__setitem__()`和`__delitem__()`

    3. 要想使得对象可迭代，需要实现`__iter__()`，并且该方法返回的对象要实现`next()`

10. 实例以及子类检查

        __instancecheck__(self, instance)  # 被内置函数isinstance()调用

        __subclasscheck__(self, subclass)  # 被内置函数issubclass()调用

11. `__call__(self, [...])`

    该方法在实例对象被当成函数使用时被调用，例如：假定`my`是`MyClass`类的实例对象，当`my(args...)`时，相当于`my.__call__(args...)`，也就是说你只要将实例被当成函数调用时的逻辑写入`__call__`中就可以了

12. 对with语句的支持

    *一个with语句的示例：*

        with open('test.txt', 'r') as f, open('test1.txt', 'r') as f1:

            pass

        __enter__(self)  # 当进入with语句时调用该方法，该方法返回的对象即是托管给with的对象

        __exit__(self, exception_type, exception_value, traceback)  # 当离开with语句时调用该方法，在with执行期间产生的异常传递到该函数中，如果你在该方法中成功处理了异常则返回True，否则返回False使异常被用户处理

13. descriptor

    *descriptor是用来封装对属性的操纵逻辑的，具体参见[descriptor 介绍](/python/2014/07/12/python-descriptor)*

        __get__(self, instance, owner)  # 当访问属性时被调用

        __set__(self, instance)   # 当设置属性时被调用

        __delete__(self, instance, value)  # 当删除属性时被调用

    **示例：**

        # 这是一个descriptor

        class Meter(object):

            def __init__(self, value=0.0):  # 属性有默认值

                self.value = value

            def __get__(self, instance, owner):

                # instance是使用Meter类的那个类的实例对象（如果直接从类访问则instance为None）

                # owner是使用Meter类的那个类

                return self.value

            def __set__(self, instance, value):

                self.value = float(value)

        # 使用descriptor的类

        class Distance(object):

            meter = Meter()

        d = Distance()

        d.meter  # 将会调用 __get__

        d.meter = 9.0  # 将会调用 __set__

    *注：使用者向descriptor传入了instance，意味着使用者和descriptor是紧耦合的*

14. 对Pickle的支持

        __getinitargs__(self)  # 对于old style class，该方法可以获取实例化对象时传入__init__()的参数

        __getnewargs__(self)  # 对于new style class，该方法可以获取实例化对象时传入__new__()的参数

        __getstate__(self)  # 序列化对象时该方法被调用，返回值为序列化结果

        __setstate__(self, state)  # 逆序列化时被调用，传入的state参数为逆序列化的结果对象

    **示例：**摘自网上的

        import time

        # 该类将值的每次改变都记录下来，pickle时将记录序列化

        class Slate(object):

            def __init__(self, value):

                self.value = value

                self.mtime = time.asctime()

                self.history = {}

            def change(self, new_value):

                self.history[self.mtime] = self.value

                self.value = new_value

                self.mtime = time .asctime()

            def history(self):

                for k, v in self.history.items():

                    print("%s => %s\n" % (k, v))

            def __getstate__(self):

                return self.history

            def __setstate__(self, state):

                self.history = state

                self.mtime = max(self.history.keys())

                self.value = self.history[self.mtime]
