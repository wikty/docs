---
title: Python Coding Style
---

## 简介

官方推荐的 Python 代码风格指南叫做 [PEP 8][1]，该风格指南来自于 Python 之父 Guido 初期拟定的 Python 代码风格。

不同的项目也许会有不同的代码风格，应该尽量跟项目的风格一致，而不是教条式的服从该指南。一致性才是风格指南所追求的，项目中代码风格的一致性，可提高项目可读性。

Many projects have their own coding style guidelines. In the event of any conflicts, such project-specific guides take precedence for that project.

One of Guido's key insights is that code is read much more often than it is written. The guidelines provided here are intended to improve the readability of code and make it consistent across the wide spectrum of Python code.

A style guide is about consistency. Consistency with this style guide is important. Consistency within a project is more important. Consistency within one module or function is the most important.

什么时候不应该依照该指南的代码风格？

However, know when to be inconsistent -- sometimes style guide recommendations just aren't applicable. In particular: do not break backwards compatibility just to comply with this PEP!

Some other good reasons to ignore a particular guideline:

1. When applying the guideline would make the code less readable, even for someone who is used to reading code that follows this PEP.
2. To be consistent with surrounding code that also breaks it (maybe for historic reasons) -- although this is also an opportunity to clean up someone else's mess (in true XP style).
3. Because the code in question predates the introduction of the guideline and there is no other reason to be modifying that code.
4. When the code needs to remain compatible with older versions of Python that don't support the feature recommended by the style guide.

## 代码排版

### 空白字符

空格和制表符之间，优先使用空格。

只有在维护旧代码为了保持一致性时，才使用制表符。

Python 3 不允许空格和制表符混合使用。Python 2 允许空格和制表符混合使用，不过可以在运行代码时，通过命令行选项 `-t` 和 `-tt` 来强制检查这些混合使用。

Spaces are the preferred indentation method.

Tabs should be used solely to remain consistent with code that is already indented with tabs.

Python 3 disallows mixing the use of tabs and spaces for indentation.

Python 2 code indented with a mixture of tabs and spaces should be converted to using spaces exclusively.

When invoking the Python 2 command line interpreter with the -t option, it issues warnings about code that illegally mixes tabs and spaces. When using -tt these warnings become errors. These options are highly recommended!

### 缩进

使用 4 个空格来表示一个缩进级别。

位于大括号、中括号以及小括号之间的连续行，要么垂直对齐，要么悬挂式对齐。

垂直对齐：后续行跟第一行的定界符保持垂直对齐

    foo = long_function_name(var_one, var_two,
                             var_three, var_four)

悬挂式对齐：后续行不必跟第一行的定界符保持对齐，可以缩进任意空白，不过要注意跟连续行之后（即定界符之后）的内容有缩进上的区别，并且连续行的首行不能有参数

    def long_function_name(
            var_one, var_two, var_three,
            var_four):
        print(var_one)

if 条件语句太长，需要写成多行时：`if` 紧跟一个空格，再紧跟 `(`，然后是条件语句，后续的条件语句行应该缩进 4 个空格，最后一行以 `)` 结束。示例如下：

    if (this_is_one_thing and
        that_is_another_thing):
        do_something()

如果 if 条件语句又紧接着一个嵌套的 if 条件语句，为了区分它们，可以在条件语句结束时添加一些注释。

当使用大括号、中括号以及小括号创建字典、列表等对象时，开始定界符后面没有内容，结束定界符应该跟最后一行内容的第一个非空字符保持对齐或者跟多行内容首行第一个字符保持对齐。

    my_list = [
        1, 2, 3,
        4, 5, 6,
        ]
    
    my_list = [
        1, 2, 3,
        4, 5, 6,
    ]

### 行最大长度

所有行的最多字符数是 79。

docstring 和注释行最大字符数是 72。

限制行最大长度的原因：

Limiting the required editor window width makes it possible to have several files open side-by-side, and works well when using code review tools that present the two versions in adjacent columns.

