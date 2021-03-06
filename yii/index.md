---
title: Yii手册
author: Xiao Wenbin
date: 2016/10/09
categories: web, php, yii
---

## 服务器配置
1. Yii自带服务器

   Yii自带服务器是一个简单的web服务器，不需要进行任何配置即可使用。yii项目根目录下运行：`php yii serve` ，即可在本地`http://localhost:8080`访问yii项目，或者可以指定运行端口`php yii serve --port=8888`

2. Apache服务器

   假设Yii项目可访问根目录为`basic/web`，相应apache服务器配置内容（配置内容要写入虚拟主机配置文件）如下：

        DocumentRoot "path/to/basic/web"
        <Directory "path/to/basic/web">
            # 开启 mod_rewrite 用于美化 URL 功能的支持（对应 pretty URL 选项）
            RewriteEngine on
            # 如果请求的是真实存在的文件或目录，直接访问
            RewriteCond %{REQUEST_FILENAME} !-f
            RewriteCond %{REQUEST_FILENAME} !-d
            # 如果请求的不是真实文件或目录，分发请求至 index.php
            RewriteRule . index.php
       
            # ...其它设置...
        </Directory>

3. Nginx服务器（需要额外安装fcgi）
   要在Nginx下运行PHP脚本需要安装`fcgi`，此外需要将以下配置内容写入到Nginx配置文件中：

        server {
            charset utf-8;
            client_max_body_size 128M;
       
            listen 80; ## listen for ipv4
            #listen [::]:80 default_server ipv6only=on; ## listen for ipv6
       
            server_name mysite.local;
            root        /path/to/basic/web;
            index       index.php;
       
            access_log  /path/to/basic/log/access.log;
            error_log   /path/to/basic/log/error.log;
       
            location / {
                # Redirect everything that isn't a real file to index.php
                try_files $uri $uri/ /index.php$is_args$args;
            }
       
            # uncomment to avoid processing of calls to non-existing static files by Yii
            #location ~ \.(js|css|png|jpg|gif|swf|ico|pdf|mov|fla|zip|rar)$ {
            #    try_files $uri =404;
            #}
            #error_page 404 /404.html;
       
            location ~ \.php$ {
                include fastcgi_params;
                fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
                #fastcgi_param HTTPS on;当运行一个 HTTPS 服务器时，配置该项后yii才能知道是https
                fastcgi_pass   127.0.0.1:9000;
                #fastcgi_pass unix:/var/run/php5-fpm.sock;
                try_files $uri =404;
            }
       
            location ~ /\.(ht|svn|git) {
                deny all;
            }
        }

同时需要对PHP进行配置，将以下内容写入`php.ini`文件：

	cgi.fix_pathinfo=0 # 能避免掉很多不必要的 stat() 系统调用
## 应用目录结构

    basic/                  应用根目录
        composer.json       Composer 配置文件, 描述包信息，主要是应用程序依赖第三方包的描述信息
        config/             包含应用配置及其它配置
            console.php     控制台应用配置信息
            web.php         Web 应用配置信息
        commands/           包含控制台命令类
        controllers/        包含控制器类
        models/             包含模型类
        runtime/            包含 Yii 在运行时生成的文件，例如日志和缓存文件
        vendor/             包含已经安装的 Composer 包，包括 Yii 框架自身
        views/              包含视图文件
        web/                Web 应用根目录，包含 Web 入口文件，服务器将此处配置为web唯一入口
            assets/         包含 Yii 发布的资源文件（javascript 和 css）
            index.php       应用入口文件
        yii                 Yii 控制台命令执行脚本，用来执行应用程序的后台任务，需要有执行权限，通过./yii <route> [arguments] [options]运行

## 应用实例的生命周期

1. 入口脚本加载应用实例的配置数组
2. 入口脚本创建一个应用实例
   1. 调用 `yii\base\Application::preInit()` 配置几个高级别应用主体属性， 比如`yii\base\Application::basePath`
   2. 注册 `yii\base\Application::errorHandler` 错误处理方法
   3. 配置应用实例
   4. 调用 `yii\base\Application::init()` 初始化， 该函数会调用 `yii\base\Application::bootstrap()` 运行引导启动组件
3. 入口脚本调用 `yii\base\Application::run()` 运行应用实例
4. 触发 `yii\base\Application::EVENT_BEFORE_REQUEST` 事件
5. 处理请求：解析请求、路由以及相关参数；创建路由指定的模块（module）、控制器（controller）和操作（action）对应的类，并运行操作（action）
6. 触发 `yii\base\Application::EVENT_AFTER_REQUEST` 事件
7. 发送响应到用户
8. 入口脚本接收应用实例传来的退出状态并完成请求的处理

## 请求的生命周期

1. 用户向入口脚本 `web/index.php` 发起请求
2. 入口脚本加载应用配置并创建一个应用实例(Application)去处理请求（需要协调各个components来完成任务）。应用实例在请求周期内全局可访问（`\Yii::$app`）
3. 应用通过请求组件(request component)来解析请求的路由信息以及相关请求参数
4. 应用创建一个跟路由对应的控制器实例(controler)去处理请求
5. 控制器实例创建一个操作实例(action)并针对操作执行过滤器(filter)。如果任何一个过滤器返回失败，则操作退出；如果所有过滤器都通过，操作将被执行
6. 操作加载一个数据模型(model)，数据模型从数据库中加载数据
7. 操作渲染一个视图(view: widget, asset bundle)，并把数据模型提供给它
8. 渲染结果返回给响应组件(response componet)
9. 响应组件发送渲染(render view)结果给用户


