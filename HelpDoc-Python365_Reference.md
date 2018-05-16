[The Python Language Reference 3.6.5](https://docs.python.org/3/reference/index.html)
=============================

## 简单介绍
1. 解释器
	- CPython：C语言解释器
	- Jython：Java解释器
	- Python for .NET：使用的是CPython，但可以管理.NET应用且使.NET库可用
	- IronPython：Python for .NET更纯粹的替代品
	- PyPy：由Python编写的解释器
2. 概念
	- 词法分析（lexical analysis）和句法分析（syntactic analysis）使用的概念几乎一样，但前者针对词，后者针对句
	- 使用巴科斯-诺尔形式（Backus-Naur form，BNF）表示词法（lexical）规则，它用于表示上下文无关文法的语言，描述了一类形式语言
	- 规则通常在一行中描述
	- 空格只是用来区分语法表示中的各个部分
	- `::=`表示定义
	- `|`表示左右2项中的任意1项，即或者
	- `*`表示不少于0次的重复
	- `+`表示不少于1次的重复
	- `[ ]`表示最多出现1次的可选项
	- `< >`表示必选项
	- `{ }`表示可重复0至无穷大次的项
	- `( )`表示分组
	- `" "`其中的字符表示字符本身
	- `斜体字`表示参数
	- `...`2个不同字符间的3个点表示在这2个ASCII字符间的范围内任选1个字符

## 词法分析
Python通过解释器（parser）读取程序，输入解释器的是由词法分析器（lexical analyzer）形成的标记（tokens）序列。Python使用Unicode编码解析程序，默认为`UTF-8`，可在[PEP 3120](https://www.python.org/dev/peps/pep-3120/)中查阅细节。

1. 行结构
	- Python程序被划分成不同的逻辑行
	- 逻辑行（logical line）尾用`NEWLINE`标记，除有`NEWLINE`标记外，语句不能跳出该行执行，而逻辑行是由不少于1条遵循行连接规则的物理行（physical line）组成；除了逻辑行开头和字符内的空格外，在1个逻辑行内，空格、tabs、formfeeds都会被忽略，注释也将被忽略
	- 物理行是一个包含结束行标记的字符序列，包括ASCII LF、ASCII序列CR LF、ASCII CR字符，Python使用ASCII LF即`\n`表示行结束符
	- 连接规则
		- 明确的行连接：在物理行的行尾使用`\`将不同的物理行连接为逻辑行，有该符号的行不能写注释
		- 隐含的行连接：如果各类括号内的字符分行写，不需要`\`符号，各行也将被认定为1个逻辑行，并且，每行都可以写注释，但如果分行首尾都使用3个单引号，虽然可以被认定为1个逻辑行，但不能写注释
	- 注释（comments）以`#`开头并以结束符结尾的物理行，它没有任何标记，将被句法忽略
	- 编码声明（encoding declarations）是指，在Python的第1或第2行，以注释形式按照`coding[=:]\s*([-\w.]+)`语法编写的代码，推荐使用`# -*- coding: <encoding-name> -*-`这样的声明
	- 在交互输入语句时，对空行的处理取决于读取-求值-输出循环（read-eval-print loop，REPL），标准的处理方式是，空的逻辑行终止多行语句
	- 缩进（indentation）用于决定多行语句是否为1个组
		- 缩进由1到8个空格组成，一般为4个空格
		- 缩进不能用`\`分割成多行
		- 单个文件内的缩进必须一致
		- Python使用栈来处理`INDENT`和`DEDENT`标记，以识别代码块
2. 其他标记：`identifiers`、`keywords`、`literals`、`operators`和`delimiters`
	- Identifiers
		- 标识的语法基于[Unicode Standard Annex #31](http://unicode.org/reports/tr31/)，且不限长度，更多细节可查阅[PEP 3131](https://www.python.org/dev/peps/pep-3131/)
		- 在Python3中，ASCII以外的字符使用Unicode Character Database版本，并包含于`unicodedata`模块中
		- Unicode类型代码中的字符释义。`Lu`全字母大写；`Ll`全字母小写；`Lt`首字母大写；`Lm`修饰字母（modifier letter）；`Lo`其他字母；`Nl`字母数字（letter numbers）；`Mn`无空格标记（nonspacing marks）；`Mc`间距组合标记（spacing combining marks）；`Nd`十进制数（decimal numbers）；`Pc`连接器标点符号（connector punctuations）；`Other_ID_Start`表示[PropList.txt](http://www.unicode.org/Public/9.0.0/ucd/PropList.txt)中的字符；`Other_ID_Continue`与`Other_ID_Start`相同
		- 所有的标识都被转换为`NFKC`（Normalization Forms, Compatibility Decomposition, followed by Canonical Composition）。标准形式共有4类，NFKC为其中1类，其他3类分别为`NFD`（Normalization Forms, Canonical Decomposition）、`NFC`（Normalization Forms, Canonical Decomposition, followed by Canonical Composition）、`NFKD`（Normalization Forms, Compatibility Decomposition），具体可查阅[Unicode Standard Annex #15](http://unicode.org/reports/tr15/)
	- Keywords
		- 以下标识是Python的关键词，拼写时必须完全准确：`False`, `class`, `finally`, `is`, `return`, `None`, `continue`, `for`, `lambda`, `try`, `True`, `def`, `from`, `nonlocal`, `while`, `and`, `del`, `global`, `not`, `with`, `as`, `elif`, `if`, `or`, `yield`, `assert`, `else`, `import`, `pass`, `break`, `except`, `in`, `raise`
		- 预留的类标识有3个：`_*`不会被`from module import *`导入；`__*__`系统定义的名称；`__*`类的私有名
	- Literals
		- 文字是一些内建类型固定值的符号
		- 文字与其前缀（包括字符前缀和字节前缀）之间不允许使用空白符
		- 源码字符由解码声明决定，默认为`UTF-8`
		- `\`反斜杠跳出字符表示，创建有特殊含义的功能，比如创建新行、输出反斜杠自身或者引用字符等
		- 字节文字包括前缀`b`或者`B`，创建的是字节类型而不是字符类型
		- 以`r`或`R`为前缀的字符和字节类型，将后续的所有字符仅作为字符处理，而不考虑其可能表示的特殊含义，这一作用称为`raw strings`，例如`\n`前加上前缀，输出为字符`\n`而不创建新行
		- 以`f`或`F`为前缀的字符表示格式化的字符串，即部分内容由变量控制其变动，格式化的表达式则置于花括号中，反斜杠不能用于格式化表达式中，表达式中的`!s`等价于`str()`、`!r`等价于`repr()`、`!a`等价于`ascii()`；`f`可与`r`连用，但不能与`b`或`u`连用，因此，只能格式化字符，不能格式化字节
		- 其他跳出字符序列的标识可查阅[Reference文档](https://docs.python.org/3/reference/lexical_analysis.html#literals)；更多关于格式化字符串的建议可查阅[PEP 498 - Literal String Interpolation](https://www.python.org/dev/peps/pep-0498/)
		- 数值包括整数、浮点数、复数（imaginary literals）共3类，每1类都可以使用单个下划线对数值进行分组
	- Operators
		- 运算符包括`+`, `-`, `*`, `**`, `/`, `//`, `%`, `@`, `<<`, `>>`, `&`, `|`, `^`, `~`, `<`, `>`, `<=`, `>=`, `==`, `!=`
	- Delimiters
		- 分隔符包括`(`, `)`, `[`, `]`, `{`, `}`, `,`, `:`, `.`, `;`, `@`, `=`, `->`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `@=`, `&=`, `|=`, `^=`, `>>=`, `<<=`, `**=`
		- 以下4个ASCII字符与其他字符结合有特殊含义：`'`, `"`, `#`, `\`
		- 以下3个ASCII字符没有在Python中使用：`$`, `?`, MD中标记代码的斜点

## 数据模型
1. 对象：值和类型
	- 对象是Python中对数据的抽象化概念，Python程序中的所有数据都以对象或对象间的关联表示
	- 每个对象都有身份，即类型和值，并且，对象一旦创建，将存储于内存中，身份无法改变，`is`运算比较的是2个对象，id()函数返回的整数表示其身份，如果在CPython解释器中，该数值表示其内存地址；对象不可被完全消除，但可能通过垃圾回收变得不可获取，在CPython解释器中，采用引用计数（reference-counting）方案检测循环链接的垃圾，即只要对象不可获取，即尽可能多地回收垃圾，但无法保证回收那些循环引用的垃圾
	- 对象类型既决定了支持对象的运算符，也决定了对象类型的值，并且与身份一样，对象的类型一经确定，不可更改；type函数返回对象类型；类型几乎影响了所有的对象行为（object behavior），甚至包括其身份：对于不可变类型，计算新值的运算可能返回的是1个有相同类型和值的已有对象，但如果是可变类型，则必定是不同的对象，例如，`a = 1; b = 1`，只要解释器允许，则`a`和`b`可以指向相同的对象和值，但如果是`c = []; d = []`，尽管`c`和`d`都是空list，但必定指向2个不同的空list
	- 对象的值既有可更改的类型，也有不可更改的类型，并且可以相互嵌套，是否可更改取决于对象它的类型
	- 容器（container）是指包含引用其他对象的对象，例如，list、tuple、dictionaries等，引用是容器值的组成部分；在大多数情况下，讨论容器的值，指的是值本身，而非包含对象的身份，但是，当讨论容器的可变性时，仅指容器所含对象的身份，因此，如果不可变容器，比如tuple，引用了可变对象，那么，可变对象改变就意味着不可变容器的值发生改变
2. 标准类型层级结构（the standard type hierarchy）
	- `None`：单一值；内建；没有返回值的情况；真实值为False
	- `NotImplemented`：单一值；内建；运算未执行；真实值为True
	- `Ellipsis`：单一值；内建；-；真实值为True
	- `numbers.Number`：非单一值；自建或内建；数学运算
		- `numbers.Integral`：整数；包括整数和布尔值2种类
		- `numbers.Real`：双精度浮点数
		- `numbers.Complex`：双精度浮点数对，用于表示复数的实部和虚部
	- `Sequences`：有限的、有序的、非负数索引的集合；切片`a[i:j]`中任意一个索引`k`满足条件`i <= k < j`；有间隔的切片`a[i:j:k]`中任意一个索引`x`满足条件`x = i + n*k, n >= 0, i <= x < j`
		- 不可变序列（Immutable Sequences）：Strings、Tuples、Bytes
		- 可变序列（Mutable Sequences）：Lists、Byte Arrays[通过`bytearray()`函数创建]
	- `Set types`：有限的、无序的、元素唯一的、无索引的不可变对象；包含2种固有类型：
		- `sets`，表示可变集合，使用`set()`函数创建，使用`add()`等函数修改
		- `Frozen sets`，表示不可变集合，使用`frozenset()`函数创建
	- `Mappings`：有限的、可变的、随意索引的对象集合；包含1种固有类型，即`Dictionaries`，使用花括号创建，`dbm.ndbm`、`dbm.gnu`以及`collections`模块可创建其他mapping类型
	- `Callable Types`：函数应用
		- `User-Defined Functions`：通过定义函数创建，特殊属性包括：`__doc__`, `__name__`, `__qualname__`, `__module__`, `__defaults__`, `__code__`, `__globals__`, `__dict__`, `__closure__`, `__annotations__`, `__kwdefaults__`，其中，除`__globals__`为只读为，其他均为可写
		- `Instance Methods`：实例方法对象是类、类实例和任何函数的组合
		- `Generator Functions`：使用`yield`语句的函数或方法
		- `Coroutine Functions`：使用`async def`定义的函数或方法
		- `Asynchronous Generator Functions`：使用`async def`定义并使用`yield`语句的函数或方法
		- `Built-in Functions`：由C语言写成的函数对象
		- `Built-in Methods`：作为参数传递给C函数
		- `Classes`：类可调用，并且可以创建与自身类似的实例
		- `Class Instances`：类的实例
	- `Modules`：模块是Python代码的基础组织单元
	- `Custom Classes`：通过类定义创建
	- `Class Instances`：通过调用类对象创建类实例
	- `I/O Objects`：也称为文件对象，表示打开的文件
	- `Internal Types`：解释器使用的一些类型
		- `Code Objects`：表示字节编译（byte-compiled）的可执行Python代码或者字节代码（bytecode）；字节对象没有上下文，不可变且没有直接或间接地关联可变对象
		- `Frame Objects`：表示执行框架，可能发生于回溯对象（traceback objects）中
		- `Traceback Objects`：表示追踪`Exception`的栈
		- `Slice Objects`：表示通过`__getitem()__`方法获取的切片
		- `Static Method Objects`：提供了一种防止函数对象转换成方法对象的途径，通过`staticmethod()`创建
		- `Class Method Objects`：与静态方法对象类似，通过将对象包裹以便从类和类实例中取出
3. 类的特殊方法名称：主要介绍与类有关的各种名称及其作用
4. 协同程序（Coroutines）：主要介绍协同程序对象如何定义；与`awaitable object`相同；协同程序的方法；异步迭代器（Asynchronous Iterators）；异步上下文管理器

## 执行模型
1. 程序的结构
	- Python程序由代码块（code blocks）构成
	- 代码块是Python程序文中的一部分，作为1个执行单元
	- 模块、函数主体、类是多个代码块；命令、脚本文件、脚本命令、传入`eval()`和`exec()`函数的字符参数都是1个代码块
	- 代码块在执行框架中被执行，该框架包含一些管理信息，并决定当代码块执行完成后，执行在何地以何种方式继续
2. 命名和捆绑
	- 名称既可与对象关联，也由名称捆绑操作来介绍，比如`for`循环中的名称
	- 名称的作用范围由其所定义的范围决定，比如`global`、`nonlocal`等语句
	- 自由变量的名称解析发生在运行时，而不是编译时，并且，自由变量是在全局名称空间中解析，而不是在最近的名称空间中
3. 例外
	- 例外意味着跳出当前代码块的控制流，去处理错误或者其他条件
	- Python解释器如果在运行时检测到错误，则通过`raise`语句执行例外情况
	- Python使用“终结”模式处理错误，这意味者Python只能检测错误，并继续执行错误发生后已定义的执行步骤，但无法修复错误和重新执行已失败的操作

## 引入系统（Import System）
在Python的1个模块中，通过引入系统获取另1个模块的内容。引入系统的作用机制分2步：第1步是通过`__import__`函数搜索模块名称，第2步是通过`import`语句将搜索结果捆绑到本地名称范围。当第1次引入模块时，Python会创建1个模块对象并初始化，如果没有找到模块，则报错`ModuleNotFoundError`。相关文档见[PEP 302: New Import Hooks](https://www.python.org/dev/peps/pep-0302/)和[PEP 420: Implicit Namespace Packages](https://www.python.org/dev/peps/pep-0420/)。
1. 包
	- 可以粗略地将包理解为文件夹，将模块理解为文件；所有的包都是模块，但并不是所有的模块都是包，即包是一类特殊的模块；任何包含`__path__`属性的模块可以理解为1个包
	- 所有的模块都有名称；可以使用`父包名称.子包名称`的形式，区分父包名称和子包名称
	- Python定义了2类包：一般包（regular packages）和名称空间包（namespace packages）
		- 一般包是1个包含`__init__.py`文件的文件夹，引入包时，将执行包中所有的`__init__.py`文件，包括子包下的该文件；该类包存在于Python3.2及其更早的版本中
		- 名称空间包的特征比一般包复杂，包括：1.由多个部分（portions）综合；2.每个部分为父包提供1个子包；3.部分既可以存在于文件系统中，也可以在zip文件、网络等Python可以搜索到的任何地方；4.不必然与文件系统的对象直接联系，可能是虚拟的模块；5.不使用一般的`__path__`属性列表，而是只要父包路径改变，即在整个包的范围内使用自定义的迭代机制，对每一个引入操作都执行一次新的搜索；6.因该类包使用动态化迭代搜索机制，任意部分可能存在多个父包，也就不存在严格的层级结构，所以子包和父包中没有`__init__.py`文件；为适应这种机制变换，当引入子包时，Python为最高层的父包创建名称空间包；7.更多细节查阅[PEP 420: Implicit Namespace Packages](https://www.python.org/dev/peps/pep-0420/)
2. 搜索和加载
	- 在`sys.modules`中寻找模块全称，找到则返回模块对象
	- 当在`sys.modules`未找到模块全称时，即搜索包含finder对象的`sys.meta_path`，这些`finders`使用包含3个参数的`find_spec()`方法并运用任何可能的策略，确定它们是否能够处理搜寻的模块，亦即引入协议（import protocol）的范畴
		- `find_spec()`方法包含的3个参数分别是名称、引入路径和目标模块（可选）
		- 如果是最高层级的模块，引入路径参数为空，但对于子模块或者子包，引入路径参数为父包`__path__`属性的值
	- 引入协议分别使用`finders`和`loaders`这2个概念对象（conceptual objects）继续执行寻找和加载任务，这2个概念对象包含了一些默认类型（列明的3种类型见下），这些类型的作用机制保证引入机制搜索的范围是可扩展的，需要强调的是，`finders`只负责找模块，而不加载模块，如果`finders`找到模块，则返回包含`loaders`的`module spec`（在Python3.4及更早的版本中，`loaders`和`module spec`是分开返回）
		- 寻找内建模块（built-in modules）
		- 寻找frozen模块
		- 寻找`import path`（包括文件系统路径、zip文件以及拥有权限的网络位置等）中包含的模块
	- 引入机制的可扩展性主要由引入钩子（import hooks）决定，Python包含2类引入钩子：
		- `meta hooks`：在引入机制开始时即启动，保证其可覆盖`sys.path`过程、`Frozen modules`甚至内建模块，通过向`sys.meta_path`增加新的finder对象发生作用
		- `import path hooks`：作为`sys.path`过程的组成部分，通过向`sys.path_hooks`增加新的可调用项发生作用
	- 应当注意到`meta path finder`和`path entry finder`（这是finders中的一种类型，搜索`sys.path`、`sys.path_hooks`和`sys.path_importer_cache`共3类路径，可大致对应于第2类钩子）尽管在类型、作用机制、协议等方面相似，但两者存在显著区别，比如，`meta path finder`在搜索开始时启动，而`path entry finder`不是
	- 替换整个引入系统最可靠的方式是，将`sys.meta_path`的默认内容全部替换为自定义内容
3. PEPs
	- [PEP 328: Imports: Multi-Line and Absolute/Relative](https://www.python.org/dev/peps/pep-0328/)
	- [PEP 338: Executing modules as scripts](https://www.python.org/dev/peps/pep-0338/)
	- [PEP 366: Main module explicit relative imports](https://www.python.org/dev/peps/pep-0366/)
	- [PEP 420: Implicit Namespace Packages](https://www.python.org/dev/peps/pep-0420/)
	- [PEP 451: A ModuleSpec Type for the Import System](https://www.python.org/dev/peps/pep-0451/)

## 语法分析
后续章节对表达式、简单语句、复杂语句和最高级组件的使用语法做了分析，有需求时再针对性学习。

## 版本记录
1. 2018年05月16日，v1.0.0