The default wrapping in most tools disrupts the visual structure of the code, making it more difficult to understand. The limits are chosen to avoid wrapping in editors with the window width set to 80, even if the tool places a marker glyph in the final column when wrapping lines. Some web based tools may not offer dynamic line wrapping at all.

如果代码在一行放不下，为了保证每行满足最大长度必须将行打断为多行，该怎么办？

* 尽量使用大括号、中括号以及小括号的包含多行的功能。The preferred way of wrapping long lines is by using Python's implied line continuation inside parentheses, brackets and braces. Long lines can be broken over multiple lines by wrapping expressions in parentheses.
* 实在不行的话，就使用转义符来连接多行内容 using a backslash for line continuation

常见需要使用转义符来连接多行内容的有：`with` 打开多个文件；`assert` 断言条件复杂

### 二元运算符和换行

多行的条件判断表达式，应该在 `and`, `or`, `+`, `-`, `*`, `==`  等二元运算符的前面还是后面进行换行呢？

推荐在二元运算符前面换行：

    income = (gross_wages
              + taxable_interest
              + (dividends - qualified_dividends)
              - ira_deduction
              - student_loan_interest)

如果在二元运算符后面换行，使得操作数远离运算符，降低可读性：

    income = (gross_wages +
              taxable_interest +
              (dividends - qualified_dividends) -
              ira_deduction -
              student_loan_interest)

### 空行的使用

模块中顶级函数和类定义前后应该包围两个空行。Surround top-level function and class definitions with two blank lines.

类中的方法前后应该包围一个空行。Method definitions inside a class are surrounded by a single blank line.

此外还可以添加额外的空白行用于函数分组、函数内逻辑分块。

分页 Python accepts the control-L (i.e. ^L) form feed character as whitespace; Many tools treat these characters as page separators, so you may use them to separate pages of related sections of your file.

## 模块语句

* Imports should usually be on separate lines. 对一个模块或包的导入写在一行

  ```
  import os
  import sys
  from subprocess import Popen, PIPE
  ```

* Imports are always put at the top of the file, just after any module comments and docstrings, and before module globals and constants. 导入语句应为位于模块顶部，紧跟在模块注释和文档字符串之后，且必须位于模块变量的前面

* 导入语句应该按照下面方式进行有序分组，分组之间用空行隔开

  1. standard library imports
  2. related third party imports
  3. local application/library specific imports

* 绝对导入和相对导入语法

  Absolute imports are recommended, as they are usually more readable and tend to be better behaved (or at least give better error messages) if the import system is incorrectly configured

  However, explicit relative imports are an acceptable alternative to absolute imports, especially when dealing with complex package layouts where using absolute imports would be unnecessarily verbose

  Standard library code should avoid complex package layouts and always use absolute imports.

* 导入类时，如果类名和当前模块名称冲突，可以导入包含该类的模块，然后用 `yourclassmodule.YourClass` 来引用该类

  ```
  from myclass import MyClass
  import myclass # myclass.MyClass
  ```

* Wildcard imports (`from <module> import *`) should be avoided, as they make it unclear which names are present in the namespace, confusing both readers and many automated tools. There is one defensible use case for a wildcard import, which is to republish an internal interface as part of a public API. 通配符导入应该被避免。不过当想要将内部接口重新发布为公开接口时，可以使用通配符导入。

## 模块级特殊变量

Module level "dunders" (i.e. names with two leading and two trailing underscores) such as `__all__`, `__author__`, `__version__`, etc. should be placed after the module docstring but before any import statements *except* `from __future__` imports. Python mandates that future-imports must appear in the module before any other code except docstrings.

一个模块顶部内容顺序的样例:

1. 文档字符串
2. `from __future__ ` 导入语句
3. 模块级 dunder 变量
4. 标准库导入、第三方库导入、项目模块导入

```
"""This is the example module.

This module does stuff.
"""

from __future__ import barry_as_FLUFL

__all__ = ['a', 'b', 'c']
__version__ = '0.1'
__author__ = 'Cardinal Biggles'

import os
import sys
```



## 源文件编码

Code in the core Python distribution should always use UTF-8 (or ASCII in Python 2).

Files using ASCII (in Python 2) or UTF-8 (in Python 3) should not have an encoding declaration.