Yii的MVC
视图
使用 布局 来展示公共代码（如，页面头部、尾部）；
将复杂的视图分成几个小视图， 可使用上面描述的渲染方法将这些小视图渲染并组装成大视图；
创建并使用 小部件 作为视图的数据块；
创建并使用助手类在视图中转换和格式化数据
模板内容，用来展示给用户的
通过yii\web\View应用组件来管理， 该组件主要提供通用方法帮助视图构造和渲染
在视图中，可访问 $this 指向 yii\web\View 来管理和渲染这个视图文件
当创建生成HTML页面的视图时， 在显示之前将用户输入数据进行转码和过滤非常重要， 否则，你的应用可能会被跨站脚本 攻击，
要显示纯文本，先调用 yii\helpers\Html::encode() 进行转码
要显示HTML内容，先调用 yii\helpers\HtmlPurifier 过滤内容
对于 小部件 渲染的视图文件默认放在 WidgetPath/views 目录， 其中 WidgetPath 代表小部件类文件所在的目录；
对于其他对象渲染的视图文件，建议遵循和小部件相似的规则。
视图渲染
在 控制器 中，可调用以下控制器方法来渲染视图：

    yii\base\Controller::render(): 渲染一个 视图名 并使用一个 布局 返回到渲染结果。
    yii\base\Controller::renderPartial(): 渲染一个 视图名 并且不使用布局。
    yii\web\Controller::renderAjax(): 渲染一个 视图名 并且不使用布局， 并注入所有注册的JS/CSS脚本和文件，通常使用在响应AJAX网页请求的情况下。
    yii\base\Controller::renderFile(): 渲染一个视图文件目录或 别名下的视图文件。
    yii\base\Controller::renderContent(): renders a static string by embedding it into the currently applicable layout. This method is available since version 2.0.1.
在 小部件 中，可调用以下小部件方法来渲染视图：

    yii\base\Widget::render(): 渲染一个 视图名.
    yii\base\Widget::renderFile(): 渲染一个视图文件目录或 别名下的视图文件。

在视图中渲染另一个视图，可以调用yii\base\View视图组件提供的以下方法：

    yii\base\View::render(): 渲染一个 视图名.
    yii\web\View::renderAjax(): 渲染一个 视图名 并注入所有注册的JS/CSS脚本和文件，通常使用在响应AJAX网页请求的情况下。
    yii\base\View::renderFile(): 渲染一个视图文件目录或 别名下的视图文件。
在任何地方都可以通过表达式 Yii::$app->view 访问 yii\base\View 应用组件， 调用它的如前所述的方法渲染视图
视图间共享数据
yii\base\View视图组件提供yii\base\View::params参数 属性来让不同视图共享数据。
布局
布局是一种特殊的视图，代表多个视图的公共部分， 例如，大多数Web应用共享相同的页头和页尾， 在每个视图中重复相同的页头和页尾，更好的方式是将这些公共放到一个布局中， 渲染内容视图后在合适的地方嵌入到布局中。
在布局中可访问两个预定义变量：$this 和 $content， 前者对应和普通视图类似的yii\base\View 视图组件 后者包含调用yii\base\Controller::render()方法渲染内容视图的结果。
可配置yii\base\Application::layout 或 yii\base\Controller::layout 使用其他布局文件， 前者管理所有控制器的布局，后者覆盖前者来控制单个控制器布局，对于模块中的控制器，可配置模块的 yii\base\Module::layout 属性指定布局文件应用到模块的所有控制器





模型
模型是代表业务数据、规则和逻辑的中心地方，通常在很多地方重用， 在一个设计良好的应用中， 模型通常比控制器代码多。属性来表示业务数据；验证规则确保数据的有效性；自定义方法实现业务逻辑；请求数据以及环境数据应该由控制器传入模型，模型不直接去访问；单模型避免太多场景；定义可被共享的模型基类集合，这些基类中应该含有最小的规则集合，然后在具体的应用实例或者模块中继承它们
基类yii\base\Model
模型有如下特性：
属性
所有非静态public成员都是属性
通过 属性 来代表业务数据，每个属性像是模型的公有可访问属性， yii\base\Model::attributes() 指定模型所拥有的属性
属性支持对象属性访问方法，支持关联数组访问方法，支持数组迭代
属性标签，可以通过$model->getAttributeLabel('address');访问，通过yii\base\Model::generateAttributeLabel()方法自动从属性名生成，可以重写该方法，或者定义重写方法 yii\base\Model::attributeLabels() 方法明确指定属性标签，返回一个以属性名为key，标签为值的数组。此外属性标签可以通过\Yii::t来进行多语言支持
场景
同一模型可能在不同场景中会有不同的业务规则和逻辑，场景特性主要应用在验证规则和块赋值
yii\base\Model::scenario 指定当前模型的场景，默认为default
指定场景
$model->scenario = 'login'
or
$model = new User(['scenario' => 'login'])
模型对应的可选场景，在定义模型时的验证规则中给出，或者通过重写scenarios()方法来自定义可选场景
scenarios() 方法默认实现会返回所有yii\base\Model::rules()方法申明的验证规则中的场景
	public function scenarios()
	{
	    $scenarios = parent::scenarios(); // 默认场景
	    // 新添加场景
	    $scenarios[self::SCENARIO_LOGIN] = ['username', 'password']; // 当前场景下的活动属性
	    $scenarios[self::SCENARIO_REGISTER] = ['username', 'email', 'password'];
	    return $scenarios;
	}
调用 yii\base\Model::validate() 来验证接收到的数据， 该方法使用yii\base\Model::rules()申明的验证规则来验证每个相关属性， 如果没有找到错误，会返回 true， 否则它会将错误保存在 yii\base\Model::errors 属性中并返回false
重写rules方法为模型的属性指定验证规则
public function rules() {
	return [
		[['username', 'email', 'subject', 'body'], 'required'],
		['email', 'email'],
		[['email', 'password'], 'required', 'on' => 'login'], // 指定该验证规则只在login场景起作用，没有使用on的规则在所有场景下都起作用
		[['title', 'description'], 'safe'], // 不需要进行规则验证的属性
		[['email', 'password', '!username'], 'required', 'on' => 'login'] // username在块赋值时，只验证不赋值
	];
}
块赋值
只有当前场景下的活动属性才会被赋值，其他属性不会被赋值
$model->attributes = \Yii::$app->request->post('ContactForm');
某些情形下对某个属性只想要验证但不想要赋值，在scenarios()或者rules()对应场景那个属性前面添加!，就表示在该场景下不允许块赋值，但要进行规则验证
模型的导出
第一步：导出为数组，yii\base\Model::attributes 属性会返回 所有 yii\base\Model::attributes() 申明的属性的值。此外还有模型的toArray()方法
第二步：数组转换为目标格式，利用各种数据转换器来完成，如yii\web\JsonResponseFormatter
可以定义fields和extraFields方法来决定toAarray返回的字段
// 明确列出每个字段，特别用于你想确保数据表或模型
// 属性改变不会导致你的字段改变(保证后端的API兼容)。
public function fields()
{
    return [
        // 字段名和属性名相同
        'id',
    
        // 字段名为 "email"，对应属性名为 "email_address"
        'email' => 'email_address',
    
        // 字段名为 "name", 值通过PHP代码返回
        'name' => function () {
            return $this->first_name . ' ' . $this->last_name;
        },
    ];
}

