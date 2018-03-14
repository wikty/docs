# 安装

## Yum

sers who want to maintain updates to the Git software will likely want to use `yum` to install Git

but the Git version that is installed this way may be older than the newest version available. If you need the latest release, consider compiling `git` from source

```
sudo yum install git
```



## Build by self

users who need features presented by a specific version of Git will want to build that version from source.

If you want to download the latest release of Git available, or simply want more flexibility in the installation process, the best method for you is to compile the software from source. This takes longer, and will not be updated and maintained through the `yum` package manager, but it will allow you to download a newer version than what is available through the CentOS repositories, and will give you some control over the options that you can include.

### install git dependencies first

```
sudo yum groupinstall "Development Tools"
sudo yum install gettext-devel openssl-devel perl-CPAN perl-devel zlib-devel
```

## download source

前往 git 在 github 上的[发布页面](https://github.com/git/git/releases)，获取最新稳定版本的链接，然后使用 `curl` 或 `wget` 下载源码，并重命名文件

```
wget https://github.com/git/git/archive/v2.1.2.tar.gz -O git.tar.gz
```

解压，然后切换到源码目录

```
tar -zxf git.tar.gz
cd git
```

生成软件依赖和硬件检查的脚本文件 `configure`

```
make configure
```

执行 pre-build，This script will also use a `--prefix` to declare `/usr/local` (the default program folder for Linux platforms) as the appropriate destination for the new binary，最终将会生成一个 `Makefile` 文件

```
./configure --prefix=/usr/local
```

执行 build 和 install，Makefiles are scriptable configuration files that are processed by the `make` utility. Our Makefile will tell `make` how to compile a program and link it to our CentOS installation so that we can execute the program properly. 大概做的事情就是：将源码编译成二进制，然后将其安装到合适的位置，此步骤可能需要 `sudo` 权限

```
sudo make install
```



# 配置

## git server

https://shenyu.me/2017/01/03/git-server.html

## git client

如果是在客户端安装 git 的话，需要将个人信息添加到 git，这样以后提交代码时可以附加个人信息

Now that you have `git` installed, you will need to submit some information about yourself so that commit messages will be generated with the correct information attached. To do this, use the `git config`command to provide the name and email address that you would like to have embedded into your commits:

```
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

```

To confirm that these configurations were added successfully, we can see all of the configuration items that have been set by typing:

```
git config --list

user.name=Your Name
user.email=you@example.com
```