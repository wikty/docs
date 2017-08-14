---
date: 2017/06/24
---

## PHP 是什么、它是怎样工作的？

### PHP 是什么

PHP 是一种脚本语言，其全称为 PHP: Hypertext Preprocessor，从名字可以看出，PHP 语言主要用来处理超文本内容（HTML），也即 PHP 一般被用于在服务器上处理以及生成 HTML 文档。不过 PHP 的用途并不限于此，它几乎可以解决其它任何编程语言能够解决的问题，是一门功能齐全的脚本语言，其主要应用领域包括：服务器端构建 web 应用、编写基于命令行的脚本程序以及构建 GUI 桌面应用程序（参见 PHP-GTK）。

所有脚本语言都是由一个解释器来执行的，比如 Javascript、Python、Perl 等脚本语言都有自己的解释器，同样 PHP 也有自己的解释器。PHP 具有一般脚本语言的优势：开发快速、跨平台能力强，现在基于 PHP 的 Web 开发框架种类繁多，提供了丰富的组件，可以快速解决 Web 开发中遇到的各种问题。除了开发框架外，PHP 内置函数库也提供了丰富的功能，比如字符串处理、正则表达式解析、XML文档解析等函数。几乎在所有主流操作系统上都有相应的 PHP 解释器程序可用，而且 PHP 支持跟主流服务器软件一起工作，跨平台能力十分强大。 

