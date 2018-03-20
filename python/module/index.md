模块化好处：

* 降低耦合度
* 重用代码
* 加快开发效率
* 便于后期维护



## 模块

模块是什么，模块之间如何交互，如何访问模块里面的内容

A module is a file containing Python definitions and statements. definitions from a module can be *imported* into other modules or into the *main* module. The file name is the module name with the suffix `.py` appended. Within a module, the module’s name (as a string) is available as the value of the global variable `__name__`.



模块包含的内容

A module can contain executable statements as well as function definitions. These statements are intended to initialize the module. They are executed only the *first* time the module name is encountered in an import statement. (They are also run if the file is executed as a script.)

In fact function definitions are also ‘statements’ that are ‘executed’; the execution of a module-level function definition enters the function name in the module’s global symbol table.

模块的名称空间

Each module has its own private symbol table, which is used as the global symbol table by all functions defined in the module. Thus, the author of a module can use global variables in the module without worrying about accidental clashes with a user’s global variables.

模块的导入

Modules can import other modules. It is customary but not required to place all import statements at the beginning of a module. The imported module names are placed in the importing module’s global symbol table:

```
import fibo
```



You can import variables and functions from a module directly into the importing module’s symbol table. This does not introduce the module name from which the imports are taken in the local symbol table:

```
from fibo import fib, fib2
```



You can import all names that a module defines. This imports all names except those beginning with an underscore (`_`). In most cases Python programmers do not use this facility since it introduces an unknown set of names into the interpreter, possibly hiding some things you have already defined:

```
from fibo import *
```



