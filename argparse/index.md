## Introduction

The [`argparse`](https://docs.python.org/3/library/argparse.html#module-argparse) module makes it easy to write user-friendly command-line interfaces. The program defines what arguments it requires, and [`argparse`](https://docs.python.org/3/library/argparse.html#module-argparse) will figure out how to parse those out of [`sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv). The [`argparse`](https://docs.python.org/3/library/argparse.html#module-argparse) module also automatically generates help and usage messages and issues errors when users give the program invalid arguments.

## Example

```

```

## Usage

1. Creating a parser
2. Adding arguments
3. Parsing command line arguments into a object

## Creating A Parser

### ArgumentParser Object's Parameters

* `prog` -  The name of the program (default: `sys.argv[0]`)
* `usage` - The string describing the program usage (default: generated from arguments added to parser)
* `description` - Text to display before the argument help (default: none)
* `epilog` - Text to display after the argument help (default: none)
* `parents` -  A list of [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser) objects whose arguments should also be included
* `prefix_chars` - The set of characters that prefix optional arguments (default: `-`)
* `fromfile_prefix_chars` - The set of characters that prefix files(default: none)
* `add_help` - Add a `-h/--help` option to the parser (default: `True`)
* `default_argument` - The global default value for all of arguments (default: `None`)

Default help/ message generated from arguments added to parser:

```
usage string, e.g., usage: prog [flags] arguments

description, a brief of what the program does and how it works

positional arguments, a list of positional arguments' usage and help string

optional arguments, a list of optional arguments' usage and help string

epilog, display additional description of the program after the arguments usage
```



#### prog

By default, [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser) objects use `sys.argv[0]` to determine how to display the name of the program in help messages. 

To change this default behavior, another value can be supplied using the `prog=` argument to [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser).

Note that the program name, whether determined from `sys.argv[0]` or from the `prog=` argument, is available to help messages using the `%(prog)s` format specifier.

#### usage

By default, [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser) calculates the usage message from the arguments it contains. The default message can be overridden with the `usage=` keyword parameter.

#### description

Most calls to the [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser) constructor will use the `description=` keyword argument. This argument gives a brief description of what the program does and how it works.

#### parents

Sometimes, several parsers share a common set of arguments. Rather than repeating the definitions of these arguments, a single parser with all the shared arguments and passed to `parents=` argument to [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser)can be used.

#### prefix_chars

Most command-line options will use `-` as the prefix, e.g. `-f/--foo`. Parsers that need to support different or additional prefix characters, e.g. for options like `+f` or `/foo`, may specify them using the `prefix_chars=` argument.

#### fromfile_prefix_chars

Sometimes, for example when dealing with a particularly long argument lists, it may make sense to keep the list of arguments in a file rather than typing it out at the command line. If the `fromfile_prefix_chars=` argument is given to the [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser) constructor, then arguments that start with any of the specified characters will be treated as files

[More](https://docs.python.org/3/library/argparse.html#fromfile-prefix-chars)

#### add_help

By default, ArgumentParser objects add an option which simply displays the parser’s help message. If `-h` or `--help` is supplied at the command line, the ArgumentParser help will be printed.

Occasionally, it may be useful to disable the addition of this help option. This can be achieved by passing `False`as the `add_help=` argument to [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser)

### Example



## Adding Arguments

### ArgumentParser.add_argument()'s parameters

* name or flags - Either a name or a list of option strings, e.g. `foo` or `-f, --foo`.
* action - The basic type of action to be taken when this argument is encountered at the command line.
* nargs - The number of command-line arguments that should be consumed.
* const - A constant value required by some [action](https://docs.python.org/3/library/argparse.html#action) and [nargs](https://docs.python.org/3/library/argparse.html#nargs) selections.
* default - The value produced if the argument is absent from the command line.
* type - The type to which the command-line argument should be converted.
* choices - A container of the allowable values for the argument.
* required - Whether or not the command-line option may be omitted (optionals only).
* help - A brief description of what the argument does.
* metavar -  A name for the argument in usage messages.
* dest - The name of the attribute to be added to the object returned by [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args).

#### name or flags

The argument must be an optional/flag, like `-f` or `--foo`, or a positional, like a list of filenames. So the first parameter for `add_argument()` must therefore be either a series of flags, or a simple argument name.

What difference between position argument and optional argument?

#### action

The `action` keyword argument specifies how the command-line arguments should be handled. The supplied actions are:

* `store` - This just stores the argument’s value. This is the default action.
* `store_const` - This stores the value specified by the [const](https://docs.python.org/3/library/argparse.html#const) keyword argument.
* `store_true` and `store_false` - These are special cases of `'store_const'` used for storing the values `True` and `False` respectively.
* `append` - This stores a list, and appends each argument value to the list. t. This is useful to allow an option to be specified multiple times.
* `append_cons` - This stores a list, and appends the value specified by the [const](https://docs.python.org/3/library/argparse.html#const) keyword argument to the list.
* `count` - This counts the number of times a keyword argument occurs.
* `version` - This expects a `version=` keyword argument in the [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument) call, and prints version information and exits when invoked

You can custom a Action subclass.

#### nargs

The `nargs` keyword argument associates a different number of command-line arguments with a single action.

If the `nargs` keyword argument is not provided, the number of arguments consumed is determined by the [action](https://docs.python.org/3/library/argparse.html#action). Generally this means a single command-line argument will be consumed and a single item (not a list) will be produced.

* `N` (an integer) - `N` arguments from the command line will be gathered together into a list.

* `?` - If the argument present and then produce as a single item, else the value from `default` wil be taked. For optional arguments, more complex

  ```
  >>> parser = argparse.ArgumentParser()
  >>> parser.add_argument('--foo', nargs='?', const='c', default='d')
  >>> parser.add_argument('bar', nargs='?', default='d')
  >>> parser.parse_args(['XX', '--foo', 'YY'])
  Namespace(bar='XX', foo='YY')
  >>> parser.parse_args(['XX', '--foo'])
  Namespace(bar='XX', foo='c')
  >>> parser.parse_args([])
  Namespace(bar='d', foo='d')
  ```

* `*` - All command-line arguments present are gathered into a list. Note that it generally doesn’t make much sense to have more than one positional argument with `nargs='*'`, but multiple optional arguments with `nargs='*'` is possible.

  ```
  >>> parser = argparse.ArgumentParser()
  >>> parser.add_argument('--foo', nargs='*')
  >>> parser.add_argument('--bar', nargs='*')
  >>> parser.add_argument('baz', nargs='*')
  >>> parser.parse_args('a b --foo x y --bar 1 2'.split())
  Namespace(bar=['1', '2'], baz=['a', 'b'], foo=['x', 'y'])
  ```

* `+` - Just like `'*'`, all command-line args present are gathered into a list. Additionally, an error message will be generated if there wasn’t at least one command-line argument present.

* `argparse.REMAINDER` - All the remaining command-line arguments are gathered into a list. This is commonly useful for command line utilities that dispatch to other command line utilities

#### const

The `const` argument of [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument) is used to hold constant values that are not read from the command line but are required for the various [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser) actions. The two most common uses of it are:

* When [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument) is called with `action='store_const'` or `action='append_const'`. With the `'store_const'` and `'append_const'` actions, the `const` keyword argument must be given.
* When [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument) is called with option strings (like `-f` or `--foo`) and `nargs='?'`. This creates an optional argument that can be followed by zero or one command-line arguments. When parsing the command line, if the option string is encountered with no command-line argument following it, the value of `const` will be assumed instead

#### default

All optional arguments and some positional arguments may be omitted at the command line. The `default`keyword argument of [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument), whose value defaults to `None`, specifies what value should be used if the command-line argument is not present. 

If the `default` value is a string, the parser parses the value as if it were a command-line argument. In particular, the parser applies any [type](https://docs.python.org/3/library/argparse.html#type) conversion argument, if provided

For optional arguments, the `default` value is used when the option string was not present at the command line.

For positional arguments with [nargs](https://docs.python.org/3/library/argparse.html#nargs) equal to `?` or `*`, the `default` value is used when no command-line argument was present.

Providing `default=argparse.SUPPRESS` causes no attribute to be added if the command-line argument was not present.

#### type

By default, [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser) objects read command-line arguments in as simple strings. However, quite often the command-line string should instead be interpreted as another type, like a [`float`](https://docs.python.org/3/library/functions.html#float) or [`int`](https://docs.python.org/3/library/functions.html#int).

To ease the use of various types of files, the argparse module provides the factory FileType which takes the `mode=`, `bufsize=`, `encoding=` and `errors=` arguments of the [`open()`](https://docs.python.org/3/library/functions.html#open) function. For example, `FileType('w')` can be used to create a writable file.

`type=` can take any callable that takes a single string argument and returns the converted value.

#### choices

Some command-line arguments should be selected from a restricted set of values. These can be handled by passing a container object as the *choices* keyword argument to [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument). When the command line is parsed, argument values will be checked, and an error message will be displayed if the argument was not one of the acceptable values.

Any object that supports the `in` operator can be passed as the *choices* value, so [`dict`](https://docs.python.org/3/library/stdtypes.html#dict) objects, [`set`](https://docs.python.org/3/library/stdtypes.html#set) objects, custom containers, etc. are all supported.

#### required

In general, the [`argparse`](https://docs.python.org/3/library/argparse.html#module-argparse) module assumes that flags like `-f` and `--bar` indicate *optional* arguments, which can always be omitted at the command line. To make an option *required*, `True` can be specified for the `required=`keyword argument to [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument)

#### help

The `help` value is a string containing a brief description of the argument. 

The `help` strings can include various format specifiers to avoid repetition of things like the program name or the argument [default](https://docs.python.org/3/library/argparse.html#default). The available specifiers include the program name, `%(prog)s` and most keyword arguments to[`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument), e.g. `%(default)s`, `%(type)s`, etc. As the help string supports %-formatting, if you want a literal `%` to appear in the help string, you must escape it as `%%`.

[`argparse`](https://docs.python.org/3/library/argparse.html#module-argparse) supports silencing the help entry for certain options, by setting the `help` value to `argparse.SUPPRESS`

#### metavar

When [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser) generates help messages, it needs some way to refer to each expected argument. By default, ArgumentParser objects use the [dest](https://docs.python.org/3/library/argparse.html#dest) value as the “name” of each object. By default, for positional argument actions, the [dest](https://docs.python.org/3/library/argparse.html#dest) value is used directly, and for optional argument actions, the [dest](https://docs.python.org/3/library/argparse.html#dest) value is uppercased. 

An alternative name can be specified with `metavar`. Note that `metavar` only changes the *displayed* name - the name of the attribute on the [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args) object is still determined by the [dest](https://docs.python.org/3/library/argparse.html#dest) value.

Different values of `nargs` may cause the metavar to be used multiple times. Providing a tuple to `metavar` specifies a different display for each of the arguments

#### dest

Most [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser) actions add some value as an attribute of the object returned by [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args). The name of this attribute is determined by the `dest` keyword argument of [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument). For positional argument actions,`dest` is normally supplied as the first argument to [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument). 

For optional argument actions, the value of `dest` is normally inferred from the option strings. [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser)generates the value of `dest` by taking the first long option string and stripping away the initial `--` string. If no long option strings were supplied, `dest` will be derived from the first short option string by stripping the initial `-`character. Any internal `-` characters will be converted to `_` characters to make sure the string is a valid attribute name.



## Parsing Arguments

Convert argument strings to objects and assign them as attributes of the namespace. Return the populated namespace.

Interface:

```
parse_args(args=None, namespace=None)
```

* args - List of strings to parse. The default is taken from [`sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv).
* namespace - An object to take the attributes. The default is a new empty [`Namespace`](https://docs.python.org/3/library/argparse.html#argparse.Namespace) object.

Sometimes it may be useful to have an ArgumentParser parse arguments other than those of [`sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv). This can be accomplished by passing a list of strings to [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args). This is useful for testing at the interactive prompt.

## How to use

### option value syntax

The [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args) method supports several ways of specifying the value of an option if it takes one.

1. the option and its value are passed as two separate arguments

   ```
   -f FOO
   -foo FOO
   ```

2. For long options, the option and value can also be passed as a single command-line argument, using `=` to separate them

   ```
   --foo=FOO
   ```

3. For short options, the option and its value can be concatenated.

   ```
   -fFOO
   ```

4. Several short options can be joined together, using only a single `-` prefix, as long as only the last option (or none of them) requires a value

   ```
   # x and y are optional args. z is a position argument.
   -xyzZOO
   ```



