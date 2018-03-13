When you raise an exception or some function you called raises an exception, that normal code flow terminates and the exception starts propagating up the call stack until it encounters a proper exception handler. If no exception handler is available to handle it, the process (or more accurately the current thread) will be terminated with an unhandled exception message.



https://docs.python.org/3/tutorial/errors.html



https://docs.microsoft.com/en-us/dotnet/standard/exceptions/best-practices-for-exceptions



https://code.tutsplus.com/tutorials/professional-error-handling-with-python--cms-25950



https://eli.thegreenplace.net/2008/08/21/robust-exception-handling/



http://www.ituring.com.cn/article/155



http://www.onjava.com/pub/a/onjava/2003/11/19/exceptions.html



https://raygun.com/blog/errors-and-exceptions/



https://stackoverflow.com/questions/15542608/design-patterns-exception-error-handling