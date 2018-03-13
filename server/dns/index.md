hostname and domain name

- hostname

   

  is the name given to the

   

  end-point

   

  (the machine in question)

  - and will be used to identify it over DNS if that is configured

- domain

   

  is the name given to the '

  network

  '

  - it will be required to reach the network from an external point (like the Internet)

It is usually written in the form,

> `hostname.domain.com` -- for example

If you are in (say) a college campus named called '`The-University`',
and its domain is called '`theuniversity.org`',
a machine on the campus network called '`mymachine`' would be addressed as, '`mymachine.theuniversity.org`'.

If you were trying to connect to this machine from your home network,
you would address it with that full name.
The **domain** part would reach you to the campus network
and the **hostname** would let you reach the exact machine in the campus.
I am avoiding the details of IP Addressing and gateways here.

For this reason, while accessing the machine from another machine within the campus
may work with just the hostname (`mymachine`) without the use of the domain name.

To taken an analogy, if you are in the same city, the street name suffices.
But, to address a place in another city, you would usually add the city name after the street.



IP address

An *IP (Internet Protocol) address* is a numerical string, like `203.0.113.0`, that is used to identify computers connected to a network, like the Internet. However, while computers can organize and process numbers like IP addresses very quickly, most people find it easier to remember words or phrases.



Domain name

some words to identify a computer



DNS

*DNS (Domain Name System)* allows us to reference computers by easy-to-remember *domain names*, like `example.com`, instead of IP addresses. 



DNS records

*DNS records* define which IP addresses map to which domain names and how to handle other kinds of requests a domain might receive.



How to make a connection between IP to domain name?

First, you need to purchase a domain name from a domain name registrar. Second, you need to set up DNS records for your domain by using a DNS hosting service.

Godaddy 既提供域名注册，有提供域名托管服务。即可以通过 Godaddy 来管理 DNS records。



DNS records

每种记录都有多个字段，各个字段取值也不同。每种记录的功能不同。

* A record, 域名到 IPv4 地址的映射
* AAA record, 域名到 IPv6 地址的映射
* CNAME record, 一个域名到另一个域名的映射
* MX record, 处理邮件的域名到另外一个域名/IP的映射
* TXT record, 为主机名关联一个字符串
* NS rescord, 为域名或子域名指定一个负责 DNS 解析的DNS server
* SRV record, 域名端口跟特定服务的映射
* ​



各种记录都有的字段 TTL

**TTL** record, or time to live, which determines how long the record will live in a visitor's local cache.

Because loading data from a local cache is fast, high TTL values make a visitor's experience faster. However, until their local cache expires and is updated by a new DNS lookup, visitors won't see any DNS changes you've made. As a result, higher TTL values give visitors better performance while lower TTL values ensure that DNS changes are picked up quickly.



**A** record, maps an IPv4 address to a domain name. This determines where to direct any requests for a domain name.

 A records have the following fields.

- HOSTNAME

  , which can be set to:

  - The **root domain** (`@`). To map a root domain, like `example.com`, to an IPv4 address, enter the `@`symbol.
  - A **subdomain prefix** (e.g. `www`). To create a subdomain, enter the subdomain prefix. For example, to create `www.example.com`, you would enter `www`.
  - A **wildcard** (`*`). To direct requests for a non-existent subdomain to a server or load balancer, enter `*`. However, if any kind of DNS record exists for a hostname, the wildcard will not apply; you will need to explicitly create an A record for it.

- WILL DIRECT TO

  , which can be set to:

  - A **DigitalOcean Droplet or Load Balancer** by typing its name and selecting it from the menu.
  - A **non-DigitalOcean resource** by entering its IP address.

It is possible to add multiple records for the same DNS entry, each pointing to a different IP address. 这种情况就是利用 DNS 均衡负载。



**AAAA** record, also called a Quad A record, maps an IPv6 address to a domain name. This determines where to direct requests for a domain name in the same way that an A record does for IPv4 addresses.

AAAA records have the following fields.

- HOSTNAME

  , which can be set to:

  - The **root domain** (`@`). To map a root domain, like `example.com`, to an IPv6 address, enter the `@`symbol.
  - A **subdomain prefix** (e.g. `www`). To create a subdomain, enter the subdomain prefix. For example, to create `www.example.com`, you would enter `www`.
  - A **wildcard** (`*`). To direct requests for a non-existent subdomain to a server or load balancer, enter `*`. However, if any kind of DNS record exists for a hostname, the wildcard will not apply; you will need to explicitly create an AAAA record for it.

- WILL DIRECT TO

  , which can be set to:

  - A **DigitalOcean Droplet** by typing its name and selecting it from the menu. All Droplets will be displayed on the list, but only those with IPv6 addresses can be selected.
  - A **non-DigitalOcean resource** by entering its IPv6 address.



**CNAME** record,  defines an alias for an A record; it points one domain to another domain instead of to an IP address. When the associated A record’s IP address changes, the CNAME will follow to the new address. 

CNAME records have the following fields.

- **HOSTNAME**, which should be set to the subdomain prefix for the new alias you want to create.
- **IS AN ALIAS OF**, which should be set to the hostname where the alias should point. For the alias to work, the hostname must have an A record or be handled by a wildcard A record. 可以用 @ 表示根域名或者输入一个子域名



**MX** record specifies the mail servers responsible for accepting email on behalf of your domain. Providers often make multiple name servers available so that if one is offline, another can respond. Each server needs its own MX record.

MX records have the following fields.

- **HOSTNAME**, which determines which host should accept email. In most cases, the hostname field should be set to `@` so that it applies to the base domain.
- **MAIL PROVIDERS MAIL SERVER**, which points to the hostname with the A record for the mail server.
- **PRIORITY**, which indicates the order in which the mail servers should contacted. This field takes a positive whole number where 1 is the highest priority.



**TXT** record is used to associate a string of text with a hostname. These are primarily used to verify that you own a domain.

TXT records have the following fields.

- **VALUE** (e.g. `example_name=example_value`), which is a name-value pair separated by an equal sign, `=`.
- **HOSTNAME**, which can be set to:
  - The **root domain** (`@`). To map a root domain, like `example.com`, to an IPv4 address, enter the `@`symbol.
  - A **subdomain prefix** (e.g. `www`). To create a subdomain, enter the subdomain prefix. For example, to create `www.example.com`, you would enter `www`.



**NS** record specifies the *name servers*, or servers that provide DNS services, for a domain or subdomain. You can use these to direct part of your traffic to another DNS service or to delegate DNS administration for a subdomain.

NS records have the following fields.

- HOSTNAME

  , which can be set to:

  - The **root domain** (`@`). To map a root domain, like `example.com`, to an IPv4 address, enter the `@`symbol.
  - A **subdomain prefix** (e.g. `www`). To create a subdomain, enter the subdomain prefix. For example, to create `www.example.com`, you would enter `www`.
  - A **wildcard** (`*`). To direct requests for a non-existent subdomain to a server or load balancer, enter `*`. However, if any kind of DNS record exists for a hostname, the wildcard will not apply; you will need to explicitly create an A record for it.

- **WILL DIRECT TO**, which should be set to the name server.



**SRV** record specifies a hostname and port number for a specific service to direct certain types of traffic to particular servers.







you can use [DNS records](https://linode.com/docs/hosting-website#add-dns-records) to point a domain name at your server and give it a more recognizable and memorable identifier.