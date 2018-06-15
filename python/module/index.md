# 模块化

模块化好处：

* 降低耦合度
* 重用代码
* 加快开发效率
* 便于后期维护


Python 提供了模块（module）和包（package）来实现模块化机制：

* 模块：是类、函数以及变量等对象的抽象名称空间（一个文件）。
* 包：是用来组织模块的抽象名称空间（一个目录）。

## 模块

### 模块是什么

A module is a file containing Python definitions and statements. definitions from a module can be *imported* into other modules or into the *main* module. The file name is the module name with the suffix `.py` appended. Within a module, the module’s name (as a string) is available as the value of the global variable `__name__`.

### 模块包含的内容

A module can contain executable statements as well as function definitions. These statements are intended to initialize the module. They are executed only the *first* time the module name is encountered in an import statement. (They are also run if the file is executed as a script.)

In fact function definitions are also ‘statements’ that are ‘executed’; the execution of a module-level function definition enters the function name in the module’s global symbol table.

### 主模块是什么

the *main* module (the collection of variables that you have access to in a script executed at the top level and in calculator mode)

该模块的 `__name__` 为 `__main__`，其对应的名称空间用来表示运行代码的顶级作用域。通过 Python 交互式解释器或者将模块作为脚本运行，即可进入该名称空间。

模块当成脚本来执行

```
python scriptname.py <arguments>
```

如果要运行标准库模块或者已经安装好的第三方库模块，则：

```
python -m the_mod
```

同模块被导入时（也执行模块的初始化代码），没差别。唯一不同在于 `__name__` 变成 `__main__`。

可以利用该特性，可以在模块中编写只有在脚本环境中才会执行的代码，如下：

```
if __name__ == "__main__":
    # execute only if run as a script
    main()
```

### 模块的名称空间

Each module has its own private symbol table, which is used as the global symbol table by all functions defined in the module. Thus, the author of a module can use global variables in the module without worrying about accidental clashes with a user’s global variables.

### 模块内容的导入

导入模块到当前模块的名称空间中

Modules can import other modules. It is customary but not required to place all import statements at the beginning of a module. The imported module names are placed in the importing module’s global symbol table:

```
import fibo
```

导入函数等对象到当前模块的名称空间中

You can import variables and functions from a module directly into the importing module’s symbol table. This does not introduce the module name from which the imports are taken in the local symbol table:

```
from fibo import fib, fib2
```

导入所有内容到当前模块的名称空间中

You can import all names that a module defines. This imports all names except those beginning with an underscore (`_`). In most cases Python programmers do not use this facility since it introduces an unknown set of names into the interpreter, possibly hiding some things you have already defined:

```
from fibo import *
```

为导入的对象在当前名称空间中其别名

