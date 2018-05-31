

## Introduction

One of NGINX’s strongest features is the ability to efficiently serve static content such as HTML and media files.

NGINX hands off dynamic content to CGI, FastCGI, or other web servers such as Apache. This content is then passed back to NGINX for delivery to the client. 

## Install

从 Nginx 仓库 *nginx.org* 来安装预编译好的二进制：The *stable* version of NGINX Open Source was installed from the *nginx.org* repository.

https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-open-source/#installing-a-prebuilt-package



## start & stop

To start nginx, run the executable file. Once nginx is started, it can be controlled by invoking the executable with the `-s` parameter. Use the following syntax:

> ```
> nginx -s signal
> ```

Where *signal* may be one of the following:

- `stop` — fast shutdown
- `quit` — graceful shutdown
- `reload` — reloading the configuration file
- `reopen` — reopening the log files

A signal may also be sent to nginx processes with the help of Unix tools such as the `kill` utility. In this case a signal is sent directly to a process with a given process ID. The process ID of the nginx master process is written, by default, to the `nginx.pid` in the directory `/usr/local/nginx/logs` or `/var/run`. For example, if the master process ID is 1628, to send the QUIT signal resulting in nginx’s graceful shutdown, execute:

> ```
> kill -s QUIT 1628
> ```

For getting the list of all running nginx processes, the `ps` utility may be used, for example, in the following way:

> ```
> ps -ax | grep nginx
> ```



Centos 7 可以通过 Systemd 来控制 Nginx

```
sudo systemctl start nginx
```

开启开机启动 Nginx

```
sudo systemctl enable nginx
```



此时可以通过浏览器访问 Nginx 默认提供的首页，如果无法访问，则可能是由于服务器上的防火墙限制，解除防火墙限制，允许 HTTP 和 HTTPS 流量：

```
sudo firewall-cmd --permanent --zone=public --add-service=http 
sudo firewall-cmd --permanent --zone=public --add-service=https
sudo firewall-cmd --reload
```



## Configuration



### basic

All NGINX configuration files are located in the `/etc/nginx/` directory. The primary configuration file is `/etc/nginx/nginx.conf`.

