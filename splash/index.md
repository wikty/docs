---
title: 轻量级浏览器Splash
author: Xiao Wenbin
date: 2016/12/03
category: splash
tags: javascript, browser
---

## Splash

Splash 是用来渲染javascript的轻量级浏览器，并可以通过附带的HTTP API来使用渲染服务。

### 安装运行

1. 安装docker
2. 拉取splash镜像：`docker pull scrapinghub/splash`
3. 运行splash实例：`docker run -p 8050:8050 scrapinghub/splash`
4. 现在可以通过本地<http://localhost:8050>来访问splash的HTTP API服务

## 多接口启动

splash可以通过http，https等接口方式来提供服务，多接口启动splash：

```
docker run -p 5023:5023 -p 8050:8050 -p 8051:8051 scrapinghub/splash
```


*注*：端口5023供telnet访问，端口8050供http访问，端口8051供https访问

### 常见服务

splash服务可以通过HTTP API访问，API参数通过GET或者POST JSON来发送

#### render.html

执行页面的javascript，返回渲染过javascript后的html文档

#### render.png & render.jpeg

执行页面的javascript，返回渲染过javascript后的页面截图

#### render.har

返回splash实例跟网站的交互信息，包含请求和相应的相关信息，内容以[HAR](http://www.softwareishard.com/blog/har-12-spec/)格式返回

#### render.json

以JSON字典格式返回渲染过javascript的页面信息

#### execute

执行自定义的渲染脚本来返回页面内容，虽然上面看的接口包括了常见的使用情形，但也可以通过execute接口来执行自定义的渲染脚本

#### 在页面环境中执行自定义javascript

splash除了执行页面中的javascript外，还可以执行通过接口参数传递自定义javascript，这些代码将在页面加载完成后且页面开始渲染前执行，这样就允许我们使用自定义javascript来修改页面内容
