[*Fail2Ban*](http://www.fail2ban.org/wiki/index.php/Main_Page) is an application that bans IP addresses from logging into your server after too many failed login attempts. Since legitimate logins usually take no more than three tries to succeed (and with SSH keys, no more than one), a server being spammed with unsuccessful logins indicates attempted malicious access.

Fail2Ban can monitor a variety of protocols including SSH, HTTP, and SMTP. By default, Fail2Ban monitors SSH only, and is a helpful security deterrent for any server since the SSH daemon is usually configured to run constantly and listen for connections from any remote IP address.

正常登录的话，尝试若干次就可以成功登陆了。但恶意攻击的登录，往往会尝试许多次，Fail2Ban 可以监控 SSH 的登录行为，对恶意尝试登录的进行屏蔽

很有用，以后配置一下

https://linode.com/docs/security/using-fail2ban-for-security/