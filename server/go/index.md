本文针对 CentOS 7，对于其它 Linux 发行版可能部分适用

虽然可以通过 `yum install go` 来安装，不过通过 yum 安装的版本较低，接下来我们将直接从 Go 官网下载二进制文件来安装。

1. 使用 `curl` 或 `wget` 从 Golang 官网[下载](https://golang.org/dl/)二进制文件，注意选择自己系统对应的版本

   ```
   curl -LO https://dl.google.com/go/go1.10.linux-amd64.tar.gz
   ```

2. 利用 `shasum` 检验文件

   ```
   shasum -a 256 go1.7.linux-amd64.tar.gz
   ```

3. 解压，将得到一个文件夹，里面的 `bin` 目录含有 go 相关的二进制文件

   ```
   tar -xvzf go1.7.linux-amd64.tar.gz
   ```

4. 更改二进制文件权限，并将其移动到 `/usr/local` 目录

   ```
   sudo chown -R root:root ./go
   sudo mv go /usr/local
   ```

5. 将 go 可执行文件目录添加到环境变量 `PATH` 中，创建、编辑文件 `/etc/profile.d`

   ```
   sudo vi /etc/profile.d/path.sh
   ```

   添加如下内容：

   ```
   export PATH=$PATH:/usr/local/go/bin
   ```

6. 如果打算开发 go 项目，需要创建 go 源文件目录、编译后可执行文件的目录以及包目录，在家目录下执行如下命令创建三个目录：

   ```
   mkdir -p ~/go/{bin,pkg,src}
   ```

7. 添加 go 相关的环境变量 `GOPATH` 和 `GOBIN`，用来指定上述刚刚创建的目录，编辑 `~/.bash_profile` 添加如下内容：

   ```
   export GOBIN="$HOME/go/bin"
   export GOPATH="$HOME/go/src"
   ```

8. 最后执行如下命令使得配置立即生效

   ```
   source /etc/profile && source ~/.bash_profile
   ```

   ​

   ​


经过上述配置后从网络下载的 go 二进制程序，会自动放在 `~/go/bin` 目录中



## Hugo 安装

Hugo uses [dep](https://github.com/golang/dep) to vendor dependencies, but we don’t commit the vendored packages themselves to the Hugo git repository. Therefore, a simple `go get` is *not* supported because the command is not vendor aware.

The simplest way is to use [mage](https://github.com/magefile/mage) (a Make alternative for Go projects.)

```
go get github.com/magefile/mage
go get -d github.com/gohugoio/hugo
cd ${GOPATH:-$HOME/go}/src/github.com/gohugoio/hugo
mage vendor
mage install
```

## Dep

`dep` is a prototype dependency management tool for Go. It requires Go 1.9 or newer to compile. **dep is safe for production use.**