// 过滤掉一些字段，特别用于你想
// 继承父类实现并不想用一些敏感字段
public function fields()
{
    $fields = parent::fields();

    // 去掉一些包含敏感信息的字段
    unset($fields['auth_key'], $fields['password_hash'], $fields['password_reset_token']);
    
    return $fields;
}




控制器
在设计良好的应用中，控制器很精练，包含的操作代码简短； 如果你的控制器很复杂，通常意味着需要重构
从应用主体接管控制后会分析请求数据并传送到模型， 传送模型结果到视图， 最后生成输出响应信息
控制器由 操作 组成，它是执行终端用户请求的最基础的单元， 一个控制器可有一个或多个操作
控制器一般是面向资源的。通常情况下，控制器用来处理请求有关的资源类型， 因此控制器ID通常为和资源有关的名词
操作通常是用来执行资源的特定操作，因此， 操作ID通常为动词
控制器Id可包含子目录前缀，例如 admin/article 代表控制器目录下面子目录admin中的ArticleController控制器
两种路由
controllerID/actionID
moduleID/controllerID/actionID
一般操作都是定义在控制器内部以action开头的方法，如果想要重用操作，可以继承yii\base\Action，然后在控制器中重写actions()方法来指定外部的操作类
public function actions()
{
    return [
        // 用类来申明"error" 操作
        'error' => 'yii\web\ErrorAction',
    
        // 用配置数组申明 "view" 操作
        'view' => [
            'class' => 'yii\web\ViewAction',
            'viewPrefix' => '',
        ],
    ];
}
继承yii\base\Action
namespace app\components;

use yii\base\Action;

class HelloWorldAction extends Action
{
    public function run() // 重写run方法
    {
    	// 返回结果就是操作要响应的内容
        return "Hello World";
    }
}
操作接受数组参数
首先操作的函数接口参数要声明为数组类型，url传入参数为?r=sit/index&id[]=123或?r=sit/index&id=123，后者自动转换为数组
控制器中的默认操作是index，如果想要重写的话，在控制器内定义属性$defaultAction = 'actionName';

控制器的生命周期
​	
	在控制器创建和配置后，yii\base\Controller::init() 方法会被调用。
	控制器根据请求操作ID创建一个操作对象:
	如果操作ID没有指定，会使用yii\base\Controller::defaultAction默认操作ID；
	如果在yii\base\Controller::actions()找到操作ID， 会创建一个独立操作；
	如果操作ID对应操作方法，会创建一个内联操作；
	否则会抛出yii\base\InvalidRouteException异常。

控制器按顺序调用应用主体、模块（如果控制器属于模块）、 控制器的 beforeAction() 方法；

    如果任意一个调用返回false，后面未调用的beforeAction()会跳过并且操作执行会被取消； action execution will be cancelled.
    默认情况下每个 beforeAction() 方法会触发一个 beforeAction 事件，在事件中你可以追加事件处理操作；

控制器执行操作:

    请求数据解析和填入到操作参数；

控制器按顺序调用控制器、模块（如果控制器属于模块）、 应用主体的 afterAction() 方法；

    默认情况下每个 afterAction() 方法会触发一个 afterAction 事件，在事件中你可以追加事件处理操作；

应用主体获取操作结果并赋值给响应

入口脚本定义全局内容
	yii定义的全局常量
	YII_DEBUG：标识应用是否运行在调试模式。当在调试模式下， 应用会保留更多日志信息，如果抛出异常，会显示详细的错误调用堆栈。 因此，调试模式主要适合在开发阶段使用，YII_DEBUG 默认值为 false。
	YII_ENV：标识应用运行的环境， 详情请查阅配置章节。 YII_ENV 默认值为 'prod'，表示应用运行在线上产品环境。
	YII_ENABLE_ERROR_HANDLER：标识是否启用 Yii 提供的错误处理， 默认为 true。


应用实例属性
id 用来区分其他应用的唯一标识ID。 主要给程序使用。为了方便协作，最好使用数字作为应用主体ID， 但不强制要求为数字。
basePath  指定该应用的根目录。 根目录包含应用系统所有受保护的源代码。可以使用路径或 路径别名 来在配置。系统预定义 @app 代表这个路径。 派生路径可以通过这个别名组成（如@app/runtime代表runtime的路径）
aliases 指定一个key/value的数组， 数组的key为别名名称，值为对应的路径。使用这个属性来定义别名， 代替 Yii::setAlias() 方法来设置。
bootstrap 一个数组，指定启动阶段需要运行的component和module，在启动阶段，每个组件都会实例化。 如果组件类实现接口 yii\base\BootstrapInterface, 也会调用 yii\base\BootstrapInterface::bootstrap() 方法，启动太多的组件会降低系统性能， 因为每次请求都需要重新运行启动组件，因此谨慎配置启动组件。引导工作必须在处理每一次请求之前都进行一遍， 因此让该过程尽可能轻量化就异常重要，请尽可能地优化这一步骤。
请尽量不要注册太多引导组件。只有他需要在 HTTP 请求处理的全部生命周期中都作用时才需要使用它。 举一个用到它的范例：一个模块需要注册额外的 URL 解析规则，就应该把它列在应用的 bootstrap 属性之中， 这样该 URL 解析规则才能在解析请求之前生效。
catchAll 在web app中用来指定一个方法捕获所有请求，通常在维护模式下使用，同一个方法处理所有用户请求。
components 注册多个在其他地方使用的应用组件，每一个应用组件指定一个key-value对的数组，key代表组件ID， value代表组件类名或 配置。可以通过表达式 \Yii::$app->ComponentID 全局访问
controllerMap yii默认的控制器映射规则，可以通过配置该项来改变，通常的应用情形是外部不同的路由想要得到相同的处理，即重用控制器
controllerNamespace 控制器默认的名称空间是app\controllers，可以通过配置该项来改变
language 该属性影响各种 国际化 ， 包括信息翻译、日期格式、数字格式等。 例如 yii\jui\DatePicker 小部件会 根据该属性展示对应语言的日历以及日期格式。
modules 该属性使用数组包含多个模块类 配置， 数组的键为模块ID
name 该属性指定你可能想展示给终端用户的应用名称， 不同于需要唯一性的 yii\base\Application::id 属性， 该属性可以不唯一，该属性用于显示应用的用途
params 该属性为一个数组，指定可以全局访问的参数， 代替程序中硬编码的数字和字符， 应用中的参数定义到一个单独的文件并随时可以访问是一个好习惯
sourceLanguage 该属性指定应用代码的语言
timeZone 该属性提供一种方式修改PHP运行环境中的默认时区，配置该属性本质上就是调用PHP函数 date_default_timezone_set()
version 该属性指定应用的版本，默认为'1.0'
charset 指定应用使用的字符集，默认值为 'UTF-8'
defaultRoute 指定的默认控制器；当请求没有指定 路由，该属性值作为路由使用，web默认路由是site，console默认路由是help， 路由规则可能包含模块ID，控制器ID，动作ID
extensions 指定应用安装和使用的 扩展， 默认使用@vendor/yiisoft/extensions.php文件返回的数组。 当你使用 Composer 安装扩展，extensions.php 会被自动生成和维护更新
layoutPath 指定查找布局文件的路径， 默认值为 @app/views/layouts
runtimePath 指定临时文件如日志文件、缓存文件等保存路径， 默认值为 @app/runtime
viewPath 默认@app/views
vendorPath 默认@app/vendor
:enableCoreCommands 控制台应用支持， 用来指定是否启用Yii中的核心命令
应用在处理请求过程中会触发事件， 可以在配置文件配置事件处理代码，如下所示：
[
    'on beforeRequest' => function ($event) {
        // ... 应用实例触发
    },
    
    'on afterRequest' => function ($event) {
        // ... 应用实例触发
    },
    
    'on beforeAction' => function ($event) {
    	// 应用实例，模块，控制器均会触发
        if (some condition) {
            $event->isValid = false; // false 停止运行后续动作
        } else {
        }
    },
    
    'on afterAction' => function ($event) {
    	// // 控制器，模块，应用实例均会触发
        if (some condition) {
            // 修改 $event->result
        } else {
        }
    },
]


