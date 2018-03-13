---
title: "Peewee, A ORM Writen By Python"
author: "Xiao Wenbin"
date: 2014-07-23T15:48:08-04:00
draft: true
tags: ["python"]
---

#Peewee, A Python's ORM Third Party Library#

ORM的全称是Object-Relational-Mapping，即通过class而不是SQL语句来操纵数据库，将复杂的SQL查询细节隐藏，直接将对象层次的关系暴露给程序员来访问数据库，Peewee是一个用Python实现的ORM，其很多特性与Django中所用的ORM相似，并且是轻量级的，可以同flask（一个python的web框架）结合使用，如果你需要的是python世界中轻量级的web解决方案，那么flask+peewee就很合适

##Peewee中的CRUD操作##

本文使用下面的代码作为讲解范例，代码中定义了 `BaseModel`，`User`, `Photo`, `Tag` 四个Model，其中`BaseModel`仅仅作为基类使用，每个`User`拥有多个`Photo`，并且`Photo`和`Tag`是多对多的关系

        import datetime

        from peewee import *

        database = SqliteDatabase('example.db')

        class BaseModel(Model):

            class Meta:

                database = database

        class User(BaseModel):

            username = CharField()

            password = CharField(default='')

            email = CharField()

            def set_password(self, passwd):

                self.password = passwd

        class Photo(BaseModel):

            user = ForeignKey(User, related_name='Photoes'

            created_date = DateTimeField(default=datetime.datetime.now)

            path = CharField()

            title = CharField()

        class Tag(BaseModel):

            user = ForeignKey(User, related_name='Tags')

            name = CharField()

        class PhotoTag(BaseModel):

            photo = ForeignKey(Photo, related_name='Tags')

            tag = ForginKey(Tag, related_name='Photoes')

        database.connect()

###Create，对象创建##

插入一行

        user = User.create(username='tom')

        user.email = 'noreply@163.com'

        user.set_password('noreply')

        user.save()  # user.id 是刚刚插入行的主键值

插入一行

        query = User.insert(**{'username': 'admin'})

        query.execute()

插入多行

        usernames = ['tom', 'james', 'tomans']

        usernames = [{'username': user} for user in usernames]

        query = User.insert_many(usernames)

        query.execute()

###Read, 对象读取###

读取一行

        user = User.get(username=='tomsan')  # 仅返回一个结果，如果没有匹配的结果则触发异常User.DoesNotExist

读取多行

        query = User.select()  # 表示返回所有列，所有行

        query.execute()  # 其实该query比较特殊是可以迭代的，在迭代时自动执行execute，所以像这样直接的调用并不常见

###Update, 对象更新###

更新一行

        user = User.get(User.id == 2)

        user.username = 'wang'

        user.save()

更新多行

        query = Photo.update(path='/09' + Photo.path).where(Photo.created_date < this_week)

        query.execute()

###Delete, 删除对象###

删除一行

        user = User.get(User.id == 2)

        user.delete_instance()

        user.delete_instance(recursive=True)  # 将与user相关的数据（存在外键引用）同时删除

删除多行

        query = User.delete().where(User.email == '')

        query.execute()

##ForeignKey##

我们以上面代码`Photo`对`User`外键引用为例，在Peewee中这种引用关系，可以通过对象进行访问

        user = User.get(User.id == 2)

        for photo in user.Photoes:  # 通过related_name进行访问的，该属性其实是一个select查询，返回user的所有photo

            pass

        for photo in user.Photoes.order_by(Photo.created_date.desc()):  # 该select查询可以添加别的方法

            pass

外键的自引用，比如类别常常含有子类别，即类别表存在自引用关系

        class Category(Model):

            name = CharField()

            # 字符串self标志自引用，初始每个类别的父类别为null，每个类别可以通过cate.children来访问子类别

            parent = ForeignKey('self', null=True, related_name='children')

##Filtering结果集##

上面用于获取一行结果的`User.get(User.id == 2)`就是最为简单的过滤形式，此外你还可以在`where()`中使用各种过滤方法，下面就介绍一些常用和特别的过滤方法

        User.select().where(User.username % '%man%')  # SQL中的LIKE子句(%, **)

        User.select().where(User.username % '%man%', User.email == '')  # and

        User.select().where((User.username % '%man%') | (User.email == ''))  # or

        Photo.select().where(Photo.created_date < this_week)  # comparise(==, <, >, <=, >=, !=, 

        users = User.select().where(User.username % '%man%')

        Photo.select().where(Photo.user << users)  # item in set

        User.select().where(User.password >> None)  # x is None

        Employee.select().where(Employee.salary.between(3000, 5000))  # query by field between

##Sorting结果集##

        User.select().order_by(User.username)

        User.select().order_by(User.username.desc())  # 注意，desc排序是在相应的Model.field上调用函数desc()

        Photo.select().join(User).order_by(User.username, Photo.created_date.desc())  # 正如在SQL语句中一样你可以添加多个sorting条件

##结果集以tuple或dict返回##

        query = User.select()

        users = query.execute()  # 通常情况是以Model实例的形式返回结果集的，users[0].username

        users = query.tuples()  # 以tuple形式返回结果集，users[0][0] is username

        users = query.dicts()  # 以tuple形式返回结果集，users[0]['username']

##SQL function##

peewee提供了SQL中的各种实用函数，这里仅仅列举很少的一部分，具体参看文档

        fn.Count(User.id).alias('count')

        fn.Lower(fn.Substr(User.username, 1, 1))

        fn.Random(), fn.Rand()

        fn.Avg(), fn.Max(), fn.Min()

##Random结果集##

如果你想要在首页上随机的展示一些东西，这个随机挑选结果集的方法就很有用了

        # PostgreSQL And SQLite

        photoes = Photo.select().order_by(fn.Random()).limit(50)  # random pick 50 photoes

        # MySQL

        photoes = Photo.select().order_by(fn.Rand()).limit(50)

##Paginate结果集##

我们知道原生的SQL提供的limit子句，可以对查询结果集提取片段，这里所谓分页只是经过简单计算后对limit的调用，毕竟很多程序需要按页来提取结果

        Photo.select().paginate（3, 20)  # (page_number, items_per_page), page_number start from 1

