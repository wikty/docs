---
date: 2017/07/03
---

## 基本语法

### PHP 混编

PHP 支持代码与 HTML, Javascript, CSS 等内容混编，开发者只要为 PHP 代码添加特定的标记 `<?php ?>` ，解释器会自动忽略哪些非代码内容。

具体来说解释器会提取脚本文件中所有 `<?php` 和 `?>` 标记之间的内容将其当成 PHP 代码，至于不在标记内的其它内容（包括空白）均会被原样输出到 HTTP 响应内容中。当脚本文件是纯 PHP 代码时，也就是说所有内容都是 PHP 代码，并且放在了标记内，如果不小心在结束标记之后添加了多余空白行，这些空白行会被添加到响应内容中的，因此对于纯 PHP 脚本文件不建议书写结束标记 `?>`。

除了 `<?php ?>` 外，还可以使用  `<script language="php"> </script>` 标记，另外通过配置 `php.ini` 中的 `short_open_tag` 可以开启短标记 `<? ?>`，配置 `asp_tags` 可以开启短标记 `<% %>`。

PHP 代码与其他内容的混编甚至是接受条件控制的，比如下面的代码会根据代码中的条件判断来决定输出哪行内容：

```php+HTML
<?php if ($expression == true): ?>
  This will show if the expression is true.
<?php else: ?>
  Otherwise this will show.
<?php endif; ?>
```

### 指令结束符

PHP 像 C 语言一样，每行代码结束都用分号来标记结束。不过 PHP 允许省略结束标记 `?>` 之前的分号，比如这样：`<?php echo "hello world!" ?>`。

### 注释

PHP 支持 C 语言的多行注释语法 `/* */` ，不过要注意：多行注释嵌套是不允许的。另外还是支持 `//` 和 `#` 语法的单行注释语法。

## 基本数据类型

PHP 支持 `boolean`, `integer`, `float`, `string`, `array`, `object`, `callable`, `resouce`, `NULL` 共 9 种基本的数据类型。要注意 PHP 是一种动态语言，变量的数据类型不是预先定义的，而是根据运行时的上下文环境来决定的。可以使用 `var_dump()`, `gettype()`, `is_int()`, `is_string()`, `is_null()` 等函数来检查变量类型。

### boolean

boolean 取值为 `TRUE` 和 `FALSE` （不区分大小写），许多条件运算的结果会自动将结果转化为 boolean 类型的，如果需要将某个值强制转化为 boolean 类型，使用语法 `(bool) $v` 或 `(boolean) $v`。

一般来说其它类型变量为空时，转化到 boolean 的结果就是 `FALSE`，比如整数为0、浮点为0.0、空字符串以及字符串 "0"、空数组、NULL、空对象都会被当成 `FALSE` 。

### integer

PHP 5.4 之后的版本支持整数以二进制、八进制、十进制、十六进制来表示，示例如下：

```php
<?php
$a = 1234; // 十进制数
$a = -123; // 负数
$a = 0123; // 八进制数 (等于十进制 83)
$a = 0x1A; // 十六进制数 (等于十进制 26)
$a = 0b11111111; // 二进制数字 (等于十进制 255)
```

值得注意的是 PHP 不支持无符号整数。整数表示范围大小跟平台有关，可以通过常量 `PHP_INT_SIZE` 来查看整数占用字节数，还可以用常量 `PHP_INT_MAX` 和 `PHP_INT_MIN` 来查看整数可表示的最大（PHP 5）和最小整数值（PHP 7）。

当整数变量溢出时，会被自动转换为浮点类型变量。PHP 不支持整除运算，要整除可以强制将结果转为整数 `(int) 1/2` 或者利用函数进行四舍五入 `round(1/2)`。

除了使用 `(int) $v` 和 `(integer) $v` 将变量强制转化为整数外，PHP 还提供了函数 `intval($var, $base=10)` 来将各种类型变量转化整数。

### float

对于浮点数要铭记一点，浮点数的精度是有限的，所以比较两个浮点数是否完全相等是没有意义的，在实际应用中通过会使用一个 epsilon 来比较两个浮点数：

```php
<?php
$a = 1.23456789;
$b = 1.23456780;
$epsilon = 0.00001;

if(abs($a-$b) < $epsilon) {
    echo "true";
}
```

当数学运算非法时，会产生一个由常量 `NAN` 表示的结果，NAN 和任何值比较的结果都是 FALSE （包括它自己），要检测 NAN 值，需要使用函数 `is_nan()`。

### string

