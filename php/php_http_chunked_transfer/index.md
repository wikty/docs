---
date: 2017/07/04
---

## 简介

动态网站的内容一般由 web 应用程序动态的生成。在响应客户端的请求之前，必须生成响应的内容，如果响应的内容很多，就需要花费更多的时间去生成它，与此同时客户端也要有等待更多的时间才能够得到响应内容，显然不利于客户体验。本文要介绍的 HTTP 分块传输编码（chunked transfer encoding）技术就是用于解决此类问题的，允许 web 应用程序可以将动态生成的内容分块后及时传输给客户端。

## HTTP 持久连接

分块传输本质上是将响应内容分成若干部分通过客户端和服务端的信道传输，而分块多次发送数据其实是依赖 HTTP 持久连接的机制实现的，下面先来简单介绍一下持久连接。

### 非持久连接

在互联网兴起的早期，HTTP 应用大多是非持久连接的，所谓非持久连接是指：客户端要请求某个资源，就需要先同服务器建立一条 TCP 连接，客户端在该 TCP 连接上发起资源的 HTTP 请求，随后服务器在该 TCP 连接上应答客户端发回 HTTP 响应，当这一轮请求/响应完成后该 TCP 连接就被关闭了。非持久连接又被叫做短连接，因为客户端和服务器之间建立的 TCP 连接仅仅进行了一次 HTTP 通信后就被关闭了，后续要再向该服务器请求资源时，需要重新建立 TCP 连接进行数据传输。非持久连接机制保证了 TCP 连接信道的高使用率，不会出现信道闲置的情况，一旦没有数据传输的需求就立马关闭了连接。

### 持久连接

但非持久连接机制忽略了一个事实：客户端和服务器交互时，在短时间内通信信道往往会被使用多次。比如当客户端对某个 URL 发起请求时，该 URL 可能包含了许多图片，CSS 等多个资源，如果客户端和服务器为每个资源建立一个 TCP 连接来传输数据，会加重服务器负担，同时由于建立 TCP 连接带来的延时会导致较差的客户端体验。为此 HTTP 协议提供了重用 TCP 连接的机制，也即允许多次 HTTP 通信（请求/响应）通过一个 TCP 连接进行传输，该机制就是持久连接。

HTTP 1.0 协议通过头信息 `Connection: keep-alive` 来实现持久连接机制，具体来说，客户端想要建立持久连接的话，发起请求时要包含该头信息，然后如果服务器支持持久连接的话，在响应中也会包含该头信息的。而 HTTP 1.1 协议默认使用持久连接进行通信。

### 重用持久连接

持久连接机制允许一对客户端和服务器之间的多次 HTTP 通信通过一条 TCP 连接来完成，可 HTTP 协议又是如何约定从一个 TCP 连接中区分多次 HTTP 通信的呢？

TCP 是面向数据流的双向连接，要在一个 TCP 连接中进行多次通信，构建在 TCP 协议之上的协议（这里指的是 HTTP 协议）必须提供一种方法来界定每次通信的数据边界，也即 HTTP 协议应该提供一种方法来从数据流中划分出每次请求或响应的数据。

在介绍数据边界确定方法之间，先来简单介绍一下要通过 TCP 连接传输的 HTTP 数据到底是什么样的？

HTTP 请求的数据格式如下：

```
request-line
general-header
request-header
entity-header
CRLF
message-body
```

HTTP 响应的数据格式如下：

```
status-line
general-header
response-header
entity-header
CRLF
message-body
```