PHP 天生是面向过程的编程语言，自从 PHP 5 开始全面支持面向对象编程。由于 PHP 主要用于构建动态 web 应用，因此 PHP 支持在脚本文件中嵌入 HTML 内容，即 PHP 和 HTML 内容的混编，程序员在脚本文件中只需要通过标识 `<?php ?>` 来指定哪部分是 PHP 代码，解析器会负责识别并执行 PHP 代码。甚至可以认为 PHP 脚本文件就是一个 HTML 文档，只不过在里面嵌套了一些 PHP 代码而已。不过 PHP 并不限于处理 HTML 文档，可以用 PHP 来处理图像、PDF 文档、XML 文档、甚至 Flash 动画。此外动态网站的开发常常会涉及到数据库访问，PHP 为各种主流数据库提供了相应的扩展（比如针对 MySQL 数据库的 mysqli 扩展），使得在 PHP 代码中访问数据库变得十分简单，利用 PHP 提供的数据库抽象层对象 [PDO](http://php.net/manual/zh/intro.pdo.php) 并结合数据库扩展使得开发者可以用一致的接口访问所有数据库。

### PHP是怎样工作的

简单来说工作过程就是，将 PHP 脚本文件以及一些参数交给 PHP 解释器去执行并将结果返回。不过由于 PHP 可以用来编写不同领域的应用，显然命令行脚本和 web 脚本跟 PHP 解释器的交互模式是不同的，命令行脚本和命令行参数一同交给解释器，并且解释器会将结果返回到命令行；而 web 脚本的执行则一般会伴随来自 web 服务器的 HTTP 请求参数，并且解释器会将结果返回给 web 服务器。

在不同应用场景下，有不同的接口跟 PHP 解释器进行交互，我们将这类接口统称为 Server Application Programming Interface (SAPI)，SAPI 是指代由服务器定义并提供给开发者来扩展服务器功能的接口，只要是按照接口约定编写的程序就可以集成到服务器中进行使用（一般又叫做 HTTP server 模块）。不过在 PHP 中 SAPI 指代更加广泛的意义，除了代表同 HTTP server 交互的接口外，还可以代表同命令行的交互接口（CLI）以及以 Common Gateway Interface (CGI) 方式同 HTTP server 交互的接口，可以将 SAPI 看成外部世界跟 PHP 解释器交互的所有类型接口的统称，也即外部世界通过 SAPI 接口同 PHP 解释器进行交互。

在 Windows 上安装 PHP 后，会得到 `php.exe` 和 `php-cgi.exe` 以及 `php-win.exe` 共三个 PHP 解释器，其中 `php.exe` 是 CLI SAPI 实现，而 `php-cgi.exe` 是 CGI SAPI 实现（更准确来讲是 FastCGI 实现，稍后会进行解释），另外 `php-win.exe` 则用于不打开控制台的命令行任务。在命令行下，运行 `php -v` 便能得知该当前系统路径下使用的是 哪种 SAPI。此外还可以使用函数 `php_sapi_name()` 以及常量 `PHP_SAPI` 来检查当前 SAPI 的类型。

## Web 应用程序是如何工作的

### 静态 web 应用程序

先来看不需要依赖 PHP 等外部程序的静态网站是如何工作的？所谓静态网站是指，网站涉及到的 HTML, CSS, Javascript 以及图片和视频等资源文档，在被请求时 HTTP server 会直接读取并返回其内容，并不进行任何动态的数据处理。所有的资源都是预先编写好，上传到服务器的，在用户浏览器对 HTTP server 发出资源请求后，HTTP server 工作就是接受请求并返回对应的资源文档内容。静态网站的工作模式简图如下：

![](web-server.svg)

其中 Web server 是服务器软硬件的统称，跟用户浏览器交互的主要是 HTTP server，二者通过 HTTP 协议来发起请求以及传回响应。可以将 HTTP server 看成是一个资源管理器，同时它提供了 HTTP 协议作为供外部用户管理资源（获取、修改、更新以及删除等）的接口。

用户浏览器跟服务器的交互过程如下：

1. 用户在浏览器输入 URL 来表明，要用哪种协议、向哪个服务器上的什么资源发起请求，同时会附带一些请求参数。比如 URL 为 http://www.example.com/profile/stats.html?username=123456，其中 `http://` 用来表明跟服务器通过 HTTP 协议交互，域名 `www.example.com` 表明向托管了该域名的 Web server 发起请求，`/profile/stats.html` 用来表明请求资源的路径，`username=123456` 表明请求附带的参数。
2. 在服务器上的 HTTP server 收到请求后，会解析请求并将请求中的资源路径映射到服务器上真实的文件路径，读取文件内容并添加响应头信息（通常包含文档类型、文档长度、文档修改时间等）后一并返回给浏览器用户

 其实在用户跟服务器交互时还有一些细节如下：

* 用户通过域名向服务器发起请求时，需要依赖 DNS 服务将域名解析为 IP 地址，最终浏览器根据 IP 地址来建立和服务器的通信信道。
* 用户除了通过 GET 类型的 HTTP 请求获取资源文档外，还可以发起 POST, DELETE, UPDATE, HEAD, OPTIONS 类型的 HTTP 请求。
* HTTP 是无状态协议，即不论是浏览器还是 HTTP server 都不会记录之前的通信状态。
* 发起请求时，域名会包含在请求头中发送给 HTTP server，有时域名用于区分部署在同一服务器上的多个 web  应用，这叫做 virtual hosting 技术，主流的 HTTP server 像 Apache, Nginx 等都支持配置虚拟主机。在同一服务器上部署多个 web 应用可以有效的利用计算机资源。
* 当请求资源的路径最终被 HTTP server 映射为服务器上的一个目录时，如何进行响应取决于 HTTP server 的配置，一般来说会尝试返回该目录下的 `index.html` 文件或者返回该目录的索引列表。

### 动态 web 应用程序

静态网站中所有资源文档都是预先上传到服务器的，在用户请求资源时直接返回这些文档即可。动态网站一个明显的区别在于，大部分资源文档都是经过动态处理生成的。当用户请求到达服务器后，动态 web 应用程序会根据请求参数动态的生成响应内容，并交给 HTTP server 传回响应给用户浏览器。而响应内容的动态生成往往会涉及到查询数据库、取回数据并将其填充到预先定义好的 HTML 模板中，最终生成一个响应文档。值得注意的是，HTTP server 只负责将生成后的动态响应内容传回给用户，HTTP server 并不负责动态响应内容的生成，那么动态响应内容是怎样生成的，是谁来负责生成的呢？负责生成动态响应内容的是一套软件系统，叫做 web 应用程序，其中会涉及到类似于 PHP 这样的脚本语言编程以及访问类似 MySQL 这样的数据库访问操作，现在可以用于编写 web 应用程序的语言、框架以及工具越来越丰富，具体使用哪种技术来构建 web 应用程序取决于自己的情况。

#### SAPI 和 CGI

那么 web  应用程序和 HTTP server 之间又是怎样交互的呢？我们知道 HTTP server 负责接收请求以及返回响应，而 web 应用程序则负责动态的生成响应内容，显然需要一个机制将 HTTP server 接收到的请求数据传递给 web 应用程序，并且在 web 应用程序生成响应内容后能够将其返回给 HTTP server。当前主要有两种方式来解决这个问题：

1. Server Application Programming Interface

   许多 HTTP server 支持开发者开发模块来扩展其功能，只要模块按照 HTTP server 约定的接口编写就可以将其作为 HTTP server 的一部分来运行。对于 web 应用程序的开发者来说，并不需要自己编写 HTTP server 模块来实现动态内容生成的功能，许多编程语言会直接提供这样的模块供 web 应用程序的开发者使用，比如 PHP 提供了 `mod_php` （Linux 系统） `php5apache2.dll` （Windows 系统）这样针对 Apache 服务器的模块，web 应用程序的开发者只需要为 Apache 服务器配置开启该模块，就可以在基于 PHP 的 web 应用程序项目中无缝的跟 HTTP server 交互：通过超全局数据 `$_GET`, `$_POST`, `$_FILES`, `$_COOKIE` 等来访问请求数据，并调用 `header` 生成响应头、调用 `echo` 返回响应内容。所有这一切都是扩展模块实现的，扩展模块赋予了 HTTP server 解析执行某种语言的能力。web 应用程序开发者无须关心跟 HTTP server 的交互是如何实现的，只要按照编程语言的规定就可以访问 HTTP 请求参数以及将响应内容返回给服务器。为 HTTP server 编写的扩展模块会作为它进程的一部分来运行，因此扩展模块相关配置项会在 HTTP server 启动时进行加载（比如 `php.ini` 会在服务器启动时加载），修改了配置项则需要重启 HTTP server 才会生效，每当有新的 HTTP 请求到达后，就将其交给相应的扩展模块进行处理。

2. Common Gateway Interface

   通用网关接口（CGI） 是 HTTP server 同外部程序交互的协议（这里的外部程序不限于 PHP 解释器），协议规定了如何将 HTTP 请求参数传递到外部程序的环境变量、如何将 HTTP 请求体通过标准输入传递到外部程序以及外部程序如何通过标准输出来返回 HTTP 响应内容等。CGI 协议的强大之处在于，任何外部程序只要它能够理解该协议并且具有标准输入、标准输出和环境变量功能，就可让它通过具有 CGI 功能的 HTTP server 来提供 web 服务。CGI 是允许通过 web 接口来访问一切资源的方案，到达 HTTP server 的请求，只要交付给特定的 CGI web 应用程序，就可以访问相应的资源。常见的脚本语言 Shell, Perl, PHP, Python 等都可以用来编写基于 CGI 的 web 应用程序，只要语言本身（附带模块或库）提供了对 CGI 协议的支持，就可以通过配置开启 HTTP server 的 CGI 功能来跟该 web 应用程序交互，比如 Apache 中的模块 `mod_cgi` 就是用于 CGI 通信的，相应的 PHP 也提供了进行 CGI 通信的解释器实现。同利用 SAPI 方式跟 HTTP server 不同在于，每个 HTTP 请求到达后，都会重新加载一次编程语言的 CGI 实现，并会作为独立进程跟 HTTP server 进行通信，这样交互的缺点也很明显，每次请求打开一个新的 CGI 进程会加重服务器负担，显然不适用于高流量的应用场景。不过这样也是有好处的，对 web 应用程序的解析执行放在独立进程中进行，利于 HTTP server 的稳定性以及系统安全，同时对 CGI web 应用程序的配置会立马反应到新的请求中，而不必重启 HTTP server 来加载新的配置。


总之，由于 HTTP server 能力有限，只能接受请求以及返回响应，要想构建动态 web 应用就需要扩展 HTTP server 的功能，一种方式是将 SAPI 模块用嵌入到 HTTP server 进程，使其具有解析执行 web 应用程序的能力；另一种方式是 HTTP server 通过 CGI 协议跟外部进程通信，将 HTTP 请求派送给 CGI web 应用程序，并将结果返回到响应中。由于 CGI 方式下，每次都要为新的请求开启一个新进程来执行 web 应用程序，这样会降低内存缓存以及数据库连接等资源的重用率，从性能角度考虑的话，SAPI 嵌入模块的方式更好些，其实在实际应用中这种方式几乎不会被使用（除了非常低流量的站点）。同时要注意 SAPI 模块嵌入 HTTP server 进程会导致进程消耗更多资源，即便在处理静态资源时，HTTP server 也总是嵌入着 SAPI 模块，而 CGI 方式下静态资源可以直接被 HTTP server 处理。

#### FastCGI

为了解决 CGI 方案的性能问题，FastCGI 协议被提了出来。FastCGI 是基于 socket 的协议，如今几乎所有主流服务器提供了对 FastCGI 协议的支持，比如 Apache 通过模块 `mod_fcgid` 来实现对 FastCGI 的支持，结合编程语言端实现的 FastCGI 管理程序，就相当于在 HTTP server 和 CGI web 应用程序之间建立了中间层。对于开启了 FastCGI 的服务器，在启动服务器时会建立到 FastCGI 管理程序的持久连接，然后会利用该持久连接来处理一系列来自 HTTP server 的请求，并通过该持久连接返回响应结果，此外 FastCGI 管理程序在内部会开启若干 CGI 守护进程，这样当请求到达时，会重用这些 CGI 守护进程，减少 CGI 进程的启动关闭，带来了性能上的提升。而且 FastCGI 协议是基于 socket 的，这样就允许 HTTP server 和 FastCGI 管理程序部署在不同的主机上，HTTP server 和 web 应用程序可以独立的进行重启，同时在某些情形下，根据请求类型将请求交付到不同主机上的 FastCGI 程序进行处理也很重要。

## 在 HTTP Server 服务器中使用 PHP

### SAPI 交互接口

PHP 最广泛的应用领域就是用来构建动态网站。那么用 PHP 构建的动态网站又是如何跟 HTTP server 结合起来的呢？HTTP server 可以看成是介于用户浏览器和资源之间的一个代理者，它只负责接受和响应用户请求，至于当用户请求到达服务器后，该如何处理以及根据用户请求参数来生成响应内容则完全不归它管，这部分工作是由 PHP 构建的 web 应用程序来完成的，那么 HTTP server 是如何将用户发起的请求转达给 web 应用程序的，web 应用程序又是如何将生成的响应内容回传给 HTTP server 的呢？

要回答这个问题就涉及到 PHP 同 HTTP server 交互模式的讨论了。之前有提到将 PHP 同外部世界的交互接口统称为 SAPI，具体涉及到跟 HTTP server 的交互主要有两种模式：

1. 一种就是 SAPI 字面理解的意思，HTTP server 一般会提供接口供开发者扩展其功能，而 PHP 为许多主流服务器都提供了相应的 SAPI 接口解释器，比如在 windows 系统上 PHP 5 为 Apache 2.0 提供了一个动态链接库 `php5apache2.dll` 实现的 SAPI ，在 Linux 系统该模块叫做 `mod_php` 或者 `libphp5.so`，可以将其直接作为 HTTP server 的模块来使用，作为模块的意思是 PHP 解释器会作为 HTTP server 进程的一部分来运行 web 应用程序中的 PHP 代码
2. 此外还可以通过 Common Gateway Interface (CGI) SAPI 接口的 PHP 解释器来运行 web 应用程序，由于基于 CGI 接口运行的 web 应用程序会在每次请求到来时启动一个 CGI 进程，导致性能低下，在实际应用中几乎不使用这种模式来运行 PHP 程序，而是使用 FastCGI SAPI 接口。要使用 FastCGI 接口需要开启服务器对 FastCGI 的支持，同时运行一个跟服务器进行交互的 FastCGI 管理程序，在 PHP 应用中，一般都会使用 [PHP-FPM](https://php-fpm.org/) 来作为 FastCGI 管理程序，PHP 5.3.3 以前 PHP-FPM 作为补丁存在于 PHP 中的，目前 PHP-FPM 已经融入了 PHP 内核，在 Windows 系统上安装 PHP 后，得到的 `php-cgi.php` 就是 PHP-FPM 版本的 FastCGI 实现。


### SAPI配置

Unix 系统下为 Apache 2 配置 SAPI 接口的 PHP 模块，参见文档：http://php.net/manual/zh/install.unix.apache2.php

### FastCGI配置

Unix 系统下为 Nginx 1.4 配置 PHP-FPM 实现的 FastCGI SAPI 模块，参见文档：http://php.net/manual/zh/install.unix.nginx.php 和 https://www.nginx.com/resources/wiki/start/topics/examples/phpfcgi/#connecting-nginx-to-php-fpm

Windows 系统下为 Nginx 配置 PHP-FPM 实现的 FastCGI SAPI 模块，参见文档：https://www.nginx.com/resources/wiki/start/topics/examples/phpfastcgionwindows/

为 Apache 配置 CGI 和 FastCGI 分别参考文档：http://httpd.apache.org/docs/2.4/howto/cgi.html 和 http://httpd.apache.org/mod_fcgid/mod/mod_fcgid.html

### 配置小结

对于 Nginx 来说，目前流行 PHP-FPM 作为 FastCGI 实现来搭配 PHP 使用。对 Apache 来说则存在 SAPI 嵌入模块和 PHP-FPM 两种方式来搭配 PHP 使用。PHP 为 Apache 提供的 SAPI 模块，在 Windows 系统上可能叫做 `php2apache2.dll` ，在 Linux 系统上可能叫做 `mod_php` 或 `libphp5.so`。

PHP-FPM 实现的 FastCGI 管理程序已经并入 PHP 内核，利用源码编译 PHP 时，通过传入选项 `--enable-fpm` 来开启 PHP-FPM 功能：`./configure --enable-fpm --with-mysql`，另外还可以为 PHP-FPM 指定运行用户名、用户组等编译参数，具体参见：http://php.net/manual/zh/install.fpm.install.php。PHP-FPM 有自己的配置文件 `php-fpm.conf` ，配置项介绍参见：http://php.net/manual/zh/install.fpm.configuration.php 。

PHP-FPM 只是关于 PHP 的 FastCGI 实现，Spawn-FCGI 是一个通用的 FastCGI 管理程序（不限于为 PHP 应用服务），它是 lighttpd 服务器的一部分，也有很多人使用 Spawn-FCGI 作为 FastCGI 的实现。

## 在 Command Line 中使用 PHP

#### CLI SAPI 的不同之处

PHP 除了用于编写 web 应用外，也常常被用来完成一些基于命令行的任务，比如批量处理数据、调度任务等。这种情形下跟 PHP 解释器交互的接口被称为 Command Line Iterface SAPI (CLI)，CLI 有许多跟面向 web 的 SAPI 不同的地方：

1. CGI SAPI 会输出 HTTP 头信息，而 CLI SAPI 不会
2. CLI SAPI 强制覆盖了 `php.ini` 中的某些配置项，因为在命令行模式下有些配置项是没意义的
3. 引入全局常量 `STDIN`, `STDOUT` 以及 `STDERR` 来代表命令行中的标准输入、标准输出和标准错误输出流
4. CLI SAPI 运行脚本时，脚本中的当前目录就是运行 CLI 时所在目录，而 CGI SAPI 脚本中的当前目录则是脚本在文件系统中所在目录（可以使用 `echo getcwd();` 进行测试）

#### 代码运行以及参数传递

命令行模式下运行 PHP 代码的方法：

1. 通过指定 PHP 脚本文件路径：`php [-f] test.php`
2. 直接运行 PHP 代码：`php -r 'print_r(get_defined_constants());'`
3. 通过标准输入流：`some_application | some_filter | php | sort -u >final_output.txt`

在命令行中运行的 PHP 代码可以接受来自命令行的参数，在脚本中通过全局变量 `$argc` 和 `$argv` 来访问，数据中第一个参数是脚本名，在命令行中向脚本传递参数时，如果参数含有 `-`，会引起命令行歧义，不知道是传递给解释器的还是传递给脚本的，为此可以插入 `--`，表明位于它之间的参数是传递给 PHP 解释器的，而位于它之后的参数都是要传递给脚本的。

#### 直接执行 PHP 脚本

通过在脚本文件头部添加 `#!/usr/bin/php` （CLI SAPI 可执行程序的位置），并为脚本文件添加可执行属性后，就可以像普通 shell 文件一样在命令行中直接执行它：`$ ./test.php`

PHP 的命令行模式能使得 PHP 脚本能完全独立于 web 服务器单独运行。如果使用 Unix 系统，需要在 PHP 脚本的最前面加上一行特殊的代码，使得它能够被执行，这样系统就能知道用哪个程序去运行该脚本。在 Windows 平台下可以将 php.exe 和 .php 文件的双击属性相关联，也可以编写一个批处理文件来用 PHP 执行脚本。为 Unix 系统增加的第一行代码不会影响该脚本在 Windows 下的运行，因此也可以用该方法编写跨平台的脚本程序。

## 向后兼容

随着 PHP 被越来越多的开发者使用，新的特性不断加到新版本 PHP 中，PHP 社区为向后兼容做多了很多工作，不过以前的遗留代码还是有两个地方不能跟新版本 PHP 兼容：

1. 从 PHP 5.4.0 开始，`$HTTP_*_VARS` 这类变量名被移除了（星号代表 GET, POST等），要访问这些变量的内容需要使用全局可见的超全局数组： `$_GET`, `$_POST`, `$_COOKIE`, `$_SERVER`, `$_FILES`, `$_ENV`, `$_REQUEST`, `$_SESSION`
2. 从 PHP 4.2.0 开始，`php.ini` 中的配置项 `register_globals=off` 也即环境变量、GET 变量，POST 变量、COOKIE 变量以及 SERVER 变量不再自动被注册为全局变量，比如以前当用户访问 `http://127.0.0.1/test.php?username=nick` 时，在页面 `test.php` 中会自动生成一个全局变量 `$username` ，但是现在只能通过超全局数据来访问 `$_GET['username']`