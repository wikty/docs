When you raise an exception or some function you called raises an exception, that normal code flow terminates and the exception starts propagating up the call stack until it encounters a proper exception handler. If no exception handler is available to handle it, the process (or more accurately the current thread) will be terminated with an unhandled exception message.







https://docs.microsoft.com/en-us/dotnet/standard/exceptions/best-practices-for-exceptions



https://code.tutsplus.com/tutorials/professional-error-handling-with-python--cms-25950



https://eli.thegreenplace.net/2008/08/21/robust-exception-handling/



https://raygun.com/blog/errors-and-exceptions/



https://stackoverflow.com/questions/15542608/design-patterns-exception-error-handling



https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python/24065533#24065533



*  philosophy

  Give a chance to handle the error before program crash

* errno vs. exception

  interrupt the execution flow

* exception hierarchy

  tree hierarchy https://docs.python.org/3/library/exceptions.html#exception-hierarchy

  https://stackoverflow.com/questions/18296653/print-the-python-exception-error-hierarchy

* raise exception

  https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement

* assert

  https://docs.python.org/3/reference/simple_stmts.html#assert

* catch exception

* finally

  cleanup job

* logging

* best practices for exception

* ​







## 简介

程序运行时，一定会有预料之外的情况，比如像系统请求内存失败、网络服务器无响应等。遇到这些意外情况时该如何处理呢？程序崩溃掉或给用户友好的提示，怎样的处理才够优雅呢？

许多编程语言提供了异常机制，其目的就在于，给了程序一次从致命错误中恢复的机会。这个恢复可能是简单的打印错误信息，或将错误记录在日志中，又或者以优雅的方式来终止程序。

Errors detected during execution are called *exceptions* and are not unconditionally fatal: you will soon learn how to handle them in Python programs



## 语法结构

