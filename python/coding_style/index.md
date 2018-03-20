---
title: Python Coding Style
---

## 简介

dfd[^1]

This document and [PEP 257](https://www.python.org/dev/peps/pep-0257) (Docstring Conventions) were adapted from Guido's original Python Style Guide essay, with some additions from Barry's style guide [[2\]](https://www.python.org/dev/peps/pep-0008/#id9).

Many projects have their own coding style guidelines. In the event of any conflicts, such project-specific guides take precedence for that project.

One of Guido's key insights is that code is read much more often than it is written. The guidelines provided here are intended to improve the readability of code and make it consistent across the wide spectrum of Python code.

A style guide is about consistency. Consistency with this style guide is important. Consistency within a project is more important. Consistency within one module or function is the most important.

However, know when to be inconsistent -- sometimes style guide recommendations just aren't applicable. When in doubt, use your best judgment. Look at other examples and decide what looks best. And don't hesitate to ask!

In particular: do not break backwards compatibility just to comply with this PEP!

Some other good reasons to ignore a particular guideline:

1. When applying the guideline would make the code less readable, even for someone who is used to reading code that follows this PEP.
2. To be consistent with surrounding code that also breaks it (maybe for historic reasons) -- although this is also an opportunity to clean up someone else's mess (in true XP style).
3. Because the code in question predates the introduction of the guideline and there is no other reason to be modifying that code.
4. When the code needs to remain compatible with older versions of Python that don't support the feature recommended by the style guide.

## 代码排版



## 字符串引号



## 表达式空白



## 结尾逗号



## 注释



## 命名



## 编程





## 参考文献

[^1]: [Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

<a name="@ref1"></a>1. [Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

[Python coding style guide for GNU Mailman](https://barry.warsaw.us/software/STYLEGUIDE.txt)



http://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/