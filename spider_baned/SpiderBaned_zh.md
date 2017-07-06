## 网站的反爬虫策略

1. 根据访问频率/访问量进行IP限制

	真实用户跟爬虫访问网站的频率高低不同，爬虫访问有两个特点：短时间集中访问以及访问具有时间周期性，爬虫的访问频率特点因为不同于普通用户，很容易被网站后台识别为爬虫。同理网站也会根据访问者对网站的访问量来识别爬虫，一般超过一定频率或一定访问量时，网站会弹出验证码窗口对访问者进行验证。

2. 根据访问内容有序性

	比较高级的反爬虫策略，通过识别访问者是否在遍历访问整个网站内容来识别是否为爬虫

3. HTTP请求头信息检查

	真实用户使用浏览器请求网页跟爬虫请求网页时，发起的HTTP请求头信息是不同的，常见的爬虫都有不同于浏览器的User-Agent字段等头信息，一般来说网站会根据HTTP请求头信息中的User-Agent,Refer等常见字段来识别爬虫，当然爬虫是可以伪造头信息的

4. 网页内容动态生成

	在Web 2.0时代，很多网页从后端渲染转换为了前端异步加载的模式，简单来说网页内容是在用户跟浏览器交互时才通过js来动态加载的，而不是一开始下载网页时就加载好了网页内容。这样的内容加载模式对于普通爬虫来说是爬取不到内容的，只有可以解析js脚本的爬虫才可以爬取网站内容

5. 频繁改变网页结构

	爬取获取网页数据的方式，就是通过解析HTML文档的结构来得到内容的，当网页结构变化时，之前的爬取就变无效了，这个问题比较棘手，只能通过网页结构校验程序及时的同时开发人员修改爬虫，当然如果网站内容不需要周期性爬取的话，这个问题是不存在的

## 避免爬虫被封锁的备选方案

1. 调低爬取速度
2. 使用Tor网络代理
3. 使用浏览器内核Phantomjs/Zombiejs
4. 构建自己的动态IP代理池
5. 购买爬虫云服务Crawlera
6. 关于防封锁的小技巧

## 调低爬取速度

该方案是规避封锁跟爬取效率的折中，一方面我们想要快速的爬取大量内容 ，另一方面我们又不希望被网站封锁。因此可以大量测试来获得网站最高限制访问频率，以后以该频率进行访问。

实际上网站不仅仅对访问频率进行限制，对访问量也进行了限制，即使以合适的频率去访问网站，当访问量超过一定额度时网站也有可能进行封锁

很多网站在检测到异常访问频/量后，访问者发起的任何请求都会得到一个验证码窗口的响应，只有访问者正确填写了验证码才能进行后续访问，否则会被识别为爬虫，这是为了保护某些访问量异常的真实用户被误判为爬虫，毕竟爬虫自动填写验证码并不简单，不过我们也可以用机器学习的方法来完成验证码的识别工作

总之，这个方案本身就是放弃生产效率的方案，不断是规避访问频率还是规避访问量都会影响到生产效率。


## 使用Tor网络代理

Tor网络可以看成一个复杂的IP代理池，爬虫可以通过Tor网络来发起网页请求，对爬虫来说可以就跟使用了动态IP一样，所以不需担心被网站封锁

该方案的缺点是，Tor网络在国内被屏蔽了，访问时不是很稳定。

## 使用浏览器内核Phantomjs/Zombiejs

有的网站采用前端JS代码动态加载页面内容的模式，因此爬虫需要能够运行JS才能够加载页面内容，为了让爬虫运行JS代码，可以使用浏览器内核Phantomjs/Zombiejs等。

但该方案仅仅限于解决前端异步加载页面内容的问题，对访问频率/量限制等问题没有任何作用

## 构建自己的动态IP代理池

该方案可以认为跟使用Tor网络类似，不过这里我们需要自己从互联网上收集免费可用的代理IP，并实时去校验IP的可用性，其实就相当于构建一个动态IP代理池，不断从互联网上收集代理IP并实时校验可用性，以供爬虫使用。

该方案可行性比较高，就是互联网上免费且稳定的IP量比较少，而且由于很多人在用，稳定IP可用的时效会比较短。

## 购买爬虫云服务

爬虫云服务一般是分布式部署的，它们自己有一套复杂的规避封锁的机制，像动态IP代理池、失败请求重新恢复、自动控制访问速率等。

爬虫云服务厂商[Crawlera][https://crawlera.com/]是不错的选择，将其集成到爬虫框架scrapy很简单

## 防封锁的小技巧

1. 动态切换User-Agent，爬虫的默认User-Agent跟浏览器的不同
2. 禁用cookie，有的网站使用cookie来统计访问频率
3. 延迟下载，每个请求之间随机休眠若干秒，让请求的时间周期模式不太明显
4. 使用搜索引擎缓存页面进行爬取，只适合抓取页面片段，要想抓取整个页面内容需要访问原网页

## 总结

现在拟采用的方案是构建我们自己的IP代理池，同时在代理池构建好之前，暂时使用Tor代理来爬取数据。