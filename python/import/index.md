## Introduction

[PEP 328](https://www.python.org/dev/peps/pep-0328/)

`import` 语句经常遇到的两个较为棘手的情形：

* 要导入许多对象时， `import` 太长。为了遵循一行代码不至于太长的约定，需要想办法将一个 `import` 语句分割为多行代码。
* `import` 语句会具有二义性，有时候难以分辨到底导入的内容是当前包中的，还是位于搜索路径 `sys.path` 中的某个包或模块的。

对于第一个问题，可以采用圆括号语法糖来修饰被导入的内容，以使得内容可以拆分为多行。

对于第二个问题，普通语法的 `import` 语句均表示绝对路径导入，即仅从搜索路径 `sys.path` 中的包或模块导入；至于相对路径的导入，即从当前包内进行导入，则需要特殊的语法来辅助（通过 `.` 作为前缀，后面会详细介绍）。

## Multi-Line Import

不推荐的导入语法：

- Write a long line with backslash continuations:

  ```
  from Tkinter import Tk, Frame, Button, Entry, Canvas, Text, \
      LEFT, DISABLED, NORMAL, RIDGE, END

  ```

- Write multiple `import` statements:

  ```
  from Tkinter import Tk, Frame, Button, Entry, Canvas, Text
  from Tkinter import LEFT, DISABLED, NORMAL, RIDGE, END
  ```

现在推荐的导入语法：

Instead, it should be possible to use Python's standard grouping mechanism (parentheses) to write the `import` statement:

```
from Tkinter import (Tk, Frame, Button, Entry, Canvas, Text,
    LEFT, DISABLED, NORMAL, RIDGE, END)
```

##  Absolute Import

在 Python 2.4 以前，像 `import foo` 这样的语句具有二义性，将优先从当前包内导入，如果当前包内没有 `foo` 包/模块则再从外部导入。因此这个时候，我们无从确定该语句是从当前包内导入，还是从外部导入的。随着 Python 外部库的不断丰富，经常会出现本地包/模块覆盖掉了第三方库的情况。

为了解决该语句的二义性问题，随后[版本](https://www.python.org/dev/peps/pep-0328/#rationale-for-absolute-imports)的 Python 中规定这类语句导入的包/模块，仅从搜索路径 `sys.path` 中进行查找，也即是[绝对导入语法](https://www.python.org/dev/peps/pep-0328/#rationale-for-absolute-imports)。绝对导入语法也是常日开发中的常见情形，我们经常需要在自己开发的应用中导入标准库、第三方库等，一般都会使用使用绝对导入语法。同时绝对导入语法也有一个明显的缺点，当包中的子包或模块被重命名或者移动时，所以对该包进行绝对导入的相关代码要做出修改。

样例：

```
# 导入标准库 os
import os

# 导入第三方库 requests
import requests
```

## Relative Import

[相对导入语法](https://www.python.org/dev/peps/pep-0328/#guido-s-decision)有两个最为常见的使用情形：

1. 导入当前包内的某个模块。
2. 通过相对导入语法，使得对包的结构进行调整时，子包不会受到任何影响。

相对导入的语法细节在历史上曾有些争议，Guido 最终决定采纳以下语法作为相对导入的语法：

1. 相对导入语法由包名和模块名前面添加的 `.` 符号来决定。
2. 一个 `.` 表示相对于当前包进行导入，即被导入内容属于当前包所在目录。
3. 两个 `.` 表示相对于当前包的父包进行导入，即被导入内容属于当前包所在的上一级目录。三个及以上，每多一个 `.` 表示从更上一级的目录导入。

官方给出的样例包的目录结构：

```
package/
    __init__.py
    subpackage1/
        __init__.py
        moduleX.py
        moduleY.py
    subpackage2/
        __init__.py
        moduleZ.py
    moduleA.py
```

假定要在 `moduleX.py` 中导入其它包和模块，样例如下：

```
from .moduleY import spam
from .moduleY import spam as ham
from . import moduleY
from ..subpackage1 import moduleY
from ..subpackage2.moduleZ import eggs
from ..moduleA import foo
from ...package import bar
# 合法但不推荐使用这种方式导入标准库
# 应该使用绝对导入语法来导入它
from ...sys import path
```

同样的样例，如果使用绝对语法导入将是这样的：

```
from package.subpackage1.moduleY import spam
from package.subpackage1.moduleY import spam as ham
from package.subpackage1 import moduleY
from package.subpackage1 import moduleY
from package.subpackage2.moduleZ import eggs
from package.moduleA import foo
from package import bar
# 现在这样导入标准库是推荐的方式，此外
# 绝对导入语法还允许：import sys.path 来
# 导入并直接使用 `sys.path`
from sys import path
```

总之相对导入语法必然是 `from <some> import <other>` 这样的格式，而绝对导入语法则 `import <some>` 和  `from <some> import <other>` 都是可以的。相对导入语法之所以不允许使用 `import <some>` 这种语法，是因为即使可以通过类似 `import .foo` 这样的语法进行导入，但 `.foo` 却是不合法的表达式。

相对导入语法背后的原理是怎样的呢？我们知道 `.` 个数代表在包结构中向上级追溯的层级数，那当前模块的又是如何知道其当前所在包结构中的什么位置呢。答案是通过模块中的变量 `__name__`，该变量记录了模块所在包结构的位置，例如上例中的 `moduleX.py` 模块中该变量的为 `package.subpackage1.moduleX`，进而由此来在包结构中进行层级追溯。

此外我们知道一个应用程序中的**主模块**（main module），作为应用的入口，具有特殊的含义，该模块中的变量 `__name__` 通常被设置为 `__main__`，而不再是上面提到的模块所在包结构中的位置。因此对于主模块，相对导入语法是无效的，我们只能使用绝对导入语法来引用其它包和模块。