A [`try`](https://docs.python.org/3.6/reference/compound_stmts.html#try) statement may have more than one except clause, to specify handlers for different exceptions. At most one handler will be executed. Handlers only handle exceptions that occur in the corresponding try clause, not in other handlers of the same [`try`](https://docs.python.org/3.6/reference/compound_stmts.html#try) statement. An except clause may name multiple exceptions as a parenthesized tuple, for example:

```
... except (RuntimeError, TypeError, NameError):
...     pass
```

A class in an [`except`](https://docs.python.org/3.6/reference/compound_stmts.html#except) clause is compatible with an exception if it is the same class or a base class

The last except clause may omit the exception name(s), to serve as a wildcard. Use this with extreme caution, since it is easy to mask a real programming error in this way! It can also be used to print an error message and then re-raise the exception (allowing a caller to handle the exception as well):

```
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
```

The [`try`](https://docs.python.org/3.6/reference/compound_stmts.html#try) … [`except`](https://docs.python.org/3.6/reference/compound_stmts.html#except) statement has an optional *else clause*, which, when present, must follow all except clauses. It is useful for code that must be executed if the try clause does not raise an exception. 

The use of the [`else`](https://docs.python.org/3.6/reference/compound_stmts.html#else) clause is better than adding additional code to the [`try`](https://docs.python.org/3.6/reference/compound_stmts.html#try) clause because it avoids accidentally catching an exception that wasn’t raised by the code being protected by the [`try`](https://docs.python.org/3.6/reference/compound_stmts.html#try) … [`except`](https://docs.python.org/3.6/reference/compound_stmts.html#except) statement.

When an exception occurs, it may have an associated value, also known as the exception’s *argument*. The presence and type of the argument depend on the exception type.

The except clause may specify a variable after the exception name. The variable is bound to an exception instance with the arguments stored in`instance.args`. For convenience, the exception instance defines [`__str__()`](https://docs.python.org/3.6/reference/datamodel.html#object.__str__) so the arguments can be printed directly without having to reference `.args`



### try

可能错问题的业务代码

### except

The [`except`](https://docs.python.org/3.6/reference/compound_stmts.html#except) clause(s) specify one or more exception handlers. When no exception occurs in the [`try`](https://docs.python.org/3.6/reference/compound_stmts.html#try) clause, no exception handler is executed. When an exception occurs in the [`try`](https://docs.python.org/3.6/reference/compound_stmts.html#try) suite, a search for an exception handler is started. This search inspects the except clauses in turn until one is found that matches the exception. An expression-less except clause, if present, must be last; it matches any exception. For an except clause with an expression, that expression is evaluated, and the clause matches the exception if the resulting object is “compatible” with the exception. An object is compatible with an exception if it is the class or a base class of the exception object or a tuple containing an item compatible with the exception.

If no except clause matches the exception, the search for an exception handler continues in the surrounding code and on the invocation stack

If the evaluation of an expression in the header of an except clause raises an exception, the original search for a handler is canceled and a search starts for the new exception in the surrounding code and on the call stack

When a matching except clause is found, the exception is assigned to the target specified after the [`as`](https://docs.python.org/3.6/reference/compound_stmts.html#as) keyword in that except clause, if present, and the except clause’s suite is executed. All except clauses must have an executable block. When the end of this block is reached, execution continues normally after the entire try statement

Before an except clause’s suite is executed, details about the exception are stored in the [`sys`](https://docs.python.org/3.6/library/sys.html#module-sys) module and can be accessed via [`sys.exc_info()`](https://docs.python.org/3.6/library/sys.html#sys.exc_info).[`sys.exc_info()`](https://docs.python.org/3.6/library/sys.html#sys.exc_info) returns a 3-tuple consisting of the exception class, the exception instance and a traceback object (see section [The standard type hierarchy](https://docs.python.org/3.6/reference/datamodel.html#types)) identifying the point in the program where the exception occurred. [`sys.exc_info()`](https://docs.python.org/3.6/library/sys.html#sys.exc_info) values are restored to their previous values (before the call) when returning from a function that handled an exception.

### else

The optional [`else`](https://docs.python.org/3.6/reference/compound_stmts.html#else) clause is executed if and when control flows off the end of the [`try`](https://docs.python.org/3.6/reference/compound_stmts.html#try) clause. [[2\]](https://docs.python.org/3.6/reference/compound_stmts.html#id6) Exceptions in the [`else`](https://docs.python.org/3.6/reference/compound_stmts.html#else) clause are not handled by the preceding [`except`](https://docs.python.org/3.6/reference/compound_stmts.html#except) clauses.

### finally

If [`finally`](https://docs.python.org/3.6/reference/compound_stmts.html#finally) is present, it specifies a ‘cleanup’ handler. The [`try`](https://docs.python.org/3.6/reference/compound_stmts.html#try) clause is executed, including any [`except`](https://docs.python.org/3.6/reference/compound_stmts.html#except) and [`else`](https://docs.python.org/3.6/reference/compound_stmts.html#else) clauses. If an exception occurs in any of the clauses and is not handled, the exception is temporarily saved. The [`finally`](https://docs.python.org/3.6/reference/compound_stmts.html#finally) clause is executed. If there is a saved exception it is re-raised at the end of the [`finally`](https://docs.python.org/3.6/reference/compound_stmts.html#finally) clause. If the [`finally`](https://docs.python.org/3.6/reference/compound_stmts.html#finally) clause raises another exception, the saved exception is set as the context of the new exception.

The exception information is not available to the program during execution of the [`finally`](https://docs.python.org/3.6/reference/compound_stmts.html#finally) clause.

The return value of a function is determined by the last [`return`](https://docs.python.org/3.6/reference/simple_stmts.html#return) statement executed. Since the [`finally`](https://docs.python.org/3.6/reference/compound_stmts.html#finally) clause always executes, a [`return`](https://docs.python.org/3.6/reference/simple_stmts.html#return) statement executed in the [`finally`](https://docs.python.org/3.6/reference/compound_stmts.html#finally) clause will always be the last one executed:

```
>>> def foo():
...     try:
...         return 'try'
...     finally:
...         return 'finally'
...
>>> foo()
'finally'
```



## 抛出异常

允许开发者将业务逻辑错误交由上层处理。

The [`raise`](https://docs.python.org/3.6/reference/simple_stmts.html#raise) statement allows the programmer to force a specified exception to occur.

`raise` 语句的用法

The sole argument to [`raise`](https://docs.python.org/3.6/reference/simple_stmts.html#raise) indicates the exception to be raised. This must be either an exception instance or an exception class (a class that derives from [`Exception`](https://docs.python.org/3.6/library/exceptions.html#Exception)). If an exception class is passed, it will be implicitly instantiated by calling its constructor with no arguments:

```
raise ValueError  # shorthand for 'raise ValueError()'
```

重新抛出异常：只检测是否发生了异常，不对异常处理，重新抛出它让上层来处理

If you need to determine whether an exception was raised but don’t intend to handle it, a simpler form of the [`raise`](https://docs.python.org/3.6/reference/simple_stmts.html#raise) statement allows you to re-raise the exception:

```
>>> try:
...     raise NameError('HiThere')
... except NameError:
...     print('An exception flew by!')
...     raise
```

`raise` 用法

无参数，重新抛出：

If no expressions are present, [`raise`](https://docs.python.org/3.6/reference/simple_stmts.html#raise) re-raises the last exception that was active in the current scope. If no exception is active in the current scope, a [`RuntimeError`](https://docs.python.org/3.6/library/exceptions.html#RuntimeError) exception is raised indicating that this is an error.

raise expression，常见的抛出方式：

 [`raise`](https://docs.python.org/3.6/reference/simple_stmts.html#raise) evaluates the first expression as the exception object. It must be either a subclass or an instance of [`BaseException`](https://docs.python.org/3.6/library/exceptions.html#BaseException). If it is a class, the exception instance will be obtained when needed by instantiating the class with no arguments.

raise expression from expression，指定异常链：

The `from` clause is used for exception chaining: if given, the second *expression* must be another exception class or instance, which will then be attached to the raised exception as the `__cause__` attribute (which is writable). If the raised exception is not handled, both exceptions will be printed:

```
>>> try:
...     print(1 / 0)
... except Exception as exc:
...     raise RuntimeError("Something bad happened") from exc
```

或者通过将 `exc` 替换为 `None` 来强制关闭异常链

## 处理异常

异常抛出者负责为错误的发生提供详细的信息，即异常参数。

异常处理者需要尽量从该错误中恢复出来，或者将错误记录在日志中，再或者交由上层调用来处理。

except 和 finally 中处理异常时或清理工作时，如果引发新的异常的话，the previous exception is then attached as the new exception’s `__context__` attribute:

```
>>> try:
...     print(1 / 0)
... except:
...     raise RuntimeError("Something bad happened")
```

## 清理工作

The [`try`](https://docs.python.org/3.6/reference/compound_stmts.html#try) statement has another optional clause which is intended to define clean-up actions that must be executed under all circumstances.

不管怎样都会执行的 `finally` 语句块

A *finally clause* is always executed before leaving the [`try`](https://docs.python.org/3.6/reference/compound_stmts.html#try) statement, whether an exception has occurred or not. When an exception has occurred in the [`try`](https://docs.python.org/3.6/reference/compound_stmts.html#try) clause and has not been handled by an [`except`](https://docs.python.org/3.6/reference/compound_stmts.html#except) clause (or it has occurred in an [`except`](https://docs.python.org/3.6/reference/compound_stmts.html#except) or [`else`](https://docs.python.org/3.6/reference/compound_stmts.html#else) clause), it is re-raised after the [`finally`](https://docs.python.org/3.6/reference/compound_stmts.html#finally) clause has been executed. The [`finally`](https://docs.python.org/3.6/reference/compound_stmts.html#finally) clause is also executed “on the way out” when any other clause of the [`try`](https://docs.python.org/3.6/reference/compound_stmts.html#try) statement is left via a [`break`](https://docs.python.org/3.6/reference/simple_stmts.html#break), [`continue`](https://docs.python.org/3.6/reference/simple_stmts.html#continue) or [`return`](https://docs.python.org/3.6/reference/simple_stmts.html#return) statement.

In real world applications, the [`finally`](https://docs.python.org/3.6/reference/compound_stmts.html#finally) clause is useful for releasing external resources (such as files or network connections), regardless of whether the use of the resource was successful.

对于预先定了清理行为的对象，优先使用 `with` 语句块

Some objects define standard clean-up actions to be undertaken when the object is no longer needed, regardless of whether or not the operation using the object succeeded or failed. The [`with`](https://docs.python.org/3.6/reference/compound_stmts.html#with) statement allows objects like files to be used in a way that ensures they are always cleaned up promptly and correctly.

```
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")

```

After the statement is executed, the file *f* is always closed, even if a problem was encountered while processing the lines. Objects which, like files, provide predefined clean-up actions will indicate this in their documentation.

## 自定义异常

异常类尽量简洁

Exception classes can be defined which do anything any other class can do, but are usually kept simple, often only offering a number of attributes that allow information about the error to be extracted by handlers for the exception. 

异常类的层级继承结构

Programs may name their own exceptions by creating a new exception class (see [Classes](https://docs.python.org/3.6/tutorial/classes.html#tut-classes) for more about Python classes). Exceptions should typically be derived from the [`Exception`](https://docs.python.org/3.6/library/exceptions.html#Exception) class, either directly or indirectly.

When creating a module that can raise several distinct errors, a common practice is to create a base class for exceptions defined by that module, and subclass that to create specific exception classes for different error conditions

异常类的命名约定

Most exceptions are defined with names that end in “Error,” similar to the naming of the standard exceptions.

Many standard modules define their own exceptions to report errors that may occur in functions they define



## 内置异常类型

https://docs.python.org/2/library/exceptions.html#bltin-exceptions



## 异常处理最佳实践

* 不要使用异常来管理程序的业务逻辑。异常中断程序正常执行流，将业务逻辑混杂于异常处理中，降低了程序的可读性。
* 异常的类名要有意义，可以反映出引起异常的原因。
* 优先使用异常，而不是以返回值的形式来返回错误代码。
* 优先捕获更加具体的异常类型。捕获抽象的异常类型可能会隐藏程序中潜在的问题。
* 根据具体的业务场景来自定义异常的层级继承结构。
* 根据程序是否可以从异常中恢复，将异常分为以下几种：Fatal: System crash states. Error: Lack of requirement. Warn: Not an error but error probability. Info: Info for user. Debug: Info for developer.
* 不要吞噬异常，也即捕获了异常却不做任何的处理。这样会给以后的程序维护带来很多麻烦。
* 不要对同一异常记录多次日志。
* 一定不要忘记在 `finally` 语句块中释放之前打开的资源。
* 一般来说，不要在循环体中处理异常，而应该将循环体整个包含到异常处理块中。
* 要注意 try-except-finally 语句块处理异常的粒度。一个异常处理语句块中最好只处理一个业务逻辑操作，不要把所有业务执行操作都塞进一个异常处理中。
* 可以考虑为异常定义代码。
* 优先使用 `with` 语句块打开文件、套接字等资源，而不是自己用  try-except-finally 来管理这些资源的异常。这样可以免去资源的手动释放。
* 如果一个业务操作很难拆分，那么应该将可能出现异常的部分放在 try 语句块中，剩余逻辑放在 else 语句块中。
* 自定义的异常类，最好实现 `__str__()` 方法，来体现异常接收到的参数，而不是通过引用异常属性 `args` 来访问这些参数。
* ​





## 参考资料

1. http://codebuild.blogspot.com/2012/01/15-best-practices-about-exception.html
2. https://docs.python.org/3.6/tutorial/errors.html
3. http://www.onjava.com/pub/a/onjava/2003/11/19/exceptions.html
4. ​