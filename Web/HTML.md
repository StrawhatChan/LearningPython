> **本文“发表于微博自媒体”，微博：[@钻石草帽](https://weibo.com/strawhatchan)**

# 概要
**本文采用知识库的方式，记录HTML以下各方面内容：**
1. 相关概念
2. HTML文件的结构
3. HTML元素、属性（attributes）、属性（properties）以及属性值（value）

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
    - 根据HTML5标准，`<html>`、`<head>`和`<body>`是可以忽略的；虽然忽略`<head>`已成为一种常态，但W3C不建议忽略`<html>`和`<body>`

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

| Year | Version                                |
| ---- | -------------------------------------- |
| 1989 | Tim Berners-Lee invented www           |
| 1991 | Tim Berners-Lee invented HTML          |
| 1993 | Dave Raggett drafted HTML+             |
| 1995 | HTML Working Group defined HTML 2.0    |
| 1997 | W3C Recommendation: HTML 3.2           |
| 1999 | W3C Recommendation: HTML 4.01          |
| 2000 | W3C Recommendation: XHTML 1.0          |
| 2008 | WHATWG HTML5 First Public Draft        |
| 2012 | WHATWG HTML5 Living Standard           |
| 2014 | W3C Recommendation: HTML5              |
| 2016 | W3C Candidate Recommendation: HTML 5.1 |

- 字符编码
    - HTML偏好`UTF-8`
    - HTML支持以下编码
        - ASCII，使用0-31和127作为控制字符；32-126作为字母、数字和符号，128-255未使用，详细信息可查阅[HTML ASCII Reference](https://www.w3schools.com/charsets/ref_html_ascii.asp)
        - ANSI，0-127的编码与ASCII相同，128-159为独立字符，160-255与UTF-8相同，详细信息可查阅[HTML ANSI (Windows-1252)](https://www.w3schools.com/charsets/ref_html_ansi.asp)
        - ISO-8859-1，0-127与ASCII相同，128-159未使用，160-255与UTF-8相同，详细信息可查阅[HTML ISO-8859-1 Reference](https://www.w3schools.com/charsets/ref_html_8859.asp)
        - UTF-8，0-127与ASCII相同，128-159未使用，160-255与ANSI和ISO-8859-1相同，256以后还包含超过10,000个不同的字符，详细信息可查阅[HTML Unicode (UTF-8) Reference](https://www.w3schools.com/charsets/ref_html_utf8.asp)
        - 完整的字符编码可查阅[HTML Character Sets](https://www.w3schools.com/charsets/default.asp)
- 文件路径
    - 文件路径描述了网站文件夹结构中某个文件的位置
    - 文件路径可用于链接外部文件，包括网页、图片、样式表、JavaScript
    - 路径有绝对路劲和相对路径2种，绝对路径指明文件的完整路径，相对路径通常以当前页面所在文件夹为基准进行判断

| 路径                           | 描述                                           |
| ------------------------------ | ---------------------------------------------- |
| `<img src="name.jpg">`         | `name.jpg`与当前页面在同一个文件夹             |
| `<img src="images/name.jpg">`  | `name.jpg`在当前文件夹内的images文件夹中       |
| `<img src="/images/name.jpg">` | `name.jpg`在当前页面根目录下的images文件夹中   |
| `<img src="../name.jpg">`      | `name.jpg`在当前页面所在文件夹的上一级文件夹中 |

- 布局
    - HTML5新增的有关布局的语义元素
    - HTML表格
        - HTML表格是为了展示表格式数据设计
        - HTML表格不是为布局设计的
        - 不要使用表格为页面布局
    - CSS浮动特性（float property）
        - CSS浮动特性是常用的布局方式
        - 缺点是与文件流锁定，可能有损灵活性
    - CSS框架（framework）
        - 如果希望快速设置布局，可使用CSS框架，如[W3.CSS](https://www.w3schools.com/w3css/default.asp)或者[Bootstrap](https://www.w3schools.com/bootstrap/default.asp)
    - CSS柔性盒子（flexbox）
        - 这是CSS3中1个新的布局模型
        - 优点是，当页面布局需要适应不同屏幕尺寸和不同显示设备时，所有元素行为都是可预期的，也就是说，控制性能很好
        - 缺点是，不支持IE10及更早的版本
- 反应式网页设计
    - 反应式网页设计（Responsive Web Design）使用HTML和CSS，重新定义页面尺寸、隐藏、收缩、放大或移动内容，使页面在所有类型的设备上都能得到漂亮的展示
    - 设计方法
        - 通过`<meta>`元素设定Viewpoint
        - 在CSS或`<style>`中使用百分比设定宽度以及最大宽度
        - 使用`<picture>`元素为不同的浏览器设定不同的图片
        - 在`font-size`的属性值后加上`vw`，意思是按照`viewport width`的百分比设定文本大小，例如` <h1 style="font-size:10vw">Hello World</h1>`意思是按照浏览器窗口大小的10%设定文本大小
        - 使用Media Queries作为重新设定文本和图片大小的附加方式

```html
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
* {
  box-sizing:border-box;
}

.left {
  background-color:#2196F3;
  padding:20px;
  float:left;
  width:20%; /* The width is 20%, by default */
}

.main {
  background-color:#f1f1f1;
  padding:20px;
  float:left;
  width:60%; /* The width is 60%, by default */
}

.right {
  background-color:#4CAF50;
  padding:20px;
  float:left;
  width:20%; /* The width is 20%, by default */
}

/* Use a media query to add a break point at 800px: */
@media screen and (max-width:800px) {
  .left, .main, .right {
    width:100%; /* The width is 100%, when the viewport is 800px or smaller */
  }
}
</style>
</head>
```

- 实体
    - 实体替代
        - HTML中的保留字符（reserved characters）必须以字符实体（character entities）替代
        - 键盘上没有的字符也可以通过实体替代
    - 实体既可以用`&entity_name`表示，也可以用`&#entity_number`表示
    - 实体对大小写敏感

| 结果     | 描述     | 实体名称   | 实体数值  |
| :------: | :------: | :--------: | :-------: |
|          | 空格     | `&nbsp;`   | `&#160;`  |
| <        | 小于     | `&lt;`     | `&#60;`   |
| >        | 大于     | `&gt;`     | `&#62;`   |
| &        | 符号     | `&amp;`    | `&#38;`   |
| "        | 双引号   | `&quot;`   | `&#34;`   |
| '        | 单引号   | `&apos;`   | `&#39;`   |
| &cent;   | 分       | `&cent;`   | `&#162;`  |
| &pound;  | 磅       | `&pound;`  | `&#163;`  |
| &yen;    | 元       | `&yen;`    | `&#165;`  |
| &euro;   | 欧元     | `&euro;`   | `&#8364;` |
| &copy;   | 版权符号 | `&copy;`   | `&#169;`  |
| &reg;    | 注册标志 | `&reg;`    | `&#174;`  |
| &trade;  | 商标     | `&trade;`  | `&#8482;` |
| &larr;   | 左箭头   | `&larr;`   | `&#8592;` |
| &uarr;   | 上箭头   | `&uarr;`   | `&#8593;` |
| &rarr;   | 右箭头   | `&rarr;`   | `&#8594;` |
| &darr;   | 下箭头   | `&darr;`   | `&#8595;` |
| &spades; | 黑桃     | `&spades;` | `&#9824;` |
| &clubs;  | 梅花     | `&clubs;`  | `&#9827;` |
| &hearts; | 黑心     | `&hearts;` | `&#9829;` |
| &diams;  | 方块     | `&diams;`  | `&#9830;` |

- 变音标记
    - 变音标记是加在字母顶上的标记，有\`&nbsp;&nbsp;&nbsp;&nbsp;’&nbsp;&nbsp;&nbsp;&nbsp;^&nbsp;&nbsp;&nbsp;&nbsp;~&nbsp;&nbsp;共4个

| 标记                 | 字符    | 组合      | 结果    |
| :------------------: | :-----: | :-------: | :-----: |
| \`  | a  | `a&#768;` | a&#768; |
| ’                   | a       | `a&#769;` | a&#769; |
| ^                    | A       | `a&#770`  | A&#770; |
| ~                    | A       | `a&#771;` | A&#771; |

- 其他与实体表示方式相同的符号集
    - 全部数学运算符列表见[UTF-8 Mathematical Operators](https://www.w3schools.com/charsets/ref_utf_math.asp)
    - 全部希腊字母列表见[UTF-8 Greek and Coptic](https://www.w3schools.com/charsets/ref_utf_greek.asp)
    - 部分货币符号列表见[UTF-8 Currency Symbols](https://www.w3schools.com/charsets/ref_utf_currency.asp)
    - 全部箭头符号列表见[UTF-8 Arrows](https://www.w3schools.com/charsets/ref_utf_arrows.asp)
    - 杂项符号列表见[UTF-8 Miscellaneous Symbols](https://www.w3schools.com/charsets/ref_utf_symbols.asp)
- URL
    - URL是Uniform Resource Locator的首字母简称，用于定位网络上的文件或者数据
    - 浏览器请求通过URL从服务器请求页面
    - URL的语法规则`scheme://prefix.domain:port/path/filename`
        - schemm：定义网络服务的类型，通常的URL类型有http、https、ftp和file
        - prefix：定义域的前缀（HTTP默认的前缀为www）
        - domain：定义域
        - port：定义端口（HTTP默认的端口是80）
        - path：定义服务器上的路径（如果忽略，则是网站根目录）
        - fielname：定义文件或资源的名称
    - URL只能使用ASCII字符编码，不能使用空格，如果使用空格则替换为`+`或者`%20`，如果使用其他非ASCII字符编码，URL将被转为能够通过网络传输的字符，并使用`%`符号加上16进制数字替代，有关替换的详细列表可查阅[HTML URL Encoding Reference](https://www.w3schools.com/tags/ref_urlencode.asp)
- XHTML
    - XHTML（EXtensible HyperText Markup Language）是使用XML写的HTML，是作为一个XML应用的HTML，几乎等同于HTML，但比HTML严格，所有主要浏览器均支持
    - 之所以设计XHTML，是因为一些小型设备不支持编写不严格的网页，而XML编写必须严格，因此将XML和HTML相结合后形成了XHTML
    - 与HTML的区别
        - 文件结构。`DOCTYPE`、`<html>`、`<head>`、`<title>`、`<body>`都是强制的
        - 元素。XHTML必须有一个根元素（root element），并且所有元素必须是嵌套的、关闭的、小写的
        - 属性。属性必须是小写的，属性值必须是加双引号的，并且不允许属性最小化
    - HTML转换为XHTML
        - 首行添加XHTML`<!DOCTYPE>`
        - 在html元素中添加`xmlns`属性
        - 将所有元素名称改为小写
        - 关闭所有空元素
        - 将所有属性名称改为小写
        - 为所有属性值加上双引号
- 浏览器支持向HTML5转换
    - 使用HTML5新语义元素时，在CSS文件中将所有新语义元素定义为`display: block;`
    - 在`<head>`标签内使用`<script>`元素，运用`document.createElement()`方法为HTML创建新元素，并使用`<style>`元素定义其样式
    - 使用HTML5新语义元素时，运用HTML5Shiv

```html
<!-- HTML5Shiv示例，包含注释部分 -->
<!--[if lt IE 9]>
  <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
<![endif]-->
```

# 元素
一份完整的HTML元素列表可查阅[HTML Element Reference](https://www.w3schools.com/tags/default.asp)
## 元素概述
- HTML元素
    - HTML元素指的是`<tagname> content</tagname>`中的所有内容，包含标签以及插入开始和结束标签中的内容
    - 没有引用任何内容的HTML元素成为空元素（empty elements），没有结束标签，例如用于指定断行的`<br>`元素，但空元素仍可以通过如`<br />`这样的开放标签（opening tag）关闭（**所谓关闭，不是指`<br><br />`这样的形式，而是直接用`<br />`**）
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
    - `<head>`标签定义整个HTML文件的原信息，用于定义文件题目、字符编码、样式、链接、脚本等元信息
    - 包含的标签
        - `<title>`：定义页面在浏览器标签中显示的题目；将网页加入收藏时，提供标题；在搜索引擎中展示的页面题目
        - `<style>`：定义整个页面的样式
        - `<meta>`：设置与网站整体相关信息
        - `<link>`：链接外部CSS文件
        - `<script>`：
        - `<base>`
    - 置于`<html>`和`<body>`之间
    - 原信息不在网页上显示
    - 
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
    - `target`为可选项，包含`_self`（在同一框架内打开页面）、`_blank`（在浏览器的新窗口或新标签打开）、`_top`（如果网页被锁定在一个框架内，该属性值可突破框架）、`_parent`（在父框架内打开页面）或者代表iframe的名称
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
    - 定义形式：`<button type="button" onclick="alert('Hello Wordl!')">content</button>`
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

- 块
    - 通过`<div>`等块级别的标签定义，通常作为HTML元素的容器（container），没有必要的属性，但`style`、`class`和`id`经常用到
    - 也可将`<div>`等块级别的元素理解为对HTML元素的一种分组方式
    - 所有块都从新的行开始，并至少占据整行
    - 其他HTML中的块元素包括：`<address>、<article>、<aside>、<blockquote>、<canvas>、<dd>、<div>、<dl>、<dt>、<fieldset>、<figcaption>、<figure>、<footer>、<form>、<h1>-<h6>、<header>、<hr>、<li>、<main>、<nav>、<noscript>、<ol>、<output>、<p>、<pre>、<section>、<table>、<tfoot>、<ul>、<video>`，详细信息可查阅[HTML Block and Inline Elements](https://www.w3schools.com/html/html_blocks.asp)
- 行内
    - 通过`<span>`标签定义，通常作为文本的容器，没有必要的属性，但`style`、`class`和`id`经常用到
    - 也可将`<span>`理解为对文本的一种分组方式
    - 不从新的行开始，只占据需要的位置宽度
    - 其他HTML中的行内元素包括：`<a>、<abbr>、<acronym>、<b>、<bdo>、<big>、<br>、<button>、<cite>、<code>、<dfn>、<em>、<i>、<img>、<input>、<kbd>、<label>、<map>、<object>、<q>、<samp>、<script>、<select>、<small>、<span>、<strong>、<sub>、<sup>、<textarea>、<time>、<tt>、<var>`，详细信息可查阅[HTML Block and Inline Elements](https://www.w3schools.com/html/html_blocks.asp)
- 内嵌框架
    - 内嵌框架（iframe）用于在网页内展示另一个网页
    - 通过`<iframe>`标签调用，以`<src="url">`属性定义网页链接
    - 可设置的属性还有`name`、`height`、`width`、`style`等，其中，`name`的属性值可以被用于链接的`target`属性，即点击链接后将在`iframe`中展示该链接对应的HTML页面

```html
<!-- iframe中name属性与链接中target属性的关系 -->
<iframe src="demo_iframe.htm" name="iframe_a"></iframe>

<p><a href="https://www.w3schools.com" target="iframe_a">W3Schools.com</a></p>
```

- JavaScript脚本
    - JavaScript能够以更加动态和交互的特性展示HTML页面
    - 通过`<script>`标签调用
    - `<script>`元素或者包含脚本语句，或者通过`<src>`属性指向外部脚本
    - 功能
        - 修改HTML内容
        - 修改HTML样式
        - 修改HTML属性
    - `<noscript>`元素作为用户禁用脚本时的替代内容
- 代码
    - `<code>`元素展示整个代码
    - `<kbd>`元素展示键盘输入
    - `<samp>`元素展示程序输出
    - `<var>`元素展示变量
- 表单
    - `<form>`元素定义了一种收集用户输入内容的形式
    - 通过`type`属性可以定义多种`<form>`元素的展示形式
- 表单相关数据组
    - 通过`<fieldset>`标签调用
    - 嵌套于`<form>`元素内，用于为表单中的相关数据分组
- 表单相关数据组标题
    - 通过`<legend>`标签调用
    - 嵌套于`<fieldset>`元素内，用于为表单设定标题
- 标签
    - 通过`<label>`标签调用
    - 为`<input>`元素设定标签，包含`for`和`form`共2个属性
- 下拉列表
    - 通过`<select>`标签调用
    - 嵌套于`<form>`元素内，用于设定下拉列表，但只能单选
- 下拉列表选项
    - 通过`<option>`标签调用
    - 嵌套于`<select>`元素内，用于设定下拉列表的选项
- 下拉列表分组
    - 通过`<optgroup>`标签调用
    - 嵌套于`<select>`元素内，用于为下拉列表选项进行分组
- 文本区域
    - 通过`<textarea>`标签调用
    - 嵌套于`<form>`元素内，用于设定文本区域
- 数据列表
    - 通过`<datalist>`标签调用，是HTML5新增的元素类型
    - 嵌套于`<form>`元素内，为`<input>`输入框设定预先准备的数据
- 输出结果
    - 通过`<output>`标签调用，是HTML5新增的元素类型
    - 嵌套于`<form>`元素内，为`<input>`输出结果
- 子块
    - 通过`<div>`标签调用，当内嵌于`<section>`和`<article>`元素时，可理解为`<section>`和`<article>`的子块
- 视频
    - 通过`<video>`标签调用，`<source>`元素内嵌于`<video>`元素，提供视频资源
    - 调用方式：`<video width="320" height="240" controls | autoplay>`，其中，`controls`表示视频控制框，`autoplay`表示自动播放
    - 嵌入YouTube视频的步骤
        - 上传视频至YouTube
        - 记录视频的ID，形式如`tgbNymZ7vqY`
        - 定义`<iframe>`元素
        - 将视频URL作为`src`属性的值
        - 使用`width`和`height`属性定义播放器尺寸
        - 增加其他URL参数
    - 如果嵌入YouTube视频，可以使用`<iframe>`、`<embed>`、`<object>`共3种方式
        - `<iframe>`调用： `<iframe width="420" height="315" src="https://www.youtube.com/embed/(tgbNymZ7vqY | tgbNymZ7vqY?autoplay=1 | tgbNymZ7vqY?playlist=tgbNymZ7vqY&loop=1 | tgbNymZ7vqY?controls=0)"></iframe> `，其中，圆括号是为了将4种选项作为1个整体观察而添加，实际没有，第1个选项和第4个选项意思相同，都是带控制的播放；第2个选项表示自动播放；第3个选项表示循环播放（如果loop=0则只播放1次）
        - `<embed>`调用：`<embed width="420" height="315" src="https://www.youtube.com/embed/tgbNymZ7vqY">`
        - `<object>`调用：`<object width="420" height="315" data="https://www.youtube.com/embed/tgbNymZ7vqY"> </object>`
    - 相关的方法、属性和事件见[HTML Audio/Video DOM Reference](https://www.w3schools.com/tags/ref_av_dom.asp)
- 音频
    - 通过`<audio>`标签调用，`<source>`元素内嵌于`<audio>`元素，提供音频资源
    - 调用方式：`<audio controls>`
    - 相关的方法、属性和事件见[HTML Audio/Video DOM Reference](https://www.w3schools.com/tags/ref_av_dom.asp)
- 对象
    - 通过`<object>`标签调用，功能与`<embed>`元素类似，是在HTML文件中嵌入对象，通常用于嵌入插件（plugins），比如java applets、PDF readers、Flash Players
    - 调用方式： `<object width="400" height="50" data="bookmark.swf"></object> `

## 格式化元素
格式化元素（formatting elements）给文本定义一些特殊的含义，调用方式与HTML的一般元素相同
- `<b>` 加粗
- `<strong>` 重要
- `<i>` 斜体
- `<em>` 焦点
- `<mark>` 黄色标记（HTML5新增）
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
- 资源`<source>`
    - `<source>`内嵌于`<picture>`、`<video>`、`<audio>`等需要提供资源的元素中
    - 调用方式：`<source media="(min-width: 650px)" srcset="imgname.jpg">`或者`<source src="movie.mp4" type="video/mp4">`
- 元信息`<meta>`
    - 隶属于`<head>`元素
    - 字符编码。HTML中使用`<meta charset="UTF-8">`定义，CSS中使用`@charset "UTF-8";`定义
    - 网站描述。`<meta name="description" content="Free Web tutorials">`
    - 关键词。`<meta name="keywords" content="HTML, CSS, XML, JavaScript">`
    - 作者。`<meta name="author" content="John Doe">`
    - 自动刷新。`<meta http-equiv="refresh" content="30">`
    - 视角。`<meta name="viewport" content="width=device-width, initial-scale=1.0">`，告诉浏览器如何控制页面的尺寸和比例（dimensions and scaling），其中，`width=device-width`表示全屏显示，`initial-scale=1.0`表示按照100%缩放大小显示
- 基础`<base>`
    - 隶属于`<head>`元素
    - 为所有的URLs定义URL和`target`的基础，可理解为
    - 调用方式：`<base href="https://www.w3schools.com/images/" target="_blank">`
        - `href="https://www.w3schools.com/images/"`表示以该链接为基础为HTML文件中的URL寻找相应文件
        - `target="_blank"`表示所有以上述链接为基础的URL都在一个新窗口打开

```html
<!-- base示例 -->
<!DOCTYPE html>
<html>
<head>
  <title>Page Title</title>
  <base href="https://www.w3schools.com/images/" target="_blank">
</head>
<body>

<img src="html5.gif">
<p>Since we have specified a base URL, the browser will look for the image "html5.gif" at "https://www.w3schools.com/images/html5.gif"</p>

<p><a href="https://www.w3schools.com">W3Schools</a></p>
<p>The link above opens in a new window. This is because the base target is set to "_blank".</p>

</body>
</html>
```

- 输入`<input>`
    - 嵌套于`<form>`元素
    - 调用方式：`<input type="text | radio | submit" name="firstname" value="Mickey">`
- 选项`<option>`
    - 嵌套于`<datalist>`元素
    - 与嵌套于`<select>`元素的`<option>`虽然名称相同，但元素类型不同
    - 调用方式：`<option value="Internet Explorer">`
- 嵌入`<embed>`
    - 在HTML文件中定义一个嵌入的对象，也包括嵌入HTML
    - 调用方式： `<embed width="400" height="50" src="bookmark.swf">`

## HTML5新元素
- 新的语义或结构元素
    - `<header>`
        - 定义文件或`<section>`的头部或1个部分，作为内容介绍的容器，可在一个文件中使用多个`<header>`
    - `<nar>`
        - 定义一系列主要的导航链接
    - `<section>`
        - 定义1个页面中的专题内容，也可以理解为相关元素块
        - 与`<article>`操作上可以相互嵌套，但不推荐相互嵌套
    - `<article>`
        - 定义1个独立的自包含的相关元素块，即可以独立地被阅读，并体现出意义
        - `<section>`可内嵌于`<article>`为`<article>`中有关联的内容进行分组，但不推荐嵌套
    - `<aside>`
        - 在内容旁边定义1个内容，类似侧边栏
    - `<footer>`
        - 定义文件的尾部或1个部分，通常包括文件作者、版权信息、链接和联系信息等，可在1个文件中使用多个`<footer>`元素
    - `<details>`
        - 定义增加的细节，通常需要点击`<summary>`定义的内容才能展开
    - `<summary>`
        - 嵌套于`<details>`内，为`<details>`定义标题
    - `<figure>`和`<figcaption>`
        - `<figure>`定义`<img>`空元素和`<figcaption>`元素的组合，其中，`<img>`定义图片，`<figcaption>`定义图片说明，`<figcaption>`紧接`<img>`
    - `<main>`
        - 定义一个页面的主体部分
    - `<mark>`
        - 为文本添加标记，默认为黄标
    - `<time>`
        - 定义日期和时间
        - 与`type`的属性值`time`不是同一类型
- 新的表单元素
    - `<datalist>`（见一般元素中的数据列表）
    - `<output>`（见一般元素中的输出结果）
- 新的输入类型（见属性值中的输入类型）
- 新的属性语法（Attribute Syntax）

| 类型   | 示例                                              |
| :----- | :------------------------------------------------ |
| 空     | `<input type="text" value="John"` **disabled**`>` |
| 不引用 | `<input type="text"` **value=John**`>`            |
| 双引号 | `<input type="text"` **value="John Doe"**`>`      |
| 单引号 | `<input type="text"` **value='John Doe'**`>`      |

- 新的作图元素
    - `<canvas>`通过脚本（通常是JavaScript脚本）画图，图形是逐个像素进行解析，详细信息可查阅[HTML5 Canvas](https://www.w3schools.com/html/html5_canvas.asp)
    - `<svg>`通过SVG DOM（基于XML，可用JavaScript脚本）做可缩放的矢量图，图形作为对象存在，不是`<canvas>`展示的以像素为单位的图形，详细信息可查阅[HTML5 SVG](https://www.w3schools.com/html/html5_svg.asp)

| Canvas                 | SVG                      |
| :--------------------- | :----------------------- |
| 解决方案有依赖性       | 解决方案独立             |
| 不支持事件处理         | 支持事件处理             |
| 文本解析能力弱         | 最适合于有大量解析的应用 |
| 可保存在图片格式的文件 | 对复杂事项的解析速度慢   |
| 适合于图片集约的游戏   | 不适合游戏应用           |

- 新的媒体元素
    - `<audio>`定义声音内容，详细信息可查阅[HTML5 Audio](https://www.w3schools.com/html/html5_audio.asp)
    - `<video>`定义视频或电影，详细信息可查阅[HTML5 Video](https://www.w3schools.com/html/html5_video.asp)
    - `<embed>`定义外部应用的容器
    - `<source>`嵌套于`<audio>`和`<video>`内部，定义媒体源
    - `<track>`嵌套于`<audio>`和`<video>`内部，定义文本追踪

| 视频格式 | 视频文件 | 描述 |
| ----   | ---  | --------    |
| MPEG 	| .mpg .mpeg | MPEG. Developed by the Moving Pictures Expert Group. The first popular video format on the web. Used to be supported by all browsers, but it is not supported in HTML5 (See MP4).|
| AVI |	.avi | AVI (Audio Video Interleave). Developed by Microsoft. Commonly used in video cameras and TV hardware. Plays well on Windows computers, but not in web browsers. |
| WMV | .wmv | WMV (Windows Media Video). Developed by Microsoft. Commonly used in video cameras and TV hardware. Plays well on Windows computers, but not in web browsers. |
| QuickTime | .mov | QuickTime. Developed by Apple. Commonly used in video cameras and TV hardware. Plays well on Apple computers, but not in web browsers. (See MP4) |
| RealVideo | .rm .ram | RealVideo. Developed by Real Media to allow video streaming with low bandwidths. It is still used for online video and Internet TV, but does not play in web browsers. |
| Flash | .swf .flv | Flash. Developed by Macromedia. Often requires an extra component (plug-in) to play in web browsers. |
| Ogg | .ogg | Theora Ogg. Developed by the Xiph.Org Foundation. Supported by HTML5.
| WebM | .webm | WebM. Developed by the web giants, Mozilla, Opera, Adobe, and Google. Supported by HTML5.
| MPEG-4 or MP4 | .mp4 | MP4. Developed by the Moving Pictures Expert Group. Based on QuickTime. Commonly used in newer video cameras and TV hardware. Supported by all HTML5 browsers. Recommended by YouTube. |

| 音频格式 | 音频文件 | 描述 |
| -----  | ------ | -------- |
| MIDI | .mid .midi | MIDI (Musical Instrument Digital Interface). Main format for all electronic music devices like synthesizers and PC sound cards. MIDI files do not contain sound, but digital notes that can be played by electronics. Plays well on all computers and music hardware, but not in web browsers. |
| RealAudio | .rm .ram | RealAudio. Developed by Real Media to allow streaming of audio with low bandwidths. Does not play in web browsers. |
| WMA | .wma | WMA (Windows Media Audio). Developed by Microsoft. Commonly used in music players. Plays well on Windows computers, but not in web browsers. |
| AAC | .aac | AAC (Advanced Audio Coding). Developed by Apple as the default format for iTunes. Plays well on Apple computers, but not in web browsers. |
| WAV | .wav | WAV. Developed by IBM and Microsoft. Plays well on Windows, Macintosh, and Linux operating systems. Supported by HTML5. |
| Ogg | .ogg | Ogg. Developed by the Xiph.Org Foundation. Supported by HTML5. |
| MP3 | .mp3 | MP3 files are actually the sound part of MPEG files. MP3 is the most popular format for music players. Combines good compression (small files) with high quality. Supported by all browsers. |
| MP4 | .mp4 | MP4 is a video format, but can also be used for audio. MP4 video is the upcoming video format on the internet. This leads to automatic support for MP4 audio by all browsers. |

## 在HTML5中被移除或替换的元素列表

| 被移除的元素 | 替代方案            |
| :----------: | :-----------------: |
| `<acronym>`  | `<abbr>`            |
| `<applet>`   | `<object>`          |
| `<basefont>` | CSS                 |
| `<big>`      | CSS                 |
| `<center>`   | CSS                 |
| `<dir>`      | `<ul>`              |
| `<font>`     | CSS                 |
| `<font>`     | X                   |
| `<frame>`    | X                   |
| `<frameset>` | X                   |
| `<noframes>` | X                   |
| `<strike>`   | CSS, `<s>`, `<del>` |
| `<tt>`       | CSS                 |

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
    - 通常在`<img>`、`<embed>`等标签中，用于定义URL
    - 调用方式：`<img src="URL">`，其中，`URL`为路径（必须包含文件后缀）
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
    - 为任意HTML元素指定唯一的ID，1个HTML元素只能有1个ID
    - ID是大小写敏感的，至少应有1个字符，不能包含空白符
    - CSS和JavaScript可对特定拥有特定的id的元素进行操作，以完成某些任务
    - 在CSS中通过在`idname`前加上`#`符号标识id，即`#idname`
    - 在JavaScript中，通过`getElementById()`对特定id进行操作
    - 衍生功能
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
    - 为HTML元素进行分组，可在CSS文件或`<style>`中以`classname`为标识对拥有该名称的所有元素定义样式，1个元素可以有多个`classname`，不同类型的元素可以是相同的`classname`
    - 可理解为通过`class`定义了一类HTML元素
    - 在CSS中可使用`tagname.classname`的方式定义该类型元素的样式
        - 如果对所有`class`定义其样式，只需要在`classname`前加上`.`符号，即`.classname{}`
        - 如果对特定类型元素的`class`定义样式，需要在`classname`前加上`tagname.`，即`tagname.classname{}`
        - `classname`不能有空格，如果有空格则表示2个`classname`，并且1个HTML元素可以有2个及以上的`classname`
    - JavaScript中可使用`getElementByClassName()`方法对特定`classname`进行操作

```html
<!-- 对所有class定义样式 -->
<style>
.city {
    background-color: tomato;
    color: white;
    padding: 10px;
}
</style>

<h2 class="city">London</h2>
<p>London is the capital of England.</p>
<h2 class="city">Paris</h2>
<p>Paris is the capital of France.</p>
<h2 class="city">Tokyo</h2>
<p>Tokyo is the capital of Japan.</p>
<!-- 对特定类型元素的class定义样式 -->
<p class="error">content</p>
p.error {
    color: red;
}
```

- name
    - 隶属于`<map>`、`<form>`、`<input>`、`<select>`等可定义名称的元素
        - 定义`<map>`的名称
        - 定义`<form>`表单的名称
        - `<input>`的必要属性，如果没有该属性，提交数据后所有数据都不会被发送
        - 定义下拉列表的名称
    - 调用方式：`<map name="name">`
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
- disabled
    - 隶属于`<input>`元素，限制当前输入框为不可输入
    - 调用方式：`disabled`或者`disabled="disabled"`
- readonly
    - 隶属于`<input>`元素，定义输入区域为只读，不可更改
    - 调用方式：`readonly`或者`readonly="readonly"`
- type
    - 隶属于`<input>`元素
    - 调用方式：`<type="text | radio | submit">`依次表示文本、单个选项、提交按钮，其中，`submit`属性值定义了将1个格式化数据提交表单处理程序（form-handler）的按钮，表单处理程序是一个典型的处理输入数据脚本的服务页面，它由`<form>`元素中的`action`属性确定
- value
    - 隶属于`<input>`元素
    - 调用方式：`<value="Mouse">`，表示默认显示的输入值
- max
    - 隶属于`<input>`元素，与`type="typename"`联合使用，定义最大数值
    - 调用方式：`<input type="date" name="bday" max="1979-12-31">`
- maxlength
    - 隶属于`<input>`元素，定义可输入的最大字符数量
    - 调用方式：` maxlength="10"`
- min
    - HTML5新增
    - 隶属于`<input>`元素，与`type="typename"`联合使用，定义最小数值
    - 调用方式：`<input type="date" name="bday" min="2000-01-02">`
- pattern
    - HTML5新增
    - 隶属于`<input>`元素，使用正则表达式检查输入值
    - 仅与`type="text | search | url | tel | email | password"`联合使用
- placeholder
    - 隶属于`<input>`元素，设定提示，并且提示文本将显示在文本框中
- required
    - HTML5新增
    - 隶属于`<input>`元素，定义输入区域为必须输入
    - 调用方式：`required`或者`required="required"`
    - 仅与`type="text | search | url | tel | email | password | date | number | checkbox | radio | file"`联合使用
- size
    - 隶属于`<input>`元素，定义输入区域的宽度（以字符数衡量）
    - 调用方式：`size="40"`
- step
    - HTML5新增
    - 隶属于`<input>`元素，定义数值迭代的步长
    - 调用方式：`step="3"`
- formaction
    - HTML5新增
    - 隶属于`<input>`元素，覆盖`<form>`的`action`属性，定义提交时发送信息的文件，与`type="submit"`和`type="image"`联合使用
- formenctype
    - HTML5新增
    - 隶属于`<input>`元素，覆盖`<form>`的`enctype`属性，仅在`method="post"`情况下使用，并与`type="submit"`和`type="image"`联合使用
- formmethod
    - HTML5新增
    - 隶属于`<input>`元素，覆盖`<form>`的`method`属性，与`type="submit"`和`type="image"`联合使用
- formnovalidate
    - HTML5新增
    - 隶属于`<input>`元素，覆盖`<form>`的`novalidate`属性，与`type="submit"`联合使用
- formtarget
    - HTML5新增
    - 隶属于`<input>`元素，覆盖`<form>`的`target`属性，与`type="submit"`和`type="image"`联合使用
- autofocus
    - HTML5新增
    - 隶属于`<input>`元素，定义页面加载后光标聚焦的位置
- list
    - 隶属于`<input>`元素，定义列表名称，并与`<datalist>`元素联合使用
- action
    - 隶属于`<form>`元素
    - 定义了当表单被提交时的处理方式，通常情况下是发送给服务器上的页面，例如PHP文件，如果没有该属性，则将提交发送给当前页面
    - 调用方式：`<form action="/action_page.php">`
- method
    - 隶属于`<form>`元素
    - 定义了当提交表单数据时使用的HTTP方法，包括`GET`和`POST`共2种
        - `GET`是默认方法，但提交的数据将在链接地址中可见，并有3000字符数的限制，用于非敏感数据
        - `POST`可以保证提交的数据不可见，且没有字符数的限制，用于敏感数据
    - 调用方式：`<form action="/action_page.php" method="get | post">` 
- accept-charset
    - 隶属于`<form>`元素
    - 定义提交表单数据的字符集
- autocomplete
    - 隶属于`<form>`、`<input>`元素
    - 定义浏览器是否自动完成表单
- enctype
    - 隶属于`<form>`元素
    - 定义提交表单数据的编码
- novalidate
    - 隶属于`<form>`元素，定义浏览器不验证表单
    - 调用方式：`novalidate`或者`novalidate="novalidate"`
- oninput
    - 隶属于`<form>`元素
    - 定义输入和输出之间的关系
    - 调用方式：`<form action="/action_page.php" oninput="x.value=parseInt(a.value)+parseInt(b.value)">`
- selected
    - 隶属于`<option>`等有选项的元素
    - 定义预选项
- multiple
    - 隶属于`<select>`、`<input>`等有选项的元素
    - 调用方式：`multiple`或者`multiple="multiple"`
    - `<select>`定义可以选择多个选项
    - 在`<input>`元素中仅与`type="email | file"`联合使用，提供一个选择按钮
- label
    - 隶属于`<optgroup>`元素
    - 此处的`label`为属性，不是`<label>`元素
    - 设定下拉列表选项的分组标签
- rows
    - 隶属于`<textarea>`元素
    - 定义文本的行数量
- cols
    - 隶属于`<textarea>`元素
    - 定义文本的列数量
- onclick
    - 隶属于`<button>`元素
    - 定义点击按钮时的提示信息
- for
    - 隶属于`<label>`、`<output>`元素
    - 用于指定名称
- form
    - 隶属于`<label>`、`<input>`元素
    - 用于指定为`<form>`元素设定的id名称，以便当元素处于`<form>`元素之外时，仍能像在`<form>`元素内一样发挥作用
- data
    - 隶属于`<object>`等元素，用于指定对象（object）

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
- 输入类型
    - 隶属于`<input>`元素，以`type="typevalue"`调用
    - HTML输入类型属性值
        - text：文本
        - password：密码
        - submit：提交
        - reset：将所有表单值还原成默认值
        - radio：单选框
        - checkbox：复选框
        - button：按钮
        - file：文件
    - HTML5输入类型属性值
        - color：颜色选择按钮
        - date：日期输入
        - datetime-local：自行输入日期（Firefox不支持）
        - email：输入邮件地址，邮件地址格式是否被自动验证依赖于浏览器是否支持（Safari不支持）
        - month：选择年月（Firefox不支持）
        - number：数字输入框
        - range：一个可通过指针移动确定的所选数据的范围
        - search：搜索区域
        - tel：电话号码（只有Safari支持）
        - time：时间输入框
        - url：链接输入（Safari不支持）
        - week：输入星期和年（Firefox不支持）

# HTML5 API's
- [HTML5 Geolocation](https://www.w3schools.com/html/html5_geolocation.asp)
    - 用于获取用户的地理位置，但由于地理位置信息为私人信息，因此，获取该信息需要获得用户的同意
- [HTML5 Drag and Drop](https://www.w3schools.com/html/html5_draganddrop.asp)
    - 实现通过鼠标抓取1个对象然后拖动到当前页面的不同位置
- [HTML5 Web Storage](https://www.w3schools.com/html/html5_webstorage.asp)
    - 网页应用能够在用户浏览器中将数据存储到本地，既不会影响网页浏览，也不需要通过传输数据存储到服务器
    - 网页存储对存储的数据量没有限制，仅受用户本地硬盘大小限制
    - 网页存储根据来源（每个来源包括域名和协议）存储和调用数据
- [HTML5 Web Workers](https://www.w3schools.com/html/html5_webworkers.asp)
    - 当在HTML页面执行脚本时，页面将变得反应迟钝，直到脚本结束
    - 网页工作者是一个在后台运行的、独立于其他脚本的、不影响页面展示的JavaScript
- [HTML5 HTML5 Server-Sent Events（SSE）](https://www.w3schools.com/html/html5_serversentevents.asp)
    - SSE允许网页自动从服务器获得更新
- HTML5 Application Cache

# 代码规范
详细内容可查阅[HTML5 Style Guide and Coding Conventions](https://www.w3schools.com/html/html5_syntax.asp)
- 正确声明文件类型
- 标签、属性等名称都用小写
- 关闭所有元素，包括空元素
- 为属性值添加双引号
- 图片添加`alt`属性
- 等号前后不加空格
- 每行代码避免超过80个字符
- 不要无理由地添加空行，只在大的或逻辑代码块后添加空行，以便阅读
- 不要使用tab键，使用2个空格符作为缩进
- 不忽略`<html>`和`<body>`标签
- 不推荐忽略`<head>`标签
- 应当添加在`<html>`元素中添加`lang`，在嵌套于`<head>`元素中的`<meta>`元素中添加`charset`属性、`viewpoint`属性值以及与`viewpoint`联合使用的`content`属性，同时将`<title>`元素嵌套于`<head>`元素中
- 使用简单的`<link>`元素，链接到CSS文件
- 短规则压缩写，长规则分行写，其中，长规则细分为以下内容
    - 将开始的大括号置于第1行
    - 在开始的大括号前留一个空格
    - 使用2个空格作为缩进
    - 在所有的“属性-值”对后加上分号，包括最后一个“属性-值”对
    - 只有当值存在空格时，才使用双引号
    - 将关闭的大括号单独作为一行，且括号前不要有空格
    - 避免每行超过80个字符
- 使用简单语法加载外部JavaScript脚本
- 因部分服务器对文件名大小写敏感，如Apache、Unix，还有部分服务器大小写不敏感，如Microsoft、IIS，那么，如果从大小写不敏感的服务器迁移至大小写敏感的服务器，就容易出现错误，避免这一问题的最佳方法是，总是使用小写字母作为文件名
- 文件后缀为`.htm`和`.html`的文件没有本质差别，唯一的差别是文化，`.htm`是因早期DOS系统将后缀名长度限制为3个字符，而`.html`则是Unix系统没有类似于DOS系统那样的限制
- 当一个URL没有指定文件名时，将提取默认文件，如`index.html`、`index.htm`、`default.html`、`default.htm`，一般的，应以`.html`作为HTML文件的后缀

# HTML参考资料
- [HTML Tag List by Alphabet](https://www.w3schools.com/tags/default.asp)
- [HTML Tag List by Category](https://www.w3schools.com/tags/ref_byfunc.asp)
- [HTML Attributes](https://www.w3schools.com/tags/ref_attributes.asp)
- [HTML Global Attributes](https://www.w3schools.com/tags/ref_standardattributes.asp)
- [HTML Events](https://www.w3schools.com/tags/ref_eventattributes.asp)
- [HTML Colors](https://www.w3schools.com/tags/ref_colornames.asp)
- [HTML Canvas](https://www.w3schools.com/tags/ref_canvas.asp)
- [HTML Audio/Video DOM](https://www.w3schools.com/tags/ref_av_dom.asp)
- [HTML Character Sets](https://www.w3schools.com/tags/ref_charactersets.asp)
- [HTML Elements and Valid DOCTYPES](https://www.w3schools.com/tags/ref_html_dtd.asp)
- [HTML URL Encoding](https://www.w3schools.com/tags/ref_urlencode.asp)
- [HTML Language Codes](https://www.w3schools.com/tags/ref_language_codes.asp)
- [HTML ISO Country Codes](https://www.w3schools.com/tags/ref_country_codes.asp)
- [HTML Status Messages](https://www.w3schools.com/tags/ref_httpmessages.asp)
- [HTML Request Methods](https://www.w3schools.com/tags/ref_httpmethods.asp)
- [Pixels to Ems Conversion](https://www.w3schools.com/tags/ref_pxtoemconversion.asp)
- [Keyboard Shortcuts](https://www.w3schools.com/tags/ref_keyboardshortcuts.asp)

# 版本记录
1. 2018年05月30日，v1.0.0

# 微博发布
- [x] 概要
- [x] 概念
- [x] 元素
    - [x] 一般元素
    - [x] 格式化元素
    - [x] 空元素
    - [x] HTML5新元素
    - [x] 在HTML5中被移除或替换的元素列表
- [x] 属性
    - [x] 属性概述
    - [x] 属性类型
    - [x] 属性值
- [x] HTML5 API's
- [x] 代码规范
- [x] HTML参考资料