应用组件

应用实例需要若干应用组件共同协同来处理请求（组件可以看成一个机器的零件，它们构成了机器的骨架），应用组件用来提供各种实用的功能，可以全局通过\Yii::$app->componentID来访问（组件已经实例化好了），例如：可以使用 \Yii::$app->db 来获取到已注册到应用的 yii\db\Connection， 使用 \Yii::$app->cache 来获取到已注册到应用的 yii\caching\Cache，可以使用\Yii::$app->urlManager来获取到已注册到应用解析请求路由到控制器的

组件是不使用不会实例化，首次使用实例化，再次使用无需实例化。第一次使用以上表达式时候会创建应用组件实例， 后续再访问会返回此实例，无需再次创建

请谨慎注册太多应用组件， 应用组件就像全局变量， 使用太多可能加大测试和维护的难度

请求前必实例化组件，有时你想在每个请求处理过程都实例化某个组件即便它不会被访问， 可以将该组件ID加入到应用主体的 yii\base\Application::bootstrap 属性中

预定义组件
request 收集用户请求参数并解析路由
db 可以执行数据库操作的数据库连接
assetManager
connection
formatter
errorHandler
dispatcher
mailer
response
session
urlManager
user
view


模块
模块在大型项目中常备使用，这些项目的特性可分组， 每个组包含一些强相关的特性， 每个特性组可以做成一个模块由特定的开发人员和开发组来开发和维护。

在特性组上，使用模块也是重用代码的好方式，一些常用特性， 如用户管理，评论管理，可以开发成模块， 这样在相关项目中非常容易被重用。
含有MVC的独立单元，可重用，注册到应用实例中，不能够单独部署，必须隶属于某个应用主体， 当一个模块被访问，和 应用主体实例 类似会创建该模块类唯一实例（即模块类的实例），模块实例用来帮模块内代码共享数据和组件
模块的目录结构
forum/
    Module.php                   模块类文件，继承自yii\base\Module
    controllers/                 包含控制器类文件
        DefaultController.php    default 控制器类文件
    models/                      包含模型类文件
    views/                       包含控制器视图文件和布局文件
        layouts/                 包含布局文件
        default/                 包含DefaultController控制器视图文件
            index.php            index视图文件
模块的初始化
public function init()
{
    parent::init();
    // 从config.php加载配置来初始化模块
    \Yii::configure($this, require(__DIR__ . '/config.php'));
}
config.php
<?php
return [
    'components' => [
        // list of component configurations
    ],
    'params' => [
        // list of parameters
    ],
];

模块控制器的名称空间
namespace app\modules\forum\controllers;
可配置yii\base\Module::controllerNamespace属性来自定义控制器类的命名空间

模块视图的名称空间
namespace app\modules\forum\views;
布局文件默认放在 views/layouts 目录下， 可配置yii\base\Module::layout属性指定布局名， 如果没有配置 layout 属性名，默认会使用应用的布局。

应用实例中使用模块
应用实例配置
[
    'modules' => [
        'forum' => [
            'class' => 'app\modules\forum\Module',
            // ... 模块其他配置 ...
        ],
    ],
]

模块defaultRoute，在没有指定控制器时，应用该配置的控制器

在模块中，可能经常需要获取模块类的实例来访问模块ID，模块参数，模块组件等， 可以使用如下语句来获取：

$module = MyModuleClass::getInstance();
也可以使用如下方式访问模块实例:

// 获取ID为 "forum" 的模块
$module = \Yii::$app->getModule('forum');

// 获取处理当前请求控制器所属的模块
$module = \Yii::$app->controller->module;

模块每个请求均启动，在应用实例中配置bootstrap

模块嵌套

模块可无限级嵌套，也就是说，模块可以包含另一个包含模块的模块， 我们称前者为父模块，后者为子模块， 子模块必须在父模块的yii\base\Module::modules属性中申明
	public function init()
	{
	    parent::init();
	
	    $this->modules = [
	        'admin' => [
	            // 此处应考虑使用一个更短的命名空间
	            'class' => 'app\modules\forum\modules\admin\Module',
	        ],
	    ];
	}


过滤器

应用实例,模块,控制器均可以定义过滤器,用来在请求处理之前和之后进行某些额外的处理