If the module name is followed by [`as`](https://docs.python.org/3/reference/compound_stmts.html#as), then the name following [`as`](https://docs.python.org/3/reference/compound_stmts.html#as) is bound directly to the imported module:

```
import fibo as fib
from fibo import fib as fibonacci
```

注：

* 模块被导入意味着其中的初始化代码会被执行
* 模块被导入意味着它在当前名称空间中可见

### 模块重新导入

在 Python 解析器的交互环境中每个模块仅加载一次，如果某个模块改变了，需要重启解析器或者使用 `importlib` 模块来对其重新导入 `importlib.relaod(modulename)`

### 模块搜索路径

1. built-in module
2. a list of directories given by the variable `sys.path`

`sys.path` 的初始化：

- The directory containing the input script (or the current directory when no file is specified). 
- [`PYTHONPATH`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH) (a list of directory names, with the same syntax as the shell variable `PATH`).
- The installation-dependent default.

After initialization, Python programs can modify [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path). 

注：the directory containing the script being run is placed at the beginning of the search path, ahead of the standard library path. This means that scripts in that directory will be loaded instead of modules of the same name in the library directory. This is an error unless the replacement is intended.

### 模块编译文件

缓存编译过的模块文件，支持 Python 多版本缓存

To speed up loading modules, Python caches the compiled version of each module in the `__pycache__` directory under the name `module.*version*.pyc`, where the version encodes the format of the compiled file; it generally contains the Python version number. For example, in CPython release 3.3 the compiled version of spam.py would be cached as `__pycache__/spam.cpython-33.pyc`. This naming convention allows compiled modules from different releases and different versions of Python to coexist.

Python checks the modification date of the source against the compiled version to see if it’s out of date and needs to be recompiled. This is a completely automatic process. Also, the compiled modules are platform-independent, so the same library can be shared among systems with different architectures.

不进行编译模块检查的情况：Python does not check the cache in two circumstances. First, it always recompiles and does not store the result for the module that’s loaded directly from the command line. Second, it does not check the cache if there is no source module. To support a non-source (compiled only) distribution, the compiled module must be in the source directory, and there must not be a source module.

手动编译：The module `compileall` can create .pyc files for all modules in a directory.

注：编译仅加快模块加载速度，不加快代码运行速度 A program doesn’t run any faster when it is read from a `.pyc` file than when it is read from a `.py` file; the only thing that’s faster about `.pyc` files is the speed with which they are loaded.

### 查看模块的内容

The built-in function [`dir()`](https://docs.python.org/3/library/functions.html#dir) is used to find out which names a module defines.

```
import sys
dir(sys)
```

Without arguments, [`dir()`](https://docs.python.org/3/library/functions.html#dir) lists the names you have defined currently:

```
dir()
```

想要查看内置的变量、函数、模块，需要借助模块 `builtins`

```
import builtins
dir(builtins)
```

## 包 - package

包可以是模块的集合，包的名称空间解决了模块之间的名称冲突问题（即不同包中的同名模块不会冲突），正如模块的名称空间解决了全局变量的名称冲突问题（即不同模块中的同名全局变量不会冲突）。访问包的名称空间的语法是，用 `.` 分隔的包名和模块名，如：`package.subpackage.module1`。

### 样例

官方的包结构样例：

```
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```

### 包的定义以及初始化

一个常规的目录（比如：`sound/effects` 目录）中创建一个空的 `__init__.py` 文件时，Python 就会将该目录当成包，并且允许目录出现嵌套的子包以及模块。`__init__.py` 除了起到声明当前目录是包之外，还具有执行包的初始化代码，定义 `__all__` 变量等功能。

有的时候包的**使用者**想要通过`from sound.effects import *` 语句的方式来导入包中所有**模块**，如果默认的机制是通过它可以导入包中所有模块的话，由于这样隐藏了导入内容的细节，会对项目有很大的副作用。此时由包的**作者**，在开发包的时候，提供一个声明来约束 `from sound.effects import *` 语句可以导入包中的哪些模块的话，就十分友好了。而 `___all__` 变量正是为此而生的。（题外话：库提供者应该负责约定库的使用接口。）

- 关于 `__all__` 变量：这是一个定义在 `__init__.py` 中的列表变量，列表中罗列出了允许包的使用者通过 `from sound.effects import *` 来导入当前包中的哪些模块。如果没有定义 `__all__` 变量，则该语句不会导入任何模块的。
- 当执行 `from sound.effects import *` 导入语句时，还发生了什么：文件 `sound/effects/__init__.py` 中代码被执行（一般用来初始化包），同时该文件中定义的全局对象被导入到了当前模块中（准确来说，只有遵从特定命名规范的全局对象才会被导入）。
- 无论如何 `import *` 语句都不是推荐的导入方式，应该尽量避免使用。

### 包当成脚本来运行

我们知道模块可以被当成脚本来运行，同样包也一样可以当成脚本来运行，首先我们需要为包添加一个 `__main__.py` 文件（如 `sound/__main__.py`），并将要在脚本环境下运行的代码放在这里（无需通过 `if __name__ == "__main__"` 进行条件判断），然后运行如下命令即可：

```
python -m sound
```

此外还可以通过 `.` 语法来直接运行包中的模块：

```
python -m sound.effects.echo
```

### 包的开发者篇 - 包的内部引用

一个包一般会有若干子包以及模块组成，并且这些子包和模块会彼此存在依赖关系，比如样例中的 `sound.filters.vocoder` 模块会引用到 `sound.effects.echo` 模块，这样如何进行导入呢，这里介绍两种导入方式：

* 绝对导入：即使用当前模块在包中的完整路径来进行导入。对于上面的例子，导入语句可以写成：`from sound.effects import echo`。
* 相对导入：即相对于当前模块的路径来进行导入。对于上面的例子，导入语句可以写成：`from ..effects import echo`。

两种导入方式均是有效的，不过推荐包的开发者使用相对导入语法。因为如果使用了相对导入语法，则在对包进行重构时，可使包中受到的影响尽可能减小（如：子包中对其内部的引用不会受到影响）。

### 包的使用者篇 - 包的外部引用

包的使用者一般使用绝对导入语法来使用包，假设现在有文件 `test.py` 跟 `sound` 包在同级目录中（不过一般都是安装在第三方库文件夹中的，位于 `sys.path` 中可以被搜索），在该文件中使用以下导入语句都是合法的：

```
# 导入后通过 `sound.effects.echo.echofilter` 引用函数 `echofilter`
import sound.effects.echo
# 导入后通过 `echo.echofilter` 即可引用函数 `echofilter`
from sound.effects import echo
# 或者直接导入该函数进行引用 `echofilter`
from sound.effects.echo import echofilter
```

以上绝对导入语句大概分类这两类：

* 通过 `from package import item` 语句进行导入时，被导入的 `item` 可能是一个包、模块、类、函数以及变量等。具体来说该语句会先从 `package` 查找看有无 `item` 对象，如果没有就查找看 `package` 中有无模块 `item`。
* 通过 `import item.subitem.subsubitem` 语句进行导入时，最后一项 `subsubitem` 一定是包或者模块，不可能是类、函数或者变量。