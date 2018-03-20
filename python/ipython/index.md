---
title: IPython简介
author: Xiao Wenbin
date: 2016/12/02
category: python
---

# IPython

IPython主要由三大组件构成：

1. 增强版的python shell交互环境
2. Client和Kernel双进程交互的执行环境
3. 交互式并行计算包`ipyparallel`

## IPython's Read-Evaluate-Print Loop

IPython的读取-执行-打印循环（简称为REPL）流程如下：

1. 客户端（Client）读取用户输入指令并将指令发送给相应的执行进程
2. 执行进程（又被叫做Kernel）接受指令，运行后将结果返回给客户端
3. 值得注意的是，不同Client可以连接到相同Kernel，并且Client和Kernel可以部署到不同机器上

运行Client和Kernel的三种方式：

```
// 控制台客户端+默认Kernel
$ jupyter console
// Qt客户端+默认Kernel
$ jupyter qtconsole
// Web客户端+默认Kernel
$ jupyter notebook

// 指定客户端使用一个已经创建好的Kernel进程
$ jupyter console --existing
// 指定不同的Kernel
$ jupyter console --kernel=ir
```

## IPython交互环境

查看对象

```
obj?
obj??
%pdoc obj
%pdef obj
%psource obj
%pfile obj
```

查找模块

```
%psearch test*
%psearch t?st
```

调用系统shell命令

```
// 执行IPython自带命令
ls
// 执行系统命令，并打印执行结果
!ls
l = !ls
// 执行系统命令，并将结果以list形式返回
!!ls
// 扩展python变量到系统shell中
v = 'test.py'
!ls $v
```

文件系统导航

```
%cd
%bookmark
```

持久化

```
%store v
%store
%store -r
```

宏

```
%marco
```

会话日志

```
%history
```

调试

```
%run -d test.py
%debug
```

运行时间估计

```
%timeit
```

