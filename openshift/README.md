

## rhc 使用指南

### rhc 介绍及安装

rhc 是 OpenShift 基于命令行的客户端工具，我们可以使用它来创建配置以及部署 OpenShift 项目。

rhc 依赖 Ruby 和 Git ，分别前往（Windows）：http://rubyinstaller.org/ 和 https://git-for-windows.github.io/ 下载并安装它们（如果想要安装 Ruby 的版本控制工具，移步 https://rvm.io/ ）。安装好 Ruby 的同时，会附带安装好用于管理 RubyRems 的包管理工具 `gem` ，而我们的 rhc 客户端就是一个 gem ，安装 rhc 命令为 `gem install rhc` 。

### rhc 初次使用

初次使用 rhc 需要为其配置 OpenShift 账户名和密码，以及生成秘钥对并上传秘钥到 OpenShift 。而这一切都可以通过运行命令 `rhc setup` ，然后跟着提示来完成。

### rhc 创建应用

可以使用 rhc 来在 OpenShift 云平台创建应用并将应用克隆到本地，运行命令 `rhc app create <app_name> <web_cartridge_name>` 。

其中 `<app_name>` 是自己定义的应用名称；`<web_cartridge_name>` 为应用指定的语言或者框架，其实 OpenShift 将语言、框架、数据库等这些资源统一抽象为 cartridge ，查询可用 cartridge 的命令 `rhc cartridge list` 。

