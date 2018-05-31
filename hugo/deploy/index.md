部署到自己的服务器：提交到源码仓库服务器后，实现自动部署：

* 源码裸仓库 Git Hook
* 用 Hugo 在临时目录中构建网站
* 拷贝网站到 Web Server 的目录中
* 要考虑 Web Server 目录的权限和执行 Git Hook 的权限
* 主题以 git submodule 方式 pull 下来，那么在自动部署时要每次都要下载主题，岂不是很费事。目前采用强制 push submodule 到远程仓库的方式来解决。每次添加一个新的主题时，手动登录服务器
* 尤其优化，Git Hook 只应该作为事件触发机制，不应将工作放在其中，因为客户端要一直等待结果



https://www.digitalocean.com/community/tutorials/how-to-deploy-a-hugo-site-to-production-with-git-hooks-on-ubuntu-14-04

https://www.digitalocean.com/community/tutorials/how-to-use-git-hooks-to-automate-development-and-deployment-tasks