过滤器是 控制器 动作 执行之前或之后执行的对象。 例如访问控制过滤器可在动作执行之前来控制特殊终端用户是否有权限执行动作， 内容压缩过滤器可在动作执行之后发给终端用户之前压缩响应内容。

可以在控制器类中覆盖它的 yii\base\Controller::behaviors() 方法来申明过滤器

控制器类的过滤器默认应用到该类的 所有 动作， 你可以配置yii\base\ActionFilter::only属性明确指定控制器应用到哪些动作
,也可以配置yii\base\ActionFilter::except属性使一些动作不执行过滤器

除了控制器外，可在 模块或应用主体 中申明过滤器。 申明之后，过滤器会应用到所属该模块或应用主体的 所有 控制器动作， 除非像上述一样配置过滤器的 yii\base\ActionFilter::only 和 yii\base\ActionFilter::except 属性。

预过滤器执行顺序为应用实例,模块,控制器的过滤器,后过滤器则反之

自定义过滤器
继承 yii\base\ActionFilter 类并覆盖 yii\base\ActionFilter::beforeAction() 和/或 yii\base\ActionFilter::afterAction() 方法来创建动作的过滤器，前者在动作执行之前执行，后者在动作执行之后执行。beforeAction() 返回值决定动作是否应该执行， 如果为false，之后的过滤器和动作不会继续执行

yii自带过滤器
Yii提供了一组常用过滤器，在yii\filters命名空间下
yii\filters\AccessControl
基于规则来决定允许还是拒绝请求动作的执行
yii\filters\auth\HttpBasicAuth
使用基于HTTP基础认证方法的令牌,通常在实现RESTful API中使用
yii\filters\ContentNegotiator 
响应内容格式处理和语言处理。 通过检查 GET 参数和 Accept HTTP头部来决定响应内容格式和语言
yii\filters\HttpCache 
HttpCache利用Last-Modified 和 Etag HTTP头实现客户端缓存
yii\filters\PageCache 
实现服务器端整个页面的缓存
yii\filters\RateLimiter 
RateLimiter 根据 漏桶算法 来实现速率限制。 主要用在实现RESTful APIs
yii\filters\VerbFilter 
VerbFilter检查请求动作的HTTP请求方式是否允许执行， 如果不允许，会抛出HTTP 405异常
yii\filters\Cors
跨域资源共享 CORS 机制允许一个网页的许多资源（例如字体、JavaScript等） 这些资源可以通过其他域名访问获取


小部件
小部件是面向对象方式来重用视图代码。
创建小部件时仍需要遵循MVC模式，通常逻辑代码在小部件类， 展示内容在视图中。
小部件是在 视图 中使用的可重用单元， 使用面向对象方式创建复杂和可配置用户界面单元
使用小部件
小部件基本上在views中使用，在视图中可调用 yii\base\Widget::widget() 方法使用小部件。 该方法使用 配置 数组初始化小部件并返回小部件渲染后的结果。一些小部件可在yii\base\Widget::begin() 和 yii\base\Widget::end() 调用中使用数据内容
创建小部件
继承 yii\base\Widget 类并覆盖 yii\base\Widget::init() 和/或 yii\base\Widget::run() 方法可创建小部件。通常init() 方法处理小部件属性， run() 方法包含小部件生成渲染结果的代码
有时小部件需要渲染很多内容，一种更好的办法 是将内容放入一个视图文件， 然后调用yii\base\Widget::render()方法渲染该视图文件
小部件的视图文件默认存储在WidgetPath/views目录，WidgetPath代表小部件类文件所在的目录



资源包

Yii在资源包中管理资源，资源包简单的说就是放在一个目录下的资源集合， 当在视图中注册一个资源包， 在渲染Web页面时会包含包中的CSS和JavaScript文件。
定义资源包

资源包指定为继承yii\web\AssetBundle的PHP类， 包名为可自动加载的PHP类名， 在资源包类中，要指定资源所在位置， 包含哪些CSS和JavaScript文件以及和其他包的依赖关系。指定yii\web\AssetBundle::basePath 和 yii\web\AssetBundle::baseUrl 让Yii知道发布资源的位置

资源类型

源资源: 资源文件和PHP源代码放在一起，不能被Web直接访问， 为了使用这些源资源，它们要拷贝到一个可Web访问的Web目录中 成为发布的资源，这个过程称为发布资源，随后会详细介绍。

发布资源: 资源文件放在可通过Web直接访问的Web目录中；

外部资源: 资源文件放在与你的Web应用不同的 Web服务器上；

注:推荐将资源文件放到Web目录以避免不必要的发布资源过程

资源依赖

当Web页面包含多个CSS或JavaScript文件时， 它们有一定的先后顺序以避免属性覆盖,我们称这种资源先后次序称为资源依赖,资源依赖主要通过yii\web\AssetBundle::depends 属性来指定,并且资源依赖关系是可传递，也就是人说A依赖B，B依赖C，那么A也依赖C

资源选项

可指定yii\web\AssetBundle::cssOptions 和 yii\web\AssetBundle::jsOptions 属性来自定义页面包含CSS和JavaScript文件的方式， 这些属性值会分别传递给 yii\web\View::registerCssFile() 和 yii\web\View::registerJsFile() 方法， 在视图 调用这些方法包含CSS和JavaScript文件时。

Bower 和 NPM 资源

大多数 JavaScript/CSS 包通过Bower 和/或 NPM管理， 如果你的应用或扩展使用这些包， 推荐你遵循以下步骤来管理库中的资源：

    修改应用或扩展的 composer.json 文件将包列入require 中， 应使用bower-asset/PackageName (Bower包) 或 npm-asset/PackageName (NPM包)来对应库。
    创建一个资源包类并将你的应用或扩展要使用的JavaScript/CSS 文件列入到类中， 应设置 yii\web\AssetBundle::sourcePath 属性为@bower/PackageName 或 @npm/PackageName， 因为根据别名Composer会安装Bower或NPM包到对应的目录下。



