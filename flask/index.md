## 应用结构

### 单模块应用

单模块应用适合小型应用程序的结构，应用的所有逻辑编写在一个 Python 模块（module）中。

#### 目录结构

示例目录结构如下：

```
/demoapp
	demoapp.py
	/static
	/templates
```

* 目录 `static` 用于存放 CSS, Javascript, 图片等在应用程序中使用到的静态资源，利用 Flask 提供的函数 `url_for` 可以十分方便的将资源映射到 URL。
* 目录 `templates` 用于存放 HTML 模板文件，可以利用 Flask 提供的函数 `render_template()` 来填充模板文件构造 HTTP 响应。
* 文件 `demoapp.py` 模块包含了应用的全部逻辑。

#### 运行应用

要运行该应用只需要在命令行中运行命令：

```
export FLASK_APP=/path/to/demoapp.py
flask run
```

其中第一步设置环境变量 `FLASK_APP` 为模块 `demoapp.py` 的路径（在 Windows 下用 `set` 来代替 `export`），第二步让 Flask 运行该应用，第二步也可以通过 `python -m flask run` 替代。如果想要开启应用的调试模式，可以在运行应用之前，设置环境变量 `export FLASK_DEBUG=true` ，不过要注意千万不要在生产环境中开启调试模式。

默认开启应用时，仅监听来自本机的请求，为了让网络中的其它计算机可以访问该应用，需要关闭应用的调试模式（设置环境变量 `FLASK_DEBUG=false`），然后运行命令 `flask run --host=0.0.0.0` 以允许应用接受来自网络中任意计算机的访问。

