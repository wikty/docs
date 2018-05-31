大多数情况下，Python的目标是成为一门简洁和一致的语言，同时避免意外情况。 然而，有些情况可能会使新人困惑。



## 可变默认参数

定义如下函数：

```
def append_to(element, to=[]):
    to.append(element)
    return to
```

运行以下代码：

```
my_list = append_to(12)
print(my_list)

my_other_list = append_to(42)
print(my_other_list)
```

误以为每次调用函数时，如果不提供第二个参数，就会创建一个新的列表，所以结果应是这样的：

```
[12]
[42]
```

但其实却是这样的

```
[12]
[12, 42]
```

当函数被定义时，Python的默认参数就被创建 *一次*，而不是每次调用函数的时候创建。 这意味着，如果您使用一个可变默认参数并改变了它，您 *将会* 在未来所有对此函数的 调用中改变这个对象。



那如果想要为默认参数指定可变参数，该怎么办？

在每次函数调用中，通过使用指示没有提供参数的默认参数（[`None`](http://docs.python.org/library/constants.html#None) 通常是 个好选择），来创建一个新的对象。

```
def append_to(element, to=None):
    if to is None:
        to = []
    to.append(element)
    return to
```



如果想要让函数具有缓存功能的话，可以利用可变默认参数仅创建一次的这个特性，可以将其作为函数多次调用的缓存变量。



## 闭包延迟绑定变量

另一个常见的困惑是Python在闭包(或在周围全局作用域（surrounding global scope）)中 绑定变量的方式。



定义函数如下：

```
def create_multipliers():
    return [lambda x : i * x for i in range(5)]
```

运行如下代码：

```
for multiplier in create_multipliers():
    print(multiplier(2))
```

期望结果：

```
0
2
4
6
8
```

而事实上结果：

```
8
8
8
8
8
```

Python的闭包是 *迟绑定* 。 这意味着闭包中用到的变量的值，是在内部函数被调用时查询得到的。

这里，不论 *任何* 返回的函数是如何被调用的， `i` 的值是调用时在周围作用域中查询到的，即循环结束后的。



值得注意的是，这个问题跟 `lambda` 无关，下面的也同样存在该问题：

```
def create_multipliers():
    multipliers = []

    for i in range(5):
        def multiplier(x):
            return i * x
        multipliers.append(multiplier)

    return multipliers
```



如果延迟绑定不是你所期望的行为，那如何避免呢？

利用默认参数在函数定义时会赋值：

```
def create_multipliers():
    return [lambda x, i=i : i * x for i in range(5)]

```

或者，您可以使用 functools.partial 函数：

```
from functools import partial
from operator import mul

def create_multipliers():
    return [partial(mul, i) for i in range(5)]
```



## 字节码文件

默认情况下，当使用文件执行Python代码时，Python解释器会自动将该文件的字节码版本写入磁盘。 比如， `module.pyc`。

这些“.pyc”文件不应该加入到您的源代码仓库。

理论上，出于性能原因，此行为默认为开启。 没有这些字节码文件，Python会在每次加载文件时 重新生成字节码。

### 禁用字节码文件

在开发阶段，生成这些字节码文件，还要排除出版本系统之外，比较烦。如果想要在开发环境下禁止字节码文件的自动生成，该怎么办？

```
$ export PYTHONDONTWRITEBYTECODE=1

```

使用 `$PYTHONDONTWRITEBYTECODE` 环境变量，Python则不会把这些文件写入磁盘， 您的开发环境将会保持良好和干净。

我建议在您的 `~/.profile` 里设置这个环境变量。

### 删除字节码文件

以下是删除所有已存在的字节码文件的好方法:

```
$ find . -type f -name "*.py[co]" -delete -or -type d -name "__pycache__" -delete

```

从项目根目录运行，所有 `.pyc` 文件会嗖地一下消失， 好多了~

### 版本控制系统忽略字节码文件

如果由于性能原因仍然需要 `.pyc` 文件，您可以随时将它们添加到版本控制存储库的忽略文件中。 流行的版本控制系统能够使用文件中定义的通配符来应用特殊规则。

一份忽略文件将确保匹配的文件未被检入存储库。 [Git](https://git-scm.com/) 使用 `.gitignore`，而 [Mercurial](https://www.mercurial-scm.org/) 使用``.hgignore```。

至少您的忽略文件应该是这样的。

```
syntax:glob   # .gitignore 文件不需要这行
*.py[cod]     # 将匹配 .pyc、.pyo 和 .pyd文件
__pycache__/  # 排除整个文件夹

```

您可能希望根据需要添加更多文件和目录。下次提交到存储库时，这些文件将不被包括。