## 简介

不同应用程序要用到不同的环境配置，也即可能要用到同一个第三方库的不同版本，而我们仅在系统上安装了一个 Python 环境，该如何在一个系统上运行多个应用呢？

Python applications will often use packages and modules that don’t come as part of the standard library. Applications will sometimes need a specific version of a library, because the application may require that a particular bug has been fixed or the application may be written using an obsolete version of the library’s interface.

This means it may not be possible for one Python installation to meet the requirements of every application. If application A needs version 1.0 of a particular module but application B needs version 2.0, then the requirements are in conflict and installing either version 1.0 or 2.0 will leave one application unable to run.

A virtual environment is a Python environment such that the Python interpreter, libraries and scripts installed into it are isolated from those installed in other virtual environments, and (by default) any libraries installed in a “system” Python, i.e., one which is installed as part of your operating system.

A virtual environment is a directory tree which contains Python executable files and other files which indicate that it is a virtual environment.

Common installation tools such as `Setuptools` and `pip` work as expected with virtual environments. In other words, when a virtual environment is active, they install Python packages into the virtual environment without needing to be told to do so explicitly.



虚拟环境，允许为环境指定特定版本的 Python 以及第三方库，为每个应用创建其专属的虚拟环境即可以解决上述问题。这样实现了应用程序之间环境的隔离，使得同一个系统上运行以及维护多个应用变得容易很多。