Python 3 对标准库编码的要求

All identifiers in the Python standard library MUST use ASCII-only identifiers, and SHOULD use English words wherever feasible (in many cases, abbreviations and technical terms are used which aren't English). In addition, string literals and comments must also be in ASCII. The only exceptions are (a) test cases testing the non-ASCII features, and (b) names of authors. Authors whose names are not based on the Latin alphabet (latin-1, ISO/IEC 8859-1 character set) MUST provide a transliteration of their names in this character set.

* 标识符必须使用 ASCII 字符且尽可能使用英语单词
* 字符常量和注释也要使用 ASCII 字符，除非出于测试目的或者代码作者名字是非 ASCII 字符



## 字符串引号

单引号和双引号每差别，要选择一种方式并在项目中保持一致。

当字符串本身含有单引号或双引号时，优先使用另外一种引号，避免使用转移符。

三引号字符串要求使用三个双引号。

In Python, single-quoted strings and double-quoted strings are the same. This PEP does not make a recommendation for this. Pick a rule and stick to it. When a string contains single or double quote characters, however, use the other one to avoid backslashes in the string. It improves readability.

For triple-quoted strings, always use double quote characters to be consistent with the docstring convention

## 表达式和语句中的空白

不该添加空白的地方

Avoid extraneous whitespace in the following situations:

- Immediately inside parentheses, brackets or braces. 大括号、中括号、小括号的内部

  ```
  Yes: spam(ham[1], {eggs: 2})
  No:  spam( ham[ 1 ], { eggs: 2 } )

  ```

- Between a trailing comma and a following close parenthesis. 逗号紧跟结束小括号

  ```
  Yes: foo = (0,)
  No:  bar = (0, )

  ```

- Immediately before a comma, semicolon, or colon: 逗号、分号、冒号的前面

  ```
  Yes: if x == 4: print x, y; x, y = y, x
  No:  if x == 4 : print x , y ; x , y = y , x

  ```

- However, in a slice the colon acts like a binary operator, and should have equal amounts on either side (treating it as the operator with the lowest priority). In an extended slice, both colons must have the same amount of spacing applied. Exception: when a slice parameter is omitted, the space is omitted. slice 语法中使用冒号时，应该将该冒号看作是优先级最低的二元运算符，两侧如果添加空白的话，数量应该相等

  Yes:

  ```
  ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
  ham[lower:upper], ham[lower:upper:], ham[lower::step]
  ham[lower+offset : upper+offset]
  ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
  ham[lower + offset : upper + offset]

  ```

  No:

  ```
  ham[lower + offset:upper + offset]
  ham[1: 9], ham[1 :9], ham[1:9 :3]
  ham[lower : : upper]
  ham[ : upper]

  ```

- Immediately before the open parenthesis that starts the argument list of a function call:用于参数列表的开始小括号前面

  ```
  Yes: spam(1)
  No:  spam (1)

  ```

- Immediately before the open parenthesis that starts an indexing or slicing:  用于缩进和slice 的开始括号前面

  ```
  Yes: dct['key'] = lst[index]
  No:  dct ['key'] = lst [index]

  ```

- More than one space around an assignment (or other) operator to align it with another. 赋值号两侧多于一个空格

  Yes:

  ```
  x = 1
  y = 2
  long_variable = 3

  ```

  No:

  ```
  x             = 1
  y             = 2
  long_variable = 3
  ```



不要在行尾留有空白

Avoid trailing whitespace anywhere. Because it's usually invisible, it can be confusing: e.g. a backslash followed by a space and a newline does not count as a line continuation marker

在赋值、条件判断、布尔运算等二元运算符两侧保留一个空白

Always surround these binary operators with a single space on either side: assignment (`=`), augmented assignment (`+=`, `-=`etc.), comparisons (`==`, `<`, `>`, `!=`, `<>`, `<=`, `>=`, `in`, `not in`, `is`, `is not`), Booleans (`and`, `or`, `not`).

当一个表达式同时出现多个运算符时，应该在优先级最低的运算符两侧保留一个空白，使得看起来好像低优先级的运算确实是后来再被计算的

If operators with different priorities are used, consider adding whitespace around the operators with the lowest priority(ies). Use your own judgment; however, never use more than one space, and always have the same amount of whitespace on both sides of a binary operator

Yes:

```
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)

```

No:

```
i=i+1
submitted +=1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)
```

不要在函数调用传递关键字参数或者函数定义指定默认参数时，在 `=` 两侧添加空白

Yes:

```
def complex(real, imag=0.0):
    return magic(r=real, i=imag)

```

No:

```
def complex(real, imag = 0.0):
    return magic(r = real, i = imag)
```

复合语句（多个语句写在一行）不被推荐，if/for/while 语句块写在一行也不推荐

Compound statements (multiple statements on the same line) are generally discouraged.

While sometimes it's okay to put an if/for/while with a small body on the same line, never do this for multi-clause statements. Also avoid folding such long lines!

## 尾部逗号

除了定义单元素的 tuple 外，在大多数情况下尾部的逗号都是可选的

Trailing commas are usually optional, except they are mandatory when making a tuple of one element

定义单元素的 tuple 时，尾部必须有逗号，并且推荐使用括号包围，可读性更强

Yes:

```
FILES = ('setup.cfg',)

```

OK, but confusing:

```
FILES = 'setup.cfg',
```

大多数情况下，添加行尾逗号，以表明列表值、参数列表等是将来可能扩展的

When trailing commas are redundant, they are often helpful when a version control system is used, when a list of values, arguments or imported items is expected to be extended over time. The pattern is to put each value (etc.) on a line by itself, always adding a trailing comma, and add the close parenthesis/bracket/brace on the next line

Yes:

```
FILES = [
    'setup.cfg',
    'tox.ini',
    ]
initialize(FILES,
           error=True,
           )
```

## 注释

Comments that contradict the code are worse than no comments. Always make a priority of keeping the comments up-to-date when the code changes!

Comments should be complete sentences. The first word should be capitalized, unless it is an identifier that begins with a lower case letter (never alter the case of identifiers!).

Block comments generally consist of one or more paragraphs built out of complete sentences, with each sentence ending in a period.

You should use two spaces after a sentence-ending period in multi- sentence comments, except after the final sentence.

块注释

Block comments generally apply to some (or all) code that follows them, and are indented to the same level as that code. Each line of a block comment starts with a `#` and a single space (unless it is indented text inside the comment).

Paragraphs inside a block comment are separated by a line containing a single `#`.

行注释

Use inline comments sparingly.

An inline comment is a comment on the same line as a statement. Inline comments should be separated by at least two spaces from the statement. They should start with a # and a single space.

## 文档字符串

- Write docstrings for all public modules, functions, classes, and methods. Docstrings are not necessary for non-public methods, but you should have a comment that describes what the method does. This comment should appear after the `def` line.

- [PEP 257](https://www.python.org/dev/peps/pep-0257) describes good docstring conventions. Note that most importantly, the `"""` that ends a multiline docstring should be on a line by itself, e.g.:

  ```
  """Return a foobang

  Optional plotz says to frobnicate the bizbaz first.
  """

  ```

- For one liner docstrings, please keep the closing `"""` on the same line.

## 命名约定

对于新模块和包推荐一下命名约定，但对于已经存在的项目，建议跟项目保持一致

New modules and packages (including third party frameworks) should be written to these standards, but where an existing library has a different style, internal consistency is preferred.

对于公开接口的命名应该反映用法而不是实现

Names that are visible to the user as public parts of the API should follow conventions that reflect usage rather than implementation.

各种编程语言中常见的各种命名风格

- `b` (single lowercase letter)

- `B` (single uppercase letter)

- `lowercase`

- `lower_case_with_underscores`

- `UPPERCASE`

- `UPPER_CASE_WITH_UNDERSCORES`

- `CapitalizedWords` (or CapWords, or CamelCase -- so named because of the bumpy look of its letters [[4\]](https://www.python.org/dev/peps/pep-0008/#id11)). This is also sometimes known as StudlyCaps.

  Note: When using acronyms in CapWords, capitalize all the letters of the acronym. Thus HTTPServerError is better than HttpServerError.

- `mixedCase` (differs from CapitalizedWords by initial lowercase character!)

- `Capitalized_Words_With_Underscores` (ugly!)

- There's also the style of using a short unique prefix to group related names together. This is not used much in Python, but it is mentioned for completeness. For example, the `os.stat()` function returns a tuple whose items traditionally have names like `st_mode`, `st_size`, `st_mtime` and so on. (This is done to emphasize the correspondence with the fields of the POSIX system call struct, which helps programmers familiar with that.)

此外在 Python 中还可以使用下划线跟以上各种风格进行组合

In addition, the following special forms using leading or trailing underscores are recognized (these can generally be combined with any case convention):

- `_single_leading_underscore`: weak "internal use" indicator. E.g. `from M import *` does not import objects whose name starts with an underscore.

- `single_trailing_underscore_`: used by convention to avoid conflicts with Python keyword, e.g.

  ```
  Tkinter.Toplevel(master, class_='ClassName')

  ```

- `__double_leading_underscore`: when naming a class attribute, invokes name mangling (inside class FooBar, `__boo` becomes`_FooBar__boo`; see below).

- `__double_leading_and_trailing_underscore__`: "magic" objects or attributes that live in user-controlled namespaces. E.g. `__init__`, `__import__` or `__file__`. Never invent such names; only use them as documented.

### [Names to Avoid](https://www.python.org/dev/peps/pep-0008/#id38)

Never use the characters 'l' (lowercase letter el), 'O' (uppercase letter oh), or 'I' (uppercase letter eye) as single character variable names.

In some fonts, these characters are indistinguishable from the numerals one and zero. When tempted to use 'l', use 'L' instead.

### [ASCII Compatibility](https://www.python.org/dev/peps/pep-0008/#id39)

Identifiers used in the standard library must be ASCII compatible as described in the [policy section](https://www.python.org/dev/peps/pep-3131/#policy-specification) of [PEP 3131](https://www.python.org/dev/peps/pep-3131).

### [Package and Module Names](https://www.python.org/dev/peps/pep-0008/#id40)

Modules should have short, all-lowercase names. Underscores can be used in the module name if it improves readability. Python packages should also have short, all-lowercase names, although the use of underscores is discouraged.

When an extension module written in C or C++ has an accompanying Python module that provides a higher level (e.g. more object oriented) interface, the C/C++ module has a leading underscore (e.g. `_socket`).

### [Class Names](https://www.python.org/dev/peps/pep-0008/#id41)

Class names should normally use the CapWords convention.

The naming convention for functions may be used instead in cases where the interface is documented and used primarily as a callable.

Note that there is a separate convention for builtin names: most builtin names are single words (or two words run together), with the CapWords convention used only for exception names and builtin constants.

### [Type variable names](https://www.python.org/dev/peps/pep-0008/#id42)

Names of type variables introduced in [PEP 484](https://www.python.org/dev/peps/pep-0484) should normally use CapWords preferring short names: `T`, `AnyStr`, `Num`. It is recommended to add suffixes `_co` or `_contra` to the variables used to declare covariant or contravariant behavior correspondingly. Examples:

```
from typing import TypeVar

VT_co = TypeVar('VT_co', covariant=True)
KT_contra = TypeVar('KT_contra', contravariant=True)

```

### [Exception Names](https://www.python.org/dev/peps/pep-0008/#id43)

Because exceptions should be classes, the class naming convention applies here. However, you should use the suffix "Error" on your exception names (if the exception actually is an error).

### [Global Variable Names](https://www.python.org/dev/peps/pep-0008/#id44)

(Let's hope that these variables are meant for use inside one module only.) The conventions are about the same as those for functions.

Modules that are designed for use via `from M import *` should use the `__all__` mechanism to prevent exporting globals, or use the older convention of prefixing such globals with an underscore (which you might want to do to indicate these globals are "module non-public").

### [Function and variable names](https://www.python.org/dev/peps/pep-0008/#id45)

Function names should be lowercase, with words separated by underscores as necessary to improve readability.

Variable names follow the same convention as function names.

mixedCase is allowed only in contexts where that's already the prevailing style (e.g. threading.py), to retain backwards compatibility.

### [Function and method arguments](https://www.python.org/dev/peps/pep-0008/#id46)

Always use `self` for the first argument to instance methods.

Always use `cls` for the first argument to class methods.

If a function argument's name clashes with a reserved keyword, it is generally better to append a single trailing underscore rather than use an abbreviation or spelling corruption. Thus `class_` is better than `clss`. (Perhaps better is to avoid such clashes by using a synonym.)

### [Method Names and Instance Variables](https://www.python.org/dev/peps/pep-0008/#id47)

Use the function naming rules: lowercase with words separated by underscores as necessary to improve readability.

Use one leading underscore only for non-public methods and instance variables.

To avoid name clashes with subclasses, use two leading underscores to invoke Python's name mangling rules.

Python mangles these names with the class name: if class Foo has an attribute named `__a`, it cannot be accessed by `Foo.__a`. (An insistent user could still gain access by calling `Foo._Foo__a`.) Generally, double leading underscores should be used only to avoid name conflicts with attributes in classes designed to be subclassed.

Note: there is some controversy about the use of __names (see below).

### [Constants](https://www.python.org/dev/peps/pep-0008/#id48)

Constants are usually defined on a module level and written in all capital letters with underscores separating words. Examples include `MAX_OVERFLOW` and `TOTAL`.

### [Designing for inheritance](https://www.python.org/dev/peps/pep-0008/#id49)

Always decide whether a class's methods and instance variables (collectively: "attributes") should be public or non-public. If in doubt, choose non-public; it's easier to make it public later than to make a public attribute non-public.

Public attributes are those that you expect unrelated clients of your class to use, with your commitment to avoid backward incompatible changes. Non-public attributes are those that are not intended to be used by third parties; you make no guarantees that non-public attributes won't change or even be removed.

We don't use the term "private" here, since no attribute is really private in Python (without a generally unnecessary amount of work).

Another category of attributes are those that are part of the "subclass API" (often called "protected" in other languages). Some classes are designed to be inherited from, either to extend or modify aspects of the class's behavior. When designing such a class, take care to make explicit decisions about which attributes are public, which are part of the subclass API, and which are truly only to be used by your base class.

With this in mind, here are the Pythonic guidelines:

- Public attributes should have no leading underscores.

- If your public attribute name collides with a reserved keyword, append a single trailing underscore to your attribute name. This is preferable to an abbreviation or corrupted spelling. (However, notwithstanding this rule, 'cls' is the preferred spelling for any variable or argument which is known to be a class, especially the first argument to a class method.)

  Note 1: See the argument name recommendation above for class methods.

- For simple public data attributes, it is best to expose just the attribute name, without complicated accessor/mutator methods. Keep in mind that Python provides an easy path to future enhancement, should you find that a simple data attribute needs to grow functional behavior. In that case, use properties to hide functional implementation behind simple data attribute access syntax.

  Note 1: Properties only work on new-style classes.

  Note 2: Try to keep the functional behavior side-effect free, although side-effects such as caching are generally fine.

  Note 3: Avoid using properties for computationally expensive operations; the attribute notation makes the caller believe that access is (relatively) cheap.

- If your class is intended to be subclassed, and you have attributes that you do not want subclasses to use, consider naming them with double leading underscores and no trailing underscores. This invokes Python's name mangling algorithm, where the name of the class is mangled into the attribute name. This helps avoid attribute name collisions should subclasses inadvertently contain attributes with the same name.

  Note 1: Note that only the simple class name is used in the mangled name, so if a subclass chooses both the same class name and attribute name, you can still get name collisions.

  Note 2: Name mangling can make certain uses, such as debugging and `__getattr__()`, less convenient. However the name mangling algorithm is well documented and easy to perform manually.

  Note 3: Not everyone likes name mangling. Try to balance the need to avoid accidental name clashes with potential use by advanced callers.

## [Public and internal interfaces](https://www.python.org/dev/peps/pep-0008/#id50)

Any backwards compatibility guarantees apply only to public interfaces. Accordingly, it is important that users be able to clearly distinguish between public and internal interfaces.

Documented interfaces are considered public, unless the documentation explicitly declares them to be provisional or internal interfaces exempt from the usual backwards compatibility guarantees. All undocumented interfaces should be assumed to be internal.

To better support introspection, modules should explicitly declare the names in their public API using the `__all__` attribute. Setting `__all__` to an empty list indicates that the module has no public API.

Even with `__all__` set appropriately, internal interfaces (packages, modules, classes, functions, attributes or other names) should still be prefixed with a single leading underscore.

An interface is also considered internal if any containing namespace (package, module or class) is considered internal.

Imported names should always be considered an implementation detail. Other modules must not rely on indirect access to such imported names unless they are an explicitly documented part of the containing module's API, such as `os.path` or a package's `__init__` module that exposes functionality from submodules.

## 编程

- Code should be written in a way that does not disadvantage other implementations of Python (PyPy, Jython, IronPython, Cython, Psyco, and such).

  For example, do not rely on CPython's efficient implementation of in-place string concatenation for statements in the form `a += b` or `a = a + b`. This optimization is fragile even in CPython (it only works for some types) and isn't present at all in implementations that don't use refcounting. In performance sensitive parts of the library, the `''.join()` form should be used instead. This will ensure that concatenation occurs in linear time across various implementations.

- Comparisons to singletons like None should always be done with `is` or `is not`, never the equality operators.

  Also, beware of writing `if x` when you really mean `if x is not None` -- e.g. when testing whether a variable or argument that defaults to None was set to some other value. The other value might have a type (such as a container) that could be false in a boolean context!

- Use `is not` operator rather than `not ... is`. While both expressions are functionally identical, the former is more readable and preferred.

  Yes:

  ```
  if foo is not None:

  ```

  No:

  ```
  if not foo is None:

  ```

- When implementing ordering operations with rich comparisons, it is best to implement all six operations (`__eq__`, `__ne__`,`__lt__`, `__le__`, `__gt__`, `__ge__`) rather than relying on other code to only exercise a particular comparison.

  To minimize the effort involved, the `functools.total_ordering()` decorator provides a tool to generate missing comparison methods.

  [PEP 207](https://www.python.org/dev/peps/pep-0207) indicates that reflexivity rules *are* assumed by Python. Thus, the interpreter may swap `y > x` with `x < y`, `y >= x` with `x <= y`, and may swap the arguments of `x == y` and `x != y`. The `sort()` and `min()` operations are guaranteed to use the `<`operator and the `max()` function uses the `>` operator. However, it is best to implement all six operations so that confusion doesn't arise in other contexts.

- Always use a def statement instead of an assignment statement that binds a lambda expression directly to an identifier.

  Yes:

  ```
  def f(x): return 2*x

  ```

  No:

  ```
  f = lambda x: 2*x

  ```

  The first form means that the name of the resulting function object is specifically 'f' instead of the generic '<lambda>'. This is more useful for tracebacks and string representations in general. The use of the assignment statement eliminates the sole benefit a lambda expression can offer over an explicit def statement (i.e. that it can be embedded inside a larger expression)

- When a resource is local to a particular section of code, use a `with` statement to ensure it is cleaned up promptly and reliably after use. A try/finally statement is also acceptable.

- Context managers should be invoked through separate functions or methods whenever they do something other than acquire and release resources. For example:

  Yes:

  ```
  with conn.begin_transaction():
      do_stuff_in_transaction(conn)

  ```

  No:

  ```
  with conn:
      do_stuff_in_transaction(conn)

  ```

  The latter example doesn't provide any information to indicate that the `__enter__` and `__exit__` methods are doing something other than closing the connection after a transaction. Being explicit is important in this case.

- Be consistent in return statements. Either all return statements in a function should return an expression, or none of them should. If any return statement returns an expression, any return statements where no value is returned should explicitly state this as `return None`, and an explicit return statement should be present at the end of the function (if reachable).

  Yes:

  ```
  def foo(x):
      if x >= 0:
          return math.sqrt(x)
      else:
          return None

  def bar(x):
      if x < 0:
          return None
      return math.sqrt(x)

  ```

  No:

  ```
  def foo(x):
      if x >= 0:
          return math.sqrt(x)

  def bar(x):
      if x < 0:
          return
      return math.sqrt(x)

  ```

- Use string methods instead of the string module.

  String methods are always much faster and share the same API with unicode strings. Override this rule if backward compatibility with Pythons older than 2.0 is required.

- Use `''.startswith()` and `''.endswith()` instead of string slicing to check for prefixes or suffixes.

  startswith() and endswith() are cleaner and less error prone. For example:

  ```
  Yes: if foo.startswith('bar'):
  No:  if foo[:3] == 'bar':

  ```

- Object type comparisons should always use isinstance() instead of comparing types directly.

  ```
  Yes: if isinstance(obj, int):

  No:  if type(obj) is type(1):

  ```

  When checking if an object is a string, keep in mind that it might be a unicode string too! In Python 2, str and unicode have a common base class, basestring, so you can do:

  ```
  if isinstance(obj, basestring):

  ```

  Note that in Python 3, `unicode` and `basestring` no longer exist (there is only `str`) and a bytes object is no longer a kind of string (it is a sequence of integers instead)

- For sequences, (strings, lists, tuples), use the fact that empty sequences are false.

  ```
  Yes: if not seq:
       if seq:

  No: if len(seq):
      if not len(seq):

  ```

- Don't write string literals that rely on significant trailing whitespace. Such trailing whitespace is visually indistinguishable and some editors (or more recently, reindent.py) will trim them.

- Don't compare boolean values to True or False using `==`.

  ```
  Yes:   if greeting:
  No:    if greeting == True:
  Worse: if greeting is True:
  ```

## Function Annotation

https://www.python.org/dev/peps/pep-0484/

## Variable Annotation



https://www.python.org/dev/peps/pep-0526/

[1]: https://www.python.org/dev/peps/pep-0008/ "Style Guide for Python Code"

[2]: https://barry.warsaw.us/software/STYLEGUIDE.txt "Python coding style guide for GNU Mailman by Barry"

[3]: http://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/ "谷歌开源项目 Python 风格指南"





# http://pythonguidecn.readthedocs.io/zh/latest/writing/style.html

如果您问Python程序员最喜欢Python的什么，他们总会说是Python的高可读性。 事实上，高度的可读性是Python语言的设计核心。这基于这样的事实：代码的 阅读比编写更加频繁。

Python代码具有高可读性的其中一个原因是它的相对完整的代码风格指引和 “Pythonic” 的习语。



# 好的代码风格可以借鉴

推荐阅读代码风格优秀的一些项目

以下是推荐阅读的Python项目。每个项目都是Python代码的典范。

- [Howdoi](https://github.com/gleitz/howdoi) Howdoi是代码搜寻工具，使用Python编写。
- [Flask](https://github.com/mitsuhiko/flask) Flask是基于Werkzeug和Jinja2，使用Python的微框架。它能够快速启动，并且开发意图良好。
- [Diamond](https://github.com/python-diamond/Diamond) Diamond是python的守护进程，它收集指标，并且将他们发布至Graphite或其它后端。 它能够收集cpu,内存，网络，i/o，负载和硬盘指标。除此，它拥有实现自定义收集器的API，该API几乎能 从任何资源中获取指标。
- [Werkzeug](https://github.com/mitsuhiko/werkzeug) Werkzeug起初只是一个WSGI应用多种工具的集成，现在它已经变成非常重要的WSGI实用模型。 它包括强大的调试器，功能齐全的请求和响应对象，处理entity tags的HTTP工具，缓存控制标头，HTTP数据，cookie处理，文件上传，强大的URL路由系统和一些社区提供的插件模块。
- [Requests](https://github.com/kennethreitz/requests) Requests是Apache2许可的HTTP库，使用Python编写。
- [Tablib](https://github.com/kennethreitz/tablib) Tablib是无格式的表格数据集库，使用Python编写。