> **本文“发表于微博自媒体”，微博：[@钻石草帽](https://weibo.com/strawhatchan)**

# 概要
**本文采用知识库的方式，记录HTML以下各方面内容：**
1. 相关概念
2. HTML文件的结构
3. HTML元素、属性（attributes）和属性（properties）

# 概念
- HTML是为创建网页设计的标准标记语言（standard markup language）
    - 代表超文本标记语言（Hyper Text Markup Language）
    - 使用标记描述网页结构
    - 以标签代表的元素构建了HTML页面的块
    - 使用简单的英文单词作为标签
    - 浏览器不显示这些标签，但通过这些标签解码（render）页面内容
- HTML5是HTML的第5次修改，截止到2018年05月28日仍在进行中，更多的含义是“很酷的页面”
- 简单HTML文件示例
    - `<!DOCTYPE html>`用于声明该文件是HTML5文件，帮助浏览器正确显示网页
        - 只能在文件顶部或者任何HTML标签之前出现1次
        - 对大小写不敏感
    - `<html>`表示1个HTML页面的根元素
    - `<head>`表示包含文件的元信息（meta information or metadata）
    - `<title>`定义文件的题目
    - `<body>`包含可见的网页内容
    - `<h1>`定义最大的标题
    - `<p>`定义1个段落

```html
<!DOCTYPE html>
<html>

<head>
    <title>Page Title</title>
</head>

<body>
    <h1>My First Heading</h1>
    <p>My first paragraph.</p>
</body>

</html> 
```

- HTML版本

| Version   | Year |
| --------- | ---- |
| HTML      | 1991 |
| HTML 2.0  | 1995 |
| HTML 3.2  | 1997 |
| HTML 4.01 | 1999 |
| XHTML     | 2000 |
| HTML5     | 2014 |

- 编码
    - HTML偏好`UTF-8`编码

# 元素
## 元素概述
- HTML元素
    - HTML元素指的是`<tagname> content</tagname>`中的所有内容，包含标签以及插入开始和结束标签中的内容
    - 没有引用任何内容的HTML元素成为空元素（empty elements），没有结束标签，例如用于指定断行的`<br>`元素，但空元素仍可以通过如`<br />`这样的开放标签（opening tag）关闭
    - HTML元素可以相互嵌套
    - 如果希望HTML文件可以被XML解析器读取，则所有的元素都必须是关闭的，包括空元素
- 标签设定方式
    - 元素`<tagname> content</tagname>`中的`<tagname>`为标签
    - 标签成对出现，包括开始标签和结束标签
    - 结束标签与开始标签的名称相同，但名称前有1个正斜杠（forward slash，/）
    - 标签对大小写不敏感，W3C推荐使用小写字母标签
- 网页浏览器
    - 浏览器的目的是读取HTML文件并展示其结构和内容
    - 浏览器不显示标签，但根据标签决定决定如何展示HTML文件
- 属性（attribute）
    - 所有的HTML元素都可以有属性
    - 属性为HTML元素（标签）提供附加信息
    - 属性通常在开始标签中
    - 属性通常使用`name=value`这样的“名称-值”对
    - W3C推荐使用小写字母属性，并将值置于双引号或者单引号中（优先使用双引号）
- 显示问题
    - 在大频幕、小频幕或者窗口变化大小的情况下，不能确定HTML的显示方式
    - 由于浏览器将自动移除额外的空格、空行等符号，因此，也不能通过添加这些符号改变HTML的显示方式

## 一般元素
- HTML文件
    - `<html>`标签定义整个HTML文件
- 元信息
    - `<head>`标签定义整个HTML文件的原信息，例如在`<head>`标签内使用`<title>`标签定义页面题目
    - 置于`<html>`和`<body>`之间
    - 原信息不显示
- 内容
    - `<body>`为内容标签，定义HTML文件的全部可见内容
    - 标题、段落、链接、图片、列表等都包含在其中
- 标题
    - HTML通过`<h1>到<h6>`定从最重要到最不重要的6个级别标题
    - `<h1>`定义重要的标题，`<h6>`定义最不重要的标题
    - 定义形式：`<h1>content</h1>`
    - 搜索引擎使用标题索引网页结构和内容
    - 不要使用标题变大或加粗文字
- 段落
    - 通过`<p>`标签定义
    - 定义形式：`<p>content</p>`
    - 浏览器自动在段落前后添加空白符
- 链接
    - 链接通过`<a>`标签下的`href`属性定义
    - 定义形式：`<a href="url" target="options" title="titlename">链接名称</a>`
    - `url`既可以是以当前文件所在目录为基准的内部文件链接，也可以是外部链接
    - `target`为可选项，包含`_blank`（在浏览器的新窗口或新标签打开）、`_top`（如果网页被锁定在一个框架内，该属性值可突破框架）
    - `title`为可选项，定义链接的题目
    - 链接颜色
        - 未访问链接为蓝色且有下划线
        - 已访问链接为紫色且有下划线
        - 活动链接为红色且有下划线
        - 可通过CSS文件修改定义的链接颜色

```css
<style>
a:link {
    color: green;
    background-color: transparent;
    text-decoration: none;
}

a:visited {
    color: pink;
    background-color: transparent;
    text-decoration: none;
}

a:hover {
    color: red;
    background-color: transparent;
    text-decoration: underline;
}

a:active {
    color: yellow;
    background-color: transparent;
    text-decoration: underline;
}
</style> 
```

- 按钮（button）
    - 按钮通过`<button>`标签定义
    - 定义形式：`<button>content</button>`
- 列表
    - 普通列表通过`<ul>`或`<ol>`标签并紧跟`<li>`标签定义
        - `<ul>`表示无序列表
        - `<ol>`表示有序列表
        - `<li>`表示列表中的项
    - 描述列表通过`<dl>`标签内嵌`<dt>`标签，以及`<dt>`标签内嵌`<dd>`标签定义
        - `<dl>`表示描述列表
        - `<dt>`表示被描述的列表项
        - `<dd>`表示描述信息
    - 所有列表元素都可以相互嵌套
    - 可通过CSS或`<style>`将列表设定为水平列表，控制的关键是`li {float: left | right;}`，即将列表内容浮动至左侧或者右侧，但不能浮动至中间；[HTML Lists](https://www.w3schools.com/html/html_lists.asp)Chapter Summary最后一句话中，认为使用`display:inline`也能实现水平列表，经在Ubuntu 18 LTS和VSCode 1.23.1下测试，**无法实现**

```html
<!-- 无序列表 -->
<ul>
    <li>list1</li>
    <li>list2</li>
    <li>list3</li>
</ul>
<!-- 有序列表 -->
<ol>
    <li>list1</li>
    <li>list2</li>
    <li>list3</li>
</ol>
<!-- 描述列表 -->
 <dl>
  <dt>Coffee</dt>
  <dd>- black hot drink</dd>
  <dt>Milk</dt>
  <dd>- white cold drink</dd>
</dl> 
```

- 预格式化
    - 通过`<pre>`标签定义，将保留空白符和断行标识符
- 注释
    - `<!-- 注释内容 -->`注释标识
- 图片地图（image Maps）
    - 图片地图是指为一张图片的不同区域分配不同的链接
    - 通过`<map>`元素设定
    - 通过`<img usemap="#mapname">`调用
- 图片
    - 通过`<picture>`标签定义，可更有弹性地设定图片来源
    - `<picture>`元素中内嵌`<source>`元素和`<img>`元素，其中，`<source>`元素指定不同的图片来源，而`<img>`元素通常放在所有`<source>`元素之后，以防浏览器不支持`<source>`元素时备用
    - `<picture>`元素读取`<source>`元素的机制是，从上到下读取，只要符合条件即选用该`<source>`元素中的图片，然后跳出`<picture>`元素
- 表格
    - 通过`<table>`标签定义表格，内嵌的元素包括表的标题、行、列、数据
        - `<caption>`标签定义表的标题，通常紧跟在`<table>`标签下一行
        - `<tr>`标签定义行
        - `<th>`标签定义表头
        - `<td>`标签定义数据
        - `<col>`标签在`<colgroup>`标签内的每一列设定样式
        - `<colgroup>`标签定义列的分组情况，并通过`<col>`标签为每一列设定样式
        - `<thead>`标签为表头设定分组
        - `<tbody>`标签为表头和表格末行设定分组
        - `<tfoot>`标签为表格末行设定分组
        - 分组标签可以简化对表格的操作，即不需要对每一行、每一列分别进行操作，而是可以对整个组进行操作，类似与`class`属性
    - 可在CSS文件中为表格定义样式，如`table, th, td {border: 1px solid black; border-collapse: collapse;border-spacing: 5px;}`、`th, td {padding: 15px;}`、`th {text-align: left;}`
    - 可通过`colspan="num"`属性设定数据占用列的数量
    - 可通过`rowspan="num"`属性设定数据占用行的数量

```html
<!-- 表格示例 -->
 <table style="width:100%">
  <tr>
    <th>Firstname</th>
    <th>Lastname</th>
    <th>Age</th>
  </tr>
  <tr>
    <td>Jill</td>
    <td>Smith</td>
    <td>50</td>
  </tr>
  <tr>
    <td>Eve</td>
    <td>Jackson</td>
    <td>94</td>
  </tr>
</table> 
```

## 格式化元素
格式化元素（formatting elements）给文本定义一些特殊的含义，调用方式与HTML的一般元素相同
- `<b>` 加粗
- `<strong>` 重要
- `<i>` 斜体
- `<em>` 焦点
- `<mark>` 黄色标记
- `<small>` 小文本
- `<del>` 删除
- `<ins>` 下划线（插入）
- `<sub>` 下角标
- `<sup>` 上角标
- `<q>` 引用
- `<blockquote>` 引用块
- `<abbr>` 简写
    - 调用方式：`<p>The <abbr title="World Health Organization">WHO</abbr> was founded in 1948.</p>`
- `<address>` 地址
    - 地址元素以斜体展示
    - 多数浏览器将在地址元素前后都加上断行符
- `<cite>` 引用作品的题目，以斜体展示
- `<bdo>` 将文字以反向顺序展示

## 空元素
- 断行符`<br>`
- 水平线`<hr>`
- 外部链接CSS文件的`<link>`，调用方式是`<link rel="stylesheet" href="styles.css">`
- 图片引用`<img>`
    - 图片通过`<img>`标签下的`src`、`alt`、`width`以及`height`等属性定义
    - 定义形式：`<img src="w3schools.jpg" alt="W3Schools.com" width="500" height="600">`或者`<img src="w3schools.jpg" alt="W3Schools.com" style="width:500px;height:600px;">`
    - W3C推荐使用`style`属性，而不是将`width`和`height`分离的属性，因为，使用`style`属性可避免被`stylesheet`替代而达不到设定预期，可查阅[示例](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_images_style)
    - HTML支持GIFs图片，即动态图片
- 图片地图`<area>`
    - `<area>`内嵌于`<map>`元素中，用于分配图片区域及其对应的链接
    - 调用方式：`<area shape="shapename" coords="num1,num2,num3,num4" alt="text" href="url">`
- 图片源`<source>`
    - `<source>`内嵌于`<picture>`元素中
    - 调用方式：`<source media="(min-width: 650px)" srcset="imgname.jpg">`

# 属性
## 属性概述
- attributes与properties的概念
    - 属性（attributes）是在开始标签内为元素提供附加信息的“名称-值”对，即`<tagname attributename="attributevalue">content</tagname>`中的“name-value”对，属性列表见[HTML Attribute Reference](https://www.w3schools.com/tags/ref_attributes.asp)
    - 属性之下还有属性（properties），即`<tagname attributename="propertyname:propertyvalue;">content</tagname>`
- attributes与properties的异同
    - 调用方式。attributes使用`attributename="attributevalue"`这样的方式调用，properties使用`propertyname:propertyvalue;`这样的方式调用
    - 分隔符。attributes属性之间使用空格作为分隔符，properties属性之间使用分号作为分隔符
- 后续行文安排
    - 以attributes属性为主
    - 如果attributes属性下还有properties属性，则直接在attributes属性下列明

## 属性类型
- href
    - 通常在`<a>`链接标签中
    - 调用方式：`<a href="HyperLink">`
- src
    - 通常在`<img>`图片标签中，用于定义URL
    - 调用方式：`<img src="imgURL">`，其中，`imgURL`为图片路径（必须包含文件后缀）
- width
    - 通常在`<img>`图片标签的`src`属性之后，用于表示宽度
    - 调用方式： `<img src="img_girl.jpg" width="500">`
    - 单位：像素（pixels/px）
- height
    - 通常在`<img>`图片标签的`src`属性之后，用于表示高度
    - 调用方式： `<img src="img_girl.jpg" height="600">`
    - 单位：像素
- alt
    - 通常在`<img>`图片标签的`src`属性之后，作为找不到文件时替换图片的文本内容
    - 调用方式：`<img src="img_girl.jpg" alt="文本内容">`
- style
    - 用于指定HTML元素的颜色、字体、大小等
    - 调用方式：`<p style="font-size:60px;color:red">content</p>`
    - `style`主要通过CSS定义，该属性下还可以设置属性（properties），一般方式为`<tagname style="propertyname:propertyvalue;">`
    - HTML调用CSS的3种方式
        - 行内。在HTML元素中使用`style`属性
        - 内部。在`<head>`部分使用`<style>`元素
        - 外部。使用外部的CSS文件
    - style下的属性
        - font-family：字体类型，调用方式：`font-family: fontname`
        - font-size：字体大小，既可以使用像素单位，也可以使用百分比单位，调用方式：`font-size: 12px`
        - color：字体颜色，调用方式：`color: colorname`
        - backgroud-color：在`<body>`标签中定义背景颜色，调用方式：`background-color: colorname`
        - text-align：字体对齐方式，调用方式：`text-align: left | right | center`
        - border：边框，调用方式：`border:2px solid Tomato`
        - padding：`border`内部的空间属性，调用方式：`border: 12px`
        - margin：`border`外部的空间属性，调用方式：`margin: 12px`
        - float：悬浮位置，调用方式：`float: left | right | center`
        - background-image：背景图片，调用方式：`background-image:url('clouds.jpg')；`
        - list-style-type：无序列表定义列表符号，调用方式：`<ul style="list-style-type:disc | circle | square | none">`
        - type：有序列表定义列表符号，调用方式：`<ol type="1 | A | a | I | i">`

```html
<!-- HTML内部调用CSS -->
<head>
<style>
body{background-color: powderblue;
}
h1{color: blue;
}
p{  color: red;
    border: 1px solid powderblue;
    padding: 30px;
    font-family: courier;
    font-size: 160%;
    margin: 50px;
}
</style>
</head>
<!-- HTML外部调用CSS文件 -->
<head>
  <link rel="stylesheet" href="styles.css">
</head>
<!-- 为id属性定义样式 -->
<p id="p01">content</p>
#p01 {
    color: blue;
}
```

- lang
    - 通常在`<html>`标签中
    - 调用方式：`<html lang="zh-han">`
- title
    - 显示当鼠标停留于HTML元素上时显示的额外内容
    - 调用方式：`<p title="文本内容">content</p>`
- disabled
    - 将输入元素定义为无效
- id
    - 为HTML元素指定唯一的ID
    - 可通过id属性创建书签
    - 可通过id属性为该拥有该id的表格设定样式

```html
<!-- 为创建标签设定id -->
<h2 id="C4">content</h2>
<!-- 当前页面跳转 -->
<a href="#C4">跳转到C4</a>
<!-- 其他页面跳转 -->
<a href="htmlname.html#C4">跳转到C4</a>
```

```html
<!-- 为特定表格设定样式创建id -->
<table id="t01">
</table>
<!-- 在CSS文档中或者<style>元素内为t01表格设定样式 -->
<style>
table#t01 {
    width: 100%;
    background-color: #f1f1c1;
}
table#t01 tr:nth-child(even) {
    background-color: #eee;
}
table#t01 tr:nth-child(odd) {
    background-color: #fff;
}
table#t01 th {
    color: white;
    background-color: black;
}
</style>
```

- class
    - 为特定类型元素定义一种样式
    - 可理解为通过`class`定义了一类HTML元素，并使用`tagname.classname`的方式定义该类型元素的样式

```html
<p class="error">content</p>
p.error {
    color: red;
}
```

- name
    - 隶属于`<map>`元素，定义map的名称
    - 调用方式：`<map name="mapname">`
- shape
    - 隶属于`<area>`元素，定义图片地图的区域形状
    - 调用方式：`shape="shapename"`
- coords
    - 隶属于`<area>`元素，定义图片地图的坐标
    - 调用方式：`coords="num1,num2,num3,num4"`
- media
    - 隶属于`<source>`元素，用于定义使用图片源的条件
    - 调用方式：`media="(min-width: 650px)"`
    - media下的属性
        - min-width，设定最小图片宽度
- srcset
    - 隶属于`<source>`元素，用于设定图片源的URL
    - 调用方式：`srcset="imgurl"`
- start
    - 隶属于`<ol>`元素，用于设定有序列表的起始计数点
    - 调用方式：`<ol start="50">`

## 属性值
- 颜色
    - 隶属于`color`、`backgroud-color`和`border`等属性
    - 颜色可以用RGB、HEX、HSL、RGBA和HSLA等不同类型的表示方式
        - RGB的格式为`rgb(red, green, blue)`，其中，`red`、`green`和`blue`的取值范围均为[0,255]
        - HEX的格式为`#rrggbb`，其中，`rr`、`gg`和`bb`的取值为[0,255]的十六进制数值
        - HSL的格式为`hsl(hue, saturation, lightness)`，其中，`hue`的取值范围为[0,360]，`saturation`的取值范围为[0%, 100%]，`Lightness`的取值范围为[0%, 100%]
        - RGBA的格式为`rgba(red, green, blue, alpha)`，其中，`alpha`表示透明度，取值范围为[0.0,1.0]
        - HSLA中的格式为`hsla(hue, saturation, lightness, alpha)`，其中，`alpha`表示透明度，取值范围为[0,1]
    - 所有浏览器共支持140种颜色名称，具体可查阅[颜色名称列表](https://www.w3schools.com/colors/colors_names.asp)

# 版本记录

# 微博发布
- [ ] 概要
- [ ] 概念
- [ ] 元素
    - [ ] 一般元素
    - [ ] 格式化元素
    - [ ] 空元素
- [ ] 属性
    - [ ] 属性概述
    - [ ] 属性类型
    - [ ] 属性值