> **本文发表于“微博自媒体”，微博：[@钻石草帽](https://weibo.com/strawhatchan)**

# 概要
**本文采用知识库的方式，记录Ubuntu以下各方面的零散知识点：**
1. 单、双系统安装
2. 文件夹结构及其作用
3. 命令的作用及其理解
4. 系统设置以及对系统的理解
5. 常用软件和工具
6. 应用过程中遇到的问题及其解决方案

# 系统安装



# 文件夹结构
- hosts
    - 文件位置：/etc/hosts
    - 通过在终端输入`sudo vi /etc/hosts`对hosts文件进行修改
    - 访问wikipedia通过修改hosts文件进行直连，只有在直连时才能编辑页面
        - 198.35.26.96 zh.wikipedia.org  #中文维基百科
        - 198.35.26.96 zh.m.wikipedia.org  #中文维基百科移动版
        - 198.35.26.96 zh-yue.wikipedia.org  #粤文维基百科
        - 198.35.26.96 zh.wikinews.org  #中文维基新闻

# 文件类型
- .bak
    - `.bak`文件是同名备份文件，即与某个文件名称相同的备份文件，备份时直接添加`.bak`后缀，还原时将文件后缀修改为源文件后缀即可

# 命令
- 网络
    - 停止网络`service network-manager stop`
    - 重启网络`service network-manager restart`
- deb包
    - 安装：`dpkg -i package.deb`
    - 仅删除包：`dpkg -r package`
    - 删除包和配置文件：`dpkg -P package`
    - 列出与包有关的文件：`dpkg -L package`
    - 显示版本：`dpkg -l package`
    - 解包：`dpkg -unpack package.deb`
    - 搜索包内容：`dpkg -S keyword`
    - 列出已安装包：`dpkg -l`
    - 列出deb包的内容：`dpkg -c package.deb`
    - 配置包：`dpkg -configure package`
    - 更多信息可通过在终端中输入`dpkg --help`或`man dpkg`查询


# 系统设置
- shadowsocks创建及开机启动
    - 自建1个`shadowsocks.json文件`放入`etc`目录
    - `shadowsocks.json文件`内容见下
    - 打开开机启动应用，新建1个开机启动项，在命令栏内输入`sudo sslocal -c /etc/shadowsocks.json`

```json
{
    "server": "填写服务器地址",
    "server_port": 填写服务器端口,
    "local_address": "127.0.0.1",
    "local_port": 填写本地端口,
    "password": "填写密码",
    "method": "填写加密方式"
}
```

- sudo免密码
    - 每次使用sudo命令都需要使用密码，为简化操作，配置sudo命令免密
    - 是否输入密码由/etc/sudoers文件控制，该文件的主要配置内容包括：
        - root：`root ALL=(ALL:ALL) ALL`意思是所有要求root权限的操作都必须使用密码
        - admin：`%admin ALL=(ALL) ALL`意思是所有要求admin权限的操作都必须使用密码
        - sudo：`%sudo ALL=(ALL:ALL) ALL`意思是所有要求sudo权限的操作都必须使用密码
    - 编辑该文件的命令为`visudo`，或者cd至/etc文件夹，输入`sudo vi sudoers`
    - 该文件是从上至下依次读取，如果需要修改配置，应当注意添加配置的位置，避免添加的配置被后续配置覆盖
    - 为了让特定用户，比如自己，在使用sudo时不需要使用密码（未设置前，sudo密码有效时间为5分钟，即5分钟后必须重新输入），可在sudo后为特定用户添加免密码配置，即在`%sudo ALL=(ALL:ALL) ALL`之后加入`username ALL=(ALL) NOPASSWD:ALL`
    - 修改完成后按Esc，输入`:wq!`强制保存并退出（`:wq!`是vim的操作命令）
- 修改源列表
    - 源列表包含2类
        - 官方源
        - PPA（Personal Package Archives）源，可添加`sudo add-apt-repository ppa:user/ppa-name`，亦可删除`sudo add-apt-repository --remove ppa:user/ppa-name`
    - 源列表通过可编辑的文件存储，文件位置：/etc/apt/sources.list，需要使用`sudo`命令才可修改，例如`sudo gedit /etc/apt/sources.list`
    - 源分为2类
        - 以deb开头的软件源
        - 以deb-src开头的源码（为提高apt-get update速度，通常使用`#`符号将源码注释掉，在需要时再开启）
    - 源地址解析，例如`deb http://cn.archive.ubuntu.com/ubuntu/ bionic main restricted universe multiverse`和`deb-src http://cn.archive.ubuntu.com/ubuntu/ bionic main restricted universe multiverse`
        - deb和deb-src定义源的类型
        - http://cn.archive.ubuntu.com/ubuntu/ 为源URL，可以换成任何源的URL
        - bionic是URL下的disks目录中的文件夹名称，也是Ubuntu 18.04 LTS版本对应的名称，17.10对应artful，16.04对应xenial，14.04对应trusty
        - main restricted universe multiverse代表URL中/disks/bionic-*下的文件夹，如为18.04版本的bionic，则代表bionic文件夹下对应名称的文件夹，如为18.04版本的bionic-security，则代表bionic-security文件夹下对应名称的文件夹，以此类推，其他版本只需修改版本对应的名称即可
        - 总结，PPA地址由3部分构成，“源类型+源地址+源文件夹结构”
    - 将源地址直接添加至sources.list，保存后关闭，在终端运行`sudo apt-get update`使对sources.list的修改生效
    - 另一种简单的但定制型更差的修改方案是通过Ubuntu Software中的Software & Updates选项进行修改，该面板可增减源、配置源文件夹、设定下载服务器等

# 常用软件和工具



# 问题及解决方案
- 单个源文件.bak备份
    - 备份`sudo cp FileName FileName.bak`
    - 还原`sudo cp FileName.bak FileName`