yii核心扩展


    yiisoft/yii2-apidoc: 提供了一个可扩展的、高效的 API 文档生成器。核心框架的 API 文档也是用它生成的。
    yiisoft/yii2-authclient: 提供了一套常用的认证客户端，例如 Facebook OAuth2 客户端、GitHub OAuth2 客户端。
    yiisoft/yii2-bootstrap: 提供了一套挂件，封装了 Bootstrap 的组件和插件。
    yiisoft/yii2-codeception: 提供了基于 Codeception 的测试支持。
    yiisoft/yii2-debug: 提供了对 Yii 应用的调试支持。当使用该扩展是， 在每个页面的底部将显示一个调试工具条。 该扩展还提供了一个独立的页面，以显示更详细的调试信息。
    yiisoft/yii2-elasticsearch: 提供对 Elasticsearch 的使用支持。它包含基本的查询/搜索支持， 并实现了 Active Record 模式让你可以将活动记录 存储在 Elasticsearch 中。
    yiisoft/yii2-faker: 提供了使用 Faker 的支持，为你生成模拟数据。
    yiisoft/yii2-gii: 提供了一个基于页面的代码生成器，具有高可扩展性，并能用来快速生成模型、 表单、模块、CRUD等。
    yiisoft/yii2-imagine: 提供了基于 Imagine 的常用图像处理功能。
    yiisoft/yii2-jui: 提供了一套封装 JQuery UI 的挂件以及它们的交互。
    yiisoft/yii2-mongodb: 提供了对 MongoDB 的使用支持。它包含基本 的查询、活动记录、数据迁移、缓存、代码生成等特性。
    yiisoft/yii2-redis: 提供了对 redis 的使用支持。它包含基本的 查询、活动记录、缓存等特性。
    yiisoft/yii2-smarty: 提供了一个基于 Smarty 的模板引擎。
    yiisoft/yii2-sphinx: 提供了对 Sphinx 的使用支持。它包含基本的 查询、活动记录、代码生成等特性。
    yiisoft/yii2-swiftmailer: 提供了基于 swiftmailer 的邮件发送功能。
    yiisoft/yii2-twig: 提供了一个基于 Twig 的模板引擎。


路由和反路由
由URL到控制器的动作为路由,由路由和请求参数到URL是反路由
yii\web\UrlManager::parseRequest 解析请求为route并解析出请求参数
 yii\web\UrlManager::createUrl 根据route和请求参数来创建url，yii\helpers\Url::to()也可以创建url

 UrlManager支持两种url格式
  the default URL format and the pretty URL format.
  The default URL format uses a query parameter named r to represent the route and normal query parameters to represent the query parameters associated with the route,  The default URL format does not require any configuration of the yii\web\UrlManager and works in any Web server setup. i.e. /index.php?r=post/view&id=100

   The pretty URL format uses the extra path following the entry script name to represent the route and the associated query parameters.To use the pretty URL format, you will need to design a set of yii\web\UrlManager::rules according to the actual requirement about how the URLs should look like i.e /index.php/post/100

    可以通过配置yii\web\UrlManager::enablePrettyUrl，来开启或关闭pretty url特性



请求组件
请求组件关于请求的信息都可以通过它来访问
$request = \Yii::$app->request
获取get或post参数
$get = $request->get(); 
// 等价于: $get = $_GET;
$id = $request->get('id');   
// 等价于: $id = isset($_GET['id']) ? $_GET['id'] : null;
$id = $request->get('id', 1);   
// 等价于: $id = isset($_GET['id']) ? $_GET['id'] : 1;
$name = $request->post('name');
// 等价于: $name = isset($_POST['name']) ? $_POST['name'] : null;
获取跟随请求体，传送的参数
// 返回所有参数
$params = $request->bodyParams;
// 返回参数 "id"
$param = $request->getBodyParam('id');
获取以及测试当前请求方法
$request->method
if ($request->isAjax) { /* 该请求是一个 AJAX 请求 */ }
if ($request->isGet)  { /* 请求方法是 GET */ }
if ($request->isPost) { /* 请求方法是 POST */ }
if ($request->isPut)  { /* 请求方法是 PUT */ }
获取关于url的信息
yii\web\Request::url：返回 /admin/index.php/product?id=100, 此URL不包括host info部分。
yii\web\Request::absoluteUrl：返回 http://example.com/admin/index.php/product?id=100, 包含host infode的整个URL。
yii\web\Request::hostInfo：返回 http://example.com, 只有host info部分。
yii\web\Request::pathInfo：返回 /product， 这个是入口脚本之后，问号之前（查询字符串）的部分。
yii\web\Request::queryString：返回 id=100,问号之后的部分。
yii\web\Request::baseUrl：返回 /admin, host info之后， 入口脚本之前的部分。
yii\web\Request::scriptUrl：返回 /admin/index.php, 没有path info和查询字符串部分。
yii\web\Request::serverName：返回 example.com, URL中的host name。
yii\web\Request::serverPort：返回 80, 这是web服务中使用的端口。
获取http header
$request->headers;
$request->headers->get('Accept');
$request->headers->has('User-Agent');
yii\web\Request::userAgent：返回 User-Agent 头。
yii\web\Request::contentType：返回 Content-Type 头的值， Content-Type 是请求体中MIME类型数据。
yii\web\Request::acceptableContentTypes：返回用户可接受的内容MIME类型。 返回的类型是按照他们的质量得分来排序的。得分最高的类型将被最先返回。
yii\web\Request::acceptableLanguages：返回用户可接受的语言。 返回的语言是按照他们的偏好层次来排序的。第一个参数代表最优先的语言。
获取用户信息
$request->userHost;
$request->userIP;

响应
web开发的本质就是要根据request来生成response
响应对象包含的信息有HTTP状态码，HTTP头和主体内容

指定状态吗
Yii::$app->response->statusCode = 200;
默认状态吗是200，因此一般无需指定200，一般是出错后抛出异常（背后会发送相应的状态吗）
常见异常
yii\web\BadRequestHttpException: status code 400.
yii\web\ConflictHttpException: status code 409.
yii\web\ForbiddenHttpException: status code 403.
yii\web\GoneHttpException: status code 410.
yii\web\MethodNotAllowedHttpException: status code 405.
yii\web\NotAcceptableHttpException: status code 406.
yii\web\NotFoundHttpException: status code 404.
yii\web\ServerErrorHttpException: status code 500.
yii\web\TooManyRequestsHttpException: status code 429.
yii\web\UnauthorizedHttpException: status code 401.
yii\web\UnsupportedMediaTypeHttpException: status code 415
如果想抛出的异常不在如上列表中，可创建一个yii\web\HttpException异常， 带上状态码抛出

