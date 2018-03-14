Linux 中许多服务都会将自己的日志写入到 `/var/log` 目录中



## Permission denied

当以一个普通用户运行一个服务时，如果遇到该问题，说明 `/var/log` 目录没有开放对普通用户的写入权限，而且也不应该开放。

The default permission for `/var` is 755 = `rwxr-xr-x`: readable and executable (you need both for a directory) by everyone, and only writable by root. Setting the permission on a file or directory to 777 is never right.

可以采用下面的方法来处理：

* 写入其它拥有写权限的文件
* 登录 root 用户，创建 `/var/log/yourservice.log` 日志文件，并将权限改为运行服务的用户

https://stackoverflow.com/questions/483781/how-should-i-log-from-a-non-root-debian-linux-daemon

## logrotate