The solution for this problem is to create a [virtual environment](https://docs.python.org/3/glossary.html#term-virtual-environment), a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages.

Different applications can then use different virtual environments. To resolve the earlier example of conflicting requirements, application A can have its own virtual environment with version 1.0 installed while application B has another virtual environment with version 2.0. If application B requires a library be upgraded to version 3.0, this will not affect application A’s environment.



- A *virtual environment* is a semi-isolated Python environment that allows packages to be installed for use by a particular application, rather than being installed system wide.
- `venv` is the standard tool for creating virtual environments, and has been part of Python since Python 3.3. Starting with Python 3.4, it defaults to installing `pip` into all created virtual environments.
- `virtualenv` is a third party alternative (and predecessor) to `venv`. It allows virtual environments to be used on versions of Python prior to 3.4, which either don’t provide `venv` at all, or aren’t able to automatically install `pip` into created environments.
- `pyvenv` was the recommended tool for creating virtual environments for Python 3.3 and 3.4, and is [deprecated in Python 3.6](https://docs.python.org/dev/whatsnew/3.6.html#deprecated-features).



一个虚拟环境有以下几部分组成：

* 特定版本的 Python
* 特定版本的第三方库
* 某些环境变量

此外还要考虑虚拟环境如下几个问题：

* 激活和退出虚拟环境
* 共享虚拟环境

## 安装多版本 Python

如果需要在同一系统上运行不同版本的 Python 代码，就需要同时安装不同版本的 Python，比如为将 Python 2 的项目迁移到 Python 3，就需要同时安装 Python 2 和 Python 3。那么如何让多版本的 Python 在系统上共存呢？

不管是 Windows, Linux 还是 Mac OS X，道理都是一样的，首先需要在系统上不同位置安装不同版本的 Python。在安装完成后，一般这些安装路径会自动添加到环境变量 `PATH` 中，并且这些不同位置 Python 的可执行文件名都是 `python.exe`，在命令行中运行 `python` 时，就无法指定到底要运行哪个版本。

为了可以精确指定版本，可以通过为不同位置的 Python 创建不同的符号链接（快捷方式），然后将这些不同的符号链接添加到环境变量 `PATH` 中，例如：安装了 `/usr/local/bin/python2.7/python.exe` 和 `/usr/local/python3.6/python.exe`，分别创建符号链接 `python27` 和 `python36`，然后将其添加到环境变量中即可。

在 Linux 上要注意的是，由于系统自带了一个 Python 并且系统上有很多软件会依赖这个版本的 Python 来运行，一般位于 `/usr/bin/python`。所以千万不要覆盖掉它。除了上面创建符号链接的方式外，还可以通过在入口脚本首行编辑 `#!/usr/local/bin/python3.6/python.exe`

On Linux systems, a Python installation will typically be included as part of the distribution. Installing into this Python installation requires root access to the system, and may interfere with the operation of the system package manager and other components of the system if a component is unexpectedly upgraded using `pip`.

On such systems, it is often better to use a virtual environment or a per-user installation when installing packages with `pip`.



### 通过 pyenv 来管理多版本 Python

[pyenv](https://github.com/yyuu/pyenv) 是一个允许多个Python解释器版本同时安装 于一台机器的工具。这解决了不同的项目需要不同版本的Python的问题。比如，为了兼容性， 可以很容易地为一个项目安装Python 2.7，而继续使用Python 3.4作为默认的编辑器。 pyenv不止限于CPython版本——它还能安装PyPy、anaconda、miniconda、stackless、jython 和ironpython解释器。

pyenv的工作原理是在一个叫做 `shims` 目录中创建Python解释器（以及其他工具像 `pip` 和 `2to3` 等）的假版本。当系统寻找名为 `python` 的应用时， 它会先在 `shims` 目录中查找，并使用那个假版本，然后会传递命令到pyenv中。 pyenv基于环境变量、 `.python-version`文件和全局默认设置的信息就知道该运行 哪个版本的Python。

[更多](https://github.com/pyenv/pyenv)



pip 和 多版本的 Python

On Linux, Mac OS X, and other POSIX systems, use the versioned Python commands in combination with the `-m` switch to run the appropriate copy of`pip`:

```
python2   -m pip install SomePackage  # default Python 2
python2.7 -m pip install SomePackage  # specifically Python 2.7
python3   -m pip install SomePackage  # default Python 3
python3.4 -m pip install SomePackage  # specifically Python 3.4

```

Appropriately versioned `pip` commands may also be available.

On Windows, use the `py` Python launcher in combination with the `-m` switch:

```
py -2   -m pip install SomePackage  # default Python 2
py -2.7 -m pip install SomePackage  # specifically Python 2.7
py -3   -m pip install SomePackage  # default Python 3
py -3.4 -m pip install SomePackage  # specifically Python 3.4
```



## 虚拟环境管理

The module used to create and manage virtual environments is called [`venv`](https://docs.python.org/3/library/venv.html#module-venv). [`venv`](https://docs.python.org/3/library/venv.html#module-venv) will usually install the most recent version of Python that you have available.

虚拟环境跟特定版本 Python 的绑定

To create a virtual environment, decide upon a directory where you want to place it, and run the [`venv`](https://docs.python.org/3/library/venv.html#module-venv) module as a script with the directory path:

```
python3 -m venv tutorial-env

```

This will create the `tutorial-env` directory if it doesn’t exist, and also create directories inside it containing a copy of the Python interpreter, the standard library, and various supporting files.

激活虚拟环境

Once you’ve created a virtual environment, you may activate it.

On Windows, run:

```
tutorial-env\Scripts\activate.bat

```

On Unix or MacOS, run:

```
source tutorial-env/bin/activate
```

Activating the virtual environment will change your shell’s prompt to show what virtual environment you’re using, and modify the environment so that running `python` will get you that particular version and installation of Python.

退出虚拟环境

有个相应的 `deactivate` 脚本来进行退出。



## 虚拟环境中的第三方库

pip 简介

You can install, upgrade, and remove packages using a program called **pip**. By default `pip` will install packages from the Python Package Index, <[https://pypi.python.org/pypi](https://pypi.python.org/pypi)>. You can browse the Python Package Index by going to it in your web browser, or you can use `pip`’s limited search feature:

```
(tutorial-env) $ pip search astronomy
```

`pip` has a number of subcommands: “search”, “install”, “uninstall”, “freeze”, etc.

在创建虚拟环境时，环境会搭载 pip，在此环境使用 pip 管理的将是当前的虚拟环境。



虚拟环境的共享

`pip freeze` will produce a similar list of the installed packages, but the output uses the format that `pip install` expects. A common convention is to put this list in a `requirements.txt` 

The `requirements.txt` can then be committed to version control and shipped as part of an application. Users can then install all the necessary packages with `install -r`:

```
pip install -r requirements.txt
```



虚拟环境变量

Environment variables are a good way to set variables needed in your application, specifically Django on Heroku. When developing and deploying a web app, different environments (local machine, live site) need different configurations (passwords, database names, etc). We can use environmental variables to setup the different environments

环境变量很有用，比如可以让应用根据环境变量来判断当前是开发模式还是生产模式。

推荐使用 https://direnv.net/





## Anaconda 发行版

https://conda.io/docs/user-guide/tasks/manage-environments.html

conda 将 Python, pip 以及第三方库都当成一样的包来管理。而且可以管理多版本共存和虚拟环境的创建、切换。



多版本共存：

To list the versions of Python that are available to install, in your Terminal window or an Anaconda Prompt, run:

```
conda search python

```

This lists all packages whose names contain the text `python`.

To list only the packages whose full name is exactly `python`, add the `--full-name` option. In your Terminal window or an Anaconda Prompt, run:

```
conda search --full-name python
```

创建虚拟环境来安装不同版本的 Python

- To create the new environment for Python 3.6, in your Terminal window or an Anaconda Prompt, run:

  ```
  conda create -n py36 python=3.6 anaconda

  ```

  NOTE: Replace `py36` with the name of the environment you want to create. `anaconda` is the metapackage that includes all of the Python packages comprising the Anaconda distribution. `python=3.6` is the package and version you want to install in this new environment. This could be any package, such as `numpy=1.7`, or [multiple packages](https://conda.io/docs/user-guide/tasks/manage-pkgs.html#installing-multiple-packages).

- To create the new environment for Python 2.7, in your Terminal window or an Anaconda Prompt, run:

  ```
  conda create -n py27 python=2.7 anaconda
  ```



虚拟环境管理

To activate an environment:

- On Windows, in your Anaconda Prompt, run `activate myenv`
- On macOS and Linux, in your Terminal Window, run `source activate myenv`



To deactivate an environment:

- On Windows, in your Anaconda Prompt, run `deactivate`
- On macOS and Linux, in your Terminal Window, run `source deactivate`

TIP: In Windows, it is good practice to deactivate one environment before activating another.



Which is the current environment:

By default, the active environment—the one you are currently using—is shown in parentheses () or brackets [] at the beginning of your command prompt:

```
(myenv) $

```

If you do not see this, run:

```
conda info --envs

```

In the environments list that displays, your current environment is highlighted with an asterisk (*).



To see a list of all packages installed in a specific environment:

- If the environment is not activated, in your Terminal window or an Anaconda Prompt, run:

  ```
  conda list -n myenv

  ```

- If the environment is activated, in your Terminal window or an Anaconda Prompt, run:

  ```
  conda list

  ```

To see if a specific package is installed in an environment, in your Terminal window or an Anaconda Prompt, run:

```
conda list -n myenv scipy
```



To remove an environment, in your Terminal window or an Anaconda Prompt, run:

```
conda remove --name myenv --all
```



To use pip in your environment, in your Terminal window or an Anaconda Prompt, run:

```
conda install -n myenv pip
source activate myenv
pip <pip_subcommand>
```



虚拟环境中的系统环境变量

https://conda.io/docs/user-guide/tasks/manage-environments.html#windows

https://conda.io/docs/user-guide/tasks/manage-environments.html#macos-and-linux



共享虚拟环境

You may want to share your environment with someone else—for example, so they can re-create a test that you have done. To allow them to quickly reproduce your environment, with all of its packages and versions, give them a copy of your `environment.yml file`.

导出虚拟环境配置

1. Activate the environment to export:

   - On Windows, in your Anaconda Prompt, run `activate myenv`
   - On macOS and Linux, in your Terminal window, run `source activate myenv`

   NOTE: Replace `myenv` with the name of the environment.

2. Export your active environment to a new file:

   ```
   conda env export > environment.yml

   ```

   NOTE: This file handles both the environment’s pip packages and conda packages.

3. Email or copy the exported `environment.yml` file to the other person.

手动创建虚拟环境配置

EXAMPLE: A more complex environment file:

```
name: stats2
channels:
  - javascript
dependencies:
  - python=3.4   # or 2.7
  - bokeh=0.9.2
  - numpy=1.9.*
  - nodejs=0.10.*
  - flask
  - pip:
    - Flask-Testing
```

导入虚拟环境配置

```
conda env create -f myenv.yml
```