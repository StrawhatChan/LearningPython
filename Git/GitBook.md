> **本文“发表于微博自媒体”，微博：[@钻石草帽](https://weibo.com/strawhatchan)**

> **本文采用知识库的方式，记录GitBook以下各方面内容：**

1. 在不同系统中安装、运行等程序层面的操作
2. 配置、命令、插件、主题等的作用及其理解
3. 在Gitbook.com上的应用
4. 应用过程中遇到的问题及其解决方案

# 安装与运行
- 安装
    - 首先安装`npm`
    - 完成`npm`的安装后使用`npm install gitbook-cli -g`安装Gitbook，其中`gitbook-cli`是Gitbook的一个命令行工具, 通过它可以在电脑上安装和管理Gitbook的多个版本
- 运行
    - 初始化。使用`gitbook init`对书籍初始化
    - 生成HTML文件。使用`gitbook build`生成书籍html文件，所有文件均存储于新建的`_book`文件夹中
    - 运行服务。使用`gitbook serve`运行服务器，服务器地址为`http://localhost:4000/`
    - 调试。使用`gitbook build --debug`输出错误信息
- 更新与卸载
    - 更新。使用`gitbook update`更新至最新版本
    - 卸载。使用`gitbook uninstall <VersionNumber>`卸载对应版本的gitbook

# 配置
## 目录结构
项目或书籍的根目录下包含`book.json`、`README.md`、`SUMMARY.md`、`GLOSSARY.md`和各部分或章节文件或文件夹。
- book.json
- README.md
    - 对整个项目或书籍的描述，以及其他想要加入的内容
- SUMMARY.md
    - 书籍目录
    - 首行`# Summary`，用于标识目录
    - 以`* [标题](文件位置)`的形式写明每一条目录及其引用的文件
    - 以索引层级标识目录的隶属关系
    - 每个部分可以使用标题或者`----`分隔符进行划分

```
# Summary

### Part I
* [Introduction](README.md)
* [Writing is nice](part1/writing.md)
* [GitBook is nice](part1/gitbook.md)

### Part II
* [We love feedback](part2/feedback_please.md)
* [Better tools for authors](part2/better_tools.md)

----

* [Last part without title](part3/title.md)
<!-- 其中，”part1/“、”part2/“、”part3/“表示不同的文件夹 -->
```

- GLOSSARY.md
    - 名词解释文件
    - 用于索引书中提到的名词
    - 使用二级标题标识每一个名词，每个标题下的正文为名词解释的内容  

```
## CDN
CDN是Content Delivery NetWork的首字母缩写，主要功能是在不同的地点缓存内容，通过负载均衡技术，将用户的请求定向到最合适的缓存服务器上去获取内容，以就近访问的方式加速用户对网站的访问，解决Internet网络拥堵状况，提高用户访问网络的响应速度

## SVG
SVG是Scalable Vector Graphics的首字母缩写，译为可缩放矢量图形，它是一种图形格式，这种图形格式允许将图形描述为图形对象的集合，例如行、矩形等，而不是颜色像素
```

- 各部分或章节文件或文件夹
    - 所有的md文件都可以放在根目录下
    - 也可以用文件夹管理书籍的各个部分，如果使用文件夹管理，在`SUMMARY.md`文件中必须标识文件路径

## book.json配置
```json
// book.json示例
{
    "title": "TecLearning",
    "author": "Strawhat Chan",
    "description": "记录Python、算法和量化的学习记录",
    "language": "zh-hans",
    "gitbook": ">=3.2.3",
    "root": ".", // 指定根目录文件夹
    "links":{
        "sidebar": {
            "微博": "https://weibo.com/strawhatchan"
        }
    },
    "plugins": ["-katex-plus",
                "mathjax"
                ]
}
// language属性包含：en, ar, bn, cs, de, en, es, fa, fi, fr, he, it, ja, ko, no, pl, pt, ro, ru, sv, uk, vi, zh-hans, zh-tw
// styles属性的设置
"styles":{
    "website": "styles/website.css",
    "ebook": "styles/ebook.css",
    "pdf": "styles/pdf.css",
    "mobi": "styles/mobi.css",
    "epub": "styles/epub.css"
}
// pluginsConfig属性的设置
"pluginsConfig": {
    "fontsettings": {
        "theme": "sepia",
        "family": "serif",
        "size": 1
    }
}
```

# 插件
## 插件的结构
Gitbook的插件建立在`Node modules`之上，`package.json`和`index.js`是插件的2个关键文件
### package.json
- 该文件有2个作用
    - 声明依赖、版本、所有者及其他运行插件的信息
    - 包含配置信息的细节内容，这些内容在`gitbook`参数中定义
- 插件名称必须以`gitbook-plugin-`开头
- `engines`必须包含`gitbook`的版本信息
- 该文件遵循[JSON-Schema指引](http://json-schema.org/)，更多信息可阅读[NPM documentation](https://docs.npmjs.com/files/package.json)
- package.json文件示例如下

```json
{
    "name": "gitbook-plugin-mytest",
    "version": "0.0.1",
    "description": "This is my first GitBook plugin",
    "engines": {
        "gitbook": ">3.x.x"
    },
    "gitbook": {
        "properties": {
            "myConfigKey": {
                "type": "string",
                "default": "it's the default value",
                "description": "It defines my awesome config!"
            }
        }
    }
}
```

### index.js
- `index.js`是插件运行的主要入口
- `index.js`文件示例如下

```js
module.exports = {
    // Map of hooks
    hooks: {},

    // Map of new blocks
    blocks: {},

    // Map of new filters
    filters: {}
};
```

## 发布插件
- Gitbook插件可在[NPM](https://www.npmjs.com/)上发布
- 发布插件必须在[npmjs.com](https://www.npmjs.com/)上创建账户
- 通过命令`npm publish`发布

## 私有插件
- 私有插件可托管于Github上，通过`git URLs`调用
- `git URLs`调用的方式为`myplugin@git+https://user@hostname/owner/project.git#VisionNumber`
    - `myplugin`表示为引入插件设定的名称
    - `@git+`为固定字符
    - `https://user@hostname/owner/project.git`为插件项目的HTTP地址
    - `#VisionNumber`表示版本号
- `git URLs`引用文件的一般的形式为`git+https://user@hostname/owner/project.git/file#commit-ish`
    - `file`为包含路径的文件名
    - `#`为必要的符号
    - `commit-ish`为标签、sha或者分支名称

# Gitbook.com应用


# 问题及解决方案


# 版本记录


# 微博发布
- [ ] 安装与运行
- [ ] 配置
    - [ ] 目录结构
    - [ ] book.json配置
- [ ] 插件
- [ ] Gitbook.com应用
- [ ] 问题及解决方案