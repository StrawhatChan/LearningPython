**本文“发表于微博自媒体”，微博：[@钻石草帽](https://weibo.com/strawhatchan)**

# 概要
**本文采用知识库的方式，记录Visual Studio Code（VSCode）以下各方面的零散知识点：**

1. 在不同系统的安装、卸载、配置
2. 使用技巧
3. 应用过程中遇到的问题及其解决方案

# 安装、卸载和配置
## 安装
- Ubuntu
    - 从[VSCode官方网站](https://code.visualstudio.com/)下载dep包
    - 双击dep包进入Ubuntu Software，点击安装即可，或者打开Teminal，cd至dep包文件夹，使用命令`sudo dpkg -i pkgname.dep`安装

## 卸载
- Ubuntu
    - 进入Ubuntu software找到VSCode，点击删除即可
    - 打开Teminal，使用命令`sudo dpkg -r pkgname.dep`卸载

## 配置
配置内容包括快捷键、插件、主题、图标主题。全局可用配置：
- 快捷键
    - 方法1：`Ctrl + Shift + P`，输入`Preferences:open keyboard shortcut`按照偏好设置即可
    - 方法2：`Ctrl + Shift + P`，输入`Extensions: install Extensions`，跳转至扩展搜索页，搜索关键词*keyboard*，根据偏好选择安装，完成安装后重新载入（reload）VSCode
- 插件
    - 如快捷键方法2中的描述，按照需求搜索插件安装、重载
- 主题
    - 使用默认主题，`Ctrl + Shift + P`，输入`Preferences:color theme`选择内置主题
    - 使用主题插件，方法如前述，推荐使用`Material Theme`
- 图标主题
    - 使用默认图标主题，`Ctrl + Shift + P`，输入`Preferences:file icon theme`选择内置主题
    - 使用主题插件，方法如前述，推荐使用`VSCode Great Icons`

### 项目配置
- settings.json
    - `Ctrl + Shift + P`，输入`Preferences:open settings`，点击打开settings设置界面，VSCode将在项目根目录中创建名为`.vscode`的文件夹，如果已存在该文件夹则不重复创建，并在该文件夹中创建名为`settings.json`的文件，可根据需要设置该文件以覆盖默认设置，比如设置Python解释器路径
- launch.json
    - 打开DeBug界面，点击界面上方齿轮`open launch.json`，VSCode将在项目根目录中创建名为`.vscode`的文件夹，如果已存在该文件夹则不重复创建，并在该文件夹中创建名为`launch.json`的文件，可根据需要设置DeBug

### Python
- 插件
    - Python
    - Markdown All in One
    - 其他根据需要安装
- settings.json
    - 设置Python解释器路径，或者`Ctrl + Shift + P`，输入`Python:select interpreter`，选择偏好的Python解释器，并由VSCode自动创建`.vscode`的文件夹和`settings.json`文件
```json
// 设置Python解释器路径，Ubuntu系统示例，其他系统或环境找到路径即可
"python.pythonPath": "/usr/bin/python3",
```
- launch.json
    - 可根据需要调试的对象设置
```json
// 部分调试内容及选项示例如下
{
    "version": "0.2.0",
    "configurations": [
        
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "stopOnEntry": false, // 按F5直接调试，如改为ture则按2次F5开始调试
            "program": "${file}"
        },
        {
            "name": "Python: Terminal (integrated)",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        },
        {
            "name": "Python: Terminal (external)",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "externalTerminal"
        },
        {
            "name": "Python: Django",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/manage.py",
            "args": [
                "runserver",
                "--noreload",
                "--nothreading"
            ],
            "debugOptions": [
                "RedirectOutput",
                "Django"
            ]
        },
        {
            "name": "Python: Module",
            "type": "python",
            "request": "launch",
            "module": "module.name"
        },
        {
            "name": "Python: All debug Options",
            "type": "python",
            "request": "launch",
            "pythonPath": "${config:python.pythonPath}",
            "program": "${file}",
            "module": "module.name",
            "env": {
                "VAR1": "1",
                "VAR2": "2"
            },
            "envFile": "${workspaceFolder}/.env",
            "args": [
                "arg1",
                "arg2"
            ],
            "debugOptions": [
                "RedirectOutput"
            ]
        }
    ]
}
```
- linting
    - VSCode默认使用Python的pylint包，如未安装，则需要打开Terminal输入`(pip | pip3) install pylint`安装
    - 除pylint外，还有`Flake8`等常用linter，可查阅[VSCode文档中的Python-linting](https://code.visualstudio.com/docs/python/linting)获取详细列表及VSCode的默认配置
    - 如果安装多个linter，`Ctrl + Shift + P`，输入`Python:select linter`选择偏好的linter即可
# 使用技巧


# 问题及解决方案