这两步执行完成后，就会开启一个 Flask 内置的服务器来运行该应用，不过这种方法仅仅适用于开发测试阶段，在生产阶段应参考 Flask 官方[部署文档](http://flask.pocoo.org/docs/0.12/deploying/#deployment)来部署应用。

### 多模块应用

多模块应用被组织在一个 Python 包（package）中，适用于大型应用，可以将应用的逻辑划分到多个模块中来编写，便于开发和维护。

#### 目录结构

示例目录结构如下：

```
/demoapp
	setup.py
	MANIFEST.in
	/demoapp
		__init__.py
		views.py
		/static
		/templates
```

* 文件 `setup.py` 和 `MANIFEST.in` 用来将应用打包，主要声明了依赖的包以及要打包的资源，使得可以将应用作为包来安装。
* 文件 `demoapp/__init__.py` 用来将应用声明为一个 Python 包，包名为 `demoapp` ，并且必须在该脚本中创建应用程序对象（Flask application object ，也即 `flask.Flask` 类的实例），以使得其它模块得以导入该应用程序对象。
* 文件 `views.py` 用来定义应用的所有视图函数（view function），即应用的请求处理函数。

`setup.py` 示例代码：

```python
from setuptools import setup

setup(
    name='demoapp',
    packages=['demoapp'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
```

`MANIFEST.in` 示例内容：

```
graft demoapp/templates
graft demoapp/static
```

`__init__.py` 示例代码：

```python
from flask import Flask
app = Flask(__name__)

# 必须在创建应用程序对象之后再导入视图函数，因为视图函数依赖到应用程序对象
import demoapp.views
```

`views.py` 示例代码：

```python
from demoapp import app
# 注意：views.py 和 __init__.py 构成了循环导入，
# 不过由于 __init__.py 中并不调用 views，所以问题不大

@app.route('/')
def index():
    return 'Hello World!'
```

#### 运行

首先需要将应用安装为 Python 包，推荐利用 [virtualenv](https://virtualenv.pypa.io/en/stable/) 这样的虚拟环境工具来将应用安装到虚拟环境中，在项目根目录下（即 `setup.py` 所在目录），运行以下命令将应用安装为包：

```
pip install --editable .
```

其中 `--editable` 表示应用源码发生变化后，不需要再次重新将应用安装为包，安装好后包名为 `demoapp`。

接下来运行以下命令：

```
export FLASK_APP=demoapp
export FLASK_DEBUG=true
flask run
```

其中环境变量 `FLASK_APP` 被设置为应用的包名，这一点是跟单模块应用不同的。

## 应用 Blueprint



## 应用配置

应用程序总需要配置各种参数，比如配置是否开启调试模式、配置会话的 secret key 等，对于小型项目将配置项硬编码在应用中还可接受，但对于大型项目硬编码配置项的方法就不可取了，大型项目往往需要将配置项写在单独的文件中，并根据应用运行在开发环境还是生产环境，会为其配置不同的参数。

### 配置对象

Flask 为应用程序对象关联了一个属性 `config` ，它是字典对象的子类，储存了应用已经加载的配置参数。开发者可以在应用中通过该属性来访问、添加以及更新配置项，对于小型项目可以直接将配置硬编码在应用中，示例如下：

```
from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True
app.config.update(
	SECERT_KEY='38fx93fd0',
	SESSION_COOKIE_NAME='session_id'
)
```

配置项有的是 Flask 内部使用的，有的是扩展使用的，有的是应用开发者自己使用的，下面就 Flask 内部常用的配置项作简单的介绍：

* `DEBUG` 调试模式的开关
* `TESTING` 测试模式的开关
* `SECRET_KEY` 用于会话数据加密解密的秘钥，更多内容参见[会话功能的介绍](http://flask.pocoo.org/docs/0.12/quickstart/#sessions)
* `SESSION_COOKIE_NAME` 用于设置会话的 cookie 名，Flask 会话是基于客户端 cookie 的，因此需要用 cookie 来存放会话数据。题外话，会话还可以通过 URL 重写或者隐藏表单项等技术来实现，不论使用哪种技术都要保证会话标识能够在客户端和服务端之间安全的传输。更多参见[维基百科](https://en.wikipedia.org/wiki/Session_(computer_science))
* `USE_X_SENDFILE` X-Sendfile 开关，web 应用程序用来执行逻辑操作，当要返回静态资源给用户时，显然直接交给 HTTP server 会更合适，Nginx, Apache 以及 Lighttpd 都支持该功能，要想在 Flask 应用中使用该功能，不仅要开启这个开关，还要配置 HTTP server。
* `LOGGER_NAME` 和 `LOGGER_HANDLER_POLICY` 均用来配置应用日志
* `SERVER_NAME` 应用所在域名和端口号，格式为：`example.com:5000`
* `JSON_AS_ASCII` 控制 Flask 提供的 JSON 序列化函数 jsonify 是编码为 ascii （`True`）还是 utf8 （`False`）
* `JSON_SORT_KEYS` 控制 Flask 提供的 JSON 序列化函数 jsonify 在编码时按照 JSON 对象的键顺序来编码，这样可以确保编码后字符串生成的 hash 摘要是一致的
* `JSONIFY_MIMETYPE` 设置 jsonify 响应的 MIME 类型
* `JSONIFY_PRETTYPRINT_REGULAR` 控制 jsonify 返回的响应内容是否缩进排版，不过对于 Ajax 请求（请求头中含有 `X-Requested-With`）响应内容总是不会缩进排版的

### 加载配置的接口

上面介绍的直接将配置项硬编码在应用中仅适用于小型项目，对于稍大一点的项目就不适合这么做了，更好的作法是将配置内容独立写在一个配置文件，然后在应用中加载它。

加载配置内容示例：

```python
app.config.from_pyfile('demoapp.cfg')
app.config.from_object('demoapp.default_settings')
app.config.from_envvar('FLASK_SETTINGS', silent=True)
```

其中第一行表示从配置文件 `demoapp.cfg` 中加载配置项到应用；第二行表示将模块（或包） `demoapp` 中的 `default_settings` 类（或模块）的内容加载到应用；第三行表示从环境变量 `FLASK_SETTINGS` 获取配置文件的路径，并将其内容加载到应用，参数 `silent=True` 表示当找不到该环境变量时，Flask 不会报错；这里连续使用多种方式来加载配置内容，后面加载的配置项会覆盖前面加载的配置项。

除了上面这几种接口，配置对象还提供了 `from_json()` 和 `from_mapping()` 来分别从 JSON 文件以及字典对象中加载配置内容，更多介绍参见[官网](http://flask.pocoo.org/docs/0.12/api/#flask.Config)。

还有一点要注意应用程序的配置对象 `app.config` 有一个属性 `root_path` 表示加载配置文件时的相对根路径，该路径如果没有显式指定的话，默认等于 `app.root_path` 。

### 配置文件内容

从以上介绍可以看出 Flask 允许开发者从 Python 配置文件、JSON 配置文件、环境变量以及 Python 字典和类中加载配置内容。不过这里主要介绍通过 `from_object()` , `from_pyfile()` 以及  `from_envvar()`）加载的配置内容是怎样的。

* `from_object()` 接受字符串和对象两种参数，字符串会被映射为相应的对象，而对象一般是模块或者类对象。通过该接口可以将模块和类对象的大写属性导入应用配置中，不过要注意该接口无法导入字典对象。

  示例代码如下：

  ```python
  DEBUG = True

  app.from_object(__name__) # 导入当前模块中的大写属性 DEBUG = True
  app.from_object('demoapp.default_settings') # 导入模块 demoapp.default_settings 中的大写属性
  app.from_object('demoapp.config.ProductionConfig') # 导入模块 demoapp.config 中 ProductionConfig 类的大写属性
  ```

  其中 `demoapp.config` 模块定义如下：

  ```python
  class Config(object):
      DEBUG = False
      TESTING = False
      DATABASE_URI = 'sqlite://:memory:'

  class ProductionConfig(Config):
      DATABASE_URI = 'mysql://user@localhost/foo'

  class DevelopmentConfig(Config):
      DEBUG = True

  class TestingConfig(Config):
      TESTING = True
  ```


* `from_pyfile()` 从 Python 配置文件加载配置内容，Python 配置文件其实就是一个遵从 Python 语法的普通 Python 文件，只不过文件中只有大写的变量名会被识别为配置项。配置文件的后缀名可以任意取，一般为 `.py` , `.cfg` ，只要保证配置文件遵从 Python 语法即可。示例如下：

  ```python
  DEBUG = False
  SECRET_KEY = '?\xbf,\xb4\x8d\xa3"<\x9c\xb0@\x0f5\xab,w\xee\x8d$0\x13\x8b83'
  ```

*  `from_envvar(envvar)` 其实只是 `from_pyfile(os.environ[envvar])` 的简写而已。

配置项的名称建议采用前缀编写法，也即同一类型的配置项具有相同的名称前缀，这样不仅仅可以起到自注释的作用，还可以利用 `app.config` 提供的方法 `get_namespace()` 来查询相同前缀的配置项。

### 生产和开发配置

一般应用在生产和开发阶段会使用不同的配置参数，比如数据库连接参数在这两个阶段通常就是不同的。为此需要某种机制来根据所处阶段为应用提供不同的配置参数。

通常使用的策略是，应用总是会去加载一个默认配置文件（将其添加到代码的版本控制系统中，使得生产环境下依然可以加载它），同时应用会根据当前是开发还是生产阶段，去加载特定阶段要使用的配置文件。为了让应用平滑的从开发阶段迁移到生产阶段，应用内部需要一致的方式来访问特定阶段的配置文件，环境变量可以很好的解决这个问题，应用中加载配置的示例如下：

```python
app = Flask(__name__)
app.config.from_object('demoapp.default_settings')
app.config.from_envvar('FLASK_SETTINGS')
```

然后需要在开发和生产阶段分别设置操作系统环境变量 `FLASK_SETTINGS` 指向特定的配置文件，使得开发和生产阶段使用不同的配置文件，而应用不需要有任何改动。

上面仅仅是提供了一个思路，在实践中不一定必须将配置文件的位置存放在操作系统的环境变量中，也可以设置一个环境变量用来标识应用所处阶段，比如：`FLASK_PROJECT_MODE` 设置为 `production` 或 `development` ，分别用来表示应用在生产或开发阶段，然后在应用内部根据该环境变量来加载不同的配置参数，示例如下：

```python
import os
from flask import Flask

app = Flask(__name__)
app.config.from_object('demoapp.default_settings')

if os.enviorn.get('FLASK_PROJECT_MODE', '') == 'production':
	app.config.from_object('demoapp.production_settings')
else:
	app.config.from_object('demoapp.development_settings')
```

这种方法要求将生产阶段和开发阶段的配置项都编写在应用中（并添加到版本控制系统），要在生成阶段变动应用的配置就必须要更改应用代码，因此不是很灵活。

### 配置应用根路径

web 应用程序使用资源文件时，需要知道这些文件在操作系统中的位置，一般都是通过相对于应用程序的根路径来定位其它资源文件的。这样的好处在于避免了对资源文件绝对路径的硬编码，使应用更具可移植性。

操作系统中的进程都有当前工作目录（current working directory）的信息，比如在 Python 中可以通过 `os.getcwd()` 来获得当前脚本的工作目录，还可以通过 `os.chdir()` 来改变当前的工作目录。如果一个 web 应用程序运行在一个进程下，应用程序的根路径就可以通过进程的工作目录来得到，可往往一个进程下面会有若干应用在运行，这时应用程序的根路径不再能够根据进程的工作目录来确定，为此 Flask 提供了机制在应用内部来引用当前应用程序的根路径。





