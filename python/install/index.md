## 不同版本的Python 解释器 

### CPython[¶](http://pythonguidecn.readthedocs.io/zh/latest/starting/which-python.html#cpython)

[CPython](http://www.python.org/) 是Python的参考实现，用C编写。它把Python代码编译成 中间态的字节码，然后由虚拟机解释。CPython为Python包和C扩展模块提供了最大限度的兼容。

### PyPy

[PyPy](http://pypy.org/) 是用RPython实现的解释器。RPython是Python的子集， 具有静态类型。这个解释器的特点是即时编译，支持多重后端（C, CLI, JVM）。

PyPy旨在提高性能，同时保持最大兼容性（参考CPython的实现）。

如果您正在寻找提高您的Python代码性能的方法，值得试一试PyPy。在一套的基准测试下， 它目前比CPython的速度快超过5倍 。

### Jython

[Jython](http://www.jython.org/) 是一个将Python代码编译成Java字节码的实现， 运行在JVM (Java Virtual Machine) 上。另外，它可以像是用Python模块一样，导入 并使用任何Java类。

如果您需要与现有的Java代码库对接或者基于其他原因需要为JVM编写Python代码，那么 Jython是最好的选择。

### IronPython

[IronPython](http://ironpython.net/) 是一个针对 .NET 框架的Python实现。它 可以用Python和.NET framework的库，也能将Python代码暴露给给.NET框架中的其他语言。

[Python Tools for Visual Studio](http://ironpython.net/tools/) 直接集成了 IronPython到Visual Studio开发环境中，使之成为Windows开发者的理想选择。

### PythonNet

[Python for .NET](http://pythonnet.github.io/) 是一个近乎无缝集成的， 提供给本机已安装的Python .NET公共语言运行时（CLR）包。它采取与IronPython （见上文）相反的方法，与其说是竞争，不如说是互补。



## 在不同操作系统上安装 Python 和 Pip

有的系统可能已经预先安装了 Python，不过往往版本较低，不适合用于开发。

### Mac OS X

安装 C 语言编译工具 XCode：` xcode-select --install `

安装操作系统的包管理工具 Homebrew：`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`，然后向 `~/.profile`  插入内容：`export PATH=/usr/local/bin:/usr/local/sbin:$PATH`

安装 Python：`brew install python`

Homebrew 允许 Python2 和 Python3 共存，分别会被命名为 `python2` 和 `python3`，同时还会安装好 `pip2` 和 `pip3`

### Windows

首先，遵照 [Chocolatey](https://chocolatey.org/install) 的安装指引。 它是 Windows 7+ 的社区系统包管理器（很像Mac OSX上的Homebrew）。

完成之后，安装Python 3会非常简单，因为Chocolatey将Python 3作为默认设置。

```
choco install python

```

一旦您运行了上述命令，您应该能够直接从控制台启动Python。（Chocolatey非常棒，会自动将Python添加到您的系统路径中。）

所有受支持的Python 3版本都包含pip，因此请确保它是最新的:

```
python -m pip install -U pip
```

### Linux

如果您使用的是Ubuntu 16.10或更新，可以通过以下命令简单地安装Python 3.6:

```
$ sudo apt-get update
$ sudo apt-get install python3.6
```

在Fedora上您可以使用 dnf 包管理器：

```
$ sudo dnf install python3
```

Python 3 默认自带 pip 的，运行以下命令行代码检查pip是否已经安装：

```
$ command -v pip
```

注意，在某些Linux发行版（包括Ubuntu和Fedora）上， `pip` 用于Python 2的，而 `pip3` 用于Python 3。

```
$ command -v pip3
```

### Pip 升级

#### Windows

更新系统级 pip

```
python -m pip install --upgrade pip
```

#### Mac OS X 和 Linux

使用系统级 pip 来更新用户 pip

```
python3 -m pip install --user --upgrade pip
```





## 安装第三方库

It’s important to note that the term “package” in this context is being used as a synonym for a [distribution](https://packaging.python.org/glossary/#term-distribution-package) (i.e. a bundle of software to be installed), not to refer to the kind of [package](https://packaging.python.org/glossary/#term-import-package) that you import in your Python source code (i.e. a container of modules). It is common in the Python community to refer to a [distribution](https://packaging.python.org/glossary/#term-distribution-package) using the term “package”. Using the term “distribution” is often not preferred, because it can easily be confused with a Linux distribution, or another larger software distribution like Python itself.

### 相关工具

首先确保 Python, Pip, setuptools, wheel 工具已经安装好了（Python 3 自带这些工具）。

更新它们

While pip alone is sufficient to install from pre-built binary archives, up to date copies of the setuptools and wheel projects are useful to ensure you can also install from source archives: 

```
python -m pip install --upgrade pip setuptools wheel
```

### 虚拟环境

Python “Virtual Environments” allow Python [packages](https://packaging.python.org/glossary/#term-distribution-package) to be installed in an isolated location for a particular application, rather than being installed globally.

将库安装在全局位置（global site-packages directory）的常见问题

* 不同应用使用同一库的不同版本
* 更新了一个某个库之后，之前运行很好的应用崩溃了
* 在共享主机上，没有权限在全局位置安装库

In all these cases, virtual environments can help you. They have their own installation directories and they don’t share libraries with other virtual environments.

Python 官方提供的两个虚拟环境工具

- [venv](https://docs.python.org/3/library/venv.html) is available by default in Python 3.3 and later, and installs [pip](https://packaging.python.org/key_projects/#pip) and [setuptools](https://packaging.python.org/key_projects/#setuptools) into created virtual environments in Python 3.4 and later.
- [virtualenv](https://packaging.python.org/key_projects/#virtualenv) needs to be installed separately, but supports Python 2.6+ and Python 3.3+, and [pip](https://packaging.python.org/key_projects/#pip), [setuptools](https://packaging.python.org/key_projects/#setuptools)and [wheel](https://packaging.python.org/key_projects/#wheel) are always installed into created virtual environments by default (regardless of Python version).

激活虚拟环境

Using [virtualenv](https://packaging.python.org/key_projects/#virtualenv):

```
virtualenv <DIR>
source <DIR>/bin/activate

```

Using [venv](https://docs.python.org/3/library/venv.html):

```
python3 -m venv <DIR>
source <DIR>/bin/activate

```

注：Windows 系统上将 `source` 替换为 `activate`.  For more information, see the [virtualenv](http://virtualenv.pypa.io/) docs or the [venv](https://docs.python.org/3/library/venv.html) docs.

### 虚拟环境管理工具

Managing multiple virtual environments directly can become tedious, so the [dependency management tutorial](https://packaging.python.org/tutorials/managing-dependencies/#managing-dependencies)introduces a higher level tool, [Pipenv](https://packaging.python.org/key_projects/#pipenv), that automatically manages a separate virtual environment for each project and application that you work on.





## Python 虚拟环境

首先确保已经正确安装了 Python 和 Pip。

虚拟环境工具通过为不同项目创建专属的 Python 虚拟环境，以实现其依赖的库独立保存在不同的路径。 这解决了“项目X依赖于 1.x 版本，但项目 Y 需要 4.x”的难题，并且维持全局的 site-packages 目录干净、易管理。



### Pip + Virtualenv

安装 pip

pip 搭载在 Python 3



[virtualenv](https://packaging.python.org/key_projects/#virtualenv) is used to manage Python packages for different projects. Using virtualenv allows you to avoid installing Python packages globally which could break system tools or other projects. You can install virtualenv using pip.

[virtualenv](https://packaging.python.org/key_projects/#virtualenv) allows you to manage separate package installations for different projects. It essentially allows you to create a “virtual” isolated Python installation and install packages into that virtual installation. When you switch projects, you can simply create a new virtual environment and not have to worry about breaking the packages installed in the other environments. It is always recommended to use a virtualenv while developing Python applications.



安装 virtualenv

On macOS and Linux:

```
python3 -m pip install --user virtualenv

```

On Windows:

```
py -m pip install --user virtualenv
```



创建虚拟环境

Change to project directory:

```
cd project_dir
```

On macOS and Linux:

```
python3 -m virtualenv env

```

On Windows:

```
py -m virtualenv env

```

The second argument is the location to create the virtualenv. Generally, you can just create this in your project and call it `env`.

virtualenv will create a virtual Python installation in the `env` folder. You should exclude your virtualenv directory from your version control system using `.gitignore` or similar.

运行带 `--no-site-packages` 选项的 `virtualenv` 将不会包括全局安装的包。 这可用于保持包列表干净，以防以后需要访问它。（这在 `virtualenv` 1.7及之后是默认行为）



激活虚拟环境

Before you can start installing or using packages in your virtualenv you’ll need to *activate* it. Activating a virtualenv will put the virtualenv-specific `python` and `pip` executables into your shell’s `PATH`.

On macOS and Linux:

```
source env/bin/activate

```

On Windows:

```
.\env\Scripts\activate
```

检查被激活的虚拟环境

You can confirm you’re in the virtualenv by checking the location of your Python interpreter, it should point to the `env` directory.

On macOS and Linux:

```
which python
```

On Windows:

```
where python
```

一旦虚拟环境被激活，通过 pip 安装的库都会在该虚拟环境过，并且项目中导入的库也会是该环境下的版本。



离开虚拟环境

If you want to switch projects or otherwise leave your virtualenv, simply run:

```
deactivate
```



要删除一个虚拟环境，只需删除它的文件夹。



虚拟环境管理工具 - virtualenvwrapper

使用 virtualenv 麻烦的地方在于，需要手动管理过个虚拟环境，然后一段时间后，您可能会有很多个虚拟环境散落在系统各处，您将有可能忘记它们的名字或者位置。

[virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/index.html) 提供了一系列命令使得和虚拟环境工作变得愉快许多。它把您所有的虚拟环境都放在一个地方。

安装（确保 **virtualenv** 已经安装了）：

```
$ pip install virtualenvwrapper
$ export WORKON_HOME=~/Envs
$ source /usr/local/bin/virtualenvwrapper.sh
```

对于Windows，您可以使用 [virtualenvwrapper-win](https://github.com/davidmarble/virtualenvwrapper-win/) 。

安装（确保 **virtualenv** 已经安装了）：

```
$ pip install virtualenvwrapper-win

```

在Windows中，WORKON_HOME默认的路径是 %USERPROFILE%Envs 。



如何用 virtualenvwrapper 来管理虚拟环境？

1. 创建一个虚拟环境：

```
$ mkvirtualenv my_project

```

这会在 `~/Envs` 中创建 `my_project` 文件夹。

1. 在虚拟环境上工作：

```
$ workon my_project

```

或者，您可以创建一个项目，它会创建虚拟环境，并在 `$WORKON_HOME` 中创建一个项目目录。 当您使用 `workon myproject` 时，会 `cd` -ed 到项目目录中。

```
$ mkproject myproject

```

**virtualenvwrapper** 提供环境名字的tab补全功能。当您有很多环境， 并且很难记住它们的名字时，这就显得很有用。

`workon` 也能停止您当前所在的环境，所以您可以在环境之间快速的切换。

1. 停止是一样的：

```
$ deactivate

```

1. 删除：

```
$ rmvirtualenv my_project
```



此外 [virtualenv-burrito](https://github.com/brainsik/virtualenv-burrito) 工具， 可以用单行命令拥有virtualenv + virtualenvwrapper的环境。



如果仅考虑 Python 3.3+ 的话，标准库 venv 可以也用来管理虚拟环境

The [`venv`](https://docs.python.org/3.6/library/venv.html#module-venv) module provides support for creating lightweight “virtual environments” with their own site directories, optionally isolated from system site directories. Each virtual environment has its own Python binary (allowing creation of environments with various Python versions) and can have its own independent set of installed Python packages in its site directories.



### Pipenv

It automatically creates and manages a virtualenv for your projects, as well as adds/removes packages from your `Pipfile` as you install/uninstall packages. It also generates the ever–important `Pipfile.lock`, which is used to produce deterministic builds.

Pipenv is primarily meant to provide users and developers of applications with an easy method to setup a working environment.

- You no longer need to use `pip` and `virtualenv` separately. They work together.
- Managing a `requirements.txt` file [can be problematic](https://www.kennethreitz.org/essays/a-better-pip-workflow), so Pipenv uses `Pipfile` and `Pipfile.lock` to separate abstract dependency declarations from the last tested combination.
- Hashes are used everywhere, always. Security. Automatically expose security vulnerabilities.
- Strongly encourage the use of the latest versions of dependencies to minimize security risks [arising from outdated components](https://www.owasp.org/index.php/Top_10-2017_A9-Using_Components_with_Known_Vulnerabilities).
- Give you insight into your dependency graph (e.g. `$ pipenv graph`).
- Streamline development workflow by loading `.env` files.



其他特性

1. 根据 Pipfile 自动寻找项目根目录。
2. 如果不存在，可以自动生成 Pipfile 和 Pipfile.lock。
3. 自动在项目目录的 .venv 目录创建虚拟环境。（当然这个目录地址通过设置WORKON_HOME改变）
4. 自动管理 Pipfile 新安装和删除的包。



关于 Pipfile

1. Pipfile 文件是 TOML 格式而不是 requirements.txt 这样的纯文本。
2. 一个项目对应一个 Pipfile，支持开发环境与正式环境区分。默认提供 default 和 development 区分。
3. 提供版本锁支持，存为 Pipfile.lock。



安装 Pipenv 工具

`Pipenv` 是 Python 项目的依赖管理器。如果您熟悉 Node.js 的 [npm](https://www.npmjs.com/) 或 Ruby 的 [bundler](http://bundler.io/)，那么它们在思路上与这些工具类似。尽管 `pip` 可以安装 Python 包， 但仍推荐使用 Pipenv，因为它是一种更高级的工具，可简化依赖关系管理的常见使用情况。

使用 `pip` 来安装 Pipenv（基于用户安装）：

```
$ pip install --user pipenv
```



使用 Pipenv 工具

切换到项目所在目录中，运行如下命令安装 `requests` 库

```
$ pipenv install requests
```

Pipenv 将在您的项目目录中安装超赞的 [Requests](https://python-requests.org/) 库并为您创建一个 `Pipfile`。 `Pipfile` 用于跟踪您的项目中需要重新安装的依赖，例如在与他人共享项目时。

要运行项目的脚本

```
$ pipenv run python main.py
```

#### Basic Concepts

- A virtualenv will automatically be created, when one doesn't exist.
- When no parameters are passed to `install`, all packages `[packages]` specified will be installed.
- To initialize a Python 3 virtual environment, run `$ pipenv --three`.
- To initialize a Python 2 virtual environment, run `$ pipenv --two`.
- Otherwise, whatever virtualenv defaults to will be the default.

#### Other Commands

- `shell` will spawn a shell with the virtualenv activated.
- `run` will run a given command from the virtualenv, with any arguments forwarded (e.g. `$ pipenv run python`).
- `check` asserts that PEP 508 requirements are being met by the current environment.
- `graph` will print a pretty graph of all your installed dependencies.



用法示例

```
❯ mkdir test_pipenv
❯ cd test_pipenv
❯ pipenv install  # 创建一个虚拟环境
Creating a virtualenv for this project…
...
Installing setuptools, pip, wheel...done.
...
To activate this project's virtualenv, run the following:
 $ pipenv shell

❯ which python3
/usr/local/Cellar/python3/3.6.1/bin/python3  # 系统自带的 Python

❯ pipenv shell  # 激活虚拟环境
Spawning environment shell (/bin/zsh). Use 'exit' to leave.
source /Users/dongweiming/.virtualenvs/test_pipenv-GP_s2TW5/bin/activate

❯ which python3  # 虚拟环境中的 Python
/Users/dongweiming/.virtualenvs/test_pipenv-GP_s2TW5/bin/python3

❯ exit  # 退出虚拟环境

```







## 同时兼容 Python2 和 Python3 的代码

https://docs.python.org/3/howto/pyporting.html



## 不同用户拥有不同的 Python 环境

a per user site-packages directory to allow users the local installation of Python packages in their home directory. 每个用户拥有各自的第三方库，不必请求系统管理员安装第三方库，也不必担心相互之间库发生冲突。

参见 [pep-0370](https://www.python.org/dev/peps/pep-0370/)



use base directory

It's located inside the user's home directory. The user site and use config directory are inside the base directory. On some systems the directory may be shared with 3rd party apps. 除了下面默认指定位置外，可以通过环境变量 `PYTHONUSERBASE` 来配置

- Unix (including Mac)

  `~/.local`

- Windows

  `%APPDATA%/Python`



user data directory

Usually the parent directory of the user site directory. It's meant for Python version specific data like config files, docs, images and translations. 

- Unix (including Mac)

  `~/.local/lib/python2.6`

- Windows

  `%APPDATA%/Python/Python26`



user site directory

A site directory inside the users' home directory. A user site directory is specific to a Python version. The path contains the version number (major and minor only).

- Unix (including Mac OS X)

  `~/.local/lib/python2.6/site-packages`

- Windows

  `%APPDATA%/Python/Python26/site-packages`



user script directory

A directory for binaries and scripts. [[10\]](https://www.python.org/dev/peps/pep-0370/#id22) It's shared across Python versions and the destination directory for scripts.

- Unix (including Mac)

  `~/.local/bin`

- Windows

  `%APPDATA%/Python/Scripts`

该目录一般是脚本、二进制等可执行文件，要在命令行下使用它们，需要将相应的路径添加到操作系统过的环境变量 `PATH` 中（注：可通过 `python -m site --user-base` 来查看 user base 目录）



The user site directory is added before the system site directories but after Python's search paths and `PYTHONPATH`. This setup allows the user to install a different version of a package than the system administrator but it prevents the user from accidently overwriting a stdlib module. Stdlib modules can still be overwritten with `PYTHONPATH`.

The user site directory can be suppressed with a new option `-s` or the environment variable `PYTHONNOUSERSITE`. The feature can be disabled globally by setting `site.ENABLE_USER_SITE` to the value `False`

The path to the user base directory can be overwritten with the environment variable `PYTHONUSERBASE`. The default location is used when `PYTHONUSERBASE` is not set or empty.

The `site` module gets two arguments `--user-base` and `--user-site` to print the path to the user base or user site directory to the standard output.

```
python3 -m site --user-site
python3 -m site --user-base
```

此外还可以通过 `site` 模块的方法 `getuserbase()` 和 `getusersitepackages()` 来获得，在调用它们后 `site` 模块中的 `USER_BASE` 和 `USER_SITE` 会被初始化。



使用 pip 时利用该特色，需要为其提供选项参数 `pip install --user`

有个技巧，若要为特定的虚拟环境安装第三方库的话，也可以先设置环境变量 `PYTHONUSERBASE` 指向虚拟环境，再使用 `pip install --user` 来安装。



