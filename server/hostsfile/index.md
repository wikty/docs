Linux 系统中的 `/etc/hosts` 配置文件中含有 IP 地址到主机名、域名以及别名的静态映射关系，又可以将其当成是 DNS 解析服务的本地映射表，并且在系统进行 DNS 解析时，它们的优先级比 DNS Server 的更高。

该文件中几种类型的记录项

别名：This is often done when previewing a site during development before the domain is live.

```
123.456.78.9 mysite
```

域名：This is useful when hosting a web or mail server.

```
123.456.78.9 example.com
```

映射 IPv6 地址：Map the alias `backupserver` to the given private IPv6 address:

```
fe80::f03c:91ff:fe24:3a2f backupserver
```

阻断流量：Block all traffic to and from the domain `example.com`. This is frequently used for content filtering or blocking advertisements 广告 via a hosts file.

```
0.0.0.0 example.com
```

Set a [fully qualified domain name](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) (FQDN). In the example below, replace *example_hostname*with your system’s hostname. The domain *example.com* can be a public internet domain (ex. a public website) or the domain of a private network (ex. your home LAN), or a subdomain (subdomain.example.com). It’s important to add the FQDN entry immediately after the *localhost* line, so it looks like below:

```
127.0.0.1 localhost
127.0.1.1 hostname.example.com example_hostname

```

A FQDN does not necessarily need to have any relationship to websites or other services hosted on the server (although it may if you wish). As an example, you might host `www.something.com` on your server, but the system’s FQDN might be `mars.somethingelse.com`.

The domain you assign as your system’s FQDN should have an “A” record in DNS pointing to your Linode’s IPv4 address. For IPv6, you should set up a “AAAA” record in DNS pointing to your Linode’s IPv6 address. For more information on configuring DNS, see our [DNS records](https://linode.com/docs/networking/dns/dns-records-an-introduction)guide.

配置 DNS 解析来源优先顺序

通过文件  `etc/nsswitch.conf` 来配置，确保 `hosts:      files dns myhostname` 这一行中

To ensure than the system prefers resolving domains listed in your hosts file over DNS resolution, the word `files` must appear in the line before `dns`.