## 安装较新版的二进制

包含在 Linux 系统官方仓库的二进制程序通常版本较老，想要安装新版二进制程序，有时就需要从软件提供商的仓库来安装，比如安装新版的 Nginx



添加远程仓库：

```
sudo vi /etc/yum.repos.d/nginx.repo
```

编辑如下内容到该文件：

```
[nginx]
name=nginx repo
baseurl=http://nginx.org/packages/mainline/<OS>/<OSRELEASE>/$basearch/
gpgcheck=0
enabled=1
```

- The `/mainline` element in the pathname points to the latest mainline version of NGINX OSS; delete it to get the latest stable version
- `<OS>` is either `rhel` or `centos`
- `<OSRELEASE>` is the release number (`6`, `6._x_`, `7`, `7._x_` and so on)

在 CentOS 7 上安装最新稳定版的 Nginx

```
[nginx]
name=nginx repo
baseurl=http://nginx.org/packages/centos/7/$basearch/
gpgcheck=0
enabled=1
```

更新仓库内容：

```
sudo yum update
```

安装 Nginx：

```
sudo yum install nginx
```