响应头
$headers = Yii::$app->response->headers;

// 增加一个 Pragma 头，已存在的Pragma 头不会被覆盖。
$headers->add('Pragma', 'no-cache');

// 设置一个Pragma 头. 任何已存在的Pragma 头都会被丢弃
$headers->set('Pragma', 'no-cache');

// 删除Pragma 头并返回删除的Pragma 头的值到数组
$values = $headers->remove('Pragma');

响应体
直接发送字符串
Yii::$app->response->content = 'hello world!';
发送特定格式内容
$response = Yii::$app->response;
$response->format = \yii\web\Response::FORMAT_JSON;
$response->data = ['message' => 'hello world'];
yii\web\Response::FORMAT_HTML: 通过 yii\web\HtmlResponseFormatter 来实现.
yii\web\Response::FORMAT_XML: 通过 yii\web\XmlResponseFormatter来实现.
yii\web\Response::FORMAT_JSON: 通过 yii\web\JsonResponseFormatter来实现.
yii\web\Response::FORMAT_JSONP: 通过 yii\web\JsonResponseFormatter来实现.
yii\web\Response::FORMAT_RAW: use this format if you want to send the response directly without applying any formatting
因为响应格式默认为yii\web\Response::FORMAT_HTML, 只需要在操作方法中返回一个字符串， 如果想使用其他响应格式，应在返回数据前先设置格式
public function actionInfo()
{
    \Yii::$app->response->format = \yii\web\Response::FORMAT_JSON;
    return [
        'message' => 'hello world',
        'code' => 100,
    ];
}
可调用yii\web\Response::redirect() 方法将用户浏览器跳转到一个URL地址
在控制器的动作中可以$this->redirect('http://example.com/new', 301);
或者
\Yii::$app->response->redirect('http://example.com/new', 301)->send();

如果当前请求为AJAX 请求， 发送一个 Location 头不会自动使浏览器跳转，为解决这个问题， yii\web\Response::redirect() 方法设置一个值为要跳转的URL的X-Redirect 头， 在客户端可编写JavaScript 代码读取该头部值然后让浏览器跳转对应的URL。

    Info: Yii 配备了一个yii.js JavaScript 文件提供常用JavaScript功能，包括基于X-Redirect头的浏览器跳转， 因此，如果你使用该JavaScript 文件(通过yii\web\YiiAsset 资源包注册)， 就不需要编写AJAX跳转的代码。


发送文件
    yii\web\Response::sendFile(): 发送一个已存在的文件到客户端
    yii\web\Response::sendContentAsFile(): 发送一个文本字符串作为文件到客户端
    yii\web\Response::sendStreamAsFile(): 发送一个已存在的文件流作为文件到客户端，如果要发送的文件非常大，应考虑使用 yii\web\Response::sendStreamAsFile() 因为它更节约内存
\Yii::$app->response->sendFile('path/to/file.txt')->send();

一些浏览器提供特殊的名为X-Sendfile的文件发送功能， 原理为将请求跳转到服务器上的文件， Web应用可在服务器发送文件前结束，为使用该功能， 可调用yii\web\Response::xSendFile()，需要参考响应服务器ngnix，apache等配置实现X-Sendfile



会话
$session = Yii::$app->session;

// 检查session是否开启 
if ($session->isActive) ...

// 开启session
$session->open();


// 获取session中的变量值，以下用法是相同的：
$language = $session->get('language');
$language = $session['language'];
$language = isset($_SESSION['language']) ? $_SESSION['language'] : null;

// 设置一个session变量，以下用法是相同的：
$session->set('language', 'en-US');
$session['language'] = 'en-US';
$_SESSION['language'] = 'en-US';

// 删除一个session变量，以下用法是相同的：
$session->remove('language');
unset($session['language']);
unset($_SESSION['language']);

// 检查session变量是否已存在，以下用法是相同的：
if ($session->has('language')) ...
if (isset($session['language'])) ...
if (isset($_SESSION['language'])) ...

// 遍历所有session变量，以下用法是相同的：
foreach ($session as $name => $value) ...
foreach ($_SESSION as $name => $value) ..

// 关闭session
$session->close();

// 销毁session中所有已注册的数据
$session->destroy();

$session元素为数组时限制直接修改
// 如下代码不会生效
$session['captcha']['number'] = 5;
$session['captcha']['lifetime'] = 3600;

// 如下代码会生效：
$session['captcha'] = [
    'number' => 5,
    'lifetime' => 3600,
];

// 如下代码也会生效：
echo $session['captcha']['lifetime'];
推荐的解决方案
// 使用带通用前缀的键来存储数组
$session['captcha.number'] = 5;
$session['captcha.lifetime'] = 3600;


自定义Session存储

yii\web\Session 类默认存储session数据为文件到服务器上， Yii提供以下session类实现不同的session存储方式：

    yii\web\DbSession: 存储session数据在数据表中
    yii\web\CacheSession: 存储session数据到缓存中，缓存和配置中的缓存组件相关
    yii\redis\Session: 存储session数据到以redis 作为存储媒介中
    yii\mongodb\Session: 存储session数据到MongoDB.

所有这些session类支持相同的API方法集，因此， 切换到不同的session存储介质不需要修改项目使用session的代码。
配置会话的存储
'components' => [
    'session' => [
        'class' => 'yii\web\DbSession',
        // 'db' => 'mydb',  // 数据库连接的应用组件ID，默认为'db'.
        // 'sessionTable' => 'my_session', // session 数据表名，默认为'session'.
    ],
],

Flash 数据

Flash数据是一种特别的session数据，它一旦在某个请求中设置后， 只会在下次请求中有效，然后该数据就会自动被删除。 常用于实现只需显示给终端用户一次的信息， 如用户提交一个表单后显示确认信息。
// 请求 #1
// 设置一个名为"postDeleted" flash 信息
$session->setFlash('postDeleted', 'You have successfully deleted your post.');
$session->addFlash('alerts', 'You have successfully deleted your post.');
$session->addFlash('alerts', 'You have successfully added a new friend.');
$session->addFlash('alerts', 'You are promoted.');


// 请求 #2
// 显示名为"postDeleted" flash 信息
echo $session->getFlash('postDeleted');
// $alerts 为名为'alerts'的flash信息，为数组格式
$alerts = $session->getFlash('alerts');

