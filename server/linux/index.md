# 起步

## VPS

VPS 供应商，选择 Linux 发行版，配置磁盘空间，Boot。

一般还会配置 root 用户的登录密码

## SSH 连接服务器

SSH 即是一个协议，又是客户端/服务器模式的一套软件。

在启动系统后，一般系统已经默认开启了 SSH 端口 22，并提供 SSH 服务。

我们可以从本地通过浏览器命令行接口或者 Command Line 来访问，不过首先你要有个 SSH 客户端。Linux 和 Mac 用户一般系统自带命令行 SSH，Windows 用户建议使用软件 [PuTTY](https://linode.com/docs/networking/using-putty)，下面以命令行 SSH 客户端为例来介绍使用方法：

登录服务器，root用户登录

```
ssh root@123.456.78.90
```

首次登陆将得到如下授权警告信息，输入 yes 并敲击回车键继续即可

```
The authenticity of host '123.456.78.90 (123.456.78.90)' can't be established.
RSA key fingerprint is 11:eb:57:f3:a5:c3:e0:77:47:c4:15:3a:3c:df:6c:d2.
Are you sure you want to continue connecting (yes/no)?
```

然后会提示要求输入密码

```
root@123.456.78.90's password:
```

看到类似如下所示，表明已经连接到了远程服务器的命令行

```
root@li123-456:~#
```

接下来就可以通过该命令行来管理配置服务器啦

## 更新系统

配置的 Linux 系统发行软件一般都是之前发布的，而在系统发布之后，针对该系统的漏洞等会用新的更新可用。从安全的角度来考虑，进入服务器后首先需要更新系统软件。并且更新系统应该作为一个日常的系统安全防范措施，应该定期更新系统才行。

 This applies the latest security patches and bug fixes to help protect your Linode against unauthorized access.

Installing software updates should be performed *regularly*. If you need help remembering, try creating a monthly alert with the calendar application on your desktop computer.

各个常用发行版更新系统的命令如下：

Debian/Ubuntu

```
apt-get update && apt-get upgrade
```

CentOS

```
yum update
```

Fedora

```
dnf upgrade
```

Arch Linux

```
pacman -Syu
```

## 设置 Hostname



疑惑？

A fully qualified domain name (FQDN) contains both a host name and a domain name.

The host name represents the network or system used to deliver a user to a certain address or location. The domain name represents the site or project that the user is accessing.

DNS 服务商处注册的域名，以及映射的 www.example.com 123.456.78.90 ，以及 blog.example.com 90.78.45.6123。跟自己服务器上设置的 hostname 有什么关系？Note that the hostname has no relationship to websites or email services hosted on it, aside from providing a name for the system itself.

疑惑？



为系统指定 hostname，该 hostname 跟托管在系统上的网站和邮件服务无关，最好不要起太常用的名字。

各个系统命令：

Arch / CentOS 7 / Debian 8 / Fedora / Ubuntu 16.04

```
hostnamectl set-hostname example_hostname
```

Debian 7 / Slackware / Ubuntu 14.04

```
echo "example_hostname" > /etc/hostname
hostname -F /etc/hostname
```

CentOS 6

```
echo "HOSTNAME=example_hostname" >> /etc/sysconfig/network
hostname "hostname"
```



为系统指定 fully qualified domain name

编辑 `/etc/hosts` 文件，在 `127.0.0.1 localhost` 后面添加一行：`127.0.1.1 sub.example.com system_hostname`



## 设置 Timezone

By default, a Linode’s Linux image will be set to UTC time (also known as Greenwich Mean Time), but this can be changed. It may be better to use the same timezone which a majority of your users are located in, or that you live in to make log file timestamps more sensible.

Debian / Ubuntu

```
dpkg-reconfigure tzdata
```

Arch Linux / CentOS 7

查看可用时区

```
timedatectl list-timezones
```

设置时区

```
timedatectl set-timezone 'Asia/Shanghai'
```



检查时间设置的结果，使用命令：

```
date
```



# 安全防护

保护主机避免未授权访问的攻击

## 定期更新系统

Keeping your software up to date is the single biggest security precaution you can take for any operating system. Software updates range from critical vulnerability patches to minor bug fixes, and many software vulnerabilities are actually patched by the time they become public.

系统自动更新富有争论：

There are arguments for and against automatic updates on servers. [Fedora’s Wiki](https://fedoraproject.org/wiki/AutoUpdates#Why_use_Automatic_updates.3F) has a good breakdown of the pros and cons, but the risk of automatic updates will be minimal if you limit them to security updates. Not all package managers make that easy or possible, though.

The practicality of automatic updates is something you must judge for yourself because it comes down to what *you* do with your Linode. Bear in mind that automatic updates apply only to packages sourced from repositories, not self-compiled applications. You may find it worthwhile to have a test environment that replicates your production server. Updates can be applied there and reviewed for issues before being applied to the live environment.

- CentOS uses *yum-cron* for automatic updates.
- Debian and Ubuntu use *unattended upgrades*.
- Fedora uses *dnf-automatic*.

## 添加普通用户

在安装系统时，系统默认会创建一个 root 用户，该用户是根用户，又叫超级用户，对系统用户无限制的任意权利，可以执行任何命令，处理任何资源。为了避免使用该用户时的误操作，我们要再自己创建一个权限受限的普通用户，以供平时跟系统的交互。

临时提升普通用户的权限：

Administrative tasks will be done using `sudo` to temporarily elevate your limited user’s privileges so you can administer your server. 如果系统没有安装 sudo，则需要先安装它。

CentOS / Fedora

创建用户

```
useradd newusername
```

修改密码

```
passwd newusername
```

添加到 wheel 组已获得 sudo 权限

```
usermod -aG wheel newusername
```

注：对于 CentOS 6 需要手动编辑配置文件 `/usr/sbin/visudo` 为 whell 组开启 sudo 权限

Ubuntu / Debian

创建用户，随后自动提示输入密码

```
adduser newusername
```

为用户添加 sudo 权限

```
adduser newusername sudo
```



退出系统，以普通用户的身份尝试 SSH 登录：

```
exit
ssh newusername@123.456.78.90
```

## 关闭 SSH 密码登录

By default, password authentication is used to connect to your Linode via SSH. A cryptographic key-pair is more secure because a private key takes the place of a password, which is generally much more difficult to brute-force.

首先需要创建一个授权的秘钥对

在创建之前，先检查一下用户家目录有没有秘钥对存在，防止创建时覆盖之前的秘钥对，一般位于 `~/.ssh/id_rsa*`

Linux / Mac 创建

```
ssh-keygen -b 4096
```

生成 id_rsa 私钥，id_rsa.pub 公钥

Windows 创建参见https://linode.com/docs/security/authentication/use-public-key-authentication-with-ssh/

创建秘钥对时，会提示输入一个 passphrase，虽然不是必须的，但建议设一个，这样别人就不能用你的私钥进行登录的



然后需要上传刚刚创建的**公钥**文件（注意不是私钥）

Linux

```
ssh-copy-id yourusername@123.456.78.90
```

Mac

首先需要在远程主机创建目录

```
mkdir -p ~/.ssh && sudo chmod -R 700 ~/.ssh/
```

然后在本机进行上传

```
scp ~/.ssh/id_rsa.pub yourusername@123.456.78.90:~/.ssh/authorized_keys
```

Windows

使用 [WinSCP](http://winscp.net/) 本地的公钥文件上传到远程服务器，需要注意的是要上传到服务器的路径：`/home/yourusername/.ssh/authorized_keys`

或者直接通过命令行登录远程服务器，创建目录和文件，并利用文本编辑器将公钥内容粘贴到上述文件中。



上传完成后，记得登录远程服务器，对目录和文件的权限进行修改：

```
sudo chmod 700 -R ~/.ssh && chmod 600 ~/.ssh/authorized_keys
```



退出系统，尝试以非密码方式登录一下 SSH，如果设置了 passphrase，会提示你输入



## 配置 SSH 守护进程

编辑文件 `/etc/ssh/sshd_config`，添加或取消注释配置项

禁止根用户通过 SSH 进行登录

仅允许普通用户通过 SSH 进行登录，根用户的权限，要么通过 sudo，要么登陆后使用 `su -` 命令来切换

```
PermitRootLogin no
```

禁止所有用户通过密码授权方式登录，看情况，如果经常从多台设备登录的话，应该保留密码登录方式

```
PasswordAuthentication no
```

限制仅接受 IPv4 或 IPv6 连接

```
# listen only on IPv4
AddressFamily inet
# listen only on IPv6
AddressFamily inet6
```

完成以上配置后，重启 SSH 服务以使配置立即生效：

CentOS 7 / Debian 8 / Fedora / Ubuntu 15.10

```
sudo systemctl restart sshd
```

CentOS 6 / Debian 7 / Unbuntu 14.04

```
sudo service ssh restart
```

## 分析 SSH 被暴力破解

CentOS 的 sshd 进程日志位于 `/var/log/secure`，其它发行版的 Linux 也许在 `/var/log/auth.log`

查看有哪些 IP 在破解 root 密码及其次数

```
sudo grep "Failed password for root" /var/log/secure | awk '{print $11}' | uniq -c | sort -nr | more
```

再来看破解猜测了哪些用户名

```
sudo grep "Failed password for invalid user" /var/log/secure | awk '{print $11}' | uniq -c | sort -nr | more
```

## 使用 DenyHosts 对 SSH 进行保护





## 使用 Fail2Ban 对 SSH 进行保护

[*Fail2Ban*](http://www.fail2ban.org/wiki/index.php/Main_Page) is an application that bans IP addresses from logging into your server after too many failed login attempts. Since legitimate logins usually take no more than three tries to succeed (and with SSH keys, no more than one), a server being spammed with unsuccessful logins indicates attempted malicious access.

Fail2Ban can monitor a variety of protocols including SSH, HTTP, and SMTP. By default, Fail2Ban monitors SSH only, and is a helpful security deterrent for any server since the SSH daemon is usually configured to run constantly and listen for connections from any remote IP address.

正常登录的话，尝试若干次就可以成功登陆了。但恶意攻击的登录，往往会尝试许多次，Fail2Ban 可以监控 SSH 的登录行为，对恶意尝试登录的进行屏蔽

很有用，以后配置一下

https://linode.com/docs/security/using-fail2ban-for-security/







## 移除无用的网络服务

Most Linux distributions install with running network services which listen for incoming connections from the internet, the loopback interface, or a combination of both. Network-facing services which are not needed should be removed from the system to reduce the attack surface of both running processes and installed packages.

查看网络服务

```
sudo ss -atpu
```

输出内容解读

```
Netid State Recv-Q Send-Q Local Address:Port Peer Address:Port
tcp LISTEN 0 128 *:ssh *:* users:(("sshd",pid=3675,fd=3))
```

sshd 进程监听来自任何地址任何端口的 IPv 4 连接

```
Netid State Recv-Q Send-Q Local Address:Port Peer Address:Port
tcp LISTEN 0 128 :::ssh :::* users:(("sshd",pid=3675,fd=4))
```

sshd 进程监听来自任何地址任何端口的 IPv 6 连接



移除软件命令

**Arch**

```
sudo pacman -Rs package_name

```

**CentOS**

```
sudo yum remove package_name

```

**Debian / Ubuntu**

```
sudo apt purge package_name

```

**Fedora**

```
sudo dnf remove package_name
```



## 防火墙

Using a *firewall* to block unwanted inbound traffic to your Linode provides a highly effective security layer. By being very specific about the traffic you allow in, you can prevent intrusions and network mapping. A best practice is to allow only the traffic you need, and deny everything else. 

最常见的几款防火墙应用

- [Iptables](https://linode.com/docs/security/firewalls/control-network-traffic-with-iptables) is the controller for netfilter, the Linux kernel’s packet filtering framework. Iptables is included in most Linux distributions by default.
- [FirewallD](https://linode.com/docs/security/firewalls/introduction-to-firewalld-on-centos) is the iptables controller available for the CentOS / Fedora family of distributions.
- [UFW](https://linode.com/docs/security/firewalls/configure-firewall-with-ufw) provides an iptables frontend for Debian and Ubuntu.

留在以后详细配置。





