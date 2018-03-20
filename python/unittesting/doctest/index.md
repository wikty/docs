---
title: Python doctest
date: 2017/09/08
---

## 简介

[doctest][1] 是一个用于单元测试的 Python 标准库模块。该模块会查找代码中的文档字符串，从中找到 Python 命令行交互代码来作为测试用例，并且会对测试用例运行结果和文档字符串中的结果进行比较。

## 样例

```python
def square(x):
    """Return the square of x.

    >>> square(2)
    4
    >>> square(-2)
    4
    """

    return x * x

if __name__ == '__main__':
    import doctest
    doctest.testmod()
```

将以上代码保存在 `test.py` 后，执行 `python test.py` 就可以运行文档字符串中的测试用例了。运行后，并没有任何输出，则说明测试用例全部通过，要想输出详细的测试日志，运行命令 `python test.py -v`。

除了上面的方式外，还可以直接调用 doctest 模块来运行测试用例：将样例代码中的 `__main__` 部分的代码删除，运行命令 `python -m doctest test.py -v`。

## 测试用例

测试用例语法

测试用例混杂在文档字符串中，doctest 从文档字符串中提取这些测试用例，其实是遵从一定规则的：以 Python 交互提示符 `>>>` 开头的文本行被视为一个测试用例；测试用例的结束以空白行或者下一个以 `>>>` 开头的文本行标识。

测试用例编写

文档字符串中的测试用例，并不需要手动编写。一般都是开发者在 Python 交互环境下对程序进行测试时，直接从命令行中复制过来的。





## 单独保存测试用例









[1]: https://docs.python.org/3.5/library/doctest.html	"doctest"

### Doctest

The [`doctest`](http://docs.python.org/library/doctest.html#module-doctest) module searches for pieces of text that look like interactive Python sessions in docstrings, and then executes those sessions to verify that they work exactly as shown.

A simple doctest in a function:

```

```

When running this module from the command line as in `python module.py`, the doctests will run and complain if anything is not behaving as described in the docstrings.

