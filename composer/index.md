---
title: Composer 入门
date: 2017/04/20
author: Xiao Wenbin
tags: composer, php
---

## 简介

Composer 是 PHP 项目中的包依赖管理工具，有点像 Node 中的 [npm](https://www.npmjs.com/) 和 Ruby 中的 [bundler](http://bundler.io/) ，使用依赖管理工具可以为每个项目维护特定版本的包以及相关依赖包，安装和更新都极其方便。

这篇文档篇幅也许有点长，而且在入门 Composer 方面也不算是优秀的文档，最近看到关于使用 Composer 的一个[交互式手册](http://composer.json.jolicode.com/)，感觉不错可以拿来作为手边的速查手册，推荐大家使用。

### 相关工具

PHP 中最为常见的扩展和第三方库管理软件有：[PECL](https://pecl.php.net/), [PEAR](http://pear.php.net/), [Composer](https://getcomposer.org/) 。PECL 是 PHP 的二进制扩展仓库，提供了许多用 C 语言编写的 PHP 扩展（以源码形式或者以预先编译好的二进制形式提供给开发者），由于这类扩展库偏底层，所以执行效率较高。PEAR 则是以重用 PHP 代码为目的而发起的一个第三方库管理项目，PEAR [仓库](http://pear.php.net/packages.php)含有大量常用第三方库来供开发者使用，使用 PEAR 工具可以方便的安装以及管理第三方库，并且还可以安装 PECL 扩展库。Composer 则是最为流行的项目依赖管理解决方案，Composer [仓库](https://packagist.org/)提供了大量第三方库供开发者使用，此外 Composer 还支持安装来自 PEAR 等第三方库。

### 原理

Composer 是针对特定项目的包依赖管理工具，也就是说在我们为项目声明依赖第三方包后，Composer 会为该项目安装这些依赖包。具体来说在项目中通过配置文件 `composer.json` 声明项目依赖的包，然后通过 Composer 工具就可以将依赖的第三方包安装到项目中的 `vendor` 目录中。

## 安装

### Unix/Linux/OS X 安装

首先要下载安装[脚本程序](https://getcomposer.org/installer)，然后校验该脚本是否有被篡改，最后运行该脚本下载 `composer.phar` 。值得注意的是，在对安装脚本进行校验时，因为不同版本脚本的校验码是不同的，所以在校验时需要将校验码替换为最新版本的校验码。最新版本校验码可以通过命令 `curl  https://composer.github.io/installer.sig` 或 `wget -q -O - https://composer.github.io/installer.sig` 来获取，另外也可以通过浏览器下载 https://composer.github.io/installer.sig 并用文本编辑器打开查看最新校验码。此外如果想要通过程序自动安装 `composer.phar` ，请参见官网的 Shell [脚本](https://getcomposer.org/doc/faqs/how-to-install-composer-programmatically.md)。

如果对如何获取脚本校验码感到困惑的话，可以直接访问[官网](https://getcomposer.org/download/)来查看安装命令。但如果已经成功获取到校验码，可以在命令行运行以下命令进行安装

```
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
php -r "if (hash_file('SHA384', 'composer-setup.php') === '这里是最新版本的校验码') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
php composer-setup.php
php -r "unlink('composer-setup.php');"
```

通过运行以上命令会在当前目录得到一个 PHP archive 文件 `composer.phar` ，它是一个可执行文件，可以直接在命令行中运行 `php composer.phar` 。不过通常我们有两种方式来使用 `composer.phar` ，一种是系统级，另一种是项目级。所谓系统级，就是将 `composer.phar` 移动到系统 `PATH` 目录中，然后就可以在任何地方通过命令 `composer` 来使用它。而项目级，则是将 `composer.phar` 移动到某个目录中，在运行 Composer 时需要精确指定路径，比如：`php bin/composer.phar` 。

### Windows 安装

Windows 下推荐使用安装程序 [Composer-Setup.exe](https://getcomposer.org/Composer-Setup.exe) 来安装 Composer，通过该程序可以自动下载 `composer.phar` 并将其添加到系统路径 `PATH` 中。安装完成后，可在命令行中通过 `composer` 来运行它。

不过如果想要按照类似于 Linux 系统上的方式安装，也是可行的。首先要像前面介绍的那样下载好 `composer.phar` ，然后将其移动系统路径 `PATH` 目录中，并且需要在相同目录下创建脚本 `composer.bat` ，内容为 `@php "%~dp0composer.phar" %*` 。

## 使用手册

假设我们已经在项目目录中安装了 `composer.phar` ，下面将以安装包 `monolog/monolog` 为例，说明如何使用 Composer

### 依赖声明文件

首先要创建依赖声明文件，用来声明项目依赖哪些第三方包，在项目目录中新建文件 `composer.json` ，填写如下内容

```
{
    "require": {
        "monolog/monolog": "1.0.*"
    }
}
```

依赖声明文件是一个 json 文件，文件中含有一个字典，字典中 `require` 键用来声明项目依赖哪些第三方包，每个被依赖的第三方包都以格式 `包名: 版本约束` 来声明。`包名` 一般由 vendor name 和 project name 构成，格式为 `vendor_name/project_name` 。`版本约束` 则用来指定项目具体依赖第三方包哪个版本，下面简单介绍一下如何指定 `版本约束`

* 特定版本

  精确指定版本号，比如：`1.0.3`

* 版本范围

  使用 `>` , `>=` , `<`, `<=` 这些比较运算符，还有或运算符 `||` 以及与运算符或 `,` ，可以灵活的指定版本范围，比如：`>=1.0 <1.1 || >=1.2` 表示版本范围  `1.0` 到 `1.1` 或者 大于等于 `1.2`。此外还可以通过连字符 `-` 来指定版本范围，比如：`1.0.0 - 2.0.0` 表示版本范围 `>=1.0.0 <2.1`

* 通配符

  通过通配符 `*` 来替代任意数字，比如：`1.0.*` 表示版本范围 `>=1.0 <1.1`

* 版本大变动

  通常来说当版本从 `1.0` 到 `2.0` 或者 `1.1` 到 `1.2` ，我们认为软件发生了较大变化，因此在指定依赖时，也希望不使用那些变化太大的版本，我们可以通过 `~` 声明依赖版本范围以某个变化较大版本为界，比如：`~1.2` 表示版本范围从 `>=1.2 <2.0.0` ，`~1.2.3` 表示版本范围 `>=1.2.3 <1.3.0` ，另外一个运算符 `^` 也有类似的功能，不过它指定的版本范围以主版本号为界，比如：`^1.2.3` 表示版本范围 `>=1.2.3 <2.0.0` ，`^0.3` 表示范围 `>=0.3.0 <0.4.0`

* 版本稳定性

  可以通过为版本约束添加后缀 `-dev` 和 `-stable` 来指定依赖的第三方包是开发版本还是稳定版本，比如：`>=1.2-stable`。如果没有指定稳定性后缀，composer 会自动推断应该使用哪种版本。

另外，https://semver.mwl.be/ 提供了根据包名查询版本约束的服务，可以利用它来计算某个包的版本约束条件。

依赖文件可以直接用文本编辑器打开编辑，也可以使用命令 `composer require madewithlove/elasticsearcher:"^0.5.0"` 来向依赖文件添加包依赖的声明。

### 安装依赖

安装项目依赖的第三方包十分简单，只要在项目所在目录运行命令 `php composer.phar install` 。该命令运行后主要产生了两个结果：

1. 下载第三方包

   composer 会根据 `composer.json` 中指定的依赖下载第三方包，并且将放在项目中的 `vendor` 目录中，具体位置跟 `包名` 相关，比如 `monolog/monolog` 最终被下载至 `vendor/monolog/monolog` 。

2. 记录第三方包版本信息

   由于第三方包的版本约束往往是一个版本范围而不是特定版本，而 composer 下载第三方包时得到的却是某个特定的版本，为了记录项目当前使用第三方包的版本信息，composer 会将这些版本信息写入到 `composer.lock` 文件中。

这里有两点需要注意：

* 一般来说，我们并不希望将项目 `vendor` 目录的第三方包内容提交至版本控制系统，因为提交第三方包内容是冗余的，我们有第三方依赖声明文件，任何时候都可以通过 composer 再次安装这些第三方包，所以要在 `vendor` 目录中创建 `.gitignore` 文件来阻止第三方包提交；
* 在项目协作时，我们希望不同开发人员使用的第三方包版本是相同的，因此安装完第三方包之后生成的 `composer.lock` 就大有用处了，我们需要将其提交到版本控制系统，然后项目协作的其它开发者在安装第三方包时就可以参照 `composer.lock` 来安装了。其实在运行 `php composer.phar install` 命令时，会查找当前目录有没有 `composer.lock` 文件，如果有的话，就按照该文件中指定的版本号来安装第三方包，如果没有的话，就安装最新版本的第三方包。

### 更新依赖

之前有介绍，在项目中存在 `composer.lock` 文件时，运行安装第三方包的命令会按照该文件中精确指定的版本来安装第三方包。可如果想要安装最新版本的第三方包呢？可以把 `composer.lock` 删除后再运行安装命令，或者运行更新第三方包的命令 `php composer.phar update` ，更新命令会下载最新版本的包文件并更新 `compsoer.lock` 文件。除了可以更新项目所有依赖，composer 还支持仅更新部分依赖 `php composer.phar update monolog/monolog` 。

有时候在运行安装命令时，会得到一个警告消息，提示 `composer.lock` 和 `composer.json` 不一致，此时需要运行更新命令来同步它们，但也许只是修改了 `composer.json` 中的描述或者作者信息，并不想更新相关包信息呢？此时可以运行命令 `composer update --lock` 来更新 `composer.lock` 。

### 自动加载

Composer 安装第三方包时，会自动生成自动加载脚本 `vendor/authload.php` ，只需要将该脚本包含在项目文件（一般是项目的入口文件）中就可以自动加载第三方包了，示例如下

```
require __DIR__ . '/vendor/autoload.php';

$log = new Monolog\Logger('name');
$log->pushHandler(new Monolog\Handler\StreamHandler('app.log', Monolog\Logger::WARNING));
$log->addWarning('Foo');
```

### 部署前的优化

在将项目部署到生成环境之前，运行一下命令来优化自动加载脚本：

```
composer dump-autoload --optimize
```

### Composer 仓库

现在然我们思考一个问题：当我们安装第三方包时，是从哪里查询这些第三方包的，又是从哪里下载这些第三方包的？

Composer 仓库正是为解决这个问题而生的，开发者可以通过 Composer 仓库发布自己开发的包，同时开发者也可以通过 Composer 仓库查询第三方包。其实 Composer 仓库只是保存了第三方包的元数据，比如：包名、版本号以及相应的下载地址，第三方包的代码一般是托管在 GitHub 这样的地方。[Packagist](https://packagist.org/) 是目前主要的 Composer 仓库，前面我们安装第三方包时，其实就是使用了这个仓库，它是默认仓库，也就是说不需要进行任何配置就可以使用这个仓库。

但有时候我们出于某些原因，不想使用这个默认仓库，要使用别的仓库只需在 `composer.json` 中添加键 `repositories` ，下面是一个示例

```
{
	"require": {
        "monolog/monolog": "1.0.*"
    },
    "repositories": [
        {
            "type": "composer",
            "url": "http://packages.example.com"
        },
        {
            "type": "composer",
            "url": "https://packages.example.com",
            "options": {
                "ssl": {
                    "verify_peer": "true"
                }
            }
        },
        {
            "type": "vcs",
            "url": "https://github.com/Seldaek/monolog"
        },
        {
            "type": "pear",
            "url": "https://pear2.php.net"
        },
        {
            "type": "package",
            "package": {
                "name": "smarty/smarty",
                "version": "3.1.7",
                "dist": {
                    "url": "http://www.smarty.net/files/Smarty-3.1.7.zip",
                    "type": "zip"
                },
                "source": {
                    "url": "https://smarty-php.googlecode.com/svn/",
                    "type": "svn",
                    "reference": "tags/Smarty_3_1_7/distribution/"
                }
            }
        }
    ]
}
```

通过示例可以看到仓库是分类型的，常见的类型有：`composer`, `vcs`, `pear`, `package`，更多关于仓库信息，参见[官网](https://getcomposer.org/doc/05-repositories.md)。下面我们主要解决一个关于仓库的问题，在中国访问国外的 Composer 仓库会比较慢，为此需要配置国内的仓库镜像：

* 全局配置

  仓库配置信息会写入到 composer 的全局配置文件中，对任何项目都有效

  ```
  composer config -g repo.packagist composer https://packagist.phpcomposer.com
  ```

* 项目配置

  只会写入当前项目的 `composer.json` 文件中的 `repositories` 中，仅对当前项目有效

  ```
  composer config repo.packagist composer https://packagist.phpcomposer.com
  ```

### 内置包

Composer 将 PHP 相关的扩展、库以及 PHP 解释器等这些预先安装组件当做内置包，简单来说内置包主要包含以下几种：`php` 代表 PHP 解释器；`ext-*` 代表 PHP 扩展；`lib-*` 代表第三方的二进制库。可以使用命令 `composer show --platform` 查看当前内置包。