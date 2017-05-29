## OpenShift

[OpenShift](https://www.openshift.com/) 是红帽（Red Hat）的应用开发云平台，该云平台支持部署基于 Java, PHP, Node.js, Python, Perl, MySQL, PostgreSQL, MongoDB, Cron 等技术的应用程序。而且在注册后可以，可以获得三个免费虚拟主机（内存 521M 硬盘 1 G），这些虚拟主机对于部署小型项目足够了。此外如果应用程序是非盈利目的，并且可以帮助到别人，OpenShift 为这类应用提供了[免费](https://www.openshift.com/grants/)托管服务。

### 术语介绍

在使用 OpenShift 时，会经常遇到一些专有术语用来描述云平台某些功能，下面将列举一些常见术语并做简短介绍

* Gear

  Gear 是虚拟主机、是代码容器。每个 Gear 都分配有 CPU 、内存、网络带宽等计算资源。我们创建好应用程序后，最终会部署在 Gear 中，由它来作为应用程序的主机。简单来说，可以将 Gear 看成是对物理主机的抽象。

* Cartridge

  在 OpenShift 云平台中，通过 Cartridge 为应用程序提供编程语言、框架、数据库等运行时软件环境。简单来说，可以将 Cartridge 看成是对软件环境的抽象。

* rhc

  [rhc](https://developers.openshift.com/managing-your-applications/client-tools.html) 是 OpenShift 基于命令行的客户端工具，可以使用它来创建、管理以及部署应用程序。除了 rhc 外，OpenShift 还提供了 [Web Console](https://openshift.redhat.com/app/console) 来管理应用程序。

## rhc 使用指南

### 安装

rhc 是 OpenShift 基于命令行的客户端工具，我们可以使用它来创建配置以及部署应用程序。

rhc 依赖 Ruby 和 Git ，Windows 用户分别分别前往：http://rubyinstaller.org/ 和 https://git-for-windows.github.io/ 下载并安装它们（其它操作系统用户，移步官网查看[教程](https://developers.openshift.com/managing-your-applications/client-tools.html)）。

* 安装 rhc

  Ruby 安装时，附带安装了用于管理 RubyRems 的包管理工具 gem ，而我们的 rhc 客户端就是一个包 ，安装 rhc 运行命令：`gem install rhc` 。

* 配置 rhc

  安装完 rhc 后，需要为其配置 OpenShift 账户名和密码，以及生成秘钥对并上传公钥到 OpenShift ，而这一切都可以通过运行交互式命令：`rhc setup ` 来完成（值得注意的是，该命令是交互式的，其中有一环节会询问是否创建秘钥对，如果电脑上已经有秘钥对，千万不要让新创建的秘钥对覆盖掉以前的秘钥对）。

### 创建应用

可以使用 rhc 在 OpenShift 云平台创建应用并将应用克隆到本地，运行命令：

```
rhc app-create -a <app_name> -t <web_cartridge_name>
```

其中 `<app_name>` 是自己定义的应用名称；`<web_cartridge_name>` 是为应用指定的软件环境（用命令 `rhc cartridge-list` 可查看当前可用软件环境）。

除了使用 rhc 创建应用外，还可以在 OpenShift 提供的 [Web Console](https://openshift.redhat.com/app/console/) 上创建应用，应用创建好之后再通过 `git clone` 命令来克隆到本地进行开发。

### 部署应用

通过以上方式克隆到本地的应用包含了 OpenShift 远程仓库的地址，并且 OpenShift 为应用提供了自动构建以及部署功能。本地修改后的项目，只需要通过 `git push` 就可以将代码提交至 OpenShift 虚拟主机，并触发 OpenShift 自动构建和部署应用。

### 常用命令

#### 账户信息

* 配置账户以及秘钥信息：`rhc setup`
* 查看 Gear 使用情况：`rhc account`
* 查看所有应用信息：`rhc domain-show`

#### 管理应用状态

以下命令假设在应用目录执行，如果在其它目录执行，需要添加命令参数指定应用名 `--app <appname>`

* 查看应用信息：`rhc app-show -v`
* 查看应用磁盘空间用量：`rhc app-show --gears quota`
* 查看应用的 SSH 信息：`rhc app-show --gears ssh`
* 启动、停止、强制停止、重启应用：`rhc app-{start|stop|force-stop|restart}`
* 清除日志和临时文件来释放磁盘空间：`rhc app-tidy`
* 持续查看应用的日志文件尾部：`rhc tail`

####  管理应用 cartridges

以下命令假设在应用目录执行，如果在其它目录执行，需要添加命令参数指定应用名 `--app <appname>`

* 查看可用 cartridge ：`rhc cartridge-list`
* 添加 cartridge ：`rhc cartridge-add <cartridgename>`
* 移除 cartridge ：`rhc cartridge-remove <cartridgename> `

#### 远程连接应用

以下命令假设在应用目录执行，如果在其它目录执行，需要添加命令参数指定应用名 `--app <appname>`

* SSH 连接到应用服务器：`rhc ssh`
* 本地端口数据转发到远程服务器：`rhc port-forward`
* 上传本地数据到应用服务器：`rhc <apppname> upload <local-file-path> <remote-file-path-relative-home-dir>`
* 下载服务器远程数据到本地：`rhc <appname> download <local-file-path> <remote-file-path-relative-home-dir>`

#### 管理应用环境变量

以下命令假设在应用目录执行，如果在其它目录执行，需要添加命令参数指定应用名 `--app <appname>`

* 查看应用的所有环境变量：`rhc env-list`
* 设置环境变量：`rhc env-set var1=value1 var2=value2`
* 通过文件内容来设置环境变量，文件中每一行内容都一个 `variable=value` ：`rhc env-set <path-to-file>`
* 删除环境变量：`rhc env-unset var1 var2`

## 数据库

数据库在 OpenShift 中也是 Cartridge。目前 OpenShift 支持 [MySQL](https://www.mysql.com/), [PostgreSQL](https://www.postgresql.org/), [MongoDB](https://www.mongodb.com/), [SQLite](https://sqlite.org/) 等数据库， 想要为应用添加数据库也十分简单。尤其是 SQLite ，OpenShift 默认 SQLite 是任何应用的标配，可以直接在命令行调用 `sqlite3` 来访问该数据库。

### 添加数据库

创建应用时添加

```
rhc app-create <myappname> <webcartridge> <dbcartridge>
```

创建应用后添加

```
rhc cartridge-add <dbcartridge> --app <myappname>
```

其中 `<myappname>` 表示应用名；`<dbcartridge>` 表示相应的数据库 Cartridge（有哪些数据库 Cartridge 可用，请使用运行查询命令：`rhc cartridge list`）。

当然除了通过 rhc 添加数据库外，也可以使用 OpenShift 的 Web 控制台来添加数据库。

### 连接数据库

在为应用添加数据库之后，OpenShift 自动将连接数据库的相关参数配置到了相应变量中，不过不同数据库用来存放数据库参数的环境变量是不一样的，查看应用的数据库连接参数：

```
rhc app show <myappname> -v
```

下面简单介绍 OpenShift 存入应用环境变量的数据库连接参数，其中 `<database>` 用来指代对应的数据库：

* `OPENSHIFT_<database>_DB_HOST` 数据库服务器所在主机名（或 IP 地址），比如：`127.0.0.1`
* `OPENSHIFT_<database>_DB_PORT` 数据库服务器所在端口，比如：`3306`
* `OPENSHIFT_<database>_DB_USERNAME` 连接数据库的用户名，比如：`root`
* `OPENSHIFT_<database>_DB_PASSWORD` 连接数据库用户的密码，比如：`123456`
* `OPENSHIFT_<database>_DB_URL` 连接数据库的 URL，比如：`mysql://root:123456@127.0.250.1:3306/`
* `OPENSHIFT_<database>_DB_SOCKET` 连接数据库的 socket，比如：`$OPENSHIFT_HOMEDIR/mysql-5.1/socket/mysql.sock`

除了上面介绍的环境变量外，下面再介绍一些在 MySQL 中独有的参数：

* `OPENSHIFT_MYSQL_DB_LOG_DIR` 数据库日志目录
* `OPENSHIFT_MYSQL_TIMEZONE` 数据库服务器的时区设置
* `OPENSHIFT_MYSQL_MAX_CONNECTIONS` 允许同时连接到数据库的客户端数量
* `OPENSHIFT_MYSQL_DEFAULT_STORAGE_ENGIN` 数据库默认储存引擎

不同编程语言访问环境变量的语法是不一样的，比如要读取 MySQL 连接 URL 的环境变量，在 PHP 中可以通过 `getenv('OPENSHIFT_MYSQL_DB_URL');` 来读取，而在 Python 需要先导入 `os` 模块，然后通过 `os.environ['OPENSHIFT_MYSQL_DB_URL']` 来读取。

### 数据库管理后台

在 OpenShift 中 [phpMyAdmin](https://www.phpmyadmin.net/) 也是一个 Cartridge，要为安装了 MySQL 数据库的应用添加 Web 管理后台轻而易举，只需要运行以下命令

```
rhc cartridge-add phpmyadmin-4 --app <myappname>
```

其中 `phpmyadmin-4` 表示安装 phpMyAdmin 4.0 ，要安装其它版本，做相应替换即可；`<myappname>` 表示应用名。

此外 OpenShift 还为 MongoDB 提供了类似于 phpMyAdmin 的 Web 管理后台 [RockMongo](https://github.com/iwind/rockmongo)，添加这个 Web 后台程序跟上面添加 phpMyAdmin 一样简单。

## Action Hook Scripts

OpenShift 提供的 Cartridge 可以实现应用程序自动构建和部署，同时还允许开发者使用 Action Hook Scripts 来参与到应用构建和部署的特定阶段。

### 创建脚本

Action Hook Scripts 是位于项目 `.openshift/action_hooks/` 目录中的脚本文件，这些脚本可以用 Shell, Python, PHP, Ruby 中任一种语言来编写，脚本命名跟其参与控制的阶段相对应，最为常见的也就是 `build` 阶段，应用在该阶段进行构建，通常我们通过编写脚本 `.openshift/action_hooks/build` 来控制应用的构建过程，比如在 PHP 应用中，可以在构建应用期间下载应用依赖的第三方库。此外还有 `pre_build`, `deploy`, `post_deploy` 也是应用构建和部署期间较为常见的 hook scripts。

要注意，Action Hook Scripts 必须具有可执行属性，在 Linux 中通过 `chmod +x <scriptname>` 为脚本添加可执行属性，Windows 中通过 `git update-index --chmod=+x .openshift/action_hooks/*` 添加可执行属性。

## 定时任务

许多web 应用程序依赖 cron 定时任务来执行一些常规任务，比如：清除临时文件、备份数据库、生成日志报告等。

### 创建定时任务

由于 cron 如此重要，OpenShift 将 cron 作为 Cartridge 供开发者使用，要想在应用中添加 cron，只需运行：

```
rhc cartridge add cron -a <appname>
```

要为应用创建定时任务，只需要将定时任务 shell 脚本放在 `.openshift/cron` 中的子目录 `minutely`, `hourly`, `daily`, `monthly`, `monthly` 下，并且这些定时任务脚本必须是可执行，Linux 中通过 `chmod +x <scriptname>` 为脚本添加可执行属性，Windows 中在提交脚本时添加可执行属性 `git update-index --chmod=+x <scriptname>`。

### 高精度定时任务

定时任务的工作原理是，cron 会以固定频率查看哪些定时任务应该被执行时，就执行相应的任务脚本。但由于 cron 查看定时任务存在时间间隔，所以任务执行的时间精度比较低，如果想要让任务以分钟级精度来执行，就需要通过脚本代码来控制了，下面是一个位于目录 `minutely` 的定时任务脚本（每分钟都运行该脚本）：

```
#!/bin/bash
minute=$(date '+%M')
if [ $minute != 12 ]; then
    exit
fi
# 判断当前时间为 12 分时，才执行以下脚本内容
# 也即以下代码定义的定时任务会在每个小时的12分时执行
# rest of the script
```

或者

```
#!/bin/bash
if [ ! -f $OPENSHIFT_DATA_DIR/last_run ]; then
  touch $OPENSHIFT_DATA_DIR/last_run
fi
if [[ $(find $OPENSHIFT_DATA_DIR/last_run -mmin +4) ]]; then #run every 5 mins
  rm -f $OPENSHIFT_DATA_DIR/last_run
  touch $OPENSHIFT_DATA_DIR/last_run
  # 通过创建一个文件来记录任务最近一次运行时间，进而实现每五分钟运行一次
  # The command(s) that you want to run every 5 minutes
fi
```

## 应用备份和恢复

OpenShift 支持应用备份和恢复，应用的备份就是创建了一份应用程序运行时的快照，备份内容不限于应用代码、相关组件的配置、数据库数据以及日志数据，可以说是对应用所有方面完完全全的备份，并且 OpenShift 支持利用应用备份的快照原样恢复应用。

### 备份

备份应用十分简单，只要运行命令

```
rhc snapshot-save <appname>
```

就会在当前目录下生成应用备份文件 `appname.tar.gz` ，传入参数 `--filepath` 可以自定义备份文件的路径。

### 恢复

恢复应用十分简单，只要运行命令

```
rhc snapshot-restore <appname>
```

就会使用当前目录下的备份文件 `appname.tar.gz` 来恢复应用 `appname` ，如果备份文件跟应用名不同，可以传入参数 `--filepath` 来指定备份文件路径。

值得注意的是，应用恢复时会完全更新 OpenShift 上应用的数据，也就是说任何在备份之后、恢复之前对应用的修改都会丢掉。

## PHP 开发

PHP 常见框架在 OpenShift 均得到很好的支持，OpenShift 官网和社区维护了常见框架 [CakePHP](https://hub.openshift.com/quickstarts/73-cakephp), [WordPress](https://hub.openshift.com/quickstarts/1-wordpress-4), [Drupal](https://hub.openshift.com/search?query=drupal), [Laravel](https://hub.openshift.com/quickstarts/115-laravel-5-0), [CodeIgniter](https://hub.openshift.com/quickstarts/16-codeigniter), [Symfony 2.3.6](https://hub.openshift.com/quickstarts/34-symfony-2-3-6), 和 [Piwik](https://hub.openshift.com/quickstarts/3-piwik) 的 Cartridge，它们为基于这些框架的应用提供了模板应用程序，是不错的开发起点。

### 创建应用

可以通过 Web [控制台](https://openshift.redhat.com/app/console/)或者 rhc 来创建应用。使用 Web 控制台创建的应用需要手动克隆到本地进行开发，而使用 rhc 创建的应用会自动克隆到本地，以下是创建 PHP 应用（基于 PHP 5.4，没有使用任何框架）的 rhc 命令

```
rhc app create myphpapp php-5.4
```

应用创建完成后，我们会得到一个模板应用，可以将这个应用作为一个起点进行后续的开发，PHP 模板应用的目录结构如下

```
├─ index.php								应用模板的首页
└─.openshift							
    ├─action_hooks							action hooks 目录
    ├─markers
    └─pear.txt								pear 依赖项
```

根据 Web 控制台的应用信息或者 rhc 命令创建应用后返回的内容，可以得到该项目的 URL 地址，在浏览器输入地址后可以看到模板应用的首页内容。

### 部署应用

当想要部署应用时，仅仅只需要通过 Git 提交并推送到 OpenShift 即可，运行命令 `git push` 后，代码会自动推送到 OpenShift 云平台，OpenShift 会关闭服务器、构建应用、部署应用、最后再重启服务器。开发者只需要将代码 push 到 OpenShift 即可，OpenShift 会自动完成后续构建以及部署工作，不过 OpenShift 也提供了一些 Action Hooks 让开发者来控制应用构建部署过程。

热部署，是一种不重启服务器的情况下部署应用的方案。常规部署方法使得，应用有一段时间是不可用的，而热部署就是一种最小化不可用时间的部署方案，OpenShift 支持 PHP 应用的热部署，只需要创建一个空文件 `.openshift/markers/hot_deploy` 并将其推送至 OpenShift，在部署该应用时 OpenShift 就会采用热部署方案。

### 设置文档跟目录

OpenShift 默认使用 Apache 服务器来运行 PHP 应用程序，为了让服务器正确的运行应用程序，需要告知服务器应用程序的入口在哪里，也即要配置 Apache 的 DocumentRoot。刚刚生成的模板应用，根目录中含有 `index.php` 并且可以通过浏览器访问该页面，说明应用根目录就是 DocumentRoot 。其实准确来讲应用根目录只是一个候选 DocumentRoot，OpenShift 默认会依次查找以下路径，将找到的第一个位置作为 DocumentRoot

```
php/
public/
public_html/
web/
www/
./
```

以上目录名几乎囊括了主流 PHP 框架默认的应用入口位置，所以在大多数情况下，是不需要配置 DocumentRoot 的。

### 管理第三方依赖

要想添加 [PEAR](http://pear.php.net/) 依赖，只需将依赖的第三方库名添加到应用中的文件 `.openshift/pear.txt` （该文件每行内容对应一个库名），并将该文件提交到 OpenShift，OpenShift 会自动为该应用加载依赖的这些第三方库。此外，如果想通过依赖管理工具 [Composer](https://getcomposer.org/) 来管理第三方库，则需要将相关命令写入 Action Hook Script 文件 `.openshift/action_hooks/build` 中，使得 OpenShift 在构建应用时加载第三方库。

另外，OpenShift 会将以下路径会添加到 PHP 的 `include_path` 中，这样在调用 `require`, `include`, `fopen`, `readfile`, `file_get_contents` 等这些函数时就会搜索以下目录，查找是否含有目标文件：

```
lib/
libs/
libraries/
src/
misc/
vendor/
vendors/
```

不过要注意，将以上目录添加到 `include_path` 跟类的自动加载是两回事。`include_path` 只是一个目录列表，在使用一些涉及到文件查找的函数时，PHP 会自动从 `include_path` 定义的目录中查找。而类的自动加载机制，用来解决手动加载被引用类的问题，也即无需在脚本中通过 `include` 和 `require` 来手动加载被引用的类，Composer 在安装第三方库的同时提供了自动加载脚本 `vendor/autoload.php` ，只要在应用入口包含该脚本，就可以实现对第三方库的自动加载。

### PHP Markers

marker 文件是 OpenShift 让开发者控制 cartridge 构建和应用部署的简单办法，这些文件中没有任何内容，仅仅根据其存在与否来发挥控制作用（就像标记一样）。marker 文件位于目录 `.openshift/markers/` 中，在 PHP 应用中，主要有以下这些 marker 文件来控制构建和部署：

- `fore_clean_build` 

  移除之前安装的所有依赖项，重新安装必须的依赖项。

- `hot_deploy`

  阻止在应用构建和部署期间重启服务器，即设置应用进行热部署。

- `disable_auto_scaling`

  阻止应用根据负载而自动伸缩。

- `user_composer`

  指定在应用每次构建时，OpenShift 自动运行命令 `composer install` 。

- `enable_public_server_status`

  设置服务器状态应用程序可公开访问。

### 环境变量

PHP cartridge 提供了 `OPENSHIFT_PHP_IP` 和 `OPENSHIFT_PHP_PORT` 来存放应用的 IP 和 Port，并且重写了一些 PHP 的默认配置项，比如： `APPLICATION_ENV`, `LOGSHIFTER_PHP_MAX_FILESIZE`, `OPENSHIFT_PHP_APC_ENABLED` 等。

通过 rhc 设置环境变量 `rhc env set APPLICATION_ENV=production` 。在 PHP 脚本中访问环境变量  `$env_var = getenv('APPLICATION_ENV');` 。

### 开启开发模式

可以通过环境变量 `APPLICATION_ENV` 来配置应用是在开发环境还是在生成环境，命令如下：

```
rhc env set APPLICATION_ENV=development
```

注：改变环境变量后，只有重启应用才能生效  `rhc app restart`

## 端口转发

SSH 协议支持端口转发，利用协议的这个特点，我们可以从本地通过 SSH 加密隧道访问远程服务器未公开的端口，比如 OpenShift 服务器只允许访问公开端口 `22`, `80`, `443`, `8000`, `8443` ，通过从本地到远程服务器建立隧道，我们就可以访问监听在远程服务器上其它非公开端口的服务了。

### 原理及应用场景

利用 SSH 端口转发来实现本地到远程通过隧道连接，其原理十分简单。在本地通过 SSH 客户端软件来跟远程服务器建立隧道连接，同时 SSH 客户端会在本地端口开启监听，并将到达该端口的数据通过隧道转发给远程服务器。

一般会在以下场景使用端口转发功能：

* 通过运行在本地的数据库管理后台来访问远程数据库（OpenShift 数据库端口是不公开的）
* 本地调试应用时使用远程数据库
* 访问远程服务器监听在非公开端口的管理后台

### 开启转发

OpenShift 客户端工具 rhc 对端口转发提供了很好的支持，只需要运行命令 `rhc port-forward --app <appname>` 就可以在本地开启若干端口，并将到达这些端口请求转发至相应远程服务器上的端口。运行以上命令后，会得到类似下面这样的反馈信息

```
Service Local               OpenShift
------- -------------- ---- -----------------
httpd   127.0.0.1:8080  =>  127.7.81.129:8080
httpd   127.0.0.1:8081  =>  127.7.81.131:8080
mysql   127.0.0.1:3306  =>  127.7.81.130:3306

Press CTRL-C to terminate port forwarding
```

这些反馈信息用来表明，对本地哪些端口的请求会被相应的转发至远程服务器的哪个端口（服务）。

