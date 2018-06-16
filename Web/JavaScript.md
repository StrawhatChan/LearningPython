> **本文“发表于微博自媒体”，微博：[@钻石草帽](https://weibo.com/strawhatchan)**

# 概要
**本文采用知识库的方式，记录JavaScript以下各方面内容：**
1. 功能、数据类型、语法、属性、方法、错误处理及调试
2. HTML DOM的对象、属性、方法、事件和节点
3. 浏览器BOM的对象以及属性和方法
4. AJAX的概述和XMLHttpRequest对象
5. JSON的概述与应用

# JS
## 概述
- 功能
    - 修改HTML内容
    - 修改HTML属性值
    - 修改HTML样式
    - 隐藏HTML元素
    - 显示HTML元素
- 脚本调用
    - JavaScript代码必须按照语法`<script> JavaScript Code </script>`调用，也可以采用`<script type="text/javascript"> JavaScript Code </script>`语法，声明脚本类型
    - JavaScript函数与事件关联紧密
    - JavaScript可在`<head>`和`<body>`标签中使用
    - 可使用`<script src="JavaScriptFilePath|URL"></script>`链接外部的JavaScript文件，JavaScript文件的后缀为`.js`
- 显示数据方式
    - innerHTML，写入HTML元素，附于方法后使用
    - document.write()，写入HTML文件，如果HTML文件已全部加载，该方式将删除所有已加载的内容，因此，仅用于测试
    - window.alert()，警告窗口，内容不在HTML文件内出现
    - console.log()，浏览器控制台
- 语句
    - 程序是由一系列计算机可执行语句组成
    - JavaScript的语句包含：值、操作符、表达式、关键词和注释
    - 语句之间使用`;`作为分隔符，一行或多行都可以，建议在最后一个语句后也加上分隔符
    - JavaScript忽略多个空白符，建议在操作符前后加上1个空格
    - 应当避免一行语句超过80个字符，在操作符处断行
    - 语句可以通过以`{}`标识的JavaScript代码块进行分组，分组的目的是将语句一起执行
    - JavaScript语句通常以关键词开始，用以决定调用JavaScript，关键词是JavaScript的保留单词（reserved words），保留单词不能用作变量名称，关键词列表如下

| 关键词      | 描述                                       |
| ----------- | ------------------------------------------ |
| break       | 结束switch或循环                           |
| continue    | 跳出循环重新开始循环                       |
| debugger    | 停止执行JavaScript调用debugging功能        |
| do...while  | 当条件成立时一直循环语句块                 |
| for         | 只要条件成立，则执行语句块                 |
| function    | 声明1个函数                                |
| if...else   | 依据条件执行语句块                         |
| return      | 退出函数                                   |
| switch      | 依据不同的情况决定是否执行语句块           |
| try...catch | 错误处理                                   |
| var         | 声明变量                                   |
| NaN         | Not a Number的简写，非合法数值，类型为数值 |
| Infinity    | 无穷大，类型为数值                         |

- 语法
    - JavaScript语法定义2种类型的值：固定值（fixed values）和变量值（variable values），固定值为文本（literals）、变量值为变量（variables）
    - 文本
        - 数字
        - 字符串
    - 变量
        - 用于存储数据
        - var用于声明变量
        - 变量名唯一
        - 不同变量名之间用`,`作为分隔符
        - `=`给变量分配值，如果未给变量分配值，则该变量拥有特殊值`undefined`
        - `values`为被分配给变量的值
    - 运算符
        - 算术，详细见[JavaScript Arithmetic](https://www.w3schools.com/js/js_arithmetic.asp)（在1个数学运算中，数值称为operands、运算符称为operator
        - 分配，详细见[JavaScript Assignment](https://www.w3schools.com/js/js_assignment.asp)
        - 比较，详细见[JavaScript Comparison and Logical Operators](https://www.w3schools.com/js/js_comparisons.asp)
        - 逻辑，详细见[JavaScript Comparison and Logical Operators](https://www.w3schools.com/js/js_comparisons.asp)
        - 类型，详细见[JavaScript Type Conversion](https://www.w3schools.com/js/js_type_conversion.asp)
        - 按位（bitwise），详细见[JavaScript Bitwise Operations](https://www.w3schools.com/js/js_bitwise.asp)
        - 运算顺序见[JavaScript Operator Precedence Values](https://www.w3schools.com/js/js_arithmetic.asp)，数值越大，运算越优先
    - 表达式，由值、变量和操作符组成，值既可以是数字，也可以是字符串
    - 注释，用`// comment`作为行注释，用`/* comment */`作为块注释
    - 识别码（identifiers）
        - 识别码是名称，且必须唯一
        - 用于为变量、关键词、函数和标签（label）命名
        - 命名规则与其他程序语言相同
        - 第1个字符必须是字母、下划线`_`或者美元符号`$`，第1个字符不允许使用数字，主要是便于区分数字和识别码
        - 后续字符可以是字母、数字、下划线或美元符号
        - <mark>大小写敏感</mark>
    - 组合变量名的方式
        - 短横线，first-name
        - 下划线，first_name
        - 单词的首字母大写，FirstName（帕斯卡，PascalCase）
        - 后续单词的首字母大写，firstName（骆驼，camelCase）
    - 字符集，JavaScript使用**Unicode**字符集，完整的Unicode字符集见[HTML Unicode (UTF-8) Reference](https://www.w3schools.com/charsets/ref_html_utf8.asp)，注意，**Unicode是字符集，UTF-8或者UTF-16是编码**
- 数据类型
    - 数值，JavaScript只有1种数值类型，即双精度浮点数，以64-bit存储，第0-51bits存储值（52 bits），第52-62bits存储指数（11 bits），第63bit存储符号（1 bit）
        - 精度。整数精确到15位，最大的小数点后数位为17，但浮点算术与Python一样，不完全准确，如果要求准确，需要使用除法
        - 原始数值不仅没有属性，也没有方法
    - 字符
    - 布尔值，只有true和false共2个值
    - 对象，使用`var varName = {};`定义，按照name:value对的方式呈现，以`,`为分隔符，使用varName.name调用value
        - 一般对象
        - 日期对象
        - 向量对象
    - 函数，使用`function funName(){};`定义，以`,`为分隔符
    - 特殊类型
        - 未定义，undefined，这是1个特殊值，可赋给数值和字符类型的变量
        - 空值，null，这是1个特殊对象，可赋给对象类型的变量
        - null和undefined值相同，但类型不同，因此，`null == undefined`返回`true`，而`null === undefined`返回`false`
    - 查询方法：使用`typeof value`查询value的数据类型
    - 数据类型转换表见下
        - 双引号中的值表示字符串
        - <font color="red">红色字体</font>表示在某些程序中不期望获得的值

```javascript
// 类型示例
typeof "John"                 // "string"
typeof 3.14                   // "number"
typeof NaN                    // "number"
typeof false                  // "boolean"
typeof [1,2,3,4]              // "object"
typeof {name:'John', age:34}  // "object"
typeof new Date()             // "object"
typeof function () {}         // "function"
typeof myCar                  // "undefined" *
typeof null                   // "object" 
```

| 原始值           | 数值                        | 字符串            | 布尔值                         |
| ---------------- | :-------------------------: | :---------------: | :----------------------------: |
| false            | 0                           | "false"           | false                          |
| true             | 1                           | "true"            | true                           |
| 0                | 0                           | "0"               | false                          |
| 1                | 1                           | "1"               | true                           |
| "0"              | 0                           | "0"               | <font color="red">true</font>  |
| "000"            | 0                           | "000"             | <font color="red">true</font>  |
| "1"              | 1                           | "1                | true                           |
| NaN              | NaN                         | "NaN"             | false                          |
| Infinity         | Infinity                    | "Infinity"        | true                           |
| -Infinity        | -Infinity                   | "-Infinity"       | true                           |
| ""               | <font color="red">0</font>  | ""                | <font color="red">false</font> |
| "20"             | 20                          | "20"              | true                           |
| "twenty"         | 20                          | "20"              | true                           |
| [ ]              | <font color="red">0</font>  | ""                | true                           |
| [20]             | <font color="red">20</font> | "20"              | true                           |
| [10,20]          | NaN                         | "10,20"           | true                           |
| ["twenty"]       | NaN                         | "twenty"          | true                           |
| ["ten","twenty"] | NaN                         | "ten, twenty"     | true                           |
| function(){}     | NaN                         | "function(){}"    | true                           |
| { }              | NaN                         | "[object Object]" | true                           |
| null             | <font color="red">0</font>  | "null"            | false                          |
| undefined        | NaN                         | "undefined"       | false                          |

- 函数
    - 组成
        - 关键词function
        - 函数名称
        - 参数组符号`()`，也是调用函数的标识
        - 参数以及参数之间的分隔符`,`
        - 执行代码组`{}`
        - 执行代码内容
    - 作用时点
        - 事件发生时
        - JavaScript调用时，调用函数必须有参数组符号`()`，如果没有参数组符号，返回函数定义内容
        - 自动调用
    - return
        - 当遇到return语句时，函数停止执行
        - 调用完函数，JavaScript自动return
        - return可以返回计算值
    - 范围
        - 2种类型的范围：本地范围（local scope）和全局范围（global scope）
        - 每个函数创建1个新范围
        - 范围决定了变量可触性（accessibility）或可见性（visibility），即函数内部定义的变量无法从外部可触或可见，这也意味着函数内部定义的变量名称可在函数外部使用
    - 变量
        - 本地变量是指在函数内部定义的变量，本地变量具有本地范围，即仅在函数内可触或可见
        - 全局变量是指函数外部声明为global的变量，全局变量具有全局范围，即当前页面的所有脚本和函数对该变量都可触或可见；如果给1个变量赋值却没有使用`var`声明该变量，那么该变量该变量是处于函数内还是函数外，都将自动成为全局变量（大部分浏览器都是在“strict mode”模式下运行，该模式不支持自动自动创建全局变量）
        - 在JavaScript中，对象和函数本身都是变量
        - 在JavaScript中，全局范围是JavaScript环境，但在HTML中，全局范围是window对象，所有的全局变量都属于window对象，调用方式是`window.VarName`，正因HTML中的全局变量或函数属于window对象，因此，全局变量可以覆盖window变量或函数，反之亦成立
        - 任意变量的生命周期于变量声明时开启；网页中的全局变量在关闭页面时删除，重新打开页面后在变量声明时再次开启；本地变量则在函数执行完成时删除
        - <mark>除非有意识地创建全局变量，否则不应创建</mark>

```javascript
// JavaScript函数组成示例
function name(parameter1, parameter2, parameter3) {
    code to be executed
}

// 参数组符号`()`是调用函数的标识
<p id="demo"></p>

<script>
function toCelsius(f) {
    return (5/9) * (f-32);
}
document.getElementById("demo").innerHTML = toCelsius;
</script>
// 返回的结果为 function toCelsius(f) { return (5/9) * (f-32); } 而不是计算值
```

- 对象
    - 对象类似Python中的类，有属性和方法，方法是操作对象的行为，方法以函数定义形式存储于属性中，也就是说，方法是作为属性存储的函数
    - 创建对象
        - 使用`var varName = {};`创建，按照name:value对的方式呈现，以`,`为分隔符
        - 使用关键词`new`创建，注意，<mark>不要使用new关键词来创建字符串、数字和布尔对象，这一做法将代码复杂化，同时降低了代码执行效率</mark>
    - 属性调用：`ObjectName.PropertyName = value`或者`ObjectName["PropertyName"]`
    - 方法调用：`ObjectName.MethodName() = values`，如果调用方法时不包含参数组符号`()`，则返回函数的定义内容
    - 日期对象
        - 使用`var d = new Date()`创建浏览器所在时区的当前日期对象
        - 使用`var d = new Date(year, month[, day, hour, minute, second, milliseconds])`创建特定的日期对象，如果忽略month，则将数值作为milliseconds对待，如果year只有2个数字，则作为19XX对待
        - 使用`var d = new Date(dateString)`创建特定的日期对象
        - 使用`var d = new Date(milliseconds)`创建特定的日期对象
        - JavaScript自“1970年1月1日00:00:00 UTC（Universal Time Coordinated）”起，以毫秒形式存储日期，意味着`var d = new Date(0)`与“1970年1月1日00:00:00 UTC”相同，一天为86 400 000毫秒，可以使用`Date.parse("dateString")`返回某个日期的毫秒形式
        - JavaScript默认输出完整的日期格式，如“Wed Mar 25 2015 08:00:00 GMT+0800 (CST)”
        - 日期默认进行字符串转换，即`document.getElementById("demo").innerHTML = d`与`document.getElementById("demo").innerHTML = d.toString()`等价
        - 关于日期的对象的参考资料见[JavaScript Date Reference](https://www.w3schools.com/jsref/jsref_obj_date.asp)
    - 向量对象，使用`var ArrayName = [item1, item2, ...];`创建，以`,`为分隔符，或者使用`var ArrayName = new Array(item1, item2, ...);`创建，其中，`new Array()`为固定字符，这两种创建向量的方法完全等价，推荐使用第1种创建方法，不推荐使用第2种创建方法，因为，如果使用`new Array()`创建向量，当向量只有1个值时，将返回undefined
        - 调用整个向量`document.getElementById("demo").innerHTML = ArrayName`
        - 调用向量中的单个值`document.getElementById("demo").innerHTML = ArrayName[IndexNumber]`，其中，IndexNumber从0开始
        - 向量中的值可以是对象、向量、值
        - <mark>向量可使用属性和方法，并且，仅支持数值索引，不支持名称索引</mark>
        - 由于向量也是对象，为解决向量和对象之间的判断问题，ECMAScript 5定义了1个新方法`Array.isArray("ArrayName")`来判断变量是否为向量，也可使用`ArrayName instanceof Array`来判断，其中，instanceof Array为固定字符
        - 关于向量的详细参考资料见[JavaScript Array Reference](https://www.w3schools.com/jsref/jsref_obj_array.asp)
- 事件
    - HTML事件是指HTML元素发生的事情，当JavaScript用于HTML页面时，JavaScript能对HTML事件作出反应
    - HTML事件可以是浏览器作出的，也可以是用户作出的，例如
        - 页面加载结束
        - 输入区域被修改
        - 按下按钮
    - 调用方式`<element event="some JavaScript">`（JavaScript代码也可以使用单引号）
    - 常用HTML事件
        - onchange，HTML元素被修改
        - onclick，用户按下HTML元素
        - onmouseover，用户将鼠标移动到HTML元素上
        - onmouseout，用户将鼠标移开HTML元素
        - onkeydown，用户按下键盘上的某个键
        - onload，浏览器完成页面加载
        - 更多的HTML事件见[HTML DOM Events, Event Porperties and Methods](https://www.w3schools.com/jsref/dom_obj_event.asp)
    - 事件处理器（Event Handlers）可以被用于处理和验证用户输入、用户行动和浏览器行动；不同的方法也能被用于让JavaScript随同事件一起发生作用
- 转义
    - 转义字符通过`\`来实现，例如，`\'`表示`'`、`\"`表示`"`、`\\`表示`\`
    - 6个转义序列，`\b`、`\f`、`\n`、`\r`、`\t`、`\v`，这些转义序列用于控制打字机或者传真机，在HTML中没有任何意义
    - 反斜杠`\`还可以用来接续新行，但不推荐使用这种方法，因为有些浏览器不支持字符后紧跟反斜杠，如果1行代码超过80个字符必须断行，最好使用`+`来接续字符串
    - 不能使用反斜杠来切断1行代码

## 对象属性
- 字符串属性
    - length，字符长度
    - constructor，返回创建字符串的原型（指的是函数，而非函数名称，适用于任何具有构建属性的变量或值）
    - prototype，针对1个对象增加属性和方法
    - 字符串的属性、方法以及HTML包裹（wrapper）方法见[JavaScript String Reference](https://www.w3schools.com/jsref/jsref_obj_string.asp)
- 数值属性
    - 调用方式：`Number.Properties`，其中，Number为固定字符，Properties表示下述属性
        - constructor，返回创建数值的原型（指的是函数，而非函数名称）
        - MAX_VALUE，返回JavaScript中的最大可能值
        - MIN_VALUE，返回JavaScript中的最小可能值
        - NEGATIVE_INFINITY，表示负无穷大
        - NaN，表示“Not-a-Number”
        - POSITIVE_INFINITY，表示无穷大
        - prototype，针对1个对象增加属性和方法
    - 数值属性不可用于变量，只能按照调用方式使用

```javascript
"John".constructor                // function String()  {[native code]}
(3.14).constructor                // function Number()  {[native code]}
false.constructor                 // function Boolean() {[native code]}
[1,2,3,4].constructor             // function Array()   {[native code]}
{name:'John',age:34}.constructor  // function Object()  {[native code]}
new Date().constructor            // function Date()    {[native code]}
function () {}.constructor        // function Function(){[native code]} 
```

## 对象方法
- 概述
    - 方法是操作对象的行为，方法以函数定义形式存储于属性中，也就是说，方法是作为属性存储的函数
    - this关键词
        - 指代函数的所有者，例如，如果1个对象有1个属性定义了1个函数，在这个函数中的this指的就是该对象
        - 不论是在函数内还是函数外单独使用时，均指代全局对象，而在浏览器中，全局对象为[object Window]，但在strict mode中因不允许默认捆绑，this的值为undefined
        - 关于this的详细介绍见[The JavaScript this Keyword](https://www.w3schools.com/js/js_this.asp)
    - 所有的字符串方法返回新的字符串，不修改源字符串，即字符串不可变：字符串不能被修改，只能被替换；字符串的属性、方法以及HTML包裹方法见[JavaScript String Reference](https://www.w3schools.com/jsref/jsref_obj_string.asp)
- 后续表述的含义
    - "idname"表示id名称
    - "strings"表示加双引号的字符串
    - "strings"[,number]表示`,number`为可选项，number为数值
    - "strings"|regular expressions表示字符串或正则表达式
    - starting index和ending index都表示数字
    - length表示数字
    - ()表示括号内不添加任何内容
    - value表示各种类型的值
    - variables表示变量
    - Array表示向量
    - ArrayName表示向量名称
    - ArrayValue表示向量值
    - CompareExpression表示比较表达式
- 预先定义的方法
    - call()
    - apply()
    - 相同：都可以用于以其他对象作为参数来调用对象方法
    - 区别：<mark>call()将参数分开对待，apply()将参数作为向量对待</mark>

```javascript
// call()示例
// 尽管this是person1的方法，但在这里this与person2关联
var person1 = {
    fullName: function() {
        return this.firstName + " " + this.lastName;
    }
}
var person2 = {
    firstName:"John",
    lastName: "Doe",
}
person1.fullName.call(person2);

// apply()示例，说明与call()的功能相同
var person = {
    fullName: function() {
        return this.firstName + " " + this.lastName;
    }
}
var person1 = {
    firstName: "Mary",
    lastName: "Doe",
}
person.fullName.apply(person1);

// 另一个call()示例，说明call()将参数分隔对待
var person = {
    fullName: function(city, country) {
        return this.firstName + " " + this.lastName + "," + city + "," + country;
    }
}
var person1 = {
    firstName:"John",
    lastName: "Doe",
}
person.fullName.call(person1, "Oslo", "Norway");
// 结果为：John Doe,Oslo,Norway

// 另一个apply()示例，说明apply()将参数作为向量对待
var person = {
    fullName: function(city, country) {
        return this.firstName + " " + this.lastName + "," + city + "," + country;
    }
}
var person1 = {
    firstName:"John",
    lastName: "Doe",
}
person.fullName.apply(person1, ["Oslo", "Norway"]);
// 结果为：John Doe,Oslo,Norway
```

### 字符
- getElementById("idname")
    - 读写HTML中拥有特定id的元素
    - 可将innerHTML附后，写入HTML文件
- indexOf("strings"[,number])
    - 找到第1个指定的字符串，并以数字方式输出其起始位置，位置信息从0开始计数，每增加一个字符（包括空格），位置计数信息加1，如果没找到，返回-1
    - [,number]为指定的搜索起始位置
    - 不接受正则表达式
- lastIndexOf("strings"[,number])
    - 找到指定字符串最后1次出现的位置计数信息，如果没找到，返回-1
    - [,number]为指定的搜索起始位置
    - 不接受正则表达式
- search("strings"|regular expressions)
    - 找到指定字符串第1次出现的位置计数信息，如果没找到，返回-1
    - 没有第2个参数
    - 可接受正则表达式
- slice(starting index, ending index)
    - 将字符串中起始位置到结束位置的字符进行切片
    - 如果位置计数信息为负数，则表示从字符串末尾开始计数，最后1个字符为-1
    - 取值区间为[starting index, ending index)
    - 如果忽略ending index，则切取从starting index开始的全部剩余字符
- substring(starting index, ending index)
    - 与slice()方法的功能类似，但不接受负数
    - 如果忽略ending index，则切取从starting index开始的全部剩余字符
- substr(starting index, length)
    - 切取自starting index开始，长度为length的字符
    - 如果忽略length，则切取从starting index开始的全部剩余字符
- replace("string1"|regular expressions, "string2")
    - 使用string2替换第1个string1，替换与被替换字符大小写敏感
    - 如果要使用大小写不敏感的替换，需使用正则表达式中的`/i`标记
    - 如果要替换全部字符，需使用正则表达式中的`/g`标记
    - 正则表达式不加单引号或双引号，JavaScript中的正则表达式见[JavaScript Regular Expressions](https://www.w3schools.com/js/js_regexp.asp)
- toUpperCase()
    - 将所有字母都变为大写字母
- toLowerCase()
    - 将所有字符都变为小写字母
- concat("string1", "string2", "string3", ……)
    - 将所有字符组合成1个字符串
- charAt(number)
    - 返回字符串特定位置的字母，只有1个数字参数，用于定位字母位置
- charCodeAt(number)
    - 返回字符串特定位置字母的Unicode
- split("string")
    - 按照指定的string将字符串转换为序列
    - 按照空格转换`split(" ")`
    - 按照逗号转换`split(",")`
    - 按照分杠转换`split("|")`
    - 按照字母转换`split("")`
- toString(number)
    - 将数值从10进制转换为其他进制
    - number参数表示目标进制数，如Object.toString(2)表示将Object从10进制数转换为2进制数
    - 如果忽略number参数，则变更为数值转换为字符串方法

### 数值
- toString()
    - 将对象从数值转换为字符串，适用于JavaScript的所有对象
    - 如果为向量，则使用`,`分隔向量值，并且，该方法是向量的默认方法，即当向量不使用任何方法时，自动使用该方法，`document.getElementById("demo").innerHTML = fruits.toString()`与`document.getElementById("demo").innerHTML = fruits`有相同的结果
- toExponential(number)
    - 将数值变量转换为指数表达方式的字符串
    - number参数表示保留的小数点位数
- toFixed(number)
    - 将数值变量转换为保留特定小数点位数的字符串
    - number参数表示保留的小数点位数
- toPrecision([number])
    - 将数值变量转换为保留特定数字位数的字符串
    - number参数表示保留的特定数字位数，如果忽略该参数，则返回与原值相同的字符串
- valueOf()
    - 将数值、数值表达式或者存储数值的变量，从数值对象转换为原始数值
- isFinite(value)
    - 检查value是否为有限数值
    - 当value为数值类型并且有限时，返回ture；其他情况返回false
    - 如果按照`Number.isFinite()`调用，则直接判断，其中Number为固定字符；如果按照`isFinite()`的全局方法调用，则先将value转换为数值，然后再进行检查
- isInteger(value)
    - 检查value是否为整数
    - 当value为数值类型并且为整数时，返回ture；其他情况返回false
    - 按照`Number.isInteger()`调用后直接判断，其中Number为固定字符
- isNaN(value)
    - 检查value是否为NaN
    - 当value为数值类型并且为NaN时，返回ture；其他情况返回false
    - 按照`Number.isNaN()`调用后直接判断，其中Number为固定字符
- isSafeInteger(value)
    - 检查value是否为安全整数
    - 当value为数值类型并且为安全整数时，返回ture；其他情况返回false
    - 按照`Number.isSafeInteger()`调用后直接判断，其中Number为固定字符
    - 安全整数（Safe Integer）是指IEEE-754双精度数值，取值范围为[-(2^53-1),2^53-1]
- Number(variables)
    - 全局方法
    - 将变量转换为数值（包括日期），如果无法被转换，返回NaN值
- parseInt()
    - 全局方法
    - 解析字符串并返回第1个值的整数部分，如果第1个值不是数值，返回NaN
- parseFloat()
    - 全局方法
    - 解析字符串并返回第1个值的数值部分，如果第1个值不是数值，返回NaN
- String(value)
    - 全局方法
    - 将数值、文字、变量或表达式转换为字符串，与toString()类似

### 向量
- push(ArrayValue)
    - 在向量末尾增加值，值可以是对象、向量或其他值
    - 如果使用IndexNumber增加向量值，但IndexNumber不是原向量的最后一个值，则中间空缺的值会被undefined填充
- join(Value)
    - 使用Value连接所有向量值
- pop()
    - 将向量的最后1个元素剔除出向量
- shift()
    - 将向量的第1个元素剔除出向量
- unshift()
    - 在向量开头增加值，值可以是对象、向量或其他值
- splice(IndexNumber,Number,ArrayValue1,ArrayValue2……)
    - IndexNumber为索引值，用于确定操作
    - Number为数值，表示从IndexNumber开始移除的原向量值数量，数值可以超过从IndexNumber开始的剩余向量值数量
    - ArrayValue1,ArrayValue2……表示增加的向量值
    - 例如，假设向量为`fruits = ["Banana", "Orange", "Apple", "Mango"]`，使用`fruits.splice(2, 2, "A","B")`得到的结果为`Banana,Orange,A,B`，即从fruits[2]也就是Apple开始，先删除2个向量值，然后添加A和B
- concat(ArrayName1|Array1, ArrayName2|Array1……)
    - 合并2个或2个以上的向量，并返回1个合并后的新向量
- slice(IndexNumber1[, IndexNumber2])
    - 将原向量从IndexNumber1向后剪切至IndexNumber2，但不包含IndexNumber2
    - 如果只有IndexNumber1，则从IndexNumber1开始向后全部剪切
    - 原向量保持不变，并生成1个新向量
- sort()
    - 如果向量值为字符串，则将向量值按字母从小到大排序
    - 如果向量值为数值，则先按首位从小到大排序，然后按第2位从小到大排序，以此类推，而不是按数值大小排序
    - 当向量值为数值并希望按数值从小到大排序时，需要借助比较函数`ArrayName.sort(function(a, b){return a - b})`，而如果要实现从大到小排序，则只需要将return a - b换成return b - a即可
- reverse()
    - 将向量值反向排序
- Math.max()
    - 应用`Math.max.apply(null, arr)`方法并定义1个函数来寻找向量最大值
    - 函数为`function myArrayMax(arr) {return Math.max.apply(null, arr);}`
    - Math.max.apply([1, 2, 3])与Math.max(1, 2, 3)等价
- Math.min()
    - 应用`Math.min.apply(null, arr)`方法并定义1个函数来寻找向量最小值
    - 函数为`function myArrayMax(arr) {return Math.min.apply(null, arr);}`
    - Math.min.apply([1, 2, 3])与Math.min(1, 2, 3)等价

### 日期
- toUTCString()
    - 将日期转换为UTC格式
- toDateString()
    - 将日期转换为易读的日期格式
- getTime()
    - 返回日期自1970年1月1日00:00:00以来的毫秒数
- getFullYear() | getUTCFullYear() | setFullYear()
    - 返回或设置4个数字的年份
- getMonth() | getUTCMonth() | setMonth()
    - 返回或设置月份数，但返回或设置数值的取值范围为[0,11]，因此，正确的月份必须加1
- getDate() | getUTCDate() | setDate()
    - 返回或设置当日数值，取值范围为[1,31]
- getHours() | getUTCHours() | setHours()
    - 返回或设置小时数，取值范围为[0,23]
- getMinutes() | getUTCMinutes() | setMinutes()
    - 返回或设置分钟数，取值范围为[0,59]
- getSeconds() | getUTCSeconds() | setSeconds()
    - 返回或设置秒数，取值范围为[0,59]
- getMillisecondes() | getUTCMillisecondes() | setMillisecondes()
    - 返回或设置毫秒数，取值范围为[0,999]
- getDay() | getUTCDay() | setDay()
    - 返回或设置星期数，取值范围为[0,6]
    - 在JavaScript中，每个星期的第1天是星期日，而不是星期一，意味着week(0)表示星期日

### 数学
- <mark>数学对象不同于其他全局对象，它不需要构建，方法和属性（常数）也是固定的，并且不要事先创建对象</mark>
- 常数
    - Math.E，返回$e$
    - Math.PI，返回$\pi$值
    - Math.SQRT2，返回$\sqrt{2}$
    - Math.SQRT1_2，返回$\sqrt{\frac{1}{2}}$
    - Math.LN2，返回$ln2$
    - Math.LN10，返回$ln10$
    - Math.LOG2E，返回$log_2e$
    - Math.LOG10E，返回$log_{10}e$
- 方法
    - Math.round(x)，四舍五入
    - Math.pow(x, y)，表示指数$x^y$
    - Math.sqrt(x)，表示开根号$\sqrt{x}$
    - Math.abs(x)，表示绝对值$|x|$
    - Math.ceil(x)，表示向上四舍五入到最近的整数
    - Math.floor(x)，表示向下四舍五入到最近的整数
    - Math.sin(x)，表示$sin(x)$
    - Math.cos(x)，表示$cos(x)$
    - Math.min(x, y, z……)，表示列表的最小值
    - Math.max(x, y, z……)，表示列表的最大值
    - Math.random()，表示[0,1]的随机数
- 布尔（Boolean）
    - 调用方式：`Boolean(CompareExpression)`、`(CompareExpression)`或者`CompareExpression`
    - 字符串、数值、表达式都为true
    - 0、-0、空字符串、undefined、null、false、NaN都为false
    - 可以使用new创建布尔对象，但不推荐，因为这种做法将代码复杂化，同时导致不可预期的错误，例如，使用`==`和`===`时，可能出现不一样的结果
    - 与布尔有关的参考资料见[JavaScript Boolean Reference](https://www.w3schools.com/jsref/jsref_obj_boolean.asp)
- 条件赋值
    - 调用方式：`variablename = (condition) ? value1:value2`，如`var voteable = (age < 18) ? "Too young":"Old enough";`表示当age小于18时，voteable变量赋值Too young，否则赋值Old enough
- 有关数学对象的参考资料见[JavaScript Math Reference](https://www.w3schools.com/jsref/jsref_obj_math.asp)

## 语句
- if-else
    - if，在条件为真时，执行后续代码块
    - else，与if相同的条件为假时，执行后续代码块
    - else if，如果第1个条件为假，指定另1个待检查的条件

```javascript
// if-else语法格式
if (condition1) {
    block of code to be executed if condition1 is true
} else if (condition2) {
    block of code to be executed if the condition1 is false and condition2 is true
} else {
    block of code to be executed if the condition1 is false and condition2 is false
}
```

- switch，指定多个可切换的、待执行的代码块
    - break关键词。如果JavaScript遇到break关键词，则跳出switch块
    - default关键词。在没有任何条件匹配的情况下指定的默认执行代码，它不是必须放置在最后1个情况中，如果不放在最后1个情况中，则最好添加break关键词
    - 如果希望2个或2个以上的情况执行同一个代码块，只需要将情况罗列即可，如switch语法格式中的case n1和case n2
    - 情况选择规则
        - 如果匹配多个情况，选择第1个匹配的
        - 如果没有任何情况可匹配，执行default
        - 如果没有default，则执行switch后的代码
    - switch使用严格比较，即使用`===`进行比较

```javascript
// switch语法格式
switch(expression) {
    case n:
        code block
        break;
    case n:
        code block
        break;
    case n1:
    case n2:
        code block
        break;
    default:
        code block
} 
```

- 循环
    - for循环，对代码块执行循环
        - statement 1在执行代码块前执行1次，即初始化循环，可已有多个值，用`,`作为分隔符，可忽略内容，但不能忽略内容后的`;`
        - statement 2定义执行代码块的条件或表达式，为真时继续执行，否则跳出循环，也可忽略，但必须在循环中加入break关键词，否则循环将无法停止
        - statement 3每次执行代码块后执行的代码，亦可忽略
    - for/in循环，针对对象的属性执行循环
    - while，当特定条件为真时执行循环，先判断条件再执行，因此，代码块可能1次也不会执行
    - do/while，当特定条件为真时执行循环，先执行再判断条件，因此，代码块至少被执行1次
    - 其他
        - 当忽略for循环的第1和第3个语句时，for循环等同于while循环
        - break关键词用于跳出整个循环
        - continue关键词用于跳过某个特定的条件，但继续循环

```javascript
// for循环语法格式
for (statement 1; statement 2; statement 3) {
    code block to be executed
}
// for/in循环示例
var person = {fname:"John", lname:"Doe", age:25};
var text = "";
var x;
for (x in person) {
    text += person[x] + " ";
} 

// while循环语法格式
while (condition) {
    code block to be executed
}

// Do/While循环语法格式
do {
    code block to be executed
}
while (condition);
```

- 标记（labels）
    - 使用`label: statements`设定标记
    - break和continue是JavaScript语句中唯一可以跳出代码块的语句
    - continue语句只能用于跳出循环中的某个特定条件
    - 如果不设定label，break关键词只能用于跳出循环或switch
    - 如果设定label，break能用于跳出代码块，这里的代码块指的是`{`和`}`包裹的代码块

```javascript
// 设定label，并使用break跳出代码块
var cars = ["BMW", "Volvo", "Saab", "Ford"];
list: {
    text += cars[0] + "<br>";
    text += cars[1] + "<br>";
    text += cars[2] + "<br>";
    break list;
    text += cars[3] + "<br>";
    text += cars[4] + "<br>";
    text += cars[5] + "<br>";
} 
```

## 正则表达式
正则表达式是形成搜索格式的字符序列，其中，搜索格式能够被用于搜索和替换文本操作
- 修饰符
    - i，不区分大小写进行匹配
    - g，全局匹配
    - m，多行匹配
- 方括号
    - [abc]，方括号内的任意字符
    - \[^abc\]，不属于方括号内的任意字符
    - [0-9]，方括号内字符之间的任意字符
    - \[^0-9\]，不在方括号内字符之间的任意字符
    - (x|y)，任意指定字符
- 元字符（metacharacter）
    - `.`，除了新行或其他行结束符以外的单个字符
    - \w，单词字符，包括a-z、A-Z、0-9以及下划线
    - \W，非单词字符
    - \d，数字
    - \D，非数字
    - \s，空白符
        - 空格
        - tab
        - 回车
        - 新行
        - 垂直tab
        - 换页
    - \S，非空白符
    - \b，从字的开头或结尾
    - \B，不从字的开头或结尾
    - \0，NUL
    - \n，新行
    - \f，换页
    - \r，回车
    - \t，tab
    - \v，垂直tab
    - \xxx，8进制数
    - \xdd，16进制数
    - \uxxxx，用16进制数xxxx表示的Unicode字符
- 量词
    - n+，至少有1个n
    - n*，0或多个n
    - n?，0或1个n
    - n{number}，number个n
    - n{number1,number2}，number1和number2个n
    - n{number,}，至少number个n
    - n$，以n结尾
    - ^n，以n开头
    - ?=n，紧跟n的字符
    - ?!n，不紧跟n的字符
- RegExp对象属性
    - constructor，返回创建RegExp的原型
    - global，检查是否设定g修饰符
    - ignoreCase，检查是否设定i修饰符
    - lastIndex，指定开始下一次匹配的索引
    - multiline，检查是否设定n修饰符
    - source，返回RegExp格式的文本
- RegExp对象方法
    - compile()，编译正则表达式，在version 1.5中已弃用
    - exec()，测试字符匹配，返回第1个匹配的结果
    - test()，测试字符匹配，返回true或false
    - toString()，返回正则表达式

## 错误处理
- 错误调试语法
    - try，测试代码块是否有错误
    - catch，处理错误
    - throw，创建自定义错误提示信息
    - finally，完成try和catch后，不论结果仍执行的代码

```javascript
// try-catch-finally的语法规则
try {
    Block of code to try
}
catch(err) {
    Block of code to handle errors
}
finally {
    Block of code to be executed regardless of the try / catch result
}

// try-throw-catch-finally示例
try {
    if(x == "") throw "empty";
    if(isNaN(x)) throw "not a number";
    x = Number(x);
    if(x < 5) throw "too low";
    if(x > 10) throw "too high";
}
catch(err) {
    message.innerHTML = "Input is " + err + ".";
}
finally {
    document.getElementById("demo").value = "";
}
```

- 错误对象与类型
    - 错误对象包含2个有用的属性：名称（name）和信息（message）
    - 错误类型
        - EvalError，eval()函数发生的错误，新版的JavaScript中已不再使用EvalError，而是使用SyntaxError代替
        - RangeError，数值不在范围内
        - ReferenceError，非法参考或关联，即使用变量前未声明
        - SyntaxError，语法错误
        - TypeError，类型错误
        - URIError，encodeURI()错误，即在URI函数中使用非法字符
    - 非标准错误对象属性（不要在公共网站上使用）
        - fileName（Mozilla）
        - lineNumber（Mozilla）
        - columnNumber（Mozilla）
        - stack（Mozilla）
        - description（Microsoft）
        - number（Microsoft）
- 调试
    - 在程序代码中测试、寻找或减少bugs（错误）称为代码调试（debugging）
    - 所有的现代浏览器都内建了JavaScript调试器
        - 作用是将错误类型报告给使用者
        - 既可开启，也可关闭
        - 可设置断点（breakpoints），即代码停止执行的位置
        - 按F12激活调试器，然后在调试器选项中选择控制台（console）
    - console.log(value)，向控制台写信息，可在浏览器调试器的控制台中查看结果
    - debugger关键词，正常情况下无效，在debugging时，相当于设置了断点

## 其他
- 吊装（hoisting）是指JavaScript默认将声明移到当前脚本或函数顶端的行为
    - 变量声明被吊装，也就是说，变量只要在JavaScript代码中声明即可使用，而不是必须在顶部声明
    - 吊装的只是声明，而不是初始化，也就是说，赋值不会被吊装
    - 为避免出现bugs，应当在当前范围开始处声明所有变量
- strict mode
    - 通过在JavaScript脚本内使用`"use strict";`来定义strict mode，主要目的是尽可能避免错误，<mark>"use strict";仅在脚本或函数的开头能够被识别</mark>
    - 自JavaScript 1.8.5（ECMAScript version 5）开始启用，早期版本自动忽略该文本表达式（literal expression）
    - 既可在整个脚本中使用，也可在定义函数时使用
    - 限制
        - 不允许使用未声明的变量、对象（从上至下依次读取脚本内容）
        - 不允许删除变量
        - 不允许删除函数
        - 不允许重复的参数名称
        - 不允许8进制文字
        - 不允许跳出8进制字符
        - 不允许写入只读属性
        - 不允许写入仅获取（get-only）属性
        - 不允许删除不可删除的属性
        - 不允许将eval作为变量
        - 不允许将arguments作为变量
        - 不允许使用with语句
        - 不允许使用eval()创建变量
        - 不允许使用保留关键词作为变量名称
        - 不允许默认捆绑（default binding）
- 保留名称
    - implements
    - interface
    - let
    - package
    - private
    - protected
    - public
    - static
    - yield
- 代码惯例
    - 编程规范
        - 在脚本和函数开始时，声明所有变量
        - 初始化变量
        - 所有识别码名称（变量和函数）都使用camelCase命名，且都以字母开始
        - 操作符两端以及逗号后都要使用空格
        - 使用4个空格缩进
        - 使用`===`进行比较
        - 设置默认值
        - 使用分号结束简单语句和对象定义
        - 将开始括号放在第1行的行末
        - 在开始括号前使用1个空格
        - 将关闭括号放在1个新行，之前不要使用空格
        - 不在复杂语句的结尾处使用分号
        - 将开始括号与对象名称放在同一行
        - 在每一个属性和它的值后使用逗号并加上1个空格
        - 字符串值使用引号，数值不使用引号
        - 不在最后1个“属性-值”对后加逗号
        - 避免1行超过80个字符，在操作符或逗号处断行
        - 有些服务器大小写敏感，而有些不敏感，为避免不同服务器间出现冲突，文件名均使用小写字母
        - 避免使用全局变量
        - 避免使用new
        - 避免使用`==`
        - 避免使用eval()
        - 避免打断return语句
    - 加速代码运行
        - 减少循环内的行动，在循环之外声明变量并为变量分配值，可加快循环速度
        - 减少HTML DOM的使用，如果必须使用，则使用本地变量
        - 避免不必要的变量
        - 延迟JavaScript的加载，将脚本放置在页面底部，让页面先行加载，或者在script标签内使用`defer="true"`
        - 避免使用with
    - JavaScript命名规则
        - 变量和函数使用camelCase（C语言通常使用PascalCase）
        - 全局变量使用UPPERCASE
        - 常量使用UPPERCASE
        - 不使用短横线和下划线（短横线通常在HTML和CSS中使用，下划线通常在PHP中使用）
        - 不使用`$`作为任何名称的开头，避免与JavaScript库名称产生冲突
- 常见错误见[JavaScript Common Mistakes](https://www.w3schools.com/js/js_mistakes.asp)
- 保留词见[JavaScript Reserved Words](https://www.w3schools.com/js/js_reserved.asp)
- JavaScript的版本见[JavaScript Versions](https://www.w3schools.com/js/js_versions.asp)

# JS HTML DOM
## 概要
- DOM定义了
    - HTML元素为对象
    - 所有HTML元素的属性和事件
    - 方法可通过所有的HTML元素
- 功能
    - 修改页面中所有的HTML元素和属性
    - 移除已存在的HTML元素和属性
    - 增加新的HTML元素和属性
    - 修改页面中所有的CSS样式
    - 对页面中所有已存在的HTML事件重新反应
    - 在页面中创建新的HTML事件
- 程序接口
    - 每个对象的属性，获取或设置的值
    - 每个对象的方法，能做的动作
- 名称说明
    - IdName，ID名称
    - TagName，tag名称
    - ClassName，类名称
    - attribute，属性
    - value，值
    - element，元素
    - strings，字符串或文本
    - function，函数
    - milliseconds，毫秒

## 对象
- document
    - document对象代表整个网页，也是寻找元素、属性、样式、事件的起点
- HTMLCollection
    - HTMLCollection对象是一系列HTML元素的类似向量列表（array-like list），可以使用索引号、id或名称调用该列表中的值，也可以用使用length属性获取列表长度
    - 无法获取属性（attribute）节点和文本节点
    - <mark>该列表不是向量，不可以使用向量方法</mark>
- NodeList
    - NodeList对象是一个HTML文件中所有节点的列表，与HTMLCollection对象类似，但只可以使用索引号调用列表中的值
    - 可获取属性（attribute）节点和文本节点
    - 一些旧版的浏览器返回NodeList对象代替HTMLCollection对象，比如getElementByClassName()方法
    - 所有的浏览器为childNodes返回NodeList对象
    - 大部分浏览器为querySelectorAll()方法返回NodeList对象
- 

## 属性
- innerHTML，获取或替换HTML元素内容，element.innerHTML = new html content
- attribute，获取或替换HTML元素的属性值，element.attribute = new value
- style.property，获取或修改HTML元素的样式，element.style.property = new style，其中，style为固定字符，有关property的列表可见<a href="JS_ref/JavaScript_html_dom_obj_style.html" target="_blank">自制HTML DOM Style Object列表</a>或者[官网HTML DOM Style Object列表](https://www.w3schools.com/jsref/dom_obj_style.asp)
- anchors，返回所有拥有名称属性的\<a\>元素
- baseURI，返回HTML文件的绝对基础URI
- body，返回\<body\>元素
- cookie，返回HTML文件的cookie
- doctype，返回HTML文件的doctype
- documentElement，返回\<html\>元素
- documentMode，返回浏览器使用的模式
- documentURI，返回HTML文件的URI
- domain，返回HTML文件服务器的域名
- embeds，返回\<embed\>元素
- forms，返回\<form\>元素
- head，返回\<head\>元素
- images，返回\<img\>元素
- implementation，返回DOM的履行
- inputEncoding，返回HTML文件的字符集
- lastModified，返回HTML文件更新的日期和时间
- links，返回所有拥有href属性的\<area\>和\<a\>元素
- readyState，返回HTML文件的加载状态
- referrer，返回关联HTML文件的URI
- scripts，返回所有\<script\>元素
- strictErrorChecking，如果强制执行错误检查则返回
- tilte，返回\<title\>元素
- URL，返回HTML文件完整的URL

## 方法
- getElementById("IdName")，依据ID寻找元素
- getElementsByTagName("TagName")，依据HTML标签名称寻找元素，返回HTMLCollection对象
- getElementsByClassName("ClassName")，依据类名称寻找元素
- querySelectorAll(value)，寻找符合条件的所有CSS选项，返回NodeList对象
- setAttribute(attribute, value)，获取或修改HTML元素的属性值
- createElement(element)，创建新的元素节点
- createTextNode("strings")，创建新的文本节点
- removeChild(element)，移除子节点，但必须知道子节点的父节点是什么，也就是说，只有在知道父节点的情况下才有可能删除子节点
- appendChild(element)，增加子节点
- replaceChild(element)，替换子节点
- insertBefore(element,child|parent)，在element节点前插入子节点或父节点
- write(text)，写入HTML输出流
- addEventListener("event", function[, useCapture])，依据事件类型执行函数，其中，事件类型不需要事件前缀，比如onclick中的on；useCapture只有true和false两个值，true表示capturing、false表示bubbing，主要功能是，当存在多个HTML元素嵌套并都设定了事件及其行动时，capturing从外向里执行，而bubbing则从里向外执行
- removeEventListener("event", function)，移除添加的EventListener

## 事件
- 事件例子
    - 点击鼠标
    - 页面已加载
    - 图片已加载
    - 鼠标移动至HTML元素
    - 输入区域改变
    - HTML表单提交
    - 敲击键盘上的按键
- 分配事件
    - 使用事件属性（attributes）为HTML元素分配事件，如` <button onclick="displayDate()">Try it</button>`
    - 基于HTML DOM使用JavaScript为HTML元素分配事件，如`<script>document.getElementById("myBtn").onclick = displayDate;</script>`
- 事件类型
    - 根对象
    - 动画
    - 剪切板
    - 拖动
    - 聚焦
    - Hash变动
    - 输入
    - 键盘
    - 鼠标
    - 页面过渡
    - 窗口历史
    - 进程
    - 存储
    - 触碰
    - CSS过渡
    - 用户交互
    - 鼠标滚轮
- 有关事件及其对象与方法的详细内容可见<a href="JS_ref/JavaScript_html_dom_event_property_method.html" target="_blank">自制HTML DOM Events列表</a>或者[官方HTML DOM Events列表](https://www.w3schools.com/jsref/dom_obj_event.asp)

## 节点
根据W3C HTML DOM标准，在HTML文件中的任何东西都是节点，使用HTML DOM可以循着节点树使用节点关系，节点树上所有的节点都对JavaScript开放，并且可以创建、修改和删除节点
- 节点类型
    - 整个文件是文件节点
    - 每一个HTML元素是元素节点
    - HTML元素内点文本是本文节点
    - 所有的注释是注释节点
- 节点关系
    - 节点树上的节点之间按照层级关系架构
    - 根（root）、父（parent）、子（child）、姊妹（sibling）用于描述节点之间的关系
        - 最顶端的节点称为根节点
        - 除根节点外，每一个节点都有父节点
        - 任意节点可以有多个子节点
        - 姊妹节点是拥有相同父节点的节点
- 节点属性
    - 2个根节点属性
        - document.body，HTML文件的body部分
        - document.documentElement，html标签内的内容
    - parentNode
    - childNodes[nodenumber]
        - innerHTML等价于childNodes[n].nodevalue，都返回节点的内容
    - firstChild
    - lastChild
    - nextSibling
    - previousSibling
    - nodeName，指代节点的名称
        - 节点名称为只读
        - 元素节点的节点名称与标签相同，并且总是大写
        - 属性（attribute）节点的节点名称为属性名称
        - 文本节点的节点名称为`#text`
        - 文件节点的节点名称为`#document`
    - nodeValue，指代节点的值
        - 元素节点的节点值为undefined
        - 文本节点的节点值为文本自身
        - 属性（attribute）节点的节点值为属性值
    - nodeType
        - 节点类型为只读
        - 列表见下

| 节点 | 类型 | 例子 |
| --- | --- | --- |
| ELEMENT_NODE | 1 | &lt;h1 class="heading"&gt;W3Schools&lt;/h1&gt; |
| ATTRIBUTE_NODE | 2 | class = "heading"（已淘汰） |
| TEXT_NODE | 3 | W3Schools |
| COMMENT_NODE | 8 | &lt;!-- 注释 --&gt; |
| DOCUMENT_NODE | 9 | HTML文件 |
| DOCUMENT_TYPE_NODE | 10 | &lt;!Doctype html&gt; |

# JS浏览器BOM
BOM是Browser Object Model的首字母简称，中文翻译为浏览器对象模型，允许JavaScript与浏览器对话，拥有属性和方法，但没有官方标准
## 对象
- window
    - 代表浏览器窗口，被所有浏览器支持
    - 所有JavaScript的全局对象、函数和变量自动成为window对象的成员
    - 全局变量是window对象的属性，甚至HTML DOM的document对象也是window对象的属性
    - 全局函数是window对象的方法
- window之下的对象
    - screen，可以不带window前缀直接调用，即window.screen.width与screen.width等价
    - location，可以不带window前缀直接调用
    - history，可以不带window前缀直接调用
    - navigator，可以不带window前缀直接调用
- cookie
    - 当服务器给浏览器发送完页面后，连接中断，服务器无法获取任何用户信息，cookies通过本地小型文本存储数据，解决如何记录用户信息的问题
    - 使用document.cookie属性创建、读取、删除cookies

## 属性和方法
- window
    - innerHeight，返回浏览器窗口的高，用px表示
    - innerWidth，返回浏览器窗口的宽，用px表示
    - open()，打开1个新的窗口
    - close()，关闭当前窗口
    - moveTo()，移动当前窗口
    - resizeTo()，调整当前窗口大小
    - alert("text")，弹出带文本的警告窗口
    - confirm("text")，弹出需要用户确定或取消的窗口
    - prompt("text1","text2")，弹出需要用户确定或取消的窗口，text1表示提示信息，text2表示默认信息
    - setTimeout(function,milliseconds)，等待一段特定的时长后执行函数，仅执行1次
    - setInterval(function,milliseconds)，每间隔milliseconds执行1次函数
    - clearTimeout(variable)，如果setTimeout()方法中的函数尚未执行，可终止执行，其中的variable为setTimeout()方法赋值的变量
    - clearInterval(variable)，终止setInterval()方法的执行，其中的variable为setInterval()方法赋值的变量
- screen
    - width，浏览器屏幕宽度
    - height，浏览器屏幕高度
    - availWidth，浏览器可用屏幕宽度
    - availHeight，浏览器可用屏幕高度
    - colorDepth，用于表示1种颜色所使用的位数（bits）
        - 最旧的电脑或手机使用8位，表示256种VGA Colors
        - 稍旧的电脑使用16位，表示65,536种High Colors
        - 现代电脑使用24位或32位硬件作为颜色解决方案，24位表示16,777,216种True Colors；32位表示4,294,967,296种Deep Colors，RGB和十六进制的颜色表示方式就是24位的解决方案
    - pixelDepth，与colorDepth相同
- location
    - href，返回当前页面的URL
    - hostname，返回网页主机的域名
    - pathname，返回当前页面的路径和文件名
    - protocol，返回页面使用的web协议，如http:或https:
    - port，返回页面网络端口，如果为80（http）或443（https）的默认端口，通常返回0或不返回任何内容
    - assign("URL")，加载1个新的文件
- history（为保护用户隐私，JavaScript在获取历史对象时存在限制）
    - back()，与在浏览器中按下后退键的效果相同
    - forward()，与在浏览器中按下前进键的效果相同
- navigator（不要依赖通过navigator返回的浏览器相关信息）
    - cookieEnabled，返回cookies是否可用，可用为true，否则为false
    - appName，返回浏览器的应用名称，Netscape是IE11、Chrome、Firefox和Safari的应用名称
    - appCodeName，返回浏览器的应用代码名称，Mozilla是Chrome、Firefox、IE、Safari和Opera的应用代码名称
    - product，返回浏览器引擎的产品名称，Gecko是大多数浏览器的产品名称
    - appVersion，返回浏览器的版本信息
    - userAgent，返回用户端通过浏览器发送给服务器的头信息（header）
    - platform，返回浏览器平台，即操作系统
    - language，返回浏览器语言
    - onLine，如果浏览器在线，返回true
    - javaEnabled()，如果Java开启，返回true

# JS AJAX
## 概述
- AJAX
    - 不是程序语言
    - 是一种从网页读写网页服务器的技术，联合使用了以下2种功能
        - 浏览器内建的XMLHttpRequest对象（用于从服务器请求数据，也是AJAX的基石）
        - JavaScript以及HTML DOM（用于展示或使用数据）
    - 代表JavaScript和XML异步（Asynchronous JavaScript And XML）
    - 涉及与服务器端的信息交换，因而需要学习SQL、Python、Node.JS、ASP、PHP等服务器端语言，以及XML、JSON等数据存储规范
- AJAX的功能
    - 页面完成加载后从服务器读取数据
    - 更新网页而不需要重新加载页面
    - 在后台向服务器发送数据
- AJAX工作机制
    - 网页发生1个事件
    - JavaScript创建1个XMLHttpRequest对象
    - XMLHttpRequest对象发送请求给服务器
    - 服务器处理请求
    - 服务器发送反馈给网页
    - 通过JavaScript读取服务器反馈
    - 通过JavaScript执行合适的行动

## XMLHttpRequest对象
- 概念
    - XMLHttpRequest对象是AJAX的基石
    - XMLHttpRequest对象被所有现代浏览器支持
    - 因安全原因，浏览器不允许通过域名交换数据，也就是说，网页和XML文件必须在同一个服务器上才可以交换数据
    - 回调函数（callback function）是将1个函数作为另1个函数参数的函数
        - 必须包含URL和作为参数的函数，其中，URL为调用open方法时的URL
        - 当在网站上有多个AJAX任务时，应该创建1个执行XMLHttpRequest对象的函数，以及1个回调函数执行每1个AJAX任务
        - 在函数中设置函数参数时，可用this指代函数本身
- 方法
    - new XMLHttpRequest()，创建XMLHttpRequest对象
    - abort()，取消当前请求
    - getAllResponseHeaders()，返回头信息
    - getResponseHeader()，返回特定头信息
    - open(method,url,async,user,psw)，特定请求
        - method，请求类型，GET或者POST，<mark>GET比POST更简单和快速，大多数情况下使用GET，但在更新服务器上的文件或数据库、发送大量数据至服务器（POST无大小限制）、发送用户输入信息时，POST比GET更加稳健和安全</mark>
        - url，文件地址
        - async，异步或同步，true为异步、false为同步；异步的作用是，当向服务器发送请求是，JavaScript不需要等待服务器的反馈，可直接执行后续的脚本，而同步则表示必须在接收到服务器的反馈后才执行后续脚本
        - user，可选项，用户名
        - psw，可选项，密码
    - send()，发送请求给服务器，为GET请求使用
    - send("string")，发送请求给服务器，为POST请求使用
    - setRequestHeader(headerName,headerValue)，为将发送的头信息增加name/value对
- 属性
    - onreadystatechange，定义1个当readyState属性改变时被调用的函数
    - readyState，保持XMLHttpRequest的状态
        - 0：请求未被初始化
        - 1：服务器连接已建立
        - 2：收到请求
        - 3：正在处理请求
        - 4：请求处理结束，反馈已准备好
    - responseText，将反馈数据作为字符串返回
    - responseXML，将反馈数据作为XML数据返回
    - status，返回请求的状态数值
        - 200："OK"
        - 403:"Forbidden"
        - 404:"Not Found"
        - 完整的状态数值及其代表的信息可查阅[HTTP Status Messages](https://www.w3schools.com/tags/ref_httpmessages.asp)
    - statusText，返回请求的状态文本，如"OK"、"Not Found"

# JS JSON
JSON是JavaScript Object Notation的首字母简称，中文翻译为JavaScript对象表示，它既是一种存储和交换数据的语法，也是使用JavaScript对象表示方法书写的文本

## 概述
- JSON是什么
    - 代表JavaScript Object Notation
    - 轻量级的数据交换格式
    - 自描述（self-describing）且易理解
    - 语言独立，意味着任何程序语言都可以将JSON作为数据使用
    - 文件后缀为".json"
    - MIME类型为"application/json"
- 功能
    - 在浏览器和服务器之间交换的只能是文本数据，而JSON是文本
    - 可将任何JavaScript对象转换到JSON，然后将JSON发送给服务器
    - 也可将任何从服务器接收到的JSON转换为JavaScript对象
- 语法
    - JSON语法是JavaScript语法的子集
    - 数据是name/value对，用`:`作为分隔符
    - name/value对用`,`作为分隔符
    - 花括号定义对象，可嵌套，使用`.property`调用属性值，delete删除对象属性
    - 方括号定义向量，可嵌套，使用索引号调用向量值，delete删除向量值
- name/value
    - JSON的name需要双引号，而JavaScript的name不需要
    - JSON的value可以是字符串、数值、JSON对象、向量、布尔值、null，JavaScript的value除JSON的value外，还加上函数、日期、undefined
    - JSON的字符串值必须且只能是双引号，但JavaScript的既可以是双引号，也可以是单引号
- JSON与XML的异同
    - 相同点
        - 自描述
        - 有层级结构
        - 被解析，且能被大部分程序语言使用
        - XMLHttpRequest可拉取
    - 不同点
        - JSON不使用结束标签
        - JSON更简短
        - JSON能够更快速地被读写
        - JSON可使用向量
        - JSON可被1个标准的JavaScript函数解析，但XML必须通过XML解析器才能解析
    - 结论
        - XML比JSON更难解析
        - JSON被解析成可用的JavaScript对象
        - 对于AJAX应用，JSON比XML更快且更简单

## 应用
- JSON.parse(string)方法
    - 解析从服务器获取的字符串数据
- JSON.stringify(variable)方法
    - 将JavaScript对象转换成字符串
- PHP
    - 在客户端和服务端交换数据，需要学习服务端的PHP语言
- JSONP
    - JSONP是一种跨域名发送JSON数据的方法
    - 不使用XMLHttpRequest对象
    - 使用\<script\>标签，即以通过脚本与服务器交换数据的方式，替代通过XMLHttpRequest对象与服务器交换数据的方式

# 参考资料
- [W3School.com JavaScript Tutorial](https://www.w3schools.com/js/default.asp)
- [JavaScript and HTML DOM Reference](https://www.w3schools.com/jsref/default.asp)

# 版本记录
1. 2018年06月17日，v1.0.0

# 微博发布
- [ ] 概要
- [ ] JS
    - [ ] 概述
    - [ ] 对象属性
    - [ ] 对象方法
        - [ ] 字符
        - [ ] 数值
        - [ ] 向量
        - [ ] 日期
        - [ ] 数学
    - [ ] 语句
    - [ ] 正则表达式
    - [ ] 错误处理
    - [ ] 其他
- [ ] JS HTML DOM
    - [ ] 概要
    - [ ] 对象
    - [ ] 属性
    - [ ] 方法
    - [ ] 事件
    - [ ] 节点
- [ ] JS浏览器BOM
    - [ ] 对象
    - [ ] 属性和方法
- [ ] JS AJAX
    - [ ] 概述
    - [ ] XMLHttpRequest对象
- [ ] JS JSON
    - [ ] 概述
    - [ ] 应用