除了使用 rhc 创建应用外，还可以在 OpenShift 提供的 Web [控制台](https://openshift.redhat.com/app/console/)上创建应用，应用创建好之后再通过 `git clone` 命令来克隆到本地。

### 部署项目

通过将以上方式克隆到本地的项目包含了 OpenShift 远程仓库的地址，并且 OpenShift 为项目默认提供了自动构建以及部署功能。本地修改后的项目，只需要通过 `git push` 就可以将代码提价至 OpenShift ，并由 OpenShift 自动构建和部署项目。



### 首次使用创建并上传公钥

```
rhc setup
```

### 创建应用（远程和本地）

```
rhc app create -a myapp -t php-5.4
```

### 添加 PHP 扩展

* 通过文件 `.openshift/pear.txt` 定义依赖扩展，例如：

  ```
  net_url
  auth_sasl
  ```

* 通过 hooks 使用包管理器加载扩展

* ​

### Action Hooks Scripts

在目录 `.openshift/action_hooks/` 中用来构建期间

脚本可执行

使用命令 `chmod`

```
chmod +x <scriptname>
```

使用命令 `git`

```
git update-index --chmod=+x .openshift/action_hooks/*
```













https://developers.openshift.com/managing-your-applications





### 构建 PHP 应用

1. 创建应用

   可以通过 Web [控制台](https://openshift.redhat.com/app/console/)或者 rhc 来创建应用。使用 Web 控制台创建的应用需要手动克隆到本地进行开发，而使用 rhc 创建的应用会自动克隆到本地，以下是创建 PHP 应用（基于 PHP 5.4）的 rhc 命令

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

2. Apache DocumentRoot

   模板应用位于项目根目录的 `index.php` 可以通过外部访问，说明项目根目录就是  DocumentRoot 。其实项目根目录只是一个候选的 DocumentRoot，OpenShift 默认会依次查找以下路径，将找到的第一个位置作为  DocumentRoot

   ```
   php/
   public/
   public_html/
   web/
   www/
   ./
   ```

   以上目录名几乎囊括了主流 PHP 框架默认的项目根目录位置。

3. 项目本地依赖

   以下路径会自动添加到 PHP 的 include_path 中，这样通过 `include()` 或者 `require()` 时会自动加载它们

   ```
   lib/
   libs/
   libraries/
   src/
   misc/
   vendor/
   vendors/
   ```

   ​

4. 管理依赖项

   通过 pear 添加扩展，在文件 `.openshift/pear.txt` 中指定依赖的扩展库名。或者在 `.openshift/action_hooks/build` 中使用 composer 来管理依赖项。

5. ​

6. 配置文档根目录

   DocumentRoot 目录默认按照下面的逻辑来决定：

   ```
   IF php/ dir exists THEN DocumentRoot=php/
   ELSE IF public/ dir exists THEN DocumentRoot=public/
   ELSE IF public_html/ dir exists THEN DocumentRoot=public_html/
   ELSE IF web/ dir exists THEN DocumentRoot=web/
   ELSE IF www/ dir exists THEN DocumentRoot=www/
   ELSE DocumentRoot=/
   ```

7. 开启开发模式

   ```
   rhc env set APPLICATION_ENV=development
   ```

   注：通过环境变量来将应用设置为开发模式后 ，需要重启应用 `rhc app restart`

8. 项目部署

   `git push`

9. 项目热部署

   然我们看使用 `git push` 后，在 OpenShift 上发生了什么？OpenShift 会关闭服务器，构建应用，部署应用，最后在重启服务器。所谓热部署就是不需要重启服务器来进行部署，这样可以减少服务器停用时间。

   通过创建 `.openshift\markers\hot_deploy` 文件来实现热部署。

10. maker目录

    `fore_clean_build` ：Will remove all previous dependencies and start installing required dependencies from scratch.

    `hot_deploy`：Will prevent the apache process from being restarted during build/deployment.

    `disable_auto_scaling`：Will prevent scalable applications from scaling up or down, according to application load.

    `use_composer`：Will enable running `composer install` on each build automatically.

    `enable_public_server_status`：Will enable server-status application path to be publicly available.

11. 环境变量

    PHP cartridge 提供了 `OPENSHIFT_PHP_IP` 和 `OPENSHIFT_PHP_PORT` 来记录应用的 IP 和 端口

    PHP cartridge 重写了某些 PHP 默认设置 `APPLICATION_ENV`等

    PHP 访问环境变量 `$env_var = getenv('OPENSHIFT_ENV_VAR');`

    rhc 设置环境变量 `rhc env set`

12. ​

### 添加数据库

创建应用时添加

```
rhc app-create <myappname> <webcartridge> <dbcartridge>
```

创建应用后添加

```
rhc cartridge-add <dbcartridge> --app <myappname>
```

添加数据库后自动添加了环境变量

要想链接数据库，需要读取关于数据库的环境变量，不过不同 数据库 cartridge 用来存放数据库参数的环境变量是不一样的，查看应用数据库参数

```
rhc app show <myappname> -v
```

```
OPENSHIFT_<database>_DB_HOST
The hostname or IP address to use to connect to your database

OPENSHIFT_<database>_DB_PORT
The port your database server is listening on

OPENSHIFT_<database>_DB_USERNAME
Your database administrative username

OPENSHIFT_<database>_DB_PASSWORD
Your database administrative user’s password

OPENSHIFT_<database>_DB_SOCKET
$OPENSHIFT_HOMEDIR/mysql-5.1/socket/mysql.sock

A AF socket you can use to connect to your database
OPENSHIFT_<database>_DB_URL
	
mysql://admin:8ddTnst22X3Y@127.0.250.1:3306/
Database connection URL you can use to connect to your database
```

### 环境变量

https://developers.openshift.com/managing-your-applications/environment-variables.html

### 后台定时任务

Many web applications and frameworks depend on the cron job scheduler to
 handle regular tasks such as cleaning up temp files, backing up 
databases, and generating reports

cron cartridge 用来在后台执行定时任务

添加 cron cartridge 到应用中`rhc cartridge add cron -a <APP>`

将定时任务脚本放在 `.openshift/cron` 中的子目录 `minutely`, `hourly`, `daily`, `monthly`, `monthly` 下（且要使用`chmod`使得它们具有可执行属性）

通过上面方法设定的任务执行时间并不是特别精确的，可以通过在脚本中代码来精确设定执行时间（`minutely`）

```
#!/bin/bash
minute=$(date '+%M')
if [ $minute != 12 ]; then
    exit
fi
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
  # The command(s) that you want to run every 5 minutes
fi
```



## db-wikity.rhcloud.com

### MySQL

```
Root User: admin51XaKTw
Root Password: 8q9z3gwf8M-Z
Database Name: db

Connection URL: mysql://$OPENSHIFT_MYSQL_DB_HOST:$OPENSHIFT_MYSQL_DB_PORT/
```

### PHPMyAdmin

```
Root User: admin51XaKTw
Root Password: 8q9z3gwf8M-Z
URL: https://db-wikity.rhcloud.com/phpmyadmin/
```

### Cron

To schedule your scripts to run on a periodic basis, add the scripts to your application's `.openshift/cron/{minutely,hourly,daily,weekly,monthly}/` directories (and commit and redeploy your application)

### SSH Remote Access

```
ssh 58f190fa0c1e6637fb00003f@db-wikity.rhcloud.com
```

