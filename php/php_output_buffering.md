---
date: 2017/07/04
---

## PHP 输出和 HTTP response

首先我们知道 HTTP response 是由头部和响应体组成的，PHP web 应用程序运行时，会生成头部信息和响应体，然后再交给 HTTP server 处理，HTTP server 会添加修改头信息并且会等待合适时机，来向用户浏览器发送响应内容。

关于上面这段描述有几个地方需要详细说明：

* 现在 HTTP server 跟浏览器之间通信很多都通过持久连接来完成，不同于非持久连接每次请求响应结束后就断开 TCP 连接，持久连接机制允许连接被重用，后续请求和响应内容可以继续利用该信道来传输。
* PHP 中用于生成响应头信息的函数有，用来生成一般头信息的 `header()` 函数和用来生成 `Set-Cookie` 头信息的 `setcookie()` 函数（被设置的 cookie 会在用户后续发起请求时附加在请求头的 `Cookie` 字段中）。由于 HTTP 响应头应先于响应体发送，所以在 `header()` 和 `setcookie()` 函数之前任何响应体内容输出都是错误的作法。
* PHP 生成的响应体内容（也即使用 `echo` 和 `print` 以及 `readfile()` 这类输出语法时）去哪里了？
* PHP 跟 HTTP server 的配置模式也会影响输出缓存
* HTTP server 负责维护跟用户浏览器的连接，同时还负责接受来自 PHP web 应用程序的响应内容，将其交付给用户浏览器，不过要记得 HTTP server 对来自PHP 的内容也是有缓存区的

PHP 中的输出缓存默认是开启的，通过配置文件中的 `output_buffering` 来控制，下面是一段摘自 `php.ini` 中对该配置项的描述：

> Output buffering is a mechanism for controlling how much output data (excluding headers and cookies) PHP should keep internally before pushing that data to the client. If your application's output exceeds this setting, PHP will send that data in chunks of roughly the size you specify. Turning on this setting and managing its maximum buffer size can yield some interesting side-effects depending on your application and web server. You may be able to send headers and cookies after you've already sent output through print or echo. You also may see performance benefits if your server is emitting less packets due to buffered output versus PHP streaming the output as it gets it. On production servers, 4096 bytes is a good setting for performance reasons. 
>
> Note: Output buffering can also be controlled via Output Buffering Control functions.
>
> Note: This directive is hardcoded to Off for the CLI SAPI

简单来说输出缓存就是一种用来控制



## PHP 中的输出函数

### 输出头信息



控制头信息的输出比较复杂

https://stackoverflow.com/questions/3258634/php-how-to-send-http-response-code

### 输出字符串

语言结构 `print $str` 或 `print($str)` ：用来将字符串输出到 PHP 的输出缓存中，要注意的是由于 `print` 是语言结构，不是函数，因此它是不可调用的。array, object, resouce 等这类变量不会自动转换为字符串内容，因而用 `print` 语法来输出它们是得不到预期内容的。

还有另外一个语言结构 `echo $str1, $str2, ...` 也是用来将字符串输出到缓存中的，唯一的不同之处在于可以接受多个字符串参数。`echo` 语法有个快捷语法：`It's a <?php echo $foo; ?>` 等价于 `It's a <?= $foo ?>`，在 PHP 5.4 之前需要开启短标记配置项 `short_open_tag` 才能使用该快捷语法。当使用 `echo` 输出多个字符串时，不推荐用字符串拼接语法将其转化为一个字符串后输出，而推荐直接使用多个参数的 `echo` 语法。另外 `print` 返回值为 1，而 `echo` 无返回值。

此外 PHP 还提供了函数 `printf()` 和 `vprintf()` 用来输出格式化后的字符串到输出缓存中，可以认为它们先格式化了字符串，然后再输出到了缓存，事实上 PHP 分别提供了函数 `sprintf()` 和 `vsprintf()` 用来做格式化字符串那部分的工作，也即 `echo sprintf()` 和 `printf()` 是等效的。

### 输出文件

有时需要将某个文件的内容写入到 PHP 的输出缓存中，比如要为用户响应一个下载文件，此时 `readfile()` 函数就很有用了，下面实现了读取文件返回给用户下载的功能：

```php
<?php
$file = 'monkey.gif';

if (file_exists($file)) {
    header('Content-Description: File Transfer');
    header('Content-Type: application/octet-stream');
    header('Content-Disposition: attachment; filename="'.basename($file).'"');
    header('Expires: 0');
    header('Cache-Control: must-revalidate');
    header('Pragma: public');
    header('Content-Length: ' . filesize($file));
    readfile($file);
    exit;
}
```

除了读取返回整个文件内容，PHP 还提供了函数 `fpassthru` 来读取并返回当前文件指针位置到文件尾所有内容。

## PHP 中控制输出缓存的函数



## 块传输

https://www.foofish.net/http-transfer-encoding.html

https://en.wikipedia.org/wiki/Chunked_transfer_encoding

http://weblog.rubyonrails.org/2011/4/18/why-http-streaming/

https://www.sitepoint.com/php-streaming-output-buffering-explained/

https://stackoverflow.com/questions/2832010/what-is-output-buffering