string 类型由一系列字符组成，每个字符用一个字节来存储，也就是意味着 string 类型仅支持 ASCII 字符集中的 256 个字符。要想在 PHP 中支持 Unicode 字符集，参见文档[国际化字符编码支持](http://php.net/manual/zh/refs.international.php)。在 PHP 内部字符串通过一个数组和标识数组长度的结构来表示，允许中间任意位置出现 NULL 字符（不同于C中的字符串以 NULL 作为结尾标识），PHP 文档中关于字符串的函数标明“二进制安全”的意思是，该函数可以处理中间位置含有 NULL 字符的字符串。

#### 字符串创建

在 PHP 中可以使用四种方式创建字符串：

1. 单引号

   用单引号把一系列字符包围起来。要在字符串中插入单引号需要用反斜杠转义 `\'` ，要在字符串中插入反斜杠仍需要反斜杠来转义 `\\` 。以单引号方式创建的字符串，转义字符只对它自己和单引号有转义作用，其它比如 `\n` 并没有转义作用，会被当成两个字符来处理。

2. 双引号

   用双引号把一系列字符包围起来。不同于单引号的是，双引号字符串中的任何转义字符都会被转义，而且双引号中的变量也会被解析。

3. heredoc

   以 `<<<` 开始，后面紧跟一个标识符，然后换行，然后是字符串内容，最后用之前定义的标识符作为字符串结束标记。切记结束标识符要位于行首，它前面不能有任何内容。heredoc 就像没有双引号的多行双引号字符串，其中的转义字符和变量都会被解析。而且从 PHP 5.3 开始可以用 heredoc 来初始化静态变量和类的属性和常量。

4. nowdoc

   nowdoc 自 PHP 5.3 引入。nowdoc 的声明语法类似于 heredoc，只有一点不同在于，nowdoc 要求位于 `<<<` 之后的标识符用单引号括起来。而且 nowdoc 的用途跟 heredoc 完全不同，nowdoc 可以看成是没有单引号的单引号字符，定义的字符串内容不会被进行解析。同样 nowdoc 可以用来初始化静态变量和类的属性和常量。

#### 字符串中变量解析

在双引号和 heredoc 的变量都会被解析后再输出到字符串中。

当 PHP 解析器遇到一个美元符号（*$*）时，会组合尽量多的标识以形成一个合法的变量名。并且支持 array 索引和 object 属性的解析：

```php
<?php
$username = array("a", "b", "c");

echo "He is $username[0]";
echo "He is $username[1]s"; // Won't work

class User {
  public $name = 'abc';
}

$user = new User();

echo "He is $user->name";
echo "He is $user->nameand is 15 years old"; // Won't work
```

当出现上面这样解释失败的情形时，可以为变量添加花括号来跟周围字符区分开（注意花括号和变量之间不要有任何空白）：

```
<?php
// 当在字符串中使用多重数组时，一定要用括号将它括起来
echo "This works: {$arr['foo'][3]}"; // echo "This works: " . $arr['foo'][3];
// 访问变量值存储的变量名的变量
echo "This is the value of the var named $name: {${$name}}";
// 对象属性名也可以通过变量来访问
class foo {
    var $bar = 'I am bar.';
}
$f = new foo()
$v = 'bar';
echo "{$f->$v}"; // I am bar.
// 访问函数返回值的变量名的变量
echo "This is the value of the var named by the return value of getName(): {${getName()}}";
// 直接在字符串中访问函数返回值是无效的
echo "This is the value of the return value on getName(): {getName()}"
// 访问对象方法返回值的变量名的变量
echo "This is the value of the var named by the return value of \$object->getName(): {${$object->getName()}}";
// 访问类常量和静态属性
class beers {
    const softdrink = 'bar';
    public static $foo = 'ipa';
}
$bar = 'test1'
$foo = 'test2'
echo "{${beers::softdrink}}"; // test1
echo "{${beers::$foo}}"; // test2
```

#### 字符串访问

字符串允许使用 `[index]` 语法来获取和修改相应位置的字符（索引从 0 开始计算），想要访问字符串中多个字符参数函数 `substr()` 和 `substr_replace()`。PHP 字符串不支持负数索引，当写入索引位置超过字符串当前长度时，会填充空格来拉长字符串。

#### 字符串运算符

字符串支持 `.` 运算符用来连接字符串，并支持 `.=` 运算符将连接后的字符串赋值给左操作数：

```php
<?php
$a = "Hello ";
$b = $a . "World!"; // now $b contains "Hello World!"

$a = "Hello ";
$a .= "World!";     // now $a contains "Hello World!"
```

PHP 是一门类型灵活的语言，甚至支持字符串表示的数字进行数学运算，下面语法是有效的：

```php
<?php
$bar = 1 + '0.9';
```

#### 转化为字符串类型

许多情形下字符串类型的转化是自动发生，比如在 echo 和 print 语句，当需要强制将变量转化为字符串时，可以使用语法 `(string) $v` 或函数 `strval()`。数组转化为字符串时，结果总是 `Array`，因此 echo 和 print 是无法打印出数组内容的。此外对于 object 和 resouce 类型变量转化为字符串也无法获得变量的更多细节，为此可以使用函数 `print_r()` 和 `var_dump()` 来获得 array, object 以及 resource 变量的内容。

除了将各种对象转化为字符串打印出来，PHP 还提供了 `serialize()/unserialize()` 这对函数来序列化和逆序列化对象。







PHP keywords - static and self

class A {
    public static function who() {
        echo __CLASS__;
    }
    
    public static function test() {
        self::who();
        //static::who();
    }
}

class B extends A {
    public static function who() {
        echo __CLASS__;
    }
}

A::test();  // print A
B::test();  // print A
由于self指代当前类,不会随继承而改变其指向

class A {
    public static function who() {
        echo __CLASS__;
    }
    
    public static function test() {
        //self::who();
        static::who();
    }
}

class B extends A {
    public static function who() {
        echo __CLASS__;
    }
}

A::test();  // print A
B::test();  // print B
由于static指向继承链中某个子类,所以由static引用的方法在继承链中确定


另外一个例子
class A {
    public static function getSelf() {
        return new self();
    }
    
    public static function getStatic() {
        return new static();
    }
    
    public function getRunSelf() {
        $cls = get_class($this);
    
        return new $cls();
    }
}

class B extends A {}

$a = new A();
$b = new B();
echo get_class(A::getSelf()); // A
echo get_class(A::getStatic()); // A 由于没有继承链, static指向当前类等同于self
echo get_class(B::getSelf()); // A 父类定义方法使用了self，则方法由父类决定
echo get_class(B::getStatic()); // B 父类方法定义中使用了static，则方法由继承链决定
echo get_class($b->getRunSelf()); // $this对应的类，是实例化对象时的那个类

PHP keywords - self and parent

self 用来指向当前类，同任何实例无关，通常用来引用属于类的东西，比如类中定义的静态量或者常量

parent 类似于self，唯一的不同是parent用来指向当前类的父类，通常用于在当前类中引用父类的方法（甚至是被当前类重写的方法也可以通过parent引用父类方法）


PHP - string

Native Char-Set
PHP only supports a 256-character set, and hence does not offer native Unicode support

Single Quoted
可以将这类字符串当成所见即所得字符串，仅转义字符串中的\\和\'，值得注意的是字符串中可以换行并且会原样输出，同时字符串中的\r\n并不会被转义

Double Quoted
字符串中的\n,\r,\t,\\,\$,\",\[0-7]{1,3},\x[0-9A-Fa-f]{1,2},\u{0-9A-Fa-f}+均进行转义，并且其中的变量会被转换

Heredoc
除了声明语法同Double Quoted不同外，字符串内部转义规则是一样的
声明语法：以<<<开始，紧跟heredoc的id，id命名规则同变量命名规则但一般写作大写字母，id可以用双引号括起来或者不添加引号，换行，字符串内容，换行，id结束符（必须写在行首且在行尾仅有分号），换行
可以作为函数参数
var_dump(array(<<<EOD
foobar!
EOD
));
可以用来初始化静态变量，类常量以及类属性（显然在heredoc中含有变量时是不能初始化他们的）

Nowdoc
也是所见即所得字符串，转义规则同Single Quoted，声明语法同Heredoc，但id必须用单引号括起来

Variable parsing
双引号和heredoc中的变量将会被解析
simple syntax
以$开始紧跟字符将被贪心识别为变量，除非使用{}括起来将识别截断，可以解析出普通变量，数组索引以及对象属性
comple syntax
可以用来解析负责的字符串表达式，就像在php中写普通字符串表达式一样写出的表达式，用{}括起来后在双引号和heredoc中就会被解析
，有一点要注意{符号是不会被解析的，除为{后面紧跟$，也就是说{$name}，其中字符串表达式$name和{}不能有空格
echo "This is the value of the var named $name: {${$name}}";

echo "This is the value of the var named by the return value of getName(): {${getName()}}";

echo "This is the value of the var named by the return value of \$object->getName(): {${$object->getName()}}";

echo "{$foo->{$baz[1]}}\n"; // 先计算{$baz[1]}再计算{$foo->{}}

// Won't work, outputs: This is the return value of getName(): {getName()}
echo "This is the return value of getName(): {getName()}";

函数，方法，类静态变量，类常量均可以在{${}}语法中被解析
class beers {
    const softdrink = 'rootbeer';
    public static $ale = 'ipa';
}

$rootbeer = 'A & W';
$ipa = 'Alexander Keith\'s';

// This works; outputs: I'd like an A & W
echo "I'd like an {${beers::softdrink}}\n";

// This works too; outputs: I'd like an Alexander Keith's
echo "I'd like an {${beers::$ale}}\n";

Index char
php7支持负索引
因为字符串内部是比特串，因此对于多字节字符使用索引访问字符串是不安全的

Dot syntax
字符串拼接语法



PHP - funcitons

函数的定义顺序和调用顺序并无强制先后
函数内部可以定义函数和类
函数可以在任何地方调用,也可以在任何地方定义,在没有指定名称空间的情况下,定义在任何地方的函数和类都是全局的
两种情况的条件定义
if条件中定义的函数,if条件没有执行则函数未定义
函数中定义的子函数,函数没有调用则子函数未定义
函数不支持函数重载,或者说无法实现函数重载
支持可变参数和默认参数;跟参数有关的函数func_num_args, func_get_arg, func_get_args
可变参数传入支持简洁语法，在参数名前添加...，则该参数是一个参数数组，并且可以在调用多参数函数时使用该操作符，其意义为将一个数组unpack，比如add(...[2, 4])将等价于add(2, 4)，另外如果引用传入可变参数只需添加前缀&即可
支持函数recursion调用
实参求值顺序是从左到右
参数传递默认是值传递（函数内部使用的参数是外部传入参数的副本），但同时支持引用传递参数（函数内部使用的参数值是外部的引用，要想使用引用传递参数，需要在定义函数时在相应参数前面添加&）
默认参数的值必须是个常量表达式，此外可以使用array()以及null
参数支持类型声明，当传入参数类型不符时会引发异常，当前可用类型如下：
Class/Interface Name（instanceof操作符能通过即可）, self(在类中方法的参数前使用，表示只接受当前类的实例作为参数), array, callable, bool, float, int, string
声明了类型并同时指定默认参数为null时，null才能通过类型检查
函数返回数组，在调用函数时需要使用list函数来接受返回的多个数据
函数返回引用，需要在定义函数时，在函数名前添加前缀&，并且在调用函数时也要在函数名前添加前缀&
php7支持返回值类型声明，语法如下function test: int {}
函数变量（实现回调函数，函数表等），在变量后面添加后缀()，就会根据变量值寻找同名函数执行，例子：
function test() { echo 'test'; }; $func = 'test'; $func();
$foo = new Foo(); $method = 'inFooMethod'; $foo->$method();
$staticMethod = 'inFooStaticMethod'; Foo::$staticMethod();
支持匿名函数，并可以通过use语法来使用父作用域的变量


PHP - Class & Object

类定义
class Test { constants; properties; methods; }
类实例化
$o = new className; or new className();
$cls = 'className'; $o = new $cls(); // 但该类不在当前名称空间时需要指定类的完全名称
在类内部，可以new self, new parent来创建实例

对象赋值
对象赋值时进行了浅复制（产生了新对象，但新对象依然引用原对象中复杂属性），当赋值时如果使用了&符号则就变成引用了（访问同一个对象）

创建新对象的方法
在静态方法中可以通过new static;来创建新对象，并且该方法可以被子类继承，用来创建子类对象
根据已经创建的对象来创建新对象new $o;

属性和方法可以同名
引用时会根据上下文以及访问权限来判断是要访问属性还是方法
php7以前如果一个属性被赋值为匿名函数，在调用时，需要先将其赋值给另外的变量，然后再调用，不过php7解除了这个限制

继承
php中的继承是单继承的
继承时子类会重写父类的属性和方法（如果父类中使用了final则无法重写），子类中可以使用parent来访问父类中被重写的方法和静态属性
除了构造函数以外，别的方法重写均要求函数签名一致

获取类的完全名称（有名称空间前缀的名称）
echo 类名::class;

属性的初始化
只能在初始化中使用常量表达式（heredoc和nowdoc也可以使用，但注意heredoc中不能有变量；常量也可以使用；数组常量也可以使用）

属性的访问
$this->property
$this->$propertyName
ClassName::staticProperty

类常量
默认访问权限是public，但可以被改变为protected，private
常量是属于类的，不是属于某个实例的
常量定义时指定值且后来是不可变的，常量值只能是常量表达式（编译时就可以确定的）
类内访问常量的语法self::Const，外部访问语法ClassName::Const，实例访问语法$o::Const

类自动加载
通过函数spl_autoload_register来定义自动加载器，在使用未定义类或者接口时就会触发自动加载器。这样可以避免在脚本中使用很多include来引入依赖类和接口

构造/析构函数
__construct
在类实例化时被调用，父类的构造函数不会被子类构造函数隐含调用，需要开发者手动调用parent::__coonstruct
__destruct
同构造函数一样，子类如果需要的话，要手动调用父类的构造函数，另外构造函数即使在脚本被exit终止也会执行的

属性和方法访问权限
public, protected, private三类访问权限，同别的编程语言没区别；不加修饰符时，默认是public
在当前类的方法中，如果传入的参数是当前类的实例，则在该方法中可以访问参数对象的protected和private属性和方法

类继承
单继承机制；父类的protected和public属性和方法会被子类继承；子类可以重写父类的属性和方法

域操作符
一般应用于访问类静态量，类常量（在类定义外部），或者被重写的属性和方法（在类定义内部）
类定义外部实用域操作符
格式一般为cls::Const注类名可以存放在变量中，于是有语法$className::staticMethod()
类定义内部使用类操作符
parent::$staticVar, self::$staticVar, parent::__construct

静态属性和方法
静态属性和方法不需要实例化一个类就可以通过类进行访问（因此在静态方法内$this不能使用），此外静态属性不能通过实例->访问（但可以通过实例::访问），静态方法可以通过实例访问
静态属性和方法是怎样继承的有待讨论

抽象类
声明了至少一个抽象方法的类就是抽象类
抽象方法就是只定义函数签名不定义函数体的
抽象类不能被实例化
抽象类中可以定义一般类中可以定义的东西，比如属性，常量等
具体类继承抽象类时必须实现所有抽象方法并且函数签名要一致（子类中方法可以定义除了抽象方法接受参数外的额外参数）且访问权限要更为宽松
abstract class AbstractClass
{
    // Force Extending class to define this method
    abstract protected function getValue();
    abstract protected function prefixValue($prefix);
    
    // Common method
    public function printOut() {
        print $this->getValue() . "\n";
    }
}


接口
定义了一系列子类必须实现的方法集合
使用关键字interface而不是class来定义接口
接口中的所有方法都是public的
类实现接口使用关键字implements，一个类可以实现多个接口
接口可以定义常量且常量不能被继承的子接口或者实现类重写，接口常量的访问语法也是域作用符

Trait
为单继承语言PHP提供了代码重用的特性，当代码不需要继承但要实现重用时，比如常见的组合模式就很适合使用trait
trait不能够实例化
trait定义使用关键字trait
trait在类定义中使用，用关键字use traitName, anotherTrait;
父类方法会被trait引入的方法重写，trait引入的方法会被当前类中定义的方法重写
在一个类中使用多个trait时，会面对名称冲突情况，为了避免不同trait中相同名称的冲突
trait A {
    public function smallTalk() {
        echo 'a';
    }
    public function bigTalk() {
        echo 'A';
    }
}

trait B {
    public function smallTalk() {
        echo 'b';
    }
    public function bigTalk() {
        echo 'B';
    }
}

class Talker {
    use A, B {
        B::smallTalk insteadof A;
        A::bigTalk insteadof B;
    }
}

class Aliased_Talker {
    use A, B {
        B::smallTalk insteadof A; // instanceof 排他
        A::bigTalk insteadof B;
        B::bigTalk as talk; // as别名机制
    }
}
类使用trait时改变访问权限
trait HelloWorld {
    public function sayHello() {
        echo 'Hello World!';
    }
}

// Change visibility of sayHello
class MyClass1 {
    use HelloWorld { sayHello as protected; }
}

// Alias method with changed visibility
// sayHello visibility not changed
class MyClass2 {
    use HelloWorld { sayHello as private myPrivateHello; }
}
trait中使用多个别的trait
trait HelloWorld {
    use Hello, World;
}
抽象trait，强制类实现相应方法
trait Hello {
    public function sayHelloWorld() {
        echo 'Hello'.$this->getWorld();
    }
    abstract public function getWorld();
}
trait静态变量和静态方法
trait Counter {
    public function inc() {
        static $c = 0;
        $c = $c + 1;
        echo "$c\n";
    }
}

class C1 {
    use Counter;
}

class C2 {
    use Counter;
}

$o = new C1(); $o->inc(); // echo 1
$p = new C2(); $p->inc(); // echo 1

trait StaticExample {
    public static function doSomething() {
        return 'Doing something';
    }
}

class Example {
    use StaticExample;
}

Example::doSomething();
trait定义属性后，在使用该trait 的类中不能定义名称一样的属性

php7支持匿名类
// PHP 7+ code
$util->setLogger(new class('warning,error') {
    public function log($msg)
    {
        echo $msg;
    }
});

重载
在访问不存在的属性和方法，或者当前作用域内没有权限访问属性和方法时，可以利用overload机制来动态的为对象添加属性和方法（这一切的背后是由php类中提供的某些magic方法实现的），另外所有overload属性方法都是public的
实现了以下magic方法，就可以实现overload（注意以下方法均在object context，不在static context）
public void __set ( string $name , mixed $value ) // $o->name = 'xiao'时调用该magic方法
public mixed __get ( string $name ) // $o->name时调用该magic方法
public bool __isset ( string $name ) // isset($o)时调用该magic方法
public void __unset ( string $name ) // unset($o)时调用该magic方法
示例
class PropertyTest
{
    /**  Location for overloaded data.  */
    private $data = array();
    
    /**  Overloading not used on declared properties.  */
    public $declared = 1;
    
    /**  Overloading only used on this when accessed outside the class.  */
    private $hidden = 2;
    
    public function __set($name, $value)
    {
        echo "Setting '$name' to '$value'\n";
        $this->data[$name] = $value;
    }
    
    public function __get($name)
    {
        echo "Getting '$name'\n";
        if (array_key_exists($name, $this->data)) {
            return $this->data[$name];
        }
    
        $trace = debug_backtrace();
        trigger_error(
            'Undefined property via __get(): ' . $name .
            ' in ' . $trace[0]['file'] .
            ' on line ' . $trace[0]['line'],
            E_USER_NOTICE);
        return null;
    }
    
    /**  As of PHP 5.1.0  */
    public function __isset($name)
    {
        echo "Is '$name' set?\n";
        return isset($this->data[$name]);
    }
    
    /**  As of PHP 5.1.0  */
    public function __unset($name)
    {
        echo "Unsetting '$name'\n";
        unset($this->data[$name]);
    }
    
    /**  Not a magic method, just here for example.  */
    public function getHidden()
    {
        return $this->hidden;
    }
}

$obj = new PropertyTest;

$obj->a = 1; // Invoke __set('a', 1)
echo $obj->a . "\n\n"; // invoke __get('a')

echo $obj->declard; // 对象拥有该属性且当前作用域可以访问该属性，所以不会调用__get
echo $obj->getHidden(); // 属性hidden在对象内部被访问，所以不会调用__get
echo $obj->hidden; // 对象定义的hidden在外部访问权限不足，所以调用了__get('hidden')

 public mixed __call ( string $name , array $arguments ) // 调用对象不存在或者不可访问的方法时调用该magic方法
public static mixed __callStatic ( string $name , array $arguments ) // 调用类不存在或者不可访问的静态方法时调用该magic方法
class MethodTest
{
    public function __call($name, $arguments)
    {
        // Note: value of $name is case sensitive.
        echo "Calling object method '$name' "
             . implode(', ', $arguments). "\n";
    }
    
    /**  As of PHP 5.3.0  */
    public static function __callStatic($name, $arguments)
    {
        // Note: value of $name is case sensitive.
        echo "Calling static method '$name' "
             . implode(', ', $arguments). "\n";
    }
}

$obj = new MethodTest;
$obj->runTest('in object context');

MethodTest::runTest('in static context');  // As of PHP 5.3.0

对象迭代
默认情况下对象的visible properties会被迭代（foreach），因为在不同作用域可以被迭代的属性是不一样的（比如类方法中和全局作用域）
对象可以实现迭代接口，来实现一个迭代器类，示例如下
class MyIterator implements Iterator
{
    private $var = array();

    public function __construct($array)
    {
        if (is_array($array)) {
            $this->var = $array;
        }
    }
    
    public function rewind()
    {
        echo "rewinding\n";
        reset($this->var);
    }
      
    public function current()
    {
        $var = current($this->var);
        echo "current: $var\n";
        return $var;
    }
      
    public function key() 
    {
        $var = key($this->var);
        echo "key: $var\n";
        return $var;
    }
      
    public function next() 
    {
        $var = next($this->var);
        echo "next: $var\n";
        return $var;
    }
      
    public function valid()
    {
        $key = key($this->var);
        $var = ($key !== NULL && $key !== FALSE);
        echo "valid: $var\n";
        return $var;
    }

}

$values = array(1,2,3);
$it = new MyIterator($values);

foreach ($it as $a => $b) {
    print "$a: $b\n";
}
实现迭代器使用接口
class MyCollection implements IteratorAggregate
{
    private $items = array();
    private $count = 0;
    
    // Required definition of interface IteratorAggregate
    public function getIterator() {
        return new MyIterator($this->items);
    }
    
    public function add($value) {
        $this->items[$this->count++] = $value;
    }
}

$coll = new MyCollection();
$coll->add('value 1');
$coll->add('value 2');
$coll->add('value 3');

foreach ($coll as $key => $val) {
    echo "key/value: [$key -> $val]\n\n";
}


Magic方法
在对象被序列化和反序列化时使用
__sleep
__wakeup
对象被转成字符串时
__toString
对象被当成函数调用时（实现了该方法，则is_callbale($o)返回true）
__invoke
当调用var_export时
static __set_state
当调用var_dump时
__debugInfo


Final关键字
类以及方法都可以使用final来修饰，表示不可被子类重写，如果类使用了final，则方法都是final的


对象复制
对象默认的克隆行为是浅复制$copy = clone $o;
对象可以定义__clone方法实现自己的复制行为，在使用clone关键字克隆对象时__clone会被调用，__clone不能被直接调用
class SubObject
{
    static $instances = 0;
    public $instance;
    
    public function __construct() {
        $this->instance = ++self::$instances;
    }
    
    public function __clone() {
        $this->instance = ++self::$instances;
    }
}

class MyCloneable
{
    public $object1;
    public $object2;
    
    function __clone()
    {
        // Force a copy of this->object, otherwise
        // it will point to same object.
        $this->object1 = clone $this->object1;
    }
}

$obj = new MyCloneable();

$obj->object1 = new SubObject();
$obj->object2 = new SubObject();

$obj2 = clone $obj;


print("Original Object:\n");
print_r($obj); // has subobject1, subobject2

print("Cloned Object:\n");
print_r($obj2); // has subobject3, subobject2


对象比较
$o1 == $o2
当对象是一个class且有相同属性和相同直时返回true
$o1 === $o2
只有引用了同一个对象时才会返回true

静态延迟邦定
被调用的方法延迟到运行时再确定，而不是在定义时根据语义确定的
延迟邦定的静态方法，就是运行时位于::前面的那个类
延迟邦定的非静态方法，就是运行时调用的那个对象对应的类
示例
class A {
    public static function who() {
        echo __CLASS__;
    }
    public static function test() {
        self::who(); // self代表定义位置的class
    }
}

class B extends A {
    public static function who() {
        echo __CLASS__;
    }
}

B::test(); // 输出A

class A {
    public static function who() {
        echo __CLASS__;
    }
    public static function test() {
        static::who(); // static延迟邦定代表调用位置的class
    }
}

class B extends A {
    public static function who() {
        echo __CLASS__;
    }
}

B::test(); // 输出B

class A {
    public static function foo() {
        static::who(); // 延迟邦定
    }
    
    public static function who() {
        echo __CLASS__."\n";
    }
}

class B extends A {
    public static function test() {
        A::foo(); // 使用精确名称调用，则直接调用A的foo，且A是邦定类
        parent::foo(); // 调用父类的foo，邦定类是C
        self::foo(); // 调用继承自父类的foo，邦定类是C
    }
    
    public static function who() {
        echo __CLASS__."\n";
    }
}
class C extends B {
    public static function who() {
        echo __CLASS__."\n";
    }
}

C::test();

PHP5以后对象表示和对象储存分离，我们看到的是对象的表示，对象表示间复制就好像对象引用一样的，因为本质上我们到的对象表示是一个记录了对象储存位置的变量
class A {
    public $foo = 1;
}  

$a = new A;
$b = $a;     // $a and $b are copies of the same identifier
             // ($a) = ($b) = <id>
$b->foo = 2;
echo $a->foo."\n";


$c = new A;
$d = &$c;    // $c and $d are references
             // ($c,$d) = <id>

$d->foo = 2;
echo $c->foo."\n";


$e = new A;

function foo($obj) {
    // ($obj) = ($e) = <id>
    $obj->foo = 2;
}

foo($e);
echo $e->foo."\n";


PHP - Namespace

解决名称冲突
在应用开发和库开发时常见的问题，就是名称冲突问题，如果所有东西放在全局空间里难免不会发生名称冲突，而有了名称空间可以避免这种冲突

名称空间定义
使用namespace关键字，并且定义要放在文件头部（只有declare可以位于namespace前面），名称空间下一般有classes (including abstracts and traits), interfaces, functions and constants
名称空间可以定义子名称空间，用\作为分隔符
声明了名称空间后意味着，当前定义的类，函数，常量是位于该名称空间下面的

一个文件多个名称空间定义（一般不推荐这样做）
namespace MyProject {

const CONNECT_OK = 1;
class Connection { /* ... */ }
function connect() { /* ... */  }
}

namespace { // global code
session_start();
$a = MyProject\connect();
echo MyProject\Connection::start();
}

名称空间的使用
Unqualified Name
没有使用前缀引用的名称，则从当前所在名称空间查找currentnamespace\theName，如果当前名称空间没有找到（具体来说只有函数和常量会全局查找，类永远在当前名称空间下查找，找不到则抱错）或者当前作用域是全局的，则从全局作用域寻找theName
Qualified Name
使用前缀引用的名称，例如here/theName，则从当前名称空间的子名称空间查找currentnamespace\here\theName，如果当前作用域是全局的则查找here\theName
Full Qualified Name
使用全局前缀，比如\top\theName，则在全局查找top\theName

访问php自带的全局函数或者类语法
\strlen('xiao');
new \Exception('error');

动态访问名称空间，对Qualified Name和Full Qualified Name不做区分，所以Full Qualified Name的第一个\可以去掉
namespace namespacename;
class classname
{
    function __construct()
    {
        echo __METHOD__,"\n";
    }
}
function funcname()
{
    echo __FUNCTION__,"\n";
}
const constname = "namespaced";

/* note that if using double quotes, "\\namespacename\\classname" must be used */
$a = '\namespacename\classname';
$obj = new $a; // prints namespacename\classname::__construct
$a = 'namespacename\classname';
$obj = new $a; // also prints namespacename\classname::__construct
$b = 'namespacename\funcname';
$b(); // prints namespacename\funcname
$b = '\namespacename\funcname';
$b(); // also prints namespacename\funcname
echo constant('\namespacename\constname'), "\n"; // prints namespaced
echo constant('namespacename\constname'), "\n"; // also prints namespaced

当前名称空间
__NAMESPACE__当前名称空间的字符串表示，全局作用域是空串
namesapce引用当前名称空间（类似self性质），可以这样使用namespace\func(); 表示调用当前名称空间下的func函数


名称空间别名机制，use必须放在文件作用域，不能放在块作用域，因为在编译时决定的
namespace foo;
use My\Full\Classname as Another;
//use My\Full\Classname as Another, My\Full\NSname; 导入多个

// this is the same as use My\Full\NSname as NSname
use My\Full\NSname;

// importing a global class
use ArrayObject;

// importing a function (PHP 5.6+)
use function My\Full\functionName;

// aliasing a function (PHP 5.6+)
use function My\Full\functionName as func;

// importing a constant (PHP 5.6+)
use const My\Full\CONSTANT;

$obj = new namespace\Another; // instantiates object of class foo\Another
$obj = new Another; // instantiates object of class My\Full\Classname
NSname\subns\func(); // calls function My\Full\NSname\subns\func
$a = new ArrayObject(array(1)); // instantiates object of class ArrayObject
// without the "use ArrayObject" we would instantiate an object of class foo\ArrayObject
func(); // calls function My\Full\functionName
echo CONSTANT; // echoes the value of My\Full\CONSTANT

PHP - exceptions

php内置异常
class Exception
{
    protected $message = 'Unknown exception';   // exception message
    private   $string;                          // __toString cache
    protected $code = 0;                        // user defined exception code
    protected $file;                            // source filename of exception
    protected $line;                            // source line of exception
    private   $trace;                           // backtrace
    private   $previous;                        // previous exception if nested exception
    
    public function __construct($message = null, $code = 0, Exception $previous = null);
    
    final private function __clone();           // Inhibits cloning of exceptions.
    
    final public  function getMessage();        // message of exception
    final public  function getCode();           // code of exception
    final public  function getFile();           // source filename
    final public  function getLine();           // source line
    final public  function getTrace();          // an array of the backtrace()
    final public  function getPrevious();       // previous exception
    final public  function getTraceAsString();  // formatted string of trace
    
    // Overrideable
    public function __toString();               // formatted string for display
}
注:继承该类的子类,如果重写__construct的话，最好在内部调用parent::__construct

Standard PHP Library - SPL
http://cn.php.net/spl

SPL Exceptions Class Tree

    LogicException (extends Exception): Exception that represents error in the program logic

        BadFunctionCallException: Exception thrown if a callback refers to an undefined function or if some arguments are missing. A typical use for this exception, is in conjunction with the is_callable() function

            BadMethodCallException : Exception thrown if a callback refers to an undefined method or if some arguments are missing. typically used in conjunction with __call magic method.

        DomainException: Exception thrown if a value does not adhere to a defined valid data domain. 

        InvalidArgumentException: Exception thrown if an argument is not of the expected type. 

        LengthException: Exception thrown if a length is invalid. 

        OutOfRangeException: Exception thrown when an illegal index was requested. This represents errors that should be detected at compile time. 

    RuntimeException (extends Exception): Exception thrown if an error which can only be found on runtime occurs

        OutOfBoundsException: Exception thrown if a value is not a valid key. This represents errors that cannot be detected at compile time.  

        OverflowException: Exception thrown when adding an element to a full container. 

        UnderflowException: Exception thrown when performing an invalid operation on an empty container, such as removing an element

        RangeException: Exception thrown to indicate range errors during program execution.  Normally this means there was an arithmetic error other than under/overflow. This is the runtime version of DomainException

        UnexpectedValueException: Exception thrown if a value does not match with a set of values. Typically this happens when a function calls another function and expects the return value to be of a certain type or value not including arithmetic or buffer related errors.