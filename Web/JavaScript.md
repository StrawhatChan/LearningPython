> **本文“发表于微博自媒体”，微博：[@钻石草帽](https://weibo.com/strawhatchan)**

？计算机中的正负数二进制表示，扫盲：[负数的二进制表示方法](https://blog.csdn.net/diandianxiyu_geek/article/details/44098121)，用于理解按位运算

# 概要
**本文采用知识库的方式，记录JavaScript以下各方面内容：**
1. 

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

| 关键词      | 描述                                |
| ----------- | ----------------------------------- |
| break       | 结束switch或循环                    |
| continue    | 跳出循环重新开始循环                |
| debugger    | 停止执行JavaScript调用debugging功能 |
| do...while  | 当条件成立时一直循环语句块          |
| for         | 只要条件成立，则执行语句块          |
| function    | 声明1个函数                         |
| if...else   | 依据条件执行语句块                  |
| return      | 退出函数                            |
| switch      | 依据不同的情况决定是否执行语句块    |
| try...catch | 错误处理                            |
| var         | 声明变量                            |

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
        - 单词的首字母大写，FirstName
        - 后续单词的首字母大写，firstName
    - 字符集，JavaScript使用**Unicode**字符集，完整的Unicode字符集见[HTML Unicode (UTF-8) Reference](https://www.w3schools.com/charsets/ref_html_utf8.asp)，注意，**Unicode是字符集，UTF-8或者UTF-16是编码**
- 数据类型
    - 数值
    - 字符
    - 向量，使用`var varName = [ ];`定义，以`,`为分隔符
    - 对象，使用`var varName = {};`定义，按照name:value对的方式呈现，以`,`为分隔符，使用varName.name调用value
    - 函数，使用`function funName(){};`定义，以`,`为分隔符
    - 特殊类型
        - 未定义，undefined，这是1个特殊值，可赋给数值和字符类型的变量
        - 空值，null，这是1个特殊对象，可赋给对象类型的变量
        - null和undefined值相同，但类型不同，因此，`null == undefined`返回`true`，而`null === undefined`返回`false`


## 方法
- document.getElementById("idname")
    - 读写HTML中拥有特定id的元素
    - 可将innerHTML附后，写入HTML文件

# JS表单


# JS对象


# JS函数



# JS HTML DOM



# JS浏览器BOM


# JS AJAX


# JS JSON


# jQuery



# AngularJS






# 版本记录

# 微博发布

