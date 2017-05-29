# 长城防火墙

## 前言

众所周知，我们生活在一个网络审查的环境中，访问敏感话题相关的互联网资源是被管制政府的。由于互联网天生的开放性，使得任何人访问任何内容都是没有限制的，政府为了防止别有用心的人进行网络舆论煽动或者传播极端言论等原因，而管制互联网的使用，将互联网上的洪水猛兽关在笼子里，或者说是将民众关在受到信息审查的互联网环境之内，发挥审查作用的一系列相关系统被叫做长城防火墙。长城防火墙是一个大型网络系统，分散部署于各地网络接入入口、骨干网络节点以及路由器等网络设备上。墙将互联网上的洪水猛兽挡在门外，同时也将民众同自由的互联网环境隔离开来。

政府希望的互联网是相对自由的，是在管制之下的自由，而不是绝对的自由，但由于相对自由往往不好去界定，在有些情况那些积极健康、有利于社会生产力提升的互联网内容也被墙挡在了门外，为此民众一直在探寻各种途径去突破长城防火墙，去享受科技文明的成果，突破长城防火墙并不意味着要去拥抱洪水猛兽，也不意味着要滥用互联网的开放性。渴望把脖子伸长，探头去看看知识自由之海，这也许是每个想要翻越长城防火墙人的共同心愿，用理性之剑迎击互联网上的洪水猛兽，用来求知之心吮吸互联网上的甘甜清泉，我们不向[方滨兴](https://zh.wikipedia.org/zh-hans/%E6%96%B9%E6%BB%A8%E5%85%B4)丢鞋，也不止步于墙内，我们希望再次拥抱自由的互联网，将内容审查交由自己的理性来完成。科学上网，抵制洪水猛兽，拥抱知识之海。

本文主要介绍几种科学上网的方案，并顺带介绍墙的工作原理，可以说墙的构建和翻墙技术是一场与时俱进的博弈，在网络被管制的这些年，墙越来越高越来越复杂，翻墙的梯子也越来越长越来越崎岖，虽然有些翻墙技术随着时间的推移变得不那么有效了，但只要翻墙的意志有继承者，梯子总规会搭起来。

## 墙

兵家有言“知己知彼，方能百战百胜”，在介绍科学上网的方案之前，先来看看长城防火墙通常使用那些技术来管制互联网。

### IP 封锁

长城防火墙系统会动态实时维护一张 IP 黑名单，当发现请求数据包的目标地址在黑名单中时，就会重置 TCP 连接，使得客户端误以为服务器端发生意外，而主动放弃继续向目标服务器发起请求。这种黑名单机制的封锁能力取决于黑名单的规模，为此长城防火墙会动态发掘应被封锁的 IP，维护实时黑名单来提高封锁能力。

长城防火墙的通过 TCP 重置来封锁目标 IP，其实就是在TCP连接握手的第二步即SYN-ACK之后分别向 TCP 两端连接的计算机发送 RST 数据包（RESET）重置连接，使得用户无法访问目标服务器的服务。重置 TCP 连接比直接丢弃数据包的封锁成本更低，因为当数据包被长城防火墙恶意丢弃之后，由于 TCP 协议的重发和超时机制，客户端会不停地等待和重发，这样加重了长城防火墙的负担，但是当客户端收到 RESET 消息时就会知道同服务端的连接被断开，不会继续等待重发了。

不过现在长城防火墙采用了更加高效的 IP 封锁方法，不同于以往的黑名单机制，探测到黑名单 IP 就重置 TCP 连接，目前长城防火墙采用的方法是路由扩散技术。简单来说路由扩散技术是这样的，通过在各地路由器中配置错误的数据包转发规则，恶意将发往某个 IP 的数据包转发至一个 “黑洞服务器” 而不是真实的目标服务器，数据包到达 “黑洞服务器” 会对其进行统计分析并做出虚假回应，使得数据包无法到达目标服务器，封锁得以实现。

### 端口封锁

结合 IP 封锁技术，长城防火墙进一步将封锁精确到端口。一些常见翻墙技术依赖特定端口提供代理服务，而长城防火墙针对这些端口的封锁，将会使得这些服务不可访问。常见被封锁端口有：

* [SSH](https://zh.wikipedia.org/wiki/Secure_Shell)的TCP协议22端口
* [PPTP](https://zh.wikipedia.org/wiki/PPTP)类型[VPN](https://zh.wikipedia.org/wiki/VPN)使用的TCP协议1723端口，[L2TP](https://zh.wikipedia.org/wiki/L2TP)类型[VPN](https://zh.wikipedia.org/wiki/VPN)使用的[UDP](https://zh.wikipedia.org/wiki/UDP)协议1701端口，IPSec类型VPN使用的[UDP](https://zh.wikipedia.org/wiki/UDP)协议500端口和4500端口，[OpenVPN](https://zh.wikipedia.org/wiki/OpenVPN)默认使用的TCP协议和UDP协议的1194端口
* [TLS](https://zh.wikipedia.org/wiki/TLS)/[SSL](https://zh.wikipedia.org/wiki/SSL)/[HTTPS](https://zh.wikipedia.org/wiki/HTTPS)的TCP协议443端口

### 域名服务器缓存污染

域名解析是访问用户接入互联网的基础技术，而所谓[域名服务器缓存污染](https://zh.wikipedia.org/zh-cn/%E5%9F%9F%E5%90%8D%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%BC%93%E5%AD%98%E6%B1%A1%E6%9F%93)是指，当用户发起域名查询时，长城防火墙会对请求解析的域名进行关键字匹配，一旦匹配，长城防火墙就会以域名解析服务器的身份返回虚假解析结果给用户，使得用户无法获得目标服务器正确的 IP 地址，从而使得目标服务器不可用。

全球的域名解析系统是层级架构的，当用户请求解析域名时，请求会先从本地域名服务器查询，在解析失败后再依次向上级域名解析服务器请求解析，直到获得解析结果，而且一般域名查询为了速度的考虑使用无连接的 UDP 协议。一般来说，当我们接入互联网时，默认会使用互联网服务提供商（ISP）所提供的域名服务器，这类域名服务器是易被污染的，其返回虚假解析结果直接导致用户无法获取目标网站正确的 IP 地址。虽然可以强制域名解析查询使用 TCP 协议，以此来获得目标服务器正确的 IP 地址，但如果长城防火墙对该 IP 进行了封锁，那么目标服务器仍然是不可用的。

### 干扰加密连接

在连接握手时，因为身份认证证书信息（即服务器的[公钥](https://zh.wikipedia.org/wiki/%E5%85%AC%E9%92%A5)）是明文传输的，防火长城会阻断特定证书的加密连接，方法和无状态TCP连接重置一样，都是先发现匹配的黑名单证书，之后通过伪装成对方向连接两端的计算机发送RST数据包（RESET）干扰两者间正常的[TCP](https://zh.wikipedia.org/wiki/TCP)连接，进而打断与特定IP地址之间的TLS加密连接（[HTTPS](https://zh.wikipedia.org/wiki/HTTPS)的443端口）握手，或者干脆直接将握手的数据包丢弃导致握手失败，从而导致TLS连接失败。但由于TLS加密技术本身的特点，这并不意味着与网站传输的内容可被破译。

切断[OpenVPN](https://zh.wikipedia.org/wiki/OpenVPN)的连接，防火长城会针对[OpenVPN](https://zh.wikipedia.org/wiki/OpenVPN)服务器回送证书完成握手创建有效加密连接时干扰连接，在使用TCP协议模式时握手会被连接重置，而使用UDP协议时含有服务器认证证书的数据包会被故意丢弃，使OpenVPN无法创建有效加密连接而连接失败。

### 关键字阻断

当长城防火墙探测到 TCP 请求数据包（比如 HTTP 请求头内容）中含有某些关键字时，会重置 TCP 连接来阻断对目标服务器的访问。

## 翻墙

接下来介绍几种常用翻墙技术，技术实施难易程度不同，相应它们的稳定性也会不同，通常情况下我们可以结合多种技术来搭建自己的梯子。

### 网页代理

### SSH 代理

### P2P 代理

### VPN 代理

### 代理 PAC

### Hosts

### GoProxy

https://github.com/phuslu/goproxy

### Shadowsocks

https://zh.wikipedia.org/wiki/Shadowsocks

### Lantern

https://zh.wikipedia.org/wiki/%E8%93%9D%E7%81%AF

### Psiphon

https://zh.wikipedia.org/zh-cn/%E8%B3%BD%E9%A2%A8

### 自由门

https://zh.wikipedia.org/wiki/%E8%87%AA%E7%94%B1%E9%97%A8

### 无界浏览

https://zh.wikipedia.org/wiki/%E6%97%A0%E7%95%8C%E6%B5%8F%E8%A7%88

### 浏览器以及插件

天行浏览器、畅游无限浏览器、星愿浏览器、X浏览器

uProxy

https://zh.wikipedia.org/wiki/UProxy

### 匿名浏览软件

Tor

https://zh.wikipedia.org/wiki/Tor

I2P

https://zh.wikipedia.org/wiki/I2P

JAP

https://zh.wikipedia.org/wiki/Java_Anon_Proxy

### 匿名 P2P

[ZeroNet](https://zh.wikipedia.org/wiki/ZeroNet) [Freenet](https://zh.wikipedia.org/wiki/Freenet) [StealthNet](https://zh.wikipedia.org/wiki/StealthNet)



https://zh.wikipedia.org/wiki/%E7%AA%81%E7%A0%B4%E7%BD%91%E7%BB%9C%E5%AE%A1%E6%9F%A5#.E6.B5.8F.E8.A7.88.E5.99.A8.E6.95.B4.E5.90.88.E5.8C.85

http://www.chinagfw.org/search/label/anti-censorship

https://fqf555.blogspot.com/2014/01/13.html

https://wsgzao.github.io/post/fq/

https://www.loyalsoldier.me/fuck-the-gfw-with-my-own-shadowsocks-server/