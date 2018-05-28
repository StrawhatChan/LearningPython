> **本文发表于“微博自媒体”，微博：[@钻石草帽](https://weibo.com/strawhatchan)**

# 概要
**本文采用知识库的方式，记录Ubuntu以下各方面的零散知识点：**
1. 单、双系统安装
2. 文件夹结构及其作用
3. 命令的作用及其理解
4. 系统设置以及对系统的理解
5. 常用软件和工具
6. 应用过程中遇到的问题及其解决方案

# 第1部分 系统安装



# 第2部分 文件夹结构



# 第3部分 命令
- 网络
    - 停止网络`service network-manager stop`
    - 重启网络`service network-manager restart`



# 第4部分 系统设置
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


# 第5部分 常用软件和工具



# 第6部分 问题及解决方案