// 请求 #3
// $result 为 false，因为flash信息已被自动删除
$result = $session->hasFlash('postDeleted');

For displaying Flash messages you can use yii\bootstrap\Alert widget in the following way:

echo Alert::widget([
   'options' => ['class' => 'alert-info'],
   'body' => Yii::$app->session->getFlash('postDeleted'),
]);


Cookies
yii\web\Request 和 yii\web\Response 通过名为'cookies'的属性维护一个cookie集合， 前者的cookie 集合代表请求提交的cookies， 后者的cookie集合表示发送给用户的cookies。
// 从 "request"组件中获取cookie集合(yii\web\CookieCollection)
$cookies = Yii::$app->request->cookies;

// 获取名为 "language" cookie 的值，如果不存在，返回默认值"en"
$language = $cookies->getValue('language', 'en');

// 另一种方式获取名为 "language" cookie 的值
if (($cookie = $cookies->get('language')) !== null) {
    $language = $cookie->value;
}

// 可将 $cookies当作数组使用
if (isset($cookies['language'])) {
    $language = $cookies['language']->value;
}

// 判断是否存在名为"language" 的 cookie
if ($cookies->has('language')) ...
if (isset($cookies['language'])) ...
// 从"response"组件中获取cookie 集合(yii\web\CookieCollection)
$cookies = Yii::$app->response->cookies;

// 在要发送的响应中添加一个新的cookie
$cookies->add(new \yii\web\Cookie([
    'name' => 'language',
    'value' => 'zh-CN',
]));

// 删除一个cookie
$cookies->remove('language');
// 等同于以下删除代码
unset($cookies['language']);



错误处理
yii\web\ErrorHandler 错误处理器默认启用， 可通过在应用的入口脚本中定义常量YII_ENABLE_ERROR_HANDLER来禁用
'components' => [
    'errorHandler' => [
        'maxSourceLines' => 20,
    ],
],
如果你想显示一个错误页面告诉用户请求是无效的或无法处理的， 可简单地抛出一个 yii\web\HttpException异常
yii\web\ErrorHandler错误处理器根据常量 YII_DEBUG的值来调整错误显示，当YII_DEBUG 为 true (表示在调试模式)， 错误处理器会显示异常以及详细的函数调用栈和源代码行数来帮助调试， 当YII_DEBUG 为 false，只有错误信息会被显示以防止应用的敏感信息泄漏
@yii/views/errorHandler/error.php: 显示不包含函数调用栈信息的错误信息，当YII_DEBUG 为 false时，所有错误都使用该视图。
@yii/views/errorHandler/exception.php: 显示包含函数调用栈信息的错误信息时使用。
可以配置错误处理器的 yii\web\ErrorHandler::errorView 和 yii\web\ErrorHandler::exceptionView 属性 使用自定义的错误显示视图。
使用指定的错误操作 来自定义错误显示更方便， 为此，首先配置errorHandler组件的 yii\web\ErrorHandler::errorAction 属性
'components' => [
    'errorHandler' => [
        'errorAction' => 'site/error',
    ],
]
常见异常
yii\base\Exception
继承自PHP的全局异常\Exception
该异常类仅仅定义了一个getName方法，用于作为别的异常类的父类

yii\base\ErrorException
继承自PHP的全局异常\ErrorException
用来表示关于php语言本身的错误

yii\base\ExitException
继承自PHP的全局异常\Exception
当程序中抛出该异常时，yii会捕获它并优雅的终止应用实例，所以自己不要去捕获它

yii\base\InvalidCallException
继承自PHP全局的\BadMethodCallException
用来说明以错误的方式调用了某个方法

yii\base\InvalidParamException
继承自PHP全局的\BadMethodCallException
向方法传递了错误的参数

yii\base\InvalidValueException
继承自全局\UnexpectedValueException
表示函数返回值类型错误

yii\base\InvalidConfigException
继承自yii\base\Exception
对象配置不正确

yii\base\UserException
继承自yii\base\Exception
用作为向终端用户显示错误的基类，这类错误往往是由用户引起的

yii\base\InvalidRouteException
继承自yii\base\UserException
表示路由无效

yii\base\UnknownClassException
yii\base\UnknownMethodException
yii\base\UnknownPropertyException
均继承自yii\base\Exception，用来说明访问了未定义的东西

yii\web\HttpException
继承自yii\base\UserException
用户不恰当的请求导致引发的异常，该异常通过属性statusCode来表示标准的http状态码
throw new \yii\web\HttpException(404, 'The requested Item could not be found.');
yii\web\BadRequestHttpException
继承自yii\web\HttpException
状态吗为400的异常
yii\web\ConflictHttpException
继承自yii\web\HttpException
状态吗为409的异常
yii\web\ForbiddenHttpException
继承自yii\web\HttpException
状态吗为403的异常
yii\web\GoneHttpException
继承自yii\web\HttpException
状态吗为410的异常
yii\web\MethodNotAllowedHttpException
405
yii\web\NotAcceptableHttpException 
406
yii\web\NotFoundHttpException
404
yii\web\ServerErrorHttpException
500
yii\web\TooManyRequestsHttpException
429
yii\web\UnauthorizedHttpException
401
yii\web\UnprocessableEntityHttpException
422
yii\web\UnsupportedMediaTypeHttpException
415




日志

Yii提供了一个强大的日志框架，这个框架具有高度的可定制性和可扩展性。使用这个框架， 你可以轻松地记录各种类型的消息，过滤它们， 并且将它们收集到不同的目标，诸如文件，数据库，邮件。

使用Yii日志框架涉及下面的几个步骤：

    在你代码里的各个地方记录 log messages；
    在应用配置里通过配置 log targets 来过滤和导出日志消息；
    检查由不同的目标导出的已过滤的日志消息（例如：Yii debugger）

日志消息

记录日志消息就跟调用下面的日志方法一样简单：

    Yii::trace()：记录一条消息去跟踪一段代码是怎样运行的。这主要在开发的时候使用。
    Yii::info()：记录一条消息来传达一些有用的信息。
    Yii::warning()：记录一个警告消息用来指示一些已经发生的意外。
    Yii::error()：记录一个致命的错误，这个错误应该尽快被检查。

这些日志记录方法针对 严重程度 和 类别 来记录日志消息。 它们共享相同的函数签名 function ($message, $category = 'application')

