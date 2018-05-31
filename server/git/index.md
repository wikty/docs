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



## Introduction

Git was designed and developed by [Linus Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds) for Linux kernel development. Git provides support for non-linear, distributed development, allowing multiple contributors to work on a project simultaneously. Git is the most popular distributed version control and source code management system

# 配置

## git server



使用 `authorized_keys` 的授权方式允许开发者访问远程 Git 仓库。



首先创建 `git` 用户并该用户创建 `.ssh` 目录和 `authorized_keys` 文件

```
$ sudo adduser git
$ sudo passwd git
$ su git
$ cd
$ mkdir .ssh && chmod 700 .ssh
$ touch .ssh/authorized_keys && chmod 600 .ssh/authorized_keys
```



然后将各个开发者的 SSH 公开秘钥添加到刚刚在远程服务器上创建的 `authorized_keys` 文件中

假设远程服务器上现在是 `git` 用户登录，并且开发者的公钥在文件 `/tmp/id_rsa.john.pub` 中，将其追加到 `authorized_keys` 文件

```
$ cat /tmp/id_rsa.john.pub >> ~/.ssh/authorized_keys
```



然后，依然是 `git` 用户登录在远程服务器，创建 bare 仓库

```
$ cd /srv/git
$ mkdir project.git
$ cd project.git
$ git init --bare
Initialized empty Git repository in /srv/git/project.git/
```

注：推荐将 git 仓库放在 `/srv/git/` 或 `/var/git/` 目录下面（https://serverfault.com/questions/432959/wheres-the-conventional-place-to-store-git-repositories-in-a-linux-file-system）



然后开发者可以在本地 push 以及 clone 该远程仓库了，假设开发者可以通过域名 `gitserver` 来访问服务器

开发者初次提交项目到远程

```
# on John's computer
$ cd myproject
$ git init
$ git add .
$ git commit -m 'initial commit'
$ git remote add origin git@gitserver:/srv/git/project.git
$ git push origin master
```

其它开发者克隆该项目

```
$ git clone git@gitserver:/srv/git/project.git
$ cd project
$ vim README
$ git commit -am 'fix for the README file'
$ git push origin master
```



基于以上设置后，任何人都可以通过 SSH 以 `git` 用户的身份登录服务器，这样会存在安全隐患，因此接来下要限制 `git` 用户的 shell

You should note that currently all these users can also log into the server and get a shell as the `git` user. If you want to restrict that, you will have to change the shell to something else in the `passwd` file.

You can easily restrict the `git` user to only doing Git activities with a limited shell tool called `git-shell` that comes with Git. If you set this as your `git` user’s login shell, then the `git` user can’t have normal shell access to your server. To use this, specify `git-shell` instead of bash or csh for your user’s login shell. To do so, you must first add `git-shell` to `/etc/shells` if it’s not already there:

```
$ cat /etc/shells   # see if `git-shell` is already in there.  If not...
$ which git-shell   # make sure git-shell is installed on your system.
$ sudo vim /etc/shells  # and add the path to git-shell from last command
```

Now you can edit the shell for a user using `chsh <username> -s <shell>`:

```
$ sudo chsh git -s $(which git-shell)
```

Now, the `git` user can only use the SSH connection to push and pull Git repositories and can’t shell onto the machine. If you try, you’ll see a login rejection like this:

```
$ ssh git@gitserver
fatal: Interactive git shell is not enabled.
hint: ~/git-shell-commands should exist and have read and execute access.
Connection to gitserver closed.
```



将已经存在的项目放在远程服务器上

首先克隆项目的裸仓库

```
$ git clone --bare my_project my_project.git
Cloning into bare repository 'my_project.git'...
done.
```

然后将该裸仓库复制到服务器上，假设服务器是 `gitserver` ，服务器上运行 Git 服务的用户名是 `git` ，且已经存在放裸仓库的父目录 `/srv/git/`，在本地利用 `scp` 来复制裸仓库到远程服务器

```
scp -r my_project.git git@gitserver:/srv/git
```

