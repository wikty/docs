# Conda brief

Conda is an open source package management system and environment management system that runs on Windows, macOS and Linux.

> *Package, dependency and environment management for any language—Python, R, Ruby, Lua, Scala, Java, JavaScript, C/ C++, FORTRAN*
>
> Conda quickly installs, runs and updates packages and their dependencies. Conda easily creates, saves, loads and switches between environments on your local computer.
>
> Conda as a package manager helps you find and install packages. If you need a package that requires a different version of Python, you do not need to switch to a different environment manager, because conda is also an environment manager. With just a few commands, you can set up a totally separate environment to run that different version of Python, while continuing to run your usual version of Python in your normal environment.

# Conda install

**Conda** is a package management system and environment management system.

**Anaconda** is the most popular Python/R distribution for data science. There are so many data science packages and tools come with it,  including SciPy, NumPy, Jupyter Notebook and many others. While Anaconda manage packages, dependencies, environments with Conda.

**Miniconda** is a small, bootstrap version of Anaconda that includes only conda, Python, the packages they depend on and a small number of other useful packages, including pip, zlib and a few others. It's a free minimal installer for conda. After install it, you can use the `conda install` command to install 720+ additional conda packages from the Anaconda repository. Also Miniconda is a Python distribution, and it can make installing Python quick and easy even for new users.

How to get them?

1. If you just want to get Conda (with Python), please download and install the [Miniconda](https://conda.io/miniconda.html).
2. If you want to get a data science platform (with Python), please download and install the [Anaconda](https://www.anaconda.com/download/).

After you installed Miniconda or Anaconda, you can use Conda with command line commands at the Anaconda Prompt for Windows, or in a Terminal window for macOS or Linux.

不要担心 Miniconda 或 Anaconda 的安装会跟电脑上本来存在的 Python 相互混淆。在 Windows 系统中，安装它们时，不要将其添加到环境变量 PATH 中，然后通过 Anaconda Prompt 访问到的 Python 是 Miniconda 和 Anaconda 自带的，通过计算的 CommandLine 访问到的 Python 则是系统原先安装的。

# Conda concepts

## Conda channels

The locations of the repositories where conda looks for packages. Channels may point to a Cloud repository or a private location on a remote or local repository that you or your organization created. The `conda channel` command has a default set of channels to search, beginning with <https://repo.continuum.io/pkgs/>, which you may override, for example, to maintain a private or internal channel. These default channels are referred to in conda commands and in the `.condarc`file by the channel name “defaults.”

## Conda environments

A conda environment is a directory that contains a specific collection of conda packages that you have installed. For example, you may have one environment with NumPy 1.7 and its dependencies, and another environment with NumPy 1.6 for legacy testing. If you change one environment, your other environments are not affected. You can easily activate or deactivate environments, which is how you switch between them. You can also share your environment with someone by giving them a copy of your `environment.yaml` file. For more information, see [Managing environments](https://conda.io/docs/user-guide/tasks/manage-environments.html).

## Conda packages

A conda package is a compressed tarball file that contains system-level libraries, Python or other modules, executable programs and other components. Conda keeps track of the dependencies between packages and platforms. The conda package format is identical across platforms and operating systems.

Conda packages are downloaded from remote channels, which are URLs to directories containing conda packages. The `conda` command searches a default set of channels, and packages are automatically downloaded and updated from [http://repo.continuum.io/pkgs/](https://repo.continuum.io/pkgs/). You can modify what remote channels are automatically searched. See also [Managing packages](https://conda.io/docs/user-guide/tasks/manage-pkgs.html).

To install conda packages, in the Terminal or an Anaconda Prompt, run:

```shell
conda install [packagename]
```

# Conda Usage

You can use Conda with command line commands at the Anaconda Prompt for Windows, or in a Terminal window for macOS or Linux.

**check version**

```
conda --version
```

**update to latest version**

```
conda update conda
```

## managing environments

Conda allows you to to create separate environments containing files, packages and their dependencies that will not interact with other environments.

With conda, you can create, export, list, remove and update environments that have different versions of Python and/or packages installed in them. Switching or moving between environments is called activating the environment. You can also share an environment file.

When you begin using conda, you already have a default environment named `base`. You don’t want to put programs into your base environment, though. Create separate environments to keep your programs isolated from each other.

1. create a new environment and install packages

   ```
   conda create --name foo scrapy
   ```

   Create an environment named `foo` and install `scrapy` package.

   TIP: By default, environments are installed into the `envs` directory in your conda directory. 

2. activate/change to the new environment

   * Windows: `activate foo`
   * Linux/macOS: `source activate foo`

   When you have changed to the new environment, any conda commands you type will go to that environment until you deactivate it.

3. deactivate current environment back to the default(base)

   * Windows: `deactivate`
   * Linux/macOS: `source deactivate`

4. list all of your environments

   ```
   conda info --envs
   ```

   TIP: The active environment is the one with an asterisk (*).

## managing python

Conda treats Python the same as any other package, so it is easy to manage and update multiple installations.

**list available python versions**

To list the versions of Python that are available to install, in your Terminal window or an Anaconda Prompt, run:

```
conda search python
```

To list only the packages whose full name is exactly `python`, add the `--full-name` option.

```
conda search --full-name python
```

**create a new environment with specified python version**

When you create a new environment, conda installs the same Python version you used when you downloaded and installed Anaconda. If you want to use a different version of Python, for example Python 3.5, simply create a new environment and specify the version of Python that you want.

```
conda create --name foo python=3.5
```

To verify that the current environment uses the new Python version, in your Terminal window or an Anaconda Prompt, run:

```
python --version
```

**update python in an environment**

If you are in an environment with Python version 3.4.2, the following command updates Python to the latest version in the 3.4 branch:

```
conda update python
```

The following command upgrades Python to another branch—3.6—by installing that version of Python:

```
conda install python=3.6
```

## managing packages

* list installed packages in current environment

  ```
  conda list
  ```

* search packages from Anaconda repository (must be connected to the Internet)

  ```
  conda search scrapy
  ```

* install packages

  ```
  conda install scrapy
  ```

* update packages

  ```
  conda update scrapy
  ```

* remove packages

  ```
  conda remove scrapy
  ```

## managing channels

Different channels can have the same package, so conda must handle these channel collisions.

There will be no channel collisions if you use only the defaults channel. There will also be no channel collisions if all of the channels you use only contain packages that do not exist in any of the other channels in your list. The way conda resolves these collisions matters only when you have multiple channels in your channel list that host the same package.

The following command adds the channel “new_channel” to the top of the channel list, making it the highest priority:

```
conda config --prepend channels new_channel
```

Conda also now has a command that adds the new channel to the bottom of the channel list, making it the lowest priority:

```
conda config --append channels new_channel
```

## configuration

The Conda Runtime Configuration file, an optional `.yaml` file that allows you to configure many aspects of conda, such as which channels it searches for packages, proxy settings and environment directories. A `.condarc` file is not included by default, but it is automatically created in your home directory when you use the `conda config` command.

## metapackage

A conda package that only lists dependencies and does not include any functional programs or libraries. The metapackage may contain links to software files that are automatically downloaded when executed. An example of a metapackage is “anaconda,” which collects together all the packages in the Anaconda installer. The command `conda create -n envname anaconda` creates an environment that exactly matches what would be created from the Anaconda installer.

