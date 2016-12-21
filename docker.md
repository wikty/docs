## Docker

Docker 为应用程序提供了独立的运行环境，使得在应用程序在构建，测试以及部署时运行在相同的环境下，更加可移植。简单来说Docker提供应用程序容器，使得应用程序具备运行所需环境，可以基于一个内核为不同的应用程序配置不同的库和环境，容器保证了运行环境的独立，使得应用程序相互之间不会影响到对方。总之，Docker可以看成为应用程序提供独立运行环境的容器

### Docker Workflow

1. 将应用程序代码以及依赖放入Docker容器

	* 创建[Dockerfile](https://docs.docker.com/engine/getstarted/step_four/)，用来指定运行环境以及拉取应用程序代码
	* 如果应用程序依赖外部服务，比如：MySQL，Redis等，需要在[Docker Compose file](https://docs.docker.com/compose/overview/)中引用它们的[镜像](https://docs.docker.com/docker-hub/repos/)
	* 通过[Docker Machine](https://docs.docker.com/machine/overview/)启动虚拟机来运行容器

2. 配置[网络](https://docs.docker.com/engine/tutorials/networkingcontainers/)以及[存储](https://docs.docker.com/engine/tutorials/dockervolumes/)

3. 上传到registry跟团队合作

4. 使用[Universal Control Plane](https://docs.docker.com/ucp/overview/)工具来管理多主机集群

5. 使用[Docker Cloud](https://docs.docker.com/docker-cloud/overview/)将应用程序部署到云上，或使用[Docker Datacenter](https://www.docker.com/products/docker-datacenter)部署到自己的物理主机上

### Windows上安装

在Windows上可以通过两种方式安装Docker：

* [Docker for Windows](https://docs.docker.com/engine/installation/windows/#docker-for-windows)

* [Docker Toolbox](https://docs.docker.com/engine/installation/windows/#docker-toolbox)

第一种安装方案，Docker是运行在windows本地的应用程序，至少需要64位的windows10，以及微软的Hyper-V开启

第二种安装方案，Docker不是windows本地的应用程序，而是通过docker-machine来创建Linux虚拟机以运行Docker



