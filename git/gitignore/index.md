## 简介

在 Git 版本系统中，文件的状态一般有三种：

* tracked，文件已经提交到版本控制系统中
* untracked，文件在工作目录中，还未提交到版本控制系统中
* ignored，文件在工作目录中且未提交，版本控制系统忽略了它

而 gitignore 机制正是用来让用户来指定哪些还未被追踪的文件将被版本控制系统忽略。注：仅适用于还未被追踪的文件，该机制对已经提交到版本控制系统的被追踪文件是无效的。

常见的应该被版本系统忽略的文件有：

* 第三方库，如：`node_modules` 目录
* 编译文件，如：`*.pyc`, `*.class` 等文件
* 软件构建目录，如：`bin`, `out` 等
* 软件运行时生成的文件，如：`*.log`, `*.lock` 等
* 操作系统文件，如：`.DS_Store` 文件
* 编辑器和 IDE 文件，如：`.idea` 目录

接下来将介绍，如何配置 Git 使得，使用版本控制系统时可以自动忽略类似这样的文件。

## 配置方式

gitignore 机制是通过编辑配置文件的方式来实现的，在运行相关命令时，Git 会自动查找 gitignore 配置文件来决定是否要忽略某个路径。

根据用户的使用意图不同，gitignore 的配置方式也不同：

* 在项目中使用，并且想要把 gitignore 规则连同项目一起分发共享给其它用户

  这类 gitignore 规则往往意味着参与该项目的所有用户都会用到它们，此时一般我们会在项目的顶级目录中创建 `.gitignore` 文件来保存配置内容。且该文件会被提交到版本控制系统。

* 在项目中使用，但仅仅限于用户自己在本地使用

  有时用户会在项目中某些文档、数据，但又不想要把这些文件共享给其它用户，此时可以将这类 gitignore 规则写入项目目录中的 `$GIT_DIR/info/exclude` 文件。此文件是不会被提交到版本控制系统的。

* 用户本地的全局配置，针对于用户自己的操作系统、文本编辑器、编程语言以及 IDE 工具等工作环境

  用户一般都有自己偏好的工作环境，有时某些工具会产生临时文件，如：Mac OS 系统会产生 `.DS_Store` 文件，Python 脚本运行时会产生 `__pycache__` 目录。此时我们一般想要在所有项目中都忽略这些文件，也即进行全局配置：通过 Git 命令指定用户的全局 gitignore 配置文件位置：`git config --global core.excludesfile FILENAME`（全局配置文件的默认位置是 `$HOME/.config/git/ignore`），然后将规则写入该文件中。

以上的多种配置方式，是可以共同存在且有相互叠加的效果。在 Git 决定是否会忽略某个还未被追踪的文件或目录时，会综合考虑上述各个配置文件中的规则，按照一定优先级别来作出最终决定。上述各种方式的优先级依次递减。

## gitignore 规则

gitignore 配置文件中，每行内容指定一个文件匹配模式，被匹配到文件将会被版本控制系统忽略追踪。

模式语法如下：