数据格式具体细节，参考[HTTP Request 说明文档](https://www.w3.org/Protocols/rfc2616/rfc2616-sec5.html#sec5)和[HTTP Response 说明文档](https://www.w3.org/Protocols/rfc2616/rfc2616-sec6.html#sec6)，简单来说请求和响应数据都由三部分组成：首行内容、头部内容以及用空白行分割的数据主体。

这里介绍几种 HTTP 协议中确定数据边界的方法：

- 最直观的想法也许就是发送方将数据内容长度一并传输给接收方，这样接收方可以利用长度信息来从数据流中截取特定长度的内容，HTTP 协议是通过 `Content-Length: xxx` 头信息来指定数据主体长度的（其中 `xxx` 表示数据主体长度值），该头部信息一般出现在 HTTP 响应中，这是因为一般发起的 HTTP 请求不含有数据主体，不过当提交表单请求时，请求中也会含有该头部（更具体来说是发起 POST 方式请求时）。请求和响应内容有特定的格式可以被客户端和服务器解析，再结合该头部信息就可以确定 HTTP 通信的数据边界了
- 另一种确定数据边界的方法叫做块传输编码（Chunked transfer encoding），是随着动态网站的兴起而被广泛应用的，也是本文介绍的重点。该方法一定程度上，让 HTTP 应用支持了以数据流形式来传输数据。下面将会专门介绍该机制是如何工作的。

### 管理持久连接

通信双方在建立了持久连接后，就可以重用该连接进行多次 HTTP 通信，但如果持久连接一直处于打开状态，即使客户端已经离开，服务端的持久连接一直处于等待状态，服务器将不堪重负，而且HTTP 协议就是被设计用来进行无状态的短时间通信的，将其用于长时间的持久通信违背了 HTTP 协议的初衷。因此需要某种机制来在合适的时机关闭持久连接。

服务器端提供了超时机制来关闭持久连接以节约资源。服务器会监听持久连接，如果发现该连接空闲超时，服务器会主动关闭该连接，例如 Apache 2.2 默认配置的超时时间值为 5 秒，服务器配置较短的超时时间，利于尽早结束那些空闲的连接。此外通信双方还可以通过头信息 `Connection: close` 来主动关闭持久连接。

更多关于持久连接的介绍，可以参考[协议标准](https://en.wikipedia.org/wiki/HTTP_persistent_connection)以及[维基百科介绍](https://en.wikipedia.org/wiki/HTTP_persistent_connection)。

## 块传输编码机制

块传输机制适用于不确定响应体内容大小的场景，比如动态生成的响应内容在全部内容生成之前无法确定其大小，如果想要一边生成一边发送数据，可以通过块传输机制来解决。更多关于 HTTP 块传输机制参见[维基百科介绍](https://en.wikipedia.org/wiki/Chunked_transfer_encoding)。

通过将响应内容划分成块编码后进行传输的，这样使得动态生成的内容可以及时的传输给客户端。具体来说，响应头部需要添加 `Transfer-Conding: chunked` 来表明响应内容将以分块传输的形式进行发送，由于响应内容将以块的形式传输，头部不再需要 `Content-Length` 来指定整个响应内容的大小。由块传输编码构造的响应内容由响应头、若干块内容、终止块、 Trailer 以及数据终止符 CRLF 构成，下面是一个响应内容示例：

```http
HTTP/1.1 200 OK\r\n
Content-Type: text/plain\r\n
Connection: keep-alive\r\n
Transfer-Encoding: chunked\r\n
\r\n
23\r\n
This is the data in the first chunk\r\n
1a\r\n
and this is the second one\r\n
3\r\n
end\r\n
0\r\n
\r\n
```

可见块内容由块大小和块数据构成，终止块是长度为零的块，同时要注意这里虽然将若干块写在了一起，在传输数据时，这些块是分开传输的。

用 Python 实现一个响应以上内容的块传输服务器示例如下：

```python
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("client address: {}".format(self.client_address))
        self.request.sendall(b"HTTP/1.1 200 OK\r\n")
        self.request.sendall(b"Content-Type: text/plain\r\n")
        self.request.sendall(b"Connection: keep-alive\r\n")
        self.request.sendall(b"Transfer-Encoding: chunked\r\n")
        self.request.sendall(b"\r\n")
        self.request.sendall(b"23\r\n")
        self.request.sendall(b"This is the data in the first chunk\r\n")
        self.request.sendall(b"1a\r\n")
        self.request.sendall(b"and this is the second one\r\n")
        self.request.sendall(b"3\r\n")
        self.request.sendall(b"end\r\n")
        self.request.sendall(b"0\r\n")
        self.request.sendall(b"\r\n")

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    print(HOST, PORT)
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
```

运行以上代码后，通过浏览器访问 http://localhost:9999 将得到结果： This is the data in the first chunkand this is the second oneend

使用块传输的一个显著优势是，将含有对图片、CSS 和 Javascript 引用的 HTML 片段先发送给客户端，这样在服务端准备生成动态内容期间，浏览器可以同时请求这些静态资源文件，最终得以加快网页加载速度。当然这也得益于客户端浏览器的工作方式，浏览器在接收到响应内容时会立即解析其中的资源链接，并行发起资源请求（参考自[此处](http://weblog.rubyonrails.org/2011/4/18/why-http-streaming/)）。

## PHP 块传输实现

在 PHP 中输出内容使用最多的也许就是 `echo` 语言结构（位于 PHP 标记之外的内容也会直接被输出）。直观上来看，我们只知道被 `echo` 的内容最终会呈现在用户浏览器中，也即 `echo` 输出的内容组成了响应体数据。另外也经常会用到 `header()` 函数来设置一些响应头。似乎 PHP 跟 HTTP server 的交互是透明的，HTTP server 只是直接将 PHP 生成的响应内容转发给了用户浏览器，事实上并非如此，HTTP server 和 PHP 的交互不仅仅取决于 PHP 的配置方式（是 SAPI 还是 FastCGI）而且取决于 PHP 脚本中控制数据输出的函数。接下来将介绍如何调用 PHP 的输出控制函数以实现块传输。

### 输出缓存机制

从 PHP 应用程序到最终生成 HTTP 响应，大致经历了三个阶段：PHP 应用程序生成响应数据保存到输出缓存中、PHP 模块缓存来自应用的数据（SAPI 方式不会缓存数据，FastCGI 会缓存数据）、HTTP server 缓存数据等待合适时机发送给客户端浏览器。本文假设 PHP 缓存大小设置为 4k 、使用不缓存数据的 SAPI 方式配置 PHP、HTTP server 缓存大小设置为 8k 。 

为什么各个环节会有这么多缓存机制？其实都是为了减少数据发送到客户端的次数。试想一下，如果 PHP 脚本中每次出现 HTML 片段或者使用了 `echo` 就立即将输出的数据发送给客户端，数据传输太频繁，降低了信道利用率。为此 PHP 中的输出缓存默认是开启的，通过配置文件中的 `output_buffering` 来控制，下面是一段摘自 `php.ini` 中对该配置项的描述：

> Output buffering is a mechanism for controlling how much output data (excluding headers and cookies) PHP should keep internally before pushing that data to the client. If your application's output exceeds this setting, PHP will send that data in chunks of roughly the size you specify. Turning on this setting and managing its maximum buffer size can yield some interesting side-effects depending on your application and web server. You may be able to send headers and cookies after you've already sent output through print or echo. You also may see performance benefits if your server is emitting less packets due to buffered output versus PHP streaming the output as it gets it. On production servers, 4096 bytes is a good setting for performance reasons. 
>
> Note: Output buffering can also be controlled via Output Buffering Control functions.
>
> Note: This directive is hardcoded to Off for the CLI SAPI

简单来说 PHP 的输出缓存机制使得输出的数据暂时保存在 PHP 内容，只有当超过缓存大小或者脚本结束后，缓存数据才会被发送出去。不过 CLI SAPI 模式下的 PHP 输出缓存是关闭的，因为 CLI SAPI 主要用于命令行交互，输出数据如果被缓存起来的话，交互就不能实时进行了。

### PHP 输出缓存示例

PHP 开启输出缓存机制后会影响到响应体的输出行为，通过浏览器访问以下脚本：

```php
<?php
echo "hello ";

sleep(5);

echo "world!";
```

通过浏览器访问该脚本时，浏览器会加载一会后再显示 hello world! ，注意这里不是先显示 hello 后显示 world! ，而是在浏览器等待 5 秒左右后显示 hello world! ，这是由于 PHP 开启了输出缓存，只有当脚本运行结束后，输出缓存中的内容才会一并发送给客户端。

PHP 的输出缓存机制同时影响到了响应头的输出，在 PHP 没有开启输出缓存时，头信息必须在响应体数据输出之前就输出，也即函数 `header()` 和 `setcookie()` 必须在任何内容输出之前被调用，不过当 PHP 开启了输出缓存后，只要输出内容没超过配置的缓存大小，就仍可以输出头信息，具体见下面两个例子：

响应内容没超过输出缓存大小时，设置响应头是合法的

```php
<?php

$times = 4;
$size = 1024 * $times;

// 共输出 4k - 1 byte 的内容
for ($i=2; $i<=$size; $i++) {
    echo "-";
}
// 输出头信息是合法的
header("Connection: close");

```

响应内容超过输出缓存大小时，设置响应头是非法的

```php
<?php

$times = 4;
$size = 1024 * $times;

// 共输出 4k 的内容
for ($i=1; $i<=$size; $i++) {
    echo "-";
}
// 输出头信息是非法的
header("Connection: close");
```

另外一个例子是输出内容超过了 PHP 配置的输出缓存大小，用浏览器访问如下脚本文件：

```php
<?php
$times = 4;
$size = 1024 * $times;

echo "-";
for ($i=1; $i<=$size; $i++) {
    echo "-";
}

sleep(5);

echo "hello world!";
```

在脚本调用 `sleep` 之前，已经输出 4k 加一字节的数据，超过了 PHP 配置的输出缓存大小 4k ，运行后可以看到浏览器处于加载状态，大概 5 秒左右后显示出了所有内容。当应用中输出内容超过 PHP 配置的输出缓存大小时，仅仅意味着缓存中的数据被发送给了 HTTP server，由于 HTTP server 也存在缓存机制，因此数据暂时还没有被发送给客户端浏览器。

将以上代码中的 `$times=4` 改为 `$times=8` 后，再次运行它，这次浏览器会立即显示许多连字符，并一直处于加载状态，然后又在连字符尾部显示了 hello world! ，并且如果打开浏览器中的开发者工具后可以发现响应头含有 `Transfer-Encoding: chunked` ，也就是说响应内容是块传输编码的。这次在调用 `sleep` 之前，脚本共输出了内容 8k 加一字节，已经超过了 HTTP server 输出缓存大小 8k ，这时 HTTP server 就对来自 PHP 应用的响应内容采用了块传输编码的机制。8k 数据在实际应用中，其实是比较大的数据了，有没有其它办法在数据量小于 8k 时依然使用块传输编码机制来发送响应内容呢？可以结合 PHP 的输出函数以及控制输出缓存函数来实现块传输。

### PHP 输出函数

#### 输出头信息

PHP 提供了函数 `header()` 用来设置 HTTP 响应的头信息。不过由于 PHP 生成的响应头最终会被 HTTP server 添加和修改，因此在 PHP 中对某些头信息的设置也许是没有意义的，比如 `Content-Length` 头信息从来不需要 PHP 中设置，HTTP server 会根据响应内容来自动添加这个响应头信息。不过由于 PHP 的配置方式以及使用的 HTTP server 不同，头信息的设置可能会面临一些跨平台的问题，例如 Stack Overflow 上关于[设置响应码](https://stackoverflow.com/questions/3258634/php-how-to-send-http-response-code)的一个问题就有许多方案。

此外 PHP 还提供了函数 `setcookie()` 来设置 `Set-Cookie` 头信息，被设置的 cookie 会在用户后续发起请求时附加在请求头的 `Cookie` 字段中。

#### 输出字符串

语言结构 `print $str` 或 `print($str)` ：用来将字符串输出到 PHP 的输出缓存中，要注意的是由于 `print` 是语言结构，不是函数，因此它是不可调用的。array, object, resouce 等这类变量不会自动转换为字符串内容，因而用 `print` 语法来输出它们是得不到预期内容的。

还有另外一个语言结构 `echo $str1, $str2, ...` 也是用来将字符串输出到缓存中的，唯一的不同之处在于可以接受多个字符串参数。`echo` 语法有个快捷语法：`It's a <?php echo $foo; ?>` 等价于 `It's a <?= $foo ?>`，在 PHP 5.4 之前需要开启短标记配置项 `short_open_tag` 才能使用该快捷语法。当使用 `echo` 输出多个字符串时，不推荐用字符串拼接语法将其转化为一个字符串后输出，而推荐直接使用多个参数的 `echo` 语法。另外 `print` 返回值为 1，而 `echo` 无返回值。

此外 PHP 还提供了函数 `printf()` 和 `vprintf()` 用来输出格式化后的字符串到输出缓存中，可以认为它们先格式化了字符串，然后再输出到了缓存，事实上 PHP 分别提供了函数 `sprintf()` 和 `vsprintf()` 用来做格式化字符串那部分的工作，也即 `echo sprintf()` 和 `printf()` 是等效的。

#### 输出文件

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

### PHP 控制输出的函数



flush vs ob_flush

https://stackoverflow.com/questions/4191385/php-buffer-ob-flush-vs-flush



ob_start

https://stackoverflow.com/questions/4401949/whats-the-use-of-ob-start-in-php

### PHP 块传输编码示例



https://www.sitepoint.com/php-streaming-output-buffering-explained/