Configuration options in NGINX are called [directives](http://nginx.org/en/docs/dirindex.html). Directives are organized into groups known as **blocks** or **contexts**.

Lines containing directives must end with a `;` or NGINX will fail to load the configuration and report an error.

Lines preceded by a `#` character are comments and not interpreted by NGINX. 



`/etc/nginx/nginx.conf` 默认配置内容：

The file starts with 5 directives: `user`, `worker_processes`, `error_log`, and `pid`. These are outside any specific block or context, so they’re said to exist in the `main` context.  The `events` and `http` blocks are areas for additional directives, and they also exist in the `main` context.

```
user  nginx;
worker_processes  1;

error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;

events {
       . . .
}

http {
       . . .
}
```



http block

The `http` block contains directives for handling web traffic. These directives are often referred to as *universal* because they are passed on to to all website configurations NGINX serves.

```
http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on;

    include /etc/nginx/conf.d/*.conf;
}
```



server block

The `http` block above contains an `include` directive which tells NGINX where website configuration files are located.

If you installed from the official NGINX repository, this line will say `include /etc/nginx/conf.d/*.conf;` as it does in the `http` block above. Each website you host with NGINX should have its own configuration file in `/etc/nginx/conf.d/`, with the name formatted as `example.com.conf`. Sites which are disabled (not being served by NGINX) should be named `example.com.conf.disabled`.

server configuration files will contain a `server` block (or blocks) for a website. 

```
server {
    listen         80 default_server;
    listen         [::]:80 default_server;
    server_name    example.com www.example.com;
    root           /var/www/example.com;
    index          index.html;
    try_files $uri /index.html;
}
```

The `listen` directive tells NGINX the hostname/IP and the TCP port where it should listen for HTTP connections. The argument `default_server` means this virtual host will answer requests on port 80 that don’t specifically match another virtual host’s listen statement. 

The `server_name` directive allows multiple domains to be served from a single IP address. The server decides which domain to serve based on the request header it receives. The `server_name` directive can also use wildcards. `*.example.com` and `.example.com` both instruct the server to process requests for all subdomains of `example.com`. Process requests for all domain names beginning with ‘example.’ using `example.`.

NGINX allows you to specify server names that are not valid domain names. NGINX uses the name from the HTTP header to answer requests, regardless of whether the domain name is valid or not.



location block

The `location` setting lets you configure how NGINX will respond to requests for resources within the server. Just like the `server_name` directive tells NGINX how to process requests for the domain, `location` directives cover requests for specific files and folders

specify request path match:

* *literal string* matches

  ```
  location / { }
  location /images/ { }
  location /blog/ { }
  location /planet/ { }
  location /planet/blog/ { }
  ```

  ​

* regular expression match (case-sensitive)

  ```
  location ~ IndexPage\.php$ { }
  location ~ ^/BlogPlanet(/|/index\.php)$ { }
  ```

  ​

* regular expression match (case-insensitive)

  ```
  location ~* \.(pl|cgi|perl|prl)$ { }
  location ~* \.(md|mdwn|txt|mkdn)$ { }
  ```

  ​

* stop searching for more specific matches

  ```
  location ^~ /images/IndexPage/ { }
  location ^~ /blog/BlogPlanet/ { }
  ```

  ​

* exact match

  ```
  location = / { }
  ```

  ​

specify how to response the request:

Once NGINX has determined which `location` directive best matches a given request, the response to this request is determined by the contents of the associated `location` directive block.

```
location / {
    root html;
    index index.html index.htm;
}
```

In this example, the document root is located in the `html/` directory. Under the default installation prefix for NGINX, the full path to this location is `/etc/nginx/html/`.

**Request:** `http://example.com/blog/includes/style.css`

**Returns:** NGINX will attempt to serve the file located at `/etc/nginx/html/blog/includes/style.css`

The `index` variable tells NGINX which file to serve if none is specified. If no `index` files are found, the server will return a 404 error.



来看一个同时配置文档根目录和 FastCGI 的 location 配置

```
location / {
    root   /srv/www/example.com/public_html;
    index  index.html index.htm;
}

location ~ \.pl$ {
    gzip off;
    include /etc/nginx/fastcgi_params;
    fastcgi_pass unix:/var/run/fcgiwrap.socket;
    fastcgi_index index.pl;
    fastcgi_param SCRIPT_FILENAME /srv/www/www.example.com/public_html$fastcgi_script_name;
}
```

除了以 `.pl` 结尾的资源请求外，其它请求都有文件系统来提供响应。`.pl` 由 FastCGI 来响应。注意：`fastcgi_param` 还指定了用来处理响应的脚本位置。

all requests for resources that end in a `.pl` extension are handled by the second location block, which specifies a `fastcgi` handler for these requests. Otherwise, NGINX uses the first location directive.









### part1: baisc



Nginx 和 Apache 的配置的一些区别：

* 多站点配置文件位置不同

  multiple site configuration files should be stored in `/etc/nginx/conf.d/` as `example.com.conf`, or `example.com.disabled`. Do not add `server` blocks directly to `/etc/nginx/nginx.conf` either, even if your configuration is relatively simple. This file is for configuring the server process, not individual websites.

* 运行服务的用户不同

  The NGINX process also runs as the username `ngnix` in the `nginx` group, so keep that in mind when adjusting permissions for website directories. For more information, see *Creating NGNIX Plus Configuration Files* .

* Apache 配置中的术语 Virtual Host 在 Nginx 中叫做 Server Block

  [as the NGINX docs point out](https://www.nginx.com/resources/wiki/start/topics/examples/server_blocks/), the term *Virtual Host* is an Apache term, even though it’s used in the `nginx.conf` file supplied from the Debian and Ubuntu repositories, and some of NGINX’s old documentation. A *Server Block* is the NGINX equivalent

根据使用服务器的目的不同应该采取不同的配置，因此没有唯一标准正确的配置，这里只提供关于配置的最佳实践原则They’re not essential to the function of your site or server, but they can have unintended and undesirable consequences if disregarded.：

首先在配置之前应该备份默认的配置文件 `nginx.conf`，这样在配置出问题时可以回退

```
cp /etc/nginx/nginx.conf /etc/nginx/nginx.conf.backup-original
```

配置完成后重新载入配置文件，使得配置生效

```
nginx -s reload
```



设置 Worker 进程数量：

Add or edit the following line in `/etc/nginx/nginx.conf`, in the area just before the `http` block. This is called the `main` block, or context, though it’s not marked in `nginx.conf` like the `http` block is. The first choice would be to set it to `auto`, or the amount of CPU cores available to your Linode.

```
worker_processes auto;
```



使 Nginx 不返回版本号

NGINX’s version number is visible by default with any connection made to the server, whether by a successful 201 connection by cURL, or a 404 returned to a browser. Disabling server tokens makes it more difficult to determine NGINX’s version, and therefore more difficult for an attacker to execute version-specific attacks

Add the following line to the `http` block of `/etc/nginx/nginx.conf`:

```
server_tokens off;
```



网站的文档根目录

The directory NGINX serves sites from differs depending on how you installed it. At the time of this writing, NGINX supplied from NGINX Inc.’s repository uses `/usr/share/nginx/`.

The NGINX docs warn that relying on the default location can result in the loss of site data when upgrading NGINX. You should use `/var/www/`, `/srv/`, or some other location that won’t be touched by package or system updates.

假设要为网站 `example.com` 指定目录 `/var/www/example.com/` 作为托管的根目录，首先需要创建该目录。

然后，相应的需要在该站点的配置文件 `/etc/nginx/conf.d/example.com.conf` 中指定该路径，在其中的 `server` 块中添加如下内容：

```
root /var/www/example.com;
```



开启对 IPv6 以及 SSL/TLS 的服务

Default NGINX configurations listen on port `80` and on all IPv4 addresses. Unless you intend your site to be inaccessible over IPv6 (or are unable to provide it for some reason), you should tell NGINX to also listen for incoming IPv6 traffic.

Add a second `listen` directive for IPv6 to the `server` block of `/etc/nginx/conf.d/example.com.conf`:

```
listen [::]:80;

```

If your site uses SSL/TLS, you would add:

```
listen [::]:443 ssl;
```



灵活配置内容压缩：

对所有内容开启压缩，容易受到攻击。

You do not want to universally enable gzip compression because, depending on your site’s content and whether you set session cookies, you risk vulnerability to the [CRIME](https://en.wikipedia.org/wiki/CRIME) and [BREACH](http://www.breachattack.com/) exploits.

Compression has been disabled by default in NGINX [for years now](http://mailman.nginx.org/pipermail/nginx/2012-September/035600.html), so it’s not vulnerable to CRIME out of the box.

对所有内容关闭压缩，网站加载速度会降低。

On the other hand, if you leave gzip compression totally disabled, you rule out those vulnerabilities and use fewer CPU cycles, but at the expense of decreasing your site’s performance.

因此我们仅压缩静态内容。

For now, and unless you know what you’re doing, the best solution is to compress only static site content such as images, HTML, and CSS.

压缩配置建议放在针对各个站点的 `server` 块，而不是针对所有站点的 `http` 块

Below is an example of how to do that, and you can view all available mime types with `cat /etc/nginx/mime.types`. Though `gzip` directives can go in the `http` block if you want it to apply to all sites served by NGINX, it’s safer to use it only inside `server` blocks for individual sites and content types.

```
gzip          on;
gzip_types    text/html text/plain text/css image/*;
```



基本配置的结果

将关于站点的配置都放在站点配置文件，全局配置文件中不要出现 `server` 块

站点配置 `/etc/nginx/conf.d/example.com.conf`

```
server {
    listen         80 default_server;
    listen         [::]:80 default_server;
    server_name    example.com www.example.com;
    root           /var/www/example.com;
    index          index.html;

    gzip             on;
    gzip_comp_level  3;
    gzip_types       text/plain text/css application/javascript image/*;
}
```

全局配置 `/etc/nginx/nginx.conf`

```
user  nginx;
worker_processes  auto;

error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;

events {
    worker_connections  1024;
}


http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on;

    include /etc/nginx/conf.d/*.conf;


    server_tokens       off;
}
```



### part2: improve performance

Nginx 性能调优。虽然网上不乏各种 Nginx 性能调优的教程，但要明白，大多调优都是针对特定环境的，不一定可以放之四海而皆准，所以不要盲目跟随，这样反而有可能会降低系统性能和安全性。更多性能调优：https://www.nginx.com/blog/tuning-nginx/

#### 托管多个网站

配置文件

In NGINX speak, a *Server Block* basically equates to a website (same as *Virtual Host* in Apache terminology). NGINX can host multiple websites, and **each site’s configuration should be in its own file**, with the name formatted as `example.com.conf`. That file should be located at `/etc/nginx/conf.d/`.

关闭托管

If you then want to disable the site *example.com*, then rename `example.com.conf` to `example.com.conf.disabled`. 

日志文件

When hosting multiple sites, be sure to separate their access and error logs with specific directives inside each site’s server block

#### 缓存内容

NGINX can cache files served by web applications and frameworks such as WordPress, Drupal and Ruby on Rails.

1. Create a folder to store cached content:

   ​

   ```
   mkdir /var/www/example.com/cache/

   ```

2. Add the `proxy_cache_path` directive to NGINX’s `http` block. Make sure the file path references the folder you just created in Step 1.

   - /etc/nginx/nginx.conf

     `1``proxy_cache_path /var/www/example.com/cache/ keys_zone=one:10m max_size=500m inactive=24h use_temp_path=off;`


   - `keys_zone=one:10m` sets a 10 megabyte shared storage zone (simply called `one`, but you can change this for your needs) for cache keys and metadata.
   - `max_size=500m` sets the actual cache size at 500 MB.
   - `inactive=24h` removes anything from the cache which has not been accessed in the last 24 hours.
   - `use_temp_path=off` writes cached files directly to the cache path. This setting is [recommended by NGNIX](https://www.nginx.com/blog/nginx-caching-guide/).

3. Add the following to your site configuration’s `server` block. If you changed the name of the storage zone in the previous step, change the directive below from `one` to the zone name you chose.

   Replace *ip-address* and *port* with the URL and port of the upstream service whose files you wish to cache. For example, you would fill in `127.0.0.1:9000` if using [WordPress](https://www.nginx.com/resources/wiki/start/topics/recipes/wordpress/) or `127.0.0.1:2638` with [Ghost](https://docs.ghost.org/v1/docs/config#section-server).

   /etc/nginx/conf.d/example.com

   ```
   proxy_cache one;
       location / {
       proxy_pass http://ip-address:port;
       }
   ```

4. If you need to clear the cache, [the easiest way](http://nginx.2469901.n2.nabble.com/best-way-to-empty-nginx-cache-td3017271.html#a3017429) is with the command:

   ​

   ```
   find /var/www/example.com/cache/ -type f -delete

   ```

   If you want more than just a basic cache clear, you can use the [proxy_cache_purge](https://www.nginx.com/products/nginx/caching/#purging) directive.

#### 修改响应头

Use [*add_header*](https://nginx.org/en/docs/http/ngx_http_headers_module.html) directives in your configuration carefully. Unlike other directives, an `add_header`directive is not inherited from parent configuration blocks. If you have the directive in both, an `add_header` directive in a `server` block will override any in your `http` area.



Below are some of the more universally-applicable header modifications. There are many more available, and you should read through the [OWASP Secure Headers Project](https://www.owasp.org/index.php/OWASP_Secure_Headers_Project) for more information.



Disable Content Sniffing：Content sniffing allows browsers to inspect a byte stream in order to determine the file format of its contents. It is generally used to help sites that do not correctly identify the MIME type of their content, but it also presents a vector for cross-site scripting and other attacks. To disable content sniffing, add the following line to your configuration’s `http` block:

```
add_header X-Content-Type-Options nosniff;
```



Limit or Disable Content Embeddin

Content embedding is when a website renders a 3rd party element (div, img, etc.), or even an entire page from a completely different website, in a `<frame>`, `<iframe>`, or `<object>` HTML block on its own site.

The `X-Frame-Options` HTTP header stops content embedding so your site can’t be presented from an embedded frame hosted on someone else’s website, one undesirable outcome being a clickjacking attack. See [*X-Frame-Options, Mozilla Developer Network*](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options) for more information.

To disallow the embedding of your content from any domain other than your own, add the following line to your configuration:

```
add_header X-Frame-Options SAMEORIGIN;

```

To disallow embedding entirely, even from within your own site’s domain:

```
add_header X-Frame-Options DENY;
```



Cross-Site Scripting (XSS) FilterPermalink
This header signals to a connecting browser to enable its cross-site scripting filter for the request responses. XSS filtering is usually enabled by default in modern browsers, but there are occasions where it’s disabled by the user. Forcing XSS filtering for your website is a security precaution, especially when your site offers dynamic content like login sessions:

```
add_header X-XSS-Protection "1; mode=block";
```



### part3: server website via https

https://linode.com/docs/web-servers/nginx/enable-tls-on-nginx-for-https-connections/



##  Performance & Security



## Serve Python Project



## Server PHP Project



托管静态内容

https://docs.nginx.com/nginx/admin-guide/web-server/serving-static-content/