* 空白行没有任何意义，可用来增加文件可读性。
* 一行内容在行尾的空白符没有任何意义。
* hash 字符 `#` 是文件中用于注释的字符，一行内容以 `#` 开头则是注释。
* slash 字符 `/` 在规则中的语义是用来表示目录的，可能出现在行首、行中、行尾。
* 不含有 slash 字符 `/` 的字符串，将被当成 shell 通配符来解析，可以使用通配符中的 `*`, `?`, `[]` 等元字符。
* 以 slash 字符 `/` 作为行首的，在顶级目录中进行匹配。
* 以 slash 字符 `/` 作为行尾的，不匹配文件项，只匹配任意位置的目录项。
* 行首的字符 `!` 表示对规则取反，也即规则本来用以指定排除哪些文件，行首添加 `!` 后则表示要包括这些文件。值得注意的是，这类规则要比定义在其前面的排除规则的优先级更高，也即某文件如果在前面被规则忽略不予以追踪了，后面可以使用取反规则来再次包括它。不过如果一个目录已经被之前的规则忽略了，那么取反规则是无法让该目录中的文件再次追踪的。
* backslash 字符 `\` 是文件中的转义符，可以用来对行首的 `#`, `!` 等字符转义，使其失去特定的语义，变为普通字符。
* 双星号 `**` 具有跨越目录层级的语义，出现在行首、行中、行尾分别具有不同的语义：
  * 行首且紧跟 slash 字符 `/` ，表示匹配任何位置 。如：规则 `**/foo` 匹配任何位置的 `foo` 文件或目录，等价于规则 `foo`；规则 `**/foo/bar` 将匹配任何地方的 `foo/bar` 文件或目录。
  * 行尾且前一个字符是 slash `/`，表示递归的匹配目录中的任何内容。如：规则 `foo/**` 将匹配目录 `foo` 中及其子目录中的任何内容。
  * 行中其前后都有一个slash `/` 字符，表示中间可以有任意多层级的目录。如：规则 `a/**/b` 既可以匹配 `a/x/b`，也可以匹配 `a/x/y/b`，还可以匹配 `a/b`。

上述在项目中作为共享目的而使用的 `.gitignore` 配置文件，一般推荐仅在项目顶级目录中（即 Git 代码仓库目录所在位置）创建一个配置文件。不过 Git 也支持项目中同时存在多个 `.gitignore` 文件，并且这些文件可以位于项目的子目录中。位于项目子目录的 `.gitignore` 中跟文件路径相关的规则，以当前 `.gitignore` 所在项目的子目录作为根路径，并且其优先级比项目顶级目录中的 `.gitignore` 更高。

## 检验调试

有时候，我们不太确定某个规则是否能达到预期的效果，或者到底是哪里配置的规则起到了作用，这时可以使用以下命令：

```
git check-ignore -v FILENAME
```

该命令会检查 FILENAME 是否会被忽略，以及是哪个配置文件的哪个规则发生了效果。并且 FILENAME 不一定必须是已经存在的文件或目录，只要是一个有效的路径名称即可。

## 规则模板

* GitHub 的 [gitignore](https://github.com/github/gitignore) 仓库含有常用的 gitignore 模板。
* [gitignore.io](https://www.gitignore.io/) 提供了线上服务，可以根据用户输入的环境来自动生成 gitignore 文件。

## 已追踪文件

要想使得 gitignore 对已提交的追踪文件生效，先要撤销对它们的追踪才行：

```
git rm --cached FILENAME
```

该命令将会把 FILENAME 从本地仓库中删除，如果想要一并也从本地目录删除的话，就去掉 `--cached` 选项。

## 示例

**示例一**

目录结构如下：

```
project/
	data/
	foo/
		bar/
		non.ppt
	help.txt
	.gitignore
```

现在想要排除 project 中除了 foo/bar 目录和 .gitignore 文件以外的所有文件，则 .gitignore 内容如下：

```
# include .gitignore in anywhere
!.gitignore

# exclude everything in the top-level directory
/*
# include foo directory
!/foo
# exclude everythin underneath the foo directory
/foo/*
# include foo/bar directory
!/foo/bar
```

**示例二**

目录结构如下：

```
project/
	data/
		/train
			a.txt
			b.txt
			.gitignore
		/test
			c.txt
			d.txt
			.gitignore
		mnist.data
		.gitignore
	model/
	tests/
	docs/
	.gitignore
```

项目中 `data` 目录中有很大的数据文件，我们不想要将它们提交到远程代码仓库，同时我们又希望将 `data` 中的目录结构提交到远程：

`project/data/.gitignore` 内容如下：

```
# ignore everything in this directory
*
# except sub-directories
!*/
# except this file
!.gitignore
```

`project/data/a/.gitignore` 和 `project/data/b/.gitignore` 内容如下：

```
# ignore everything in this directory
*
# except this file
!.gitignore
```

