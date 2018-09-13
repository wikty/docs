## Windows查看端口被哪个程序占用

	# 查询占用端口的PID
	$ netstat -aon | findstr "8080"
	  TCP    127.0.0.1:8118         0.0.0.0:0              LISTENING       1760
	# 查询占用端口的程序名
	$ tasklist | findstr "1760"
	  privoxy.exe                   1760 Console                    1      8,788 K

## Windows命令行字符集切换为支持UTF-8

	$ chcp 65001

## Pandoc常用命令

	# markdown转为完整的html
	$ pandoc test.md -s -o your-filename-for-new-document.html
	# markdown转为LaTeX
	$ pandoc test.md -s -o your-filename-for-new-document.tex
	# 中文markdown转为pdf
	# 首先要下载模板文件放在当前目录：https://github.com/tzengyuxio/pages/tree/gh-pages/pandoc
	# 将模板文件中的字体替换为系统支持的中文字体，比如：mainfont="SimSun"
	$ pandoc test.md -o outfile.pdf --latex-engine=xelatex -template=pm-template.latex
	# markdown转为revealjs的slide
	# 下载revealjs文件放在当前目录
	$ pandoc -t revealjs -V theme=black -s -i --self-contained readme.md -o readme.html

## PHPMyAdmin上传文件大小限制修改配置文件项目

	post_max_size = 800M 
	upload_max_filesize = 800M 
	max_execution_time = 5000 
	max_input_time = 5000 
	memory_limit = 1000M

## SQL添加外键

	ALTER TABLE 表名 ADD FOREIGN KEY (字段名) REFERENCES 表名(字段名)

## SQL批量删除表

	Select CONCAT( 'drop table ', table_name, ';' ) 
	FROM information_schema.tables 
	Where table_name LIKE 'tbl_prefix_%’;

## SQL载入CSV文件

	LOAD DATA LOCAL INFILE ‘./test.txt’
	INTO TABLE table_name
	FIELDS TERMINATED BY ‘,’
	LINES TERMINATED BY ‘\n’
	(field1, field2, field3);

## mysql导入数据库文件

	mysql -u用户名 -p密码 数据库名 < data.sql

## Curl Post Json

	curl -H "Content-Type: application/json" -X POST -d '{"username":"mouse","command": 101}' http://localhost/users

## Git删除远程分支
	
	git push origin :branchName
	或者
	git push origin —delete branchName

## Git删除本地分支
	
	git branch -D branchName

## 远程登录下载服务器资源

	scp -r user@your.server.example.com:/path/to/foo /home/user/Desktop/

## 防止根用户误删文件的命令

	chattr和lsattr

## Git经典的多人协作方式

	# 克隆项目（含有master和develop分支，默认远程分支origin）
	$ git clone the-project-url
	# 从origin/develop分支检出到开发者自己的分支（同时创建开发者分支），注意：项目开发过程中一直要在开发者自己的分支上进行，千万不要跳转到master分支上修改项目
	$ git checkout -b wikty origin/develop
	# 修改项目后暂存代码
	$ git add .
	# 将暂存的代码提交到本地代码仓库
	$ git commit -m 'brief description about commit'
	# 拉取远程origin/develop分支中的变动到本地
	# --rebase的作用在于将远程变化和本地变化叠加而不是合并，这样产生的提交历史更为清晰
	$ git pull —-rebase origin develop
	# 如果远程的变动和本地的变动有冲突，则需要手动解决，查看冲突
	$ git status
	# 当没有冲突后，将本地代码提交到开发者相应的远程分支上
	$ git push origin wikty
	# 在Gitlab项目管理页面生成一个Merge Request
	该Merge Request注明，想要从开发者自己的分支合并到develop分支上，并需要制定一个code reviewer来负责代码审查，其实这个request一般会告知项目所有成员的，所以也可以将merge request看成是对特色功能的一种讨论请求
	# 负责reviewer的开发者在Gitlab管理页面进行审查
	审查通过将开发者分支合并到develop
	# 当要发布项目时，在Gitlab的管理页面
	将develop分支合并到master分支
	
	# 发布到线上服务器
	开发者本地checkout到master分支
	从gitlab拉取代码到本地master分支
	添加线上源码仓库，git remote add repo repo@testrepo:mycompany/myproject
	代码推送到线上源码仓库，git push repo master
	在本地master分支上打tag，git tag 1.0.627
	将tag发布到线上，git push repo 1.0.627
	使用项目发布程序，利用tag发布程序