## 简介

Input -> Process -> Output











### stdint stdout stderr



`sys.``stdin`

`sys.``stdout`

`sys.``stderr`

[File objects](https://docs.python.org/3.6/glossary.html#term-file-object) used by the interpreter for standard input, output and errors:

- `stdin` is used for all interactive input (including calls to [`input()`](https://docs.python.org/3.6/library/functions.html#input));
- `stdout` is used for the output of [`print()`](https://docs.python.org/3.6/library/functions.html#print) and [expression](https://docs.python.org/3.6/glossary.html#term-expression) statements and for the prompts of [`input()`](https://docs.python.org/3.6/library/functions.html#input);
- The interpreter’s own prompts and its error messages go to `stderr`.

These streams are regular [text files](https://docs.python.org/3.6/glossary.html#term-text-file) like those returned by the [`open()`](https://docs.python.org/3.6/library/functions.html#open) function. Their parameters are chosen as follows:

- The character encoding is platform-dependent. Under Windows, if the stream is interactive (that is, if its `isatty()` method returns `True`), the console codepage is used, otherwise the ANSI code page. Under other platforms, the locale encoding is used (see [`locale.getpreferredencoding()`](https://docs.python.org/3.6/library/locale.html#locale.getpreferredencoding)).

  Under all platforms though, you can override this value by setting the [`PYTHONIOENCODING`](https://docs.python.org/3.6/using/cmdline.html#envvar-PYTHONIOENCODING) environment variable before starting Python.

- When interactive, standard streams are line-buffered. Otherwise, they are block-buffered like regular text files. You can override this value with the [`-u`](https://docs.python.org/3.6/using/cmdline.html#cmdoption-u) command-line option.

Note

 

To write or read binary data from/to the standard streams, use the underlying binary [`buffer`](https://docs.python.org/3.6/library/io.html#io.TextIOBase.buffer) object. For example, to write bytes to [`stdout`](https://docs.python.org/3.6/library/sys.html#sys.stdout), use `sys.stdout.buffer.write(b'abc')`.

However, if you are writing a library (and do not control in which context its code will be executed), be aware that the standard streams may be replaced with file-like objects like [`io.StringIO`](https://docs.python.org/3.6/library/io.html#io.StringIO) which do not support the `buffer` attribute.



### text output formatting

There are ways to format your output;

* the first way is to do all the string handling yourself; using string slicing and concatenation operations you can create any layout you can imagine. The string type has some methods that perform useful operations for padding strings to a given column width; these will be discussed shortly. 比如：`str.zjust()`, `str.center()` 等
* The second way is to use [formatted string literals](https://docs.python.org/3/reference/lexical_analysis.html#f-strings), or the [`str.format()`](https://docs.python.org/3/library/stdtypes.html#str.format) method.
* The [`string`](https://docs.python.org/3/library/string.html#module-string) module contains a [`Template`](https://docs.python.org/3/library/string.html#string.Template) class which offers yet another way to substitute values into strings.

`str.format` 用法

```
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print('{1} and {0}'.format('spam', 'eggs'))
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
```

`'!a'` (apply [`ascii()`](https://docs.python.org/3/library/functions.html#ascii)), `'!s'` (apply [`str()`](https://docs.python.org/3/library/stdtypes.html#str)) and `'!r'` (apply [`repr()`](https://docs.python.org/3/library/functions.html#repr)) can be used to convert the value before it is formatted

```
print('My hovercraft is full of {!r}.'.format(contents))
```

An optional `':'` and format specifier can follow the field name. This allows greater control over how the value is formatted. Passing an integer after the `':'` will cause that field to be a minimum number of characters wide.

```
print('The value of PI is approximately {0:.3f}.'.format(math.pi))
```

For a complete overview of string formatting with [`str.format()`](https://docs.python.org/3/library/stdtypes.html#str.format), see [Format String Syntax](https://docs.python.org/3/library/string.html#formatstrings).

字符串格式化的老式风格

```
print('The value of PI is approximately %5.3f.' % math.pi)
```

More information can be found in the [printf-style String Formatting](https://docs.python.org/3/library/stdtypes.html#old-string-formatting) section.



## File Input and Output



### mode

*mode* can be `'r'` when the file will only be read, `'w'` for only writing (an existing file with the same name will be erased), and `'a'`opens the file for appending; any data written to the file is automatically added to the end. `'r+'` opens the file for both reading and writing.

In text mode, the default when reading is to convert platform-specific line endings (`\n` on Unix, `\r\n` on Windows) to just `\n`. When writing in text mode, the default is to convert occurrences of `\n` back to platform-specific line endings. This behind-the-scenes modification to file data is fine for text files, but will corrupt binary data like that in `JPEG` or `EXE` files. Be very careful to use binary mode when reading and writing such files.



### with statement

It is good practice to use the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) keyword when dealing with file objects. The advantage is that the file is properly closed after its suite finishes, even if an exception is raised at some point. Using [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) is also much shorter than writing equivalent [`try`](https://docs.python.org/3/reference/compound_stmts.html#try)-[`finally`](https://docs.python.org/3/reference/compound_stmts.html#finally) blocks:

### api

To read a file’s contents, call `f.read(size)`, which reads some quantity of data and returns it as a string (in text mode) or bytes object (in binary mode).*size* is an optional numeric argument. When *size* is omitted or negative, the entire contents of the file will be read and returned; it’s your problem if the file is twice as large as your machine’s memory. Otherwise, at most *size* bytes are read and returned. If the end of the file has been reached, `f.read()`will return an empty string (`''`).

`f.readline()` reads a single line from the file; a newline character (`\n`) is left at the end of the string, and is only omitted on the last line of the file if the file doesn’t end in a newline. 

If you want to read all the lines of a file in a list you can also use `list(f)` or `f.readlines()`.

`f.write(string)` writes the contents of *string* to the file, returning the number of characters written. Other types of objects need to be converted – either to a string (in text mode) or a bytes object (in binary mode) – before writing them

`f.tell()` returns an integer giving the file object’s current position in the file represented as number of bytes from the beginning of the file when in binary mode and an opaque number when in text mode.

To change the file object’s position, use `f.seek(offset, from_what)`. The position is computed from adding *offset* to a reference point; the reference point is selected by the *from_what* argument. A *from_what* value of 0 measures from the beginning of the file, 1 uses the current file position, and 2 uses the end of the file as the reference point. *from_what* can be omitted and defaults to 0, using the beginning of the file as the reference point.

### binary mode

bytes data -> writer -> file

bytes data <- reader -> file

### text mode

text data -> encoder -> writer -> file

text data <- decoder <- reader <- file







