> **本文“发表于微博自媒体”，微博：[@钻石草帽](https://weibo.com/strawhatchan)**

# 概要
**本文采用知识库的方式，记录Markdown以下各方面内容：**

1. 排版规则
2. 数学表达规则

# 排版
- 为标题设定ID
    - 可为每个标题设定ID
    - 通过`# Hello {#id}`或者`# Hello # {#id}`这样的方式设定ID
- 段落
    - 1个或多个空行用于区分段落
    - 空行为只要空白符的行
- 强调
    - `*这是斜体文字*`*这是斜体文字*
    - `_这也是斜体问题_`_这也是斜体问题_
    - `**这是加粗文字**`**这是加粗文字**
    - `__这也是加粗文字__`__这也是加粗文字__
    - `~~这是删除文字~~`~~这是删除文字~~
    - `_这是不同强调的**合并**文字_`_这是不同强调的**合并**文字_
- 列表
    - 分无序和有序2种
```
这是一个无序列表
- 第1个1级序列
- 第2个1级序列
    - 第1个2级序列
    - 第2个2级序列

这是一个有序和无序列表组合
1. 有序列表1
2. 有序列表2
3. 有序列表3
    - 无序列表
    - 无序列表
```
- 链接
    - 链接形式：\[链接名称\]\(链接地址 "可选的链接标题"\)
- 参考
    - 参考引用：\[参考名称\]\[参考ID\]
    - 参考设定：\[参考ID\]: 参考链接地址 "可选的参考标题"
- 图片
    - 图片引用：\!\[图片标题\]\(图片链接\)
- 引用块
    - 行首使用\>符号设定引用块
    - 引用块可以嵌套，第1层嵌套使用1个\>，第2层嵌套连续使用2个\>，以此类推
- 表格
    - 表头与其他数据部分使用\-符号分隔
    - 不同的列之间使用`|`符号分隔

| First Header  | Second Header |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |

- 代码块

无高亮的代码块
```
｀｀｀
function test() {
　 console.log("notice the blank line before this function?");
}
｀｀｀
```

有高亮的代码块
```　　
｀｀｀ruby
function test() {
  console.log("notice the blank line before this function?");
}
｀｀｀
```

行内代码
通过\`代码\`引用行内代码
- HTML
    - 支持HTML，但不支持HTML内的markdown语法
- 水平线
    - 使用连续3个以上（含3个）的`.`、`-`或`*`都可以创建水平分隔线
- 忽略Markdown语法
    - 使用`\`反斜杠忽略Markdown语法符号，例如使用`\*\*`输出2个星号，而不是加粗

# MathJax
## 机制与配置
- 途径与机制
    - 从CDN调用
        - 将有数学公式的页面链接到CDN的MathJax
        - 将数学公式从MathJax推送到页面
    - 将MathJax安装在本地服务器上
        - 机制同上，只是链接和推送的服务器不一样
    - 将MathJax安装在本地磁盘中
        - 机制同上，不同点同上
    - 免费CDN
        - [cdnjs.com](https://cdnjs.com/)
        - [jsdelivr.com](https://jsdelivr.com)
        - [unpkg.com](https://unpkg.com/)
        - [rawgit.com](https://rawgit.com/)
        - [gitcdn.xyz](http://gitcdn.xyz/)
- 实现调用
    - 将以下代码置于网页的`<head>`部分
    - 置于`<body>`部分也可以，但更倾向于放在`<head>`部分
    - 下述代码将在CDN上加载MathJax 2.7.4版本，识别网页中的TeXt、MathML和AsciiMath，并使用CSS生成HTML来显示数学公式
    - `TeX-MML-AM_CHTML`是最常用的联合配置属性，但不是最有效的，其他配置可参考MathJax的[Combined Configurations页面](https://docs.mathjax.org/en/latest/config-files.html#common-configurations)
    - 如果既希望使用CDN，同时也希望使用本地配置文件，则需要添加参数
```javascript
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
// 更一般的形式，其中，path-to-MathJax为路径，可以是HTTP，也可以是本地服务器或磁盘地址；[async]，如果为HTTP地址，则需要该参数，如果不是HTTP地址，而是本地服务器或磁盘，则不需要；configuration表示配置方式
<script type="text/javascript" [async]
  src="path-to-MathJax/MathJax.js?config=configuration">
</script>
// 既希望使用CDN，同时也希望使用本地配置文件
<script type="text/javascript"
    src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML,MathJax.Ajax.loadComplete(" http://myserver.com/MathJax/config/local/local.js ")">
</script>
```
- 解析机制
    - MathJax可对TeX、LaTeX、MathML和AsciiMath等表示方法进行解析
    - 解析对象通过`configuration`来确定
    - 使用`$$...$$`和`\[...\]`作为整行数学公式分隔符，使用`\(...\)`作为行内数学公式分隔符
    - 默认情况下不使用`$...$`作为行业数学公式分隔符，因为单个`$`符号经常使用于非数学设定，可能导致一些文本错误地被当作数学公式对待
    - 如果想要使用单个`$`符号，则需要在调用代码前加上一段代码（见下），更多关于`tex2jax`的细节可查阅[The tex2jax Preprocessor页面](https://docs.mathjax.org/en/latest/options/preprocessors/tex2jax.html#configure-tex2jax)以及[MathJax TeX and LaTeX Support页面](https://docs.mathjax.org/en/latest/tex.html#tex-support)
```javascript
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
  tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}
});
</script>
// 更完整的代码
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    extensions: ["tex2jax.js"],
    jax: ["input/TeX", "output/HTML-CSS"],
    tex2jax: {
      inlineMath: [ ['$','$'], ["\\(","\\)"] ],
      displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
      processEscapes: true
    },
    "HTML-CSS": { fonts: ["TeX"] }
  });
