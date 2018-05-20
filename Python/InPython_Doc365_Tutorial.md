**本文“发表于微博自媒体”，微博：[@钻石草帽](https://weibo.com/strawhatchan)**

[The Python Tutorial 3.6.5](https://docs.python.org/3/tutorial/index.html)
=============================

## 基本概念
1. 解释器
2. 如何进入Python的交互模式
3. 默认编码及其修改方式
4. 编程范式
5. 变量类型
	- 公有变量（public variables），Python中没有特定标识的变量都是公有变量
	- 保护变量，即以单下划线开头的变量，这类变量只有类实例和子类实例能访问，需通过类提供的接口进行访问，不能用`from mdule import *`导入
	- 私有变量或方法名（private variables / method names），是以双下划线开头的变量，只有类对象自己能访问，子类对象和外部都不能访问（Python实质上并没有严格的私有变量，Python中所谓的私有变量，实质是利用name mangling技术将`__var`变量自动转换为`_classname__var`，导致外部无法直接通过变量名访问，但可以通过`实例名._classname__var`访问）
	- 系统定义变量，即前后均有双下划线的变量，形如`__var__`，代表Python中特殊方法的专用标识，如`__init__（）`代表类的构造函数

## 数据类型
1. 数值
2. 字符
3. 图形

## 运算符
1. 数值运算
	- 加减乘除
	- 幂运算
	- 模运算（余数）
2. 逻辑运算
	- 布尔运算（and或者or）
	- 大小判断（`<, >, <=, >=, ==`）
3. 集合运算
	- `-`表示在前者中但不在后者中；`|`表示在前者或后者中；`&`表示在前者和后者中；`^`表示在前者或者后者中，但不同时在两者中

## 控制语句
1. if语句
2. while语句
3. for语句
	- 作用机制：**1. 使用iter()函数将容器对象（container object）存储为迭代对象，如果在类中定义`iter()`函数，则使用`__iter__()`方法； 2. 该对象定义了`__next__()`方法，该方法逐个访问容器中的元素；3. 当访问完容器中的全部元素后，`__next__()`方法触发`StopIteration Exception`停止for循环**
	- 根据for语句的作用机制，可以利用`iter()`函数和`next()`函数还原for语句的执行过程
4. range函数
5. break、continue和else在循环中的应用
6. pass语句
7. 定义函数
	- 参数默认值
	- 位置参数（positional arguments）
	- 关键词参数（keyword arguments）
	- 不定项参数（arbitrary arguments）
	- list或tuple拆包传入函数参数
	- lambda表达式
	- 文档字符（Documentation Strings）
	- 函数注解（Function Annotation）

## 数据结构
1. lists
	- list通过方括号创建
	- list可用的方法
	- list可切片（slice）
	- 将list当作stack处理
	- 将list当作queue处理
	- list的多种创建方式
	- list中可包含list
	- del和pop删除list元素
2. tuples
	- tuple通过逗号分割元素或者圆括号创建
	- tuple元素不可更改
	- tuple中可包含tuple
	- tuple可包含list
3. sets
	- 使用花括号创建set，但空set必须使用set()而不能用花括号
	- set不排序，也没有重复项
	- set可以使用集合运算
4. Dictionaries
	- 可使用花括号或者dict函数创建key-value对
	- 使用keys进行索引
	- 属性值可修改

## 代码组织
1. 模块（modules）
	- 后缀为py的文件
	- 主要作用是将长文件分割为单一功能的短文件，以便管理
	- 每个模块都有它自己的私人符号表（private symbol table），以区别全局符号表（global symbol table）
	- 模块在引用后可调用其中的函数或脚本，引入时可通过“as”重命名模块名称，同时，经引用的模块名称存储于引用模块的全局符号表中
	- 模块可以引用模块
	- 可以引用整个模块，也只可以引用模块中的部分或全部函数
	- 如果将`__name__ == "__main__"`作为引入模块的条件，模块可以作为脚本执行，作用与引入模块执行函数相同
	- 引入模块时的搜索路径顺序依次为：脚本所在目录、Python系统目录、安装依赖的默认目录（注意：由于搜索目录有先后次序，应避免先引入的模块名称与后引入的模块名称发生冲突，否则先引入的模块将被后引入的模块覆盖），并且Python系统目录可以通过sys.path.method进行修改
	- Python缓存每一个引用模块的汇编版本后，存储于`__pycache__`目录下的module.version.pyc文件中；缓存文件允许不同的Python版本同时存在；缓存机制是比较源和缓存文件的日期，如果过期则重新缓存，而在不同的环境中，总是重新汇编文件而不是直接读取缓存文件，如果没有源模块，则不检查缓存
	- dir函数可以找出模块中定义的内容，如函数、变量、模块等，但是，dir函数无法列出内建的函数和变量，需要先引入builtins模块，然后用dir(builtint)函数列出内建函数和变量
2. 包（packages）
	- package是由一系列结构化的模块组成的文件体系
	- package的每一个文件夹中都包含一个初始化文件`__init__.py`，该文件是用于标识package，以区别于其他文件夹
	- 引用时，既可以引用包，也可以引用模块，还可以引用函数或变量
	- 引用package时，既可以绝对引用，也可以相对引用

## 输入与输出
1. 输入和输出格式
	- Python可以通过函数或者方法规范输入和输出格式
	- 可以通过占位符以及format方法规范输入和输出格式
2. 读取和写入文件
	- open函数返回文件对象，有`r`（读取），`w`（写入）和`r+`（读取和写入）共3个可选参数，如果在参数后加上字母`b`，则以二进制模式读取或写入文档
	- 使用open函数时，加上with关键词，以便在打开文件后自动关闭文件，单独使用open无法达到该效果
	- 文件对象有多个方法
3. JSON模块
	- JSON全称为JavaScript Object Notation，广泛用于存储结构化的、类型复杂的数据
	- 需要引入JSON模块，才可对JSON文件进行读取和写入操作

## 错误调试
1. try-except语句
	- except语句可以使用圆括号并用逗号隔开多个错误类型名称，以便同时检测多个错误类型(因为无法确定错误类型，不推荐使用这种方式)
	- try后并列多个except语句，并为每一个except列出其错误提示，有利于准确定位错误类型，其作用顺序是：先发生则先提示
	- except后如果没有定义错误类型，可理解为通配符，通过其他方式调试错误，以便确认错误类型
2. try-except-else语句
	- 当不触发except时，执行else后的代码
3. try-except-else-finally或try-finally语句
	- 无论是否执行try、except或者else后的语句，finally后的内容都将被执行
4. raise语句
	- 强制触发特定错误
5. 可自定义新的Exception类

## 类（classes）
1. 定义
	- namespace
		- namespace是从名称到对象的关系图
		- 不同的namespace之间不存在任何关系
		- 模块属性和模块的全局名称共享相同的namespace
		- 模块属性既可以是只读，比如`__dict__`属性，也可以是写入
		- namespace在不同的时点创建，也有不同的生命周期，其中，内建名称随Python解释器启动创建，且不会被删除；模块的全局namespace在模块被读取时创建，至解释器关闭清除；函数的本地namespace在引入函数时创建，函数返回或者发生错误且未在函数内部处理时删除
		- 解释器最先调用的模块被称为`__main__`，拥有全局namespace
	- scope
		- scope是namespace可直接通过的Python程序的文本范畴，不论其名称关联是否适格
		- scope是固定的，但使用是动态的，namespace至少可以通过4层嵌套的scope，也是Python的搜索顺序，依次是innermost（含local） 、nearest enclosing（含non-local和non-global）、next-to-last（含模块的global names）以及outermost（含built-in names，但built-in names也是global names，因此，严格意义上只有3个）
		- 如果没有global语句，分配名称都会进入innermost scope，即包括local的scope，并且分配给names时，不复制数据，只是将names与对象绑定
		- 所有申明新名称的操作都使用本地范围，包括import和定义函数
```python
# Scopes和Namespaces作用机制示例
def scope_test():
	def do_local():
		spam = "local spam"
	def do_nonlocal():
		nonlocal spam
		spam = "nonlocal spam"
	def do_global():
		global spam
		spam = "global spam"
	spam = "test spam"
	do_local()
	# local scope覆盖了do_local中的spam
	print("After local assignment:", spam) 
	do_nonlocal()
	# 申明spam为nonlocal，local scope不起作用
	print("After nonlocal assignment:", spam) 
	do_global()
	# 虽然申明spam为global，但在函数内部存在nonlocal，优先搜寻到nonlocal scope后即停止
	print("After global assignment:", spam) 
scope_test()
print("In global scope:", spam) # 申明spam为global，在函数之外起作用
# 输出结果为：
# After local assignment: test spam
# After nonlocal assignment: nonlocal spam
# After global assignment: nonlocal spam
# In global scope: global spam
```
2. 类对象
	- 类属性（attribute references）
		- 通过`obj.refnames`调用
		- 所有的refnames都存储于类的namespace中
		- 属性包括2种，一种是不需要申明的数据，另一种是必须申明的方法（属于某个对象的函数）
		- 方法对象可以直接存储于或传递给定义的变量，比如`xf = x.f()`调用时使用`xf()`
	- 实例（instantiation）
		- 实例作为函数概念使用
		- 没有参数的类对象函数直接返回一个实例
		- 创建实例相当于将类对象分配给本地变量
		- 实例定义了`__init__()`这种特殊的方法，自动将类对象分配给定义的变量，其中，`__init__()`方法包含参数，参数间以逗号隔开，并且第1个self参数是必要参数
	- 类属性和实例的关系
		- 因属性定义操作，所以通过属性来操作实例
		- 有效的实例对象名称依赖于它的类
		- 类的所有属性都是定义实例方法的函数对象，如果类MyClass分配给x，即`x = MyClass()`，并且，在MyClass中定义了数据属性i和函数属性f，则`x.f`不是方法，`MyClass.i`也不是函数，但`x.f`是一个有效的方法对象，`MyClass.f`是一个函数对象，也就是说，`x.f`和`MyClass.f`不是相同的事物（也可以这样理解：函数是类的内部属性，方法则是类的外部属性）
		- 方法（Method）的作用机制：**1. 如果实例属性关联的不是数据属性，则搜索类中的函数对象名称；2. 如果属性名称与类中的函数对象名称匹配，则将实例对象和函数对象打包创建一个方法对象；3. 当方法对象引用一个参数列表时，将实例对象和参数列表组建为一个新的参数列表；4. 函数对象引用新组建的参数列表执行函数**（正因这一作用机制，使用方法时不输入任何参数也不会报错，因为，实例本身已作为方法的第1个参数，即self参数，这个参数并非有特定含义，只是一种惯例）
		- 实例变量仅对每一个实例，类变量则对全部实例
```Python
## 实例变量仅对每一个实例，类变量则对全部实例
class Dog:
	kind = 'canine' # 所有实例共享变量
	def __init__(self, name): # 每一个实例特有变量
		self.name = name
d = Dog('Fido')
e = Dog('Buddy')
d.kind # 所有实例共享
e.kind # 所有实例共享
d.name # d实例特有
e.name # e实例特有
## 输出结果
canine
canine
Fido
Buddy
```
3. 继承
	- 同一模块中的类以及其他模块中的类，都可以被当前模块中的类继承，这一特性避免重复编写类
	- 如果引用同一模块中的类，在申明类的圆括号中列出需要引用的类名称即可；如果引用其他模块中的类，则在圆括号中按照`modulename.Classname`的格式列出模块名
	- 类可以同时继承多个类，在圆括号中用逗号隔开
	- 在类继承的前提下，搜索类属性时，首先在当前类中搜索，如果没有该属性，则继续在被继承的类中搜索；如果有多层继承关系，则继续往下一层搜索（因为这种搜索逻辑，基础层类的属性将被上层类的属性替代）
4. Generators
	- generators是创建迭代器的工具
	- 使用generators生成迭代器后，其他函数写法与一般函数写法相同，但函数内通过yield返回数据
	- 任何generators能够做的，都能通过以类为基础的迭代器完成，即在类中定义`__iter__()`和`__next__()`方法
	- 在2次使用函数间，generators定义的本地变量和执行状态都将被自动保存
	- generators终止时，自动执行`StopIteration`
	- generators表达式：`Expression for Var in Range`，其中，`Expression`为表达式，`Var`为表达式中的变量，`Range`为变量范围
5. 特定事项
	- 当数据属性和方法属性名称相同时，数据属性将覆盖方法属性，在大型程序中，这种错误极难被发现，在命名时使用一些惯例有助于避免出现名称冲突，具体包括：方法首字母或者全部字母大写，并使用动词；数据用独有前缀标识，并使用名词
	- 通常类的函数都被置于申明类之后，但类的函数对象并非必须都在这些位置上定义，还可以采取以下方法：在类的同一文件中，先定义函数，然后将函数对象分配给类下的本地变量
	- 类中的方法可以通过使用self参数引用同一类中的方法
	- 类的方法可使用全局变量，但不推荐使用全局变量，因为这样容易造成赋值混乱
	- 每一个值都是一个对象，因而存在类，类存储为`object.__class__`

## 标准库（Standard Library）
1. 包：email，json，gettext，locale，codecs
2. 模块：os，shutil，glob，sys，getopt，argparse，re，math，random，statistics，urllib.request，smtplib，datetime，zlib，gzip，bz2，lzma，zipfile，tarfile，timeit，doctest，unittest，sqlite3
3. 函数：dir，help
4. 方法：replace

## 虚拟环境和包
1. 虚拟环境
	- 基于Python的软件和包都在不断更新，而不同版本的软件开发可能需要用到不同版本的包，所以需要创建不同的虚拟环境，以便满足上述要求
	- 创建环境的语法：`python3 -m venv turorial-env`这将在工作目录中创建一个`tutorial-env`的文件夹，该文件夹内包含Python解释器、标准库和多种支持文件
	- 激活环境的语法：`source tutorial-env/bin/activate`激活环境后，将改变终端目录至创建的虚拟环境文件，并使用定义的Python解释器版本
2. 包的管理
	- 使用pip程序对Python包进行管理，包括安装、升级、删除、查阅等操作
	- 安装：`pip install packagename`
		- 特定版本安装：`pip install packagename==VersionNumber`
	- 升级: `pip install --upgrade packagename`
	- 删除:`pip uninstall packagenames`，即可同时删除多个包
	- 查阅
		- 在Python Package Index上搜索包：`pip search packagename`
		- 查阅包信息：`pip show packagename`
		- 查阅已安装的包列表：`pip list`
		- 列出可以直接用于安装命令的已安装包列表：`pip freeze > requirements.txt`(输出已安装包列表到requirements.txt文件)，然后通过`pip install -r requirements.txt`将已安装的包全部安装(例如，复制全部包到虚拟环境中)

## 其他
- 其他文件：library-index、installing-index、reference-index
- Python资源
	- https://www.python.org
	- https://code.activestate.com/recipes/langs/python/
	- http://www.pyvideo.org
	- https://scipy.org
- 更改解释器：IPython或者bpython
- 浮点数问题
	- 浮点数通常是近似数，而不是准确数，因此，会看到`0.1 + 0.1 + 0.1 == 0.3`为`False`的情形，甚至用`round`等近似方法处理也会返回`False`，解决方案是使用SciPy项目提供的有关数学和统计分析的包，或者使用decimal模块、fractions模块以及float下的方法
	- 表示错误（representation error）以及浮点数问题的根本原因是**十进制除法不能准确地由2进制除法表示**
- Unix系统下，首行输入`#!/usr/bin/env python3.6`意思是在虚拟环境中使用Python3.6作为脚本的解释器，其中，Python3.6可换成其他程序语言，比如Perl等；当指定脚本解释器后，可通过`chmod +x`命令将脚本作为可执行程序
- site模块提供了用户自定义模块的功能
- 附件A是名词解释

## 版本记录
1. 2018年05月11日，v1.0.0