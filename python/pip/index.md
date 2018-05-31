## 简介

As a popular open source development project, Python has an active supporting community of contributors and users that also make their software available for other Python developers to use under open source license terms.



## 基本用法



安装和更新

You can install the latest version of a package by specifying a package’s name

```
pip install scrapy
```

You can also install a specific version of a package by giving the package name followed by `==` and the version number:

```
 pip install scrapy==2.7
```

you can run `pip install --upgrade` to upgrade the package to the latest version

```
pip install --upgrade scrapy
```



安装到当前用户

To install [packages](https://packaging.python.org/glossary/#term-distribution-package) that are isolated to the current user, use the `--user` flag:

```
pip install --user SomeProject
```

Note that the `--user` flag has no effect when inside a virtual environment



移除

`pip uninstall` followed by one or more package names will remove the packages



查询

`pip show` will display information about a particular packag

`pip list` will display all of the packages installed in current environment

`pip freeze` will produce a similar list of the installed packages, but the output uses the format that `pip install` expects. A common convention is to put this list in a `requirements.txt` 



Find pre-release and development versions, in addition to stable versions. By default, pip only finds stable versions.

```
pip install --pre SomeProject
```



Some packages have optional [extras](https://setuptools.readthedocs.io/en/latest/setuptools.html#declaring-extras-optional-features-with-their-own-dependencies). You can tell pip to install these by specifying the extra in brackets:

```
pip install requests[security]
```







### 安装方式



Install a list of requirements specified in a [Requirements File](https://pip.pypa.io/en/latest/user_guide/#requirements-files).

```
pip install -r requirements.txt
```

The `requirements.txt` can then be committed to version control and shipped as part of an application. Users can then install all the necessary packages with `install -r`:

```
pip install -r requirements.txt
```



Install a project from VCS in “editable” mode. pip can install packages directly from their version control system. For example, you can install directly from a git repository:

For more information on supported version control systems and syntax, see pip’s documentation on [VCS Support](https://pip.pypa.io/en/latest/reference/pip_install/#vcs-support).

```
pip install -e git+https://git.repo/some_pkg.git#egg=SomeProject          # from git
pip install -e hg+https://hg.repo/some_pkg#egg=SomeProject                # from mercurial
pip install -e svn+svn://svn.repo/some_pkg/trunk/#egg=SomeProject         # from svn
```



Installing from local src, pip can install a package directly from source

```
pip install <path>
```

Installing from local src in [Development Mode](https://setuptools.readthedocs.io/en/latest/setuptools.html#development-mode), i.e. in such a way that the project appears to be installed, but yet is still editable from the src tree.  pip can install packages from source in [development mode](https://setuptools.readthedocs.io/en/latest/setuptools.html#development-mode), meaning that changes to the source directory will immediately affect the installed package without needing to re-install

```
pip install --editable <path>
```



Install a particular source archive file.

If you have a local copy of a [Distribution Package](https://packaging.python.org/glossary/#term-distribution-package)’s archive (a zip, wheel, or tar file) you can install it directly with pip:

```
pip install ./downloads/SomeProject-1.0.4.tar.gz

```

If you have a directory containing archives of multiple packages, you can tell pip to look for packages there and not to use the [Python Package Index (PyPI)](https://packaging.python.org/glossary/#term-python-package-index-pypi) at all:

```
pip install --no-index --find-links=file:///local/dir/ SomeProject
pip install --no-index --find-links=/local/dir/ SomeProject
pip install --no-index --find-links=relative/dir/ SomeProject
```

This is useful if you are installing packages on a system with limited connectivity or if you want to strictly control the origin of distribution packages.



更改默认安装源

```
pip install --index-url http://my.package.repo/simple/ SomeProject
```



添加额外安装源

```
pip install --extra-index-url http://my.package.repo/simple SomeProject
```



### 限制 pip 全局安装第三方库

为了确保您当您使用 `pip install` 时是将包安装在激活的虚拟环境中，考虑在 `~/.bashrc`文件中加上以下一行：

```
export PIP_REQUIRE_VIRTUALENV=true

```

在保存完这个修改以及使用 `source ~/.bashrc` 来source一下 `~/.bashrc` 文件后，如果您不在一个虚拟环境中，pip就不会让您安装包。如果您试着在虚拟环境外使用 `pipinstall` ，pip将会柔和地提示您需要一个激活的虚拟环境来安装包。

```
$ pip install requests
Could not find an activated virtualenv (required).

```

您也可以通过编辑 `pip.conf` 或 `pip.ini`来做相同的配置。 :file:`pip.conf` 被Unix和Mac OS X操作系统使用，能够在这里找到：

```
$HOME/.pip/pip.conf

```

类似的， `pip.ini` 被Windows操作系统使用，能够在这里找到：

```
%HOME%\pip\pip.ini

```

如果在这些位置中并没有 `pip.conf` 或 `pip.ini` ， 您可以在对应的操作系统中创建一个正确名字的新文件。

如果您早就拥有配置文件了，只需将下行添加到 `[global]` 设置下， 即可要求一个激活的虚拟环境：

```
require-virtualenv = true

```

如果您没有配置文件，您需要创建一个新的，然后把下面几行添加到这个新文件中：

```
[global]
require-virtualenv = true

```

当然，您也需要在全局范围内安装一些包（通常是在多个项目中都要一直用到的包）， 可以添加下面内容到 `~/.bashrc` 来完成：

```
gpip() {
    PIP_REQUIRE_VIRTUALENV="" pip "$@"
}

```

在保存完这个修改以及使用 `source ~/.bashrc` 来source一下 `~/.bashrc` 文件后，您现在可以通过运行 `gpip install` 来在全局范围内安装包。 您可以把函数名改成任何您喜欢的，只要记住当您要用pip在全局范围内安装包的时候使用 那个名字就行了。



### pip 缓存第三方库

每个开发者都有偏好的库，当您工作在大量不同的项目上时，这些项目之间肯定有一些重叠的库。 比如说，您可能在多个不同的项目上使用了 `requests` 。

每当您开始一个新项目（并有一个新的虚拟环境）重新下载相同的包/库是没有必要的。幸运的是， 自从6.0版本开始，pip提供 [默认缓存机制](https://pip.pypa.io/en/stable/reference/pip_install/#caching) 而无需任何配置。

当使用更老的版本时，你可以用下面的方式来配置pip，以使它尝试重用已安装的包。

在UNIX系统中，您可以添加以下两行到您的 `.bashrc` 或 `.bash_profile` 文件中。

```
export PIP_DOWNLOAD_CACHE=$HOME/.pip/cache

```

您可以设置成任何您喜欢的路径（只要设置了写权限）。添加完后， `source` 下您的`.bashrc` （或者 `.bash_profile` ）文件，就设置好啦。

另一个进行相同配置的方法是通过 `pip.conf` 或 `pip.ini` 文件来做， 这取决于您的系统。如果您用Windows，就将下面一行添加到 `pip.ini` 文件中的 `[global]` 设置下：

```
download-cache = %HOME%\pip\cache

```

类似的，如果您使用UNIX，就将下面一行添加到 `pip.conf` 文件中的 `[global]` 设置下：

```
download-cache = $HOME/.pip/cache

```

虽然您可以使用任何您喜欢的存储缓存的路径，但是仍然推荐在 `pip.conf` 或者 `pip.ini`文件所在目录下床架一个新的文件夹 *in* 。如果您不相信自己能够处理好 这个路径，就使用这里提供的内容就好，不会有问题的。



## 安装源

Python 第三方库的来源：Python Package Index

You can install, upgrade, and remove packages using a program called **pip**. By default `pip` will install packages from the Python Package Index, <[https://pypi.python.org/pypi](https://pypi.python.org/pypi)>. You can browse the Python Package Index by going to it in your web browser, or you can use `pip`’s limited search feature: `pip search scrapy`







### 从 PyPI 源安装

The most common usage of [pip](https://packaging.python.org/key_projects/#pip) is to install from the [Python Package Index](https://packaging.python.org/glossary/#term-python-package-index-pypi) using a [requirement specifier](https://packaging.python.org/glossary/#term-requirement-specifier). Generally speaking, a requirement specifier is composed of a project name followed by an optional [version specifier](https://packaging.python.org/glossary/#term-version-specifier). [**PEP 440**](https://www.python.org/dev/peps/pep-0440) contains a [**full specification**](https://www.python.org/dev/peps/pep-0440#version-specifiers) of the currently supported specifiers. Below are some examples.

To install the latest version of “SomeProject”:

```
pip install 'SomeProject'

```

To install a specific version:

```
pip install 'SomeProject==1.4'

```

To install greater than or equal to one version and less than another:

```
pip install 'SomeProject>=1,<2'

```

To install a version that’s [**“compatible”**](https://www.python.org/dev/peps/pep-0440#compatible-release) with a certain version: [[4\]](https://packaging.python.org/tutorials/installing-packages/#id9)

```
pip install 'SomeProject~=1.4.2'

```

In this case, this means to install any version “==1.4.*” version that’s also “>=1.4.2”.



### 从 Source Distribution 和 Wheel 安装

[pip](https://packaging.python.org/key_projects/#pip) can install from either [Source Distributions (sdist)](https://packaging.python.org/glossary/#term-source-distribution-or-sdist) or [Wheels](https://packaging.python.org/glossary/#term-wheel), but if both are present on PyPI, pip will prefer a compatible [wheel](https://packaging.python.org/glossary/#term-wheel).

[Wheels](https://packaging.python.org/glossary/#term-wheel) are a pre-built [distribution](https://packaging.python.org/glossary/#term-distribution-package) format that provides faster installation compared to [Source Distributions (sdist)](https://packaging.python.org/glossary/#term-source-distribution-or-sdist), especially when a project contains compiled extensions.

If [pip](https://packaging.python.org/key_projects/#pip) does not find a wheel to install, it will locally build a wheel and cache it for future installs, instead of rebuilding the source distribution in the future.

