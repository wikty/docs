有很多服务希望随系统一起启动，这样在重启系统后，不必要在逐一启动它们

## CentOS 以前的方法：

`chkconfig`

## CentOS 7 的方法：

`systemctl`

对于 httpd 以及 mysqld 可以这样做

开启随系统启动

```
sudo systemctl enable httpd.service
```

关闭随系统启动

```
sudo systemctl disable httpd.service
```



不过我有两个疑问：

* 服务在启动时会加载配置文件，要如何指定服务的配置文件加载机制呢？
* 如果我的服务不是 Apache 和 MySQL 这种标准的服务，而仅仅是一个二进制文件，该如何处理，先把它做成一个 service 吗？



感觉这两篇文章可以解惑

https://www.digitalocean.com/community/tutorials/how-to-configure-a-linux-service-to-start-automatically-after-a-crash-or-reboot-part-1-practical-examples

https://www.digitalocean.com/community/tutorials/how-to-configure-a-linux-service-to-start-automatically-after-a-crash-or-reboot-part-2-reference