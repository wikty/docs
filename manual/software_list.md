* Windows系统安装之前需要准备的软件安装包
  1. 无线网卡驱动（如果打算连接有线网络，无线驱动就暂时不需要）
  2. 显卡驱动（电脑没有显卡驱动，画面会很丑）
  3. 中文输入法软件（安装英文版系统的话，不可以输入中文）
  4. 浏览器（一般情况Windows系统对自带版本较低的IE，可以准备一个自己比较喜欢的浏览器安装包）

* 软件开发工具类
1.   Git
         网址：[https://git-scm.com/](https://git-scm.com/) 
         简介：包含Git GUI，Git Bash，Git CMD以及Git核心组件

2.   SourceTree (W, M)
           网址：[https://www.sourcetreeapp.com/](https://www.sourcetreeapp.com/)
       　简介：强大的Git GUI工具

3.   BitTorrent
           网址：[http://www.bittorrent.com/](http://www.bittorrent.com/)
           简介：BT下载工具

4.   在线HTML转PDF
           网址：[http://pdfcrowd.com/](http://pdfcrowd.com/)
           简介：还支持浏览器插件进行转换

5.   Markdown转PDF
           简介：NodeJS的一个第三方包可以实现转换功能，  npm install markdown-pdf
           简介：在线转换工具，http://markdown2pdf.com/

6.   Pandoc
           网址：[http://pandoc.org/](http://pandoc.org/)
           简介：实现各种文本文档（markdown，pdf，word，epub，latex等）之间的转换

7.   TeX/LaTeX for Windows
           网址： [http://miktex.org/](http://miktex.org/)
           简介：LaTeX的Windows实现

8.   Adobe Digital Editions
           网址：[http://www.adobe.com/solutions/ebook/digital-editions/download.html](http://www.adobe.com/solutions/ebook/digital-editions/download.html)
           简介：epub文件查看器

9.   在线Markdown文档编辑
           网址：[https://stackedit.io/](https://stackedit.io/)
           简介：炫酷的在线Markdown编辑器

10.   Sublime Text
          网址：http://www.sublimetext.com/
          简介：很好用的纯文本编辑工具，结合各种第三方包（https://packagecontrol.io/installation#Simple）可以搭建各种语言的IDE环境

11.   Atom
          网址：[https://atom.io/](https://atom.io/)
          简介：风格类似Sublime的黑客文本编辑工具，据说是GitHub社区开发的 

12.   Tor
          网址：[http://www.torproject.org/](http://www.torproject.org/)
          简介：通过Tor网络匿名访问互联网，提供socks5代理进入Tor网络，Vidalia跨平台的tor控制GUI工具

13.   Privoxy
          网址：[http://www.privoxy.org/](http://www.privoxy.org/)
          简介：提供http，https等代理，并可以将代理forward到socks代理。因此tor+privoxy是以http访问tor网络的解决方案

14.   CMake
         网址：[https://cmake.org/](https://cmake.org/) 
         简介：跨平台软件构建工具，通过配置文件控制构建过程，生成Makefile或者VS的workspace等构建文档，使得同一份源码可以使用make或VS来构建

15.   VirtualBox
          网址：[https://www.virtualbox.org/](https://www.virtualbox.org/)
          简介：虚拟机，在同一物理主机上可以模拟多个操作系统环境

16.   Vagrant
          网址：[https://www.vagrantup.com/](https://www.vagrantup.com/)
          简介：方便快速的搭建虚拟机开发环境，也即可以快捷的搭建配置了特定软件的虚拟机环境，比如基于Linux系统，需要PHP5.0以及Yii 2.0并且依赖curl库，只需要将这些配置信息写入就可以构建一致的开发环境

17.   Docker
          网址：https://www.docker.com/
          简介：提供容器开发环境，暂时理不清它跟vagrant的区别

18.   CoreOS
          网址：https://coreos.com/
          简介：一个操作系统，提供了在应用容器内部署应用所需要的基础功能环境以及一系列用于服务发现和配置共享的内建工具 

19.   FFmpeg
          网址：[http://www.ffmpeg.org/](http://www.ffmpeg.org/)
         简介：用来记录、转换数字音频、视频，并能将其转化为流的开源计算机程序

20.   Xmind
          网址：[http://www.xmind.net/](http://www.xmind.net/)
          简介：思维导图软件

21.   PuTTy
          网址：[http://www.putty.org/](http://www.putty.org/)
          简介：Windows上的SSH客户端

22.   SQLite browser
          网址：http://sqlitebrowser.org/ 
          简介：SQLite数据的GUI管理工具，可以增删改查

23.   Cmd Markdown
          网址：[https://www.zybuluo.com/cmd/#](https://www.zybuluo.com/cmd/#)
          简介：Markdown编辑工具

24.   Typora
          网址：[https://typora.io/](https://typora.io/)
          简介：将预览和编辑放在一起的markdown编辑器

25.   phantomjs 
          网址：[http://phantomjs.org/](http://phantomjs.org/) 
          简介：浏览器内核，提供了丰富的API来访问浏览器的功能

26.   selenium 
          网址：[http://docs.seleniumhq.org/](http://docs.seleniumhq.org/) 
          简介：用来模拟用户访问浏览器行为的工具，提供了各种语言来跟浏览器交互（即各种语言实现的webdriver）

27.   MinGW
      网址：[http://mingw.org](http://mingw.org)
      简介：提供常见GNU工具集用于开发Windows程序，同时MinGW并没有为Windows程序提供POSIX API的运行时库

28.   Cygwin

     网址：http://www.cygwin.com/

     简介：为Windows提供了大量GNU工具集，同时提供了POSIX API的动态运行时库，但是基于Linux的程序需要重新在Cygwin下构建，才能运行于Windows

29.   Curl

      网址：https://curl.haxx.se/

      简介：以URLs语法来进行数据传输，支持HTTP、HTTPS、FTP等常见网络传输协议

30.   EasyBCD

      网址：http://neosmart.net/EasyBCD/

      简介：辅助Windows系统上安装双体统的工具，可以方便的修改磁盘引导内容

31.   Ext2Fsd

      网址：http://www.ext2fsd.com/

      简介：在Windows上实现ext2文件系统的访问

32.   FlashBack

      网址：https://www.flashbackrecorder.com/

      简介：电脑屏幕录制软件

33.   Graphviz

     网址：http://graphviz.org/

     简介：图可视化

34.   Octoparse

     网址：http://www.octoparse.com/

     简介：不需要写代码就可以使用的爬虫客户端

35.   Redis

     网址：https://redis.io/

     简介：内存数据库，可以用来做消息队列

36.   UltraISO

     网址：https://www.ultraiso.com/

     简介：制作修改烧录ISO文件的软件，可以用来制作U盘启动盘

37.   XAMPP

     网址：https://www.apachefriends.org/zh_cn/index.html

     简介：一站式搭建PHP+Apache+MySQL环境

38.   Nginx

     网址：http://nginx.org/

     简介：服务器软件

39.   RunHiddenConsole

     网址：https://www.nginx.com/resources/wiki/start/topics/examples/phpfastcgionwindows/

     简介：在Windows脚本中启动进程，关闭脚本后不影响进程，常用来启动常驻系统的服务

40.   Rufus

     网址：https://rufus.akeo.ie/

     简介：制作U盘启动的小巧工具

41.   ​







* 软件开发语言类

  1. Anaconda
         网址：[https://www.continuum.io/](https://www.continuum.io/)
         简介：基于Python的数据科学平台，包含了IPython([http://ipython.org/)，Jupyter](http://ipython.org/%29%EF%BC%8CJupyter) Notebook(http://jupyter.org/) 
  2. PyCharm
         网址：[https://www.jetbrains.com/pycharm/](https://www.jetbrains.com/pycharm/)
         简介：Python开发的IDE
  3. RStduio
         网址： [https://www.rstudio.com/](https://www.rstudio.com/)
         简介：R开发的IDE
  4. Code::Blocks
         网址：[http://www.codeblocks.org/](http://www.codeblocks.org/)
         简介：C/C++开发的IDE
  5. Octave
         网址：[http://www.gnu.org/software/octave/](http://www.gnu.org/software/octave/)
         简介：可以看成是开源版Matlab的IDE