If the module name is followed by [`as`](https://docs.python.org/3/reference/compound_stmts.html#as), then the name following [`as`](https://docs.python.org/3/reference/compound_stmts.html#as) is bound directly to the imported module:

```
import fibo as fib
from fibo import fib as fibonacci
```



Python 解析器的交互环境中每个模块仅加载一次，如果某个模块改变了，需要重启解析器或者使用 `importlib` 模块来对其重新导入 `importlib.relaod(modulename)`



模块当成脚本来执行

```
python scriptname.py <arguments>
```

同模块被导入时（也执行代码），没差别。唯一不同在于 `__name__` 变成 `__main__`，因此可以根据它来条件判断，以便将当成脚本时需要执行的代码单独分开

This is often used either to provide a convenient user interface to a module, or for testing purposes (running the module as a script executes a test suite).



模块的搜索路径

1. built-in module
2.  a list of directories given by the variable `sys.path`

`sys.path` 的初始化：

- The directory containing the input script (or the current directory when no file is specified). symlink 将包含原始文件所在目录
- [`PYTHONPATH`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH) (a list of directory names, with the same syntax as the shell variable `PATH`).
- The installation-dependent default.

After initialization, Python programs can modify [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path). 

小心覆盖内置模块：he directory containing the script being run is placed at the beginning of the search path, ahead of the standard library path. This means that scripts in that directory will be loaded instead of modules of the same name in the library directory. This is an error unless the replacement is intended.



缓存编译过的模块文件，支持 Python 多版本缓存

To speed up loading modules, Python caches the compiled version of each module in the `__pycache__` directory under the name `module.*version*.pyc`, where the version encodes the format of the compiled file; it generally contains the Python version number. For example, in CPython release 3.3 the compiled version of spam.py would be cached as `__pycache__/spam.cpython-33.pyc`. This naming convention allows compiled modules from different releases and different versions of Python to coexist.

Python checks the modification date of the source against the compiled version to see if it’s out of date and needs to be recompiled. This is a completely automatic process. Also, the compiled modules are platform-independent, so the same library can be shared among systems with different architectures.

不进行编译模块检查的情况：Python does not check the cache in two circumstances. First, it always recompiles and does not store the result for the module that’s loaded directly from the command line. Second, it does not check the cache if there is no source module. To support a non-source (compiled only) distribution, the compiled module must be in the source directory, and there must not be a source module.

手动编译：The module `compileall` can create .pyc files for all modules in a directory.

注：编译仅加快模块加载速度，不加快代码运行速度 A program doesn’t run any faster when it is read from a `.pyc` file than when it is read from a `.py` file; the only thing that’s faster about `.pyc` files is the speed with which they are loaded.



查看模块的内容：

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



## 包

包解决了模块名称冲突的问题

Packages are a way of structuring Python’s module namespace by using “dotted module names”. For example, the module name `A.B` designates a submodule named `B` in a package named `A`. Just like the use of modules saves the authors of different modules from having to worry about each other’s global variable names, the use of dotted module names saves the authors of multi-module packages like NumPy or the Python Imaging Library from having to worry about each other’s module names.



包的结构：

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



包的 `__init__.py` 作用

标识目录是包；定义包的初始化代码；

The `__init__.py` files are required to make Python treat the directories as containing packages; this is done to prevent directories with a common name, such as `string`, from unintentionally hiding valid modules that occur later on the module search path. In the simplest case, `__init__.py` can just be an empty file, but it can also execute initialization code for the package or set the `__all__` variable



包的开发者决定包可以导出哪些模块

Now what happens when the user writes `from sound.effects import *`? Ideally, one would hope that this somehow goes out to the filesystem, finds which submodules are present in the package, and imports them all. This could take a long time and importing sub-modules might have unwanted side-effects that should only happen when the sub-module is explicitly imported.

The only solution is for the package author to provide an explicit index of the package. The [`import`](https://docs.python.org/3/reference/simple_stmts.html#import) statement uses the following convention: if a package’s `__init__.py` code defines a list named `__all__`, it is taken to be the list of module names that should be imported when `from packageimport *` is encountered. It is up to the package author to keep this list up-to-date when a new version of the package is released. Package authors may also decide not to support it, if they don’t see a use for importing * from their package. For example, the file `sound/effects/__init__.py` could contain the following code:

```
__all__ = ["echo", "surround", "reverse"]
```

If `__all__` is not defined, the statement `from sound.effects import *` does *not* import all submodules from the package `sound.effects` into the current namespace; it only ensures that the package `sound.effects` has been imported (possibly running any initialization code in `__init__.py`) and then imports whatever names are defined in the package. This includes any names defined (and submodules explicitly loaded) by `__init__.py`.

Although certain modules are designed to export only names that follow certain patterns when you use `import *`, it is still considered bad practice in production code.

Remember, there is nothing wrong with using `from Package import specific_submodule`! In fact, this is the recommended notation



包的导入

全路径导入模块

Users of the package can import individual modules from the package, for example:

```
import sound.effects.echo
```

This loads the submodule `sound.effects.echo`. It must be referenced with its full name.

```
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
```

直接导入模块

An alternative way of importing the submodule is:

```
from sound.effects import echo

```

This also loads the submodule `echo`, and makes it available without its package prefix, so it can be used as follows:

```
echo.echofilter(input, output, delay=0.7, atten=4)
```

直接导入模块中的方法

Yet another variation is to import the desired function or variable directly:

```
from sound.effects.echo import echofilter

```

Again, this loads the submodule `echo`, but this makes its function `echofilter()` directly available:

```
echofilter(input, output, delay=0.7, atten=4)
```

两种导入方式的注意点：

Note that when using `from package import item`, the item can be either a submodule (or subpackage) of the package, or some other name defined in the package, like a function, class or variable. The `import` statement first tests whether the item is defined in the package; if not, it assumes it is a module and attempts to load it. If it fails to find it, an [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError) exception is raised.

Contrarily, when using syntax like `import item.subitem.subsubitem`, each item except for the last must be a package; the last item can be a module or a package but can’t be a class or function or variable defined in the previous item.



包中的交叉引用

绝对导入

When packages are structured into subpackages (as with the `sound` package in the example), you can use absolute imports to refer to submodules of siblings packages. For example, if the module `sound.filters.vocoder` needs to use the `echo` module in the `sound.effects` package, it can use `fromsound.effects import echo`.

相对导入

You can also write relative imports, with the `from module import name` form of import statement. These imports use leading dots to indicate the current and parent packages involved in the relative import. From the `surround` module for example, you might use:

```
from . import echo
from .. import formats
from ..filters import equalizer
```

注意 `__main__` 中的导入：Note that relative imports are based on the name of the current module. Since the name of the main module is always `"__main__"`, modules intended for use as the main module of a Python application must always use absolute imports.