至此所有对该远程仓库拥有读写权限的用户就可以 pull/push 了







似乎经过上面的设置，即使对于小型团队也是不够的，比如所有的开发者拥有对所有仓库的读写权利，这样显然是有问题的，如果想要设置仓库对不同用户的权限，需要继续下面的步骤

If you’re a small outfit or are just trying out Git in your organization and have only a few developers, things can be simple for you. One of the most complicated aspects of setting up a Git server is user management. If you want some repositories to be read-only for certain users and read/write for others, access and permissions can be a bit more difficult to arrange.

One of the most complicated aspects of setting up a Git server is user management. If you want some repositories to be read-only for certain users and read/write for others, access and permissions can be a bit more difficult to arrange.

如果团队里的每个人都拥有服务器的 SSH 登录权限，如果想要控制开发者对仓库的权限，只需要控制服务器上用户对文件的正常读写权限即可。

如果团队中不是所有人都拥有 SSH 登录权限，要想将某个仓库的权限授予开发者，可以在服务器上为开发者 `adduser` 添加账户和密码，这样做难免会有点繁琐。更常见的作法是，在服务器上创建一个 `git` 用户，并将想要授予写权限的开发者的 SSH 公钥添加到 `git` 用户的 `~/.ssh/authorized_keys` 文件中。注：这并不会影响 git 的提交记录，SSH 登录账户跟 git 提交记录是两回事。并不是说以 `git` 用户登录到服务器，就意味着是以该用户提交的。



经过上面的设置后，可以允许少数开发者通过 SSH 来读写 Git 远程仓库了。对于小项目来说这已经足够了，如果有更多需求的话，还需要更加复杂的配置 Git 服务

In the next few sections, you’ll see how to expand to more sophisticated setups. This discussion will include not having to create user accounts for each user, adding public read access to repositories, setting up web UIs and more. However, keep in mind that to collaborate with a couple of people on a private project, all you *need* is an SSH server and a bare repository.



Git 图像界面接口

Now that you have basic read/write and read-only access to your project, you may want to set up a simple web-based visualizer. Git comes with a CGI script called GitWeb that is sometimes used for this.

If you want to check out what GitWeb would look like for your project, Git comes with a command to fire up a temporary instance if you have a lightweight web server on your system like `lighttpd` or `webrick`. On Linux machines, `lighttpd` is often installed, so you may be able to get it to run by typing `git instaweb` in your project directory. If you’re running a Mac, Leopard comes preinstalled with Ruby, so `webrick` may be your best bet. To start `instaweb` with a non-lighttpd handler, you can run it with the `--httpd` option.

```
$ git instaweb --httpd=webrick
```

GitWeb is pretty simplistic though. If you’re looking for a more modern, fully featured Git server, there are some several open source solutions out there that you can install instead. As GitLab is one of the more popular ones, we’ll cover installing and using it as an example. This is a bit more complex than the GitWeb option and likely requires more maintenance, but it is a much more fully featured option.





https://www.digitalocean.com/community/tutorials/how-to-set-up-a-private-git-server-on-a-vps

This can be a great option if you want to keep your code private while you work. While open-souce tends to be the status quo, there are some times when you don't want to have your code freely available.

