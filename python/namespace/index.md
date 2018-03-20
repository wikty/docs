

## 显式指定名称空间的语句

### global

The [`global`](https://docs.python.org/3.6/reference/simple_stmts.html#global) statement is a declaration which holds for the entire current code block. It means that the listed identifiers are to be interpreted as globals. It would be impossible to assign to a global variable without [`global`](https://docs.python.org/3.6/reference/simple_stmts.html#global), although free variables may refer to globals without being declared global.

Names listed in a [`global`](https://docs.python.org/3.6/reference/simple_stmts.html#global) statement must not be used in the same code block textually preceding that [`global`](https://docs.python.org/3.6/reference/simple_stmts.html#global) statement.

Names listed in a [`global`](https://docs.python.org/3.6/reference/simple_stmts.html#global) statement must not be defined as formal parameters or in a [`for`](https://docs.python.org/3.6/reference/compound_stmts.html#for) loop control target, [`class`](https://docs.python.org/3.6/reference/compound_stmts.html#class) definition, function definition, [`import`](https://docs.python.org/3.6/reference/simple_stmts.html#import) statement, or variable annotation.

[`global`](https://docs.python.org/3.6/reference/simple_stmts.html#global) is a directive to the parser. It applies only to code parsed at the same time as the [`global`](https://docs.python.org/3.6/reference/simple_stmts.html#global) statement. In particular, a [`global`](https://docs.python.org/3.6/reference/simple_stmts.html#global) statement contained in a string or code object supplied to the built-in [`exec()`](https://docs.python.org/3.6/library/functions.html#exec) function does not affect the code block *containing* the function call, and code contained in such a string is unaffected by [`global`](https://docs.python.org/3.6/reference/simple_stmts.html#global) statements in the code containing the function call. The same applies to the [`eval()`](https://docs.python.org/3.6/library/functions.html#eval) and [`compile()`](https://docs.python.org/3.6/library/functions.html#compile) functions.

## nonlocal

The [`nonlocal`](https://docs.python.org/3.6/reference/simple_stmts.html#nonlocal) statement causes the listed identifiers to refer to previously bound variables in the nearest enclosing scope excluding globals. This is important because the default behavior for binding is to search the local namespace first. The statement allows encapsulated code to rebind variables outside of the local scope besides the global (module) scope.

Names listed in a [`nonlocal`](https://docs.python.org/3.6/reference/simple_stmts.html#nonlocal) statement, unlike those listed in a [`global`](https://docs.python.org/3.6/reference/simple_stmts.html#global) statement, must refer to pre-existing bindings in an enclosing scope (the scope in which a new binding should be created cannot be determined unambiguously).

Names listed in a [`nonlocal`](https://docs.python.org/3.6/reference/simple_stmts.html#nonlocal) statement must not collide with pre-existing bindings in the local scope.