</script>
```
- 延迟配置
    - 当配置文件加载完毕MathJax即开始配置过程，所以配置加载于MathJax.js之前
    - 有时却需要延迟配置，例如，将MathJax作为主题的一部分后，希望修改特定网页的配置
    - 通过设定`delayStartupUntil=[options]`参数控制配置与其他加载的启动次序
        - 默认为`none`，意思是不延迟
        - 可选参数`onload`，可阻止MathJax启动配置过程，直到网页的`onLoad`管理器启动，这允许MathJax寻找当前页面中所有的`text/x-mathjax-config`块
        - 可选参数`configured`，可阻止MathJax启动配置过程，直到`MathJax.Hub.Configured()`方法被引用，这允许通过设定`MathJax.Hub.Configured()`的位置，在特定位置重新启动配置过程；如果`MathJax.Hub.Configured()`没有被引用，MathJax将不会启动配置过程
```javascript
// 在<header>中加入
<script type="text/javascript"
   src="path-to-MathJax/MathJax.js?config=TeX-AMS-MML_HTMLorMML&delayStartupUntil=configured">
</script>
// 在<footer>中加入
<script type="text/javascript">
  MathJax.Hub.Configured()
</script>
```
- 配置顺序
    - 从行内`MathJax = {...}`执行`AuthorInit()`
    - 通过`config=`将配置作为脚本参数执行
    - 从行内`MathJax = {...}`执行作者的配置
    - 执行行内脚本主体
    - 如果提交了推迟启动，等待启动信号
    - 执行`text/x-mathjax-config`块
    - 执行所有先前已进入配置队列的配置内容
- 输出方式
    - 使用`HTML-with-CSS`
    - 使用SVG
    - 使用浏览器支持的`MathML`
- 文字支持
    - 支持的种类
        - MathJax TeX
        - STIX General
        - Asana Math
        - Neo Euler
        - Gyre Pgaella
        - Gyre Termes
        - Latin Modern
    - 设定页面文字
        - 使用`&locale=XX`设定页面显示语言
```javascript
<script src="https://example.com/mathjax/MathJax.js?config=TeX-AMS_CHTML&locale=fr"></script>
```
- MathJax.Hub.Config
    - [The core options](https://docs.mathjax.org/en/latest/options/hub.html)
    - [Preprocessor options](https://docs.mathjax.org/en/latest/options/preprocessors/index.html)
    - [Input processor options](https://docs.mathjax.org/en/latest/options/input-processors/index.html)
    - [Output processor options](https://docs.mathjax.org/en/latest/options/output-processors/index.html)
    - [Extension options](https://docs.mathjax.org/en/latest/options/extensions/index.html)
    - [Other options](https://docs.mathjax.org/en/latest/options/other/index.html)
    - [Third-party Extensions](https://docs.mathjax.org/en/latest/options/ThirdParty.html)
```javascript
// 示例
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    extensions: ["tex2jax.js", "Safe.js"],
    jax: ["input/TeX", "output/HTML-CSS"], // 输入和输出形式
    tex2jax: {
      inlineMath: [ ['$','$'], ["\\(","\\)"] ],
      displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
      processEscapes: true
    },
    TeX: {
        TagSide: "left",
        Macros: {
            RR: '{\\bf R}',
            bold: ['{\\bf #1}', 1]
        }
    }
    "HTML-CSS": {
        fonts: ["TeX"] 
    }
  });
</script>
```
- 存储与处理机制
    - MathJax使用`<script>`标签识别数学公式
    - 每个`<script>`标签都有一个`type`属性，用于识别`script`的种类
    - 默认的`type`属性为`type="text/javascript`，只要有该属性，浏览器都将这个`script`作为javascript程序
    - MathJax使用`type="math/tex"`识别TeX和LaTeX表示方法；使用`type="math/mml"`识别MathML表示方法；使用`type="math/asciimath"`识别AsciiMath表示方法
    - 当`tex2jax`、`mml2jax`或者`asciimath2jax`预处理器运行时，即创建包含有上述`type`属性的`<script>`标签，以便MathJax能够进行处理
```javascript
// 处理数学公式的形式
// 行内数学公式
<script type="math/tex">x+\sqrt{1-x^2}</script>
// 整行数学公式
<script type="math/tex; mode=display">
  \sum_{n=1}^\infty {1\over n^2} = {\pi^2\over 6}
</script>
```
- 对MathJax启动顺序的详细介绍见[The MathJax Startup Sequence](https://docs.mathjax.org/en/latest/advanced/startup.html)
- 写MathJax扩展的指引见[Tutorial: Extension writing](https://docs.mathjax.org/en/latest/advanced/extension-writing.html)
- MathJax中使用的变量、对象、类的信息，可查阅[The MathJax API](https://docs.mathjax.org/en/latest/api/index.html)
- MathJax图标引用见[MathJax Badges](https://docs.mathjax.org/en/latest/misc/badges.html)

## 数学符号


## 参考资料
- [MathJax的Github页面](https://github.com/mathjax/MathJax)
- [MathJax的文档](https://docs.mathjax.org/en/latest/start.html)及其[Github地址](https://github.com/mathjax/MathJax-docs)

# 版本记录

# 微博发布
- [ ] 排版
- [ ] MathJax
    - [ ] 机制与配置
    - [ ] 数学符号
    - [ ] 参考资料