There is one major concern for many and that is a web interface to your repositories. GitHub accomplishes this amazingly well. There are applications that you can install such as [Gitosis](https://wiki.archlinux.org/index.php/Gitosis), [GitList](http://gofedora.com/insanely-awesome-web-interface-git-repos/), and [Goblet](http://git.kaarsemaker.net/). We don't go over those in this tutorial, but if you rely heavily on a graphic interface then you may want to look over those and think about installing one of them as soon as you done installing your Git server.

图形接口和 SSH 协议接口。

In this tutorial we are going to talk about two methods of managing your code on your own server. One is running a bare, basic Git server and and the second one is via a GUI tool called [GitLab](https://about.gitlab.com/).



https://git-scm.com/book/en/v2/Git-on-the-Server-Setting-Up-the-Server



开发者 SSH 秘钥创建

https://help.github.com/articles/generating-ssh-keys

首先检查 `~/.ssh` 目录下是否已经存在秘钥

```
ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/schacon/.ssh/id_rsa):
Created directory '/home/schacon/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/schacon/.ssh/id_rsa.
Your public key has been saved in /home/schacon/.ssh/id_rsa.pub.
The key fingerprint is:
d0:82:24:8e:d7:f1:bb:9b:33:53:96:93:49:da:9b:e3 schacon@mylaptop.local
```



### git server 官方教程

Running a Git server is fairly straightforward. First, you choose which protocols you want your server to communicate with. The first section of this chapter will cover the available protocols and the pros and cons of each. The next sections will explain some typical setups using those protocols and how to get your server running with them. Last, we’ll go over a few hosted options, if you don’t mind hosting your code on someone else’s server.



A remote repository is generally a *bare repository* — a Git repository that has no working directory. Because the repository is only used as a collaboration point, there is no reason to have a snapshot checked out on disk; it’s just the Git data. In the simplest terms, a bare repository is the contents of your project’s `.git` directory and nothing else.



git 支持的各种通信协议：

Git can use four distinct protocols to transfer data: Local, HTTP, Secure Shell (SSH) and Git.

* Local Protocol

The most basic is the *Local protocol*, in which the remote repository is in another directory on the same host. This is often used if everyone on your team has access to a shared filesystem such as an NFS mount, or in the less likely case that everyone logs in to the same computer. The latter wouldn’t be ideal, because all your code repository instances would reside on the same computer, making a catastrophic loss much more likely.

 To clone a repository like this, or to add one as a remote to an existing project, use the path to the repository as the URL. For example, to clone a local repository, you can run something like this:

```
$ git clone /srv/git/project.git
```

Or you can do this:

```
$ git clone file:///srv/git/project.git
```

To add a local repository to an existing Git project, you can run something like this:

```
$ git remote add local_proj /srv/git/project.git
```

Then, you can push to and pull from that remote via your new remote name `local_proj` as though you were doing so over a network.

* The HTTP Protocols: Smart HTTP & DumbHTTP

Git can communicate over HTTP using two different modes. Prior to Git 1.6.6, there was only one way it could do this which was very simple and generally read-only. In version 1.6.6, a new, smarter protocol was introduced that involved Git being able to intelligently negotiate data transfer in a manner similar to how it does over SSH. In the last few years, this new HTTP protocol has become very popular since it’s simpler for the user and smarter about how it communicates. The newer version is often referred to as the *Smart* HTTP protocol and the older way as *Dumb*HTTP.

Smart HTTP operates very similarly to the SSH or Git protocols but runs over standard HTTPS ports and can use various HTTP authentication mechanisms, meaning it’s often easier on the user than something like SSH, since you can use things like username/password authentication rather than having to set up SSH keys.

It has probably become the most popular way to use Git now, since it can be set up to both serve anonymously like the `git://` protocol, and can also be pushed over with authentication and encryption like the SSH protocol. Instead of having to set up different URLs for these things, you can now use a single URL for both. If you try to push and the repository requires authentication (which it normally should), the server can prompt for a username and password. The same goes for read access.

If the server does not respond with a Git HTTP smart service, the Git client will try to fall back to the simpler *Dumb* HTTP protocol. The Dumb protocol expects the bare Git repository to be served like normal files from the web server. The beauty of Dumb HTTP is the simplicity of setting it up. Basically, all you have to do is put a bare Git repository under your HTTP document root and set up a specific `post-update` hook, and you’re done

* The SSH Protocol

A common transport protocol for Git when self-hosting is over SSH. This is because SSH access to servers is already set up in most places — and if it isn’t, it’s easy to do. SSH is also an authenticated network protocol and, because it’s ubiquitous, it’s generally easy to set up and use.

To clone a Git repository over SSH, you can specify an `ssh://` URL like this:

```
$ git clone ssh://[user@]server/project.git
```

Or you can use the shorter scp-like syntax for the SSH protocol:

```
$ git clone [user@]server:project.git
```

In both cases above, if you don’t specify the optional username, Git assumes the user you’re currently logged in as.

The negative aspect of SSH is that it doesn’t support anonymous access to your Git repository. If you’re using SSH, people *must* have SSH access to your machine, even in a read-only capacity, which doesn’t make SSH conducive to open source projects for which people might simply want to clone your repository to examine it. If you’re using it only within your corporate network, SSH may be the only protocol you need to deal with. If you want to allow anonymous read-only access to your projects and also want to use SSH, you’ll have to set up SSH for you to push over but something else for others to fetch from.

* The Git Protocol

Next is the Git protocol. This is a special daemon that comes packaged with Git; it listens on a dedicated port (9418) that provides a service similar to the SSH protocol, but with absolutely no authentication. In order for a repository to be served over the Git protocol, you must create a `git-daemon-export-ok` file — the daemon won’t serve a repository without that file in it — but other than that there is no security. Either the Git repository is available for everyone to clone, or it isn’t. This means that there is generally no pushing over this protocol. You can enable push access but, given the lack of authentication, anyone on the internet who finds your project’s URL could push to that project. Suffice it to say that this is rare.

The Git protocol is often the fastest network transfer protocol available. If you’re serving a lot of traffic for a public project or serving a very large project that doesn’t require user authentication for read access, it’s likely that you’ll want to set up a Git daemon to serve your project. It uses the same data-transfer mechanism as the SSH protocol but without the encryption and authentication overhead.

The downside of the Git protocol is the lack of authentication. It’s generally undesirable for the Git protocol to be the only access to your project. Generally, you’ll pair it with SSH or HTTPS access for the few developers who have push (write) access and have everyone else use `git://`for read-only access.



## 第三方托管方案

You have several options to get a remote Git repository up and running so that you can collaborate with others or share your work.

Running your own server gives you a lot of control and allows you to run the server within your own firewall, but such a server generally requires a fair amount of your time to set up and maintain. If you place your data on a hosted server, it’s easy to set up and maintain; however, you have to be able to keep your code on someone else’s servers, and some organizations don’t allow that.

It should be fairly straightforward to determine which solution or combination of solutions is appropriate for you and your organization.

If you don’t want to go through all of the work involved in setting up your own Git server, you have several options for hosting your Git projects on an external dedicated hosting site. Doing so offers a number of advantages: a hosting site is generally quick to set up and easy to start projects on, and no server maintenance or monitoring is involved. Even if you set up and run your own server internally, you may still want to use a public hosting site for your open source code – it’s generally easier for the open source community to find and help you with.

These days, you have a huge number of hosting options to choose from, each with different advantages and disadvantages. To see an up-to-date list, check out the GitHosting page on the main Git wiki at [https://git.wiki.kernel.org/index.php/GitHosting](https://git.wiki.kernel.org/index.php/GitHosting)

We’ll cover using GitHub in detail in [GitHub](https://git-scm.com/book/en/v2/ch00/ch06-github), as it is the largest Git host out there and you may need to interact with projects hosted on it in any case, but there are dozens more to choose from should you not want to set up your own Git server.



## git client

After you [install Git](https://linode.com/docs/development/version-control/how-to-install-git-on-mac-and-windows), configure it for first time use using `git config`, a built-in tool that obtains and sets configuration variables. These configuration variables are located in three different places on a GNU/Linux system:

- `/etc/gitconfig` - stores the configuration information for all system users and their respective repositories.
- `~/.gitconfig` - stores user-specific configuration files on the system.
- `.git/config` - this is the configuration file of your current working repository.

For a Windows system, the `.gitconfig` file is located in the `$HOME` directory of the user’s profile. The full path is `C:\Document and Settings\$USER` or `C:\Users\$USER`

After installing Git make sure your username and email address are set correctly. To verify, use the command:

```
git config --list
```

If your name and email are not listed in the output, use the following commands to set them manually, replacing `examplename` and `user@example.com`:

```
git config --global user.name examplename
git config --global user.email user@example.com
```





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