##Count, Scalar##

对结果集行数进行统计用count()，若结果集仅含一行且是数字值，使用scalar()提取该行数据

        Photo.select().count()

        Photo.select(fn.Count(fn.Distinct(Photo.path))).scalar()  # return 30

        Employee.select(fn.Min(Employee.salary), fn.Max(Employee.salary)).scalar(as_tuple=True)  # return (200, 300)

##Iterate large results##

若按照常规的方式迭代大型结果集的话对内存的消耗将十分厉害，为此peewee专门提供了优化的迭代方式

        for p in Photo.select().execute().iterator():

            pass

        for p in Photo.select().native().execute().iterator():

            pass

##Group by##

对数据进行分组处理是很常见的应用，比如将用户分组后统计每个用户发布的消息数目，为此peewee提供了分组的快捷方式annotate()，以及常规的group_by()方法

        User.select().annotate(Photo)  # is equivalent to the following

        User.select(User, fn.Count(Photo.id).alias('count')).join(Photo).group_by(User)

        User.select().join(Photo, JOIN_LEFT_OUTER).annotate(Photo)  # results include the user(have no photo)

        User.select().annotate(Photo, fn.Max(Photo.created_date).alias('latest'))

        Tag.select().join(PhotoTag).join(Photo).group_by(Tag).having(fn.Count(Photo.id) > 5)

        Tag.select(Tag, fn.Count(Photo.id).alias('count')).join(PhotoTag).join(Photo).group_by(Tag).having(fn.Count(Photo.id) > 5)

##Alias##

在引用别名时要使用peewee提供的SQL()函数

        User.select(User, fn.Count(Photo.id).alias('ct')).join(Photo).group_by(User).order_by(SQL('ct'))

##transaction, 事务##

with管理事务

        with db.transaction():

            user.delete_instance(recursive=True)  # 如果有异常发生，自动回滚

使用decorator

        @db.commit_on_success

        def delete_user(user):

            user.delete_instance(recursive=True)

关闭自动提交功能

        try:

            db.set_autocommit(False)  # 创建数据库默认是自动提交的，就是说每次SQL都直接提交，关闭后在需要显式提交

            user.delete_instance(recursive=True)

        except Exception as e:

            db.rollback()

            raise e

        else:

            try:

                db.commit()

            except Exception as e:

                db.rollback()

                raise e

        finally:

            db.set_autocommit(True)

##自定义主键##

默认peewee为每个model提供一个整数值的主键，但你也可以自己定义主键

        import uuid

        import peewee

        class Test(Model):

            id = CharField(primary_key=True)  # 通过参数primary_key=True指定主键

        t = Test.create(id=str(uuid.uuid4()))

为多对多中间表使用复合键为主键

        from peewee import *

        class PhotoTag(Model):

            photo = ForeignKey(Photo)

            tag = ForeignKey(Tag)

            class Meta:

                primary_key = CompositeKey('photo', 'tag')
