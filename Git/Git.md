> **本文“发表于微博自媒体”，微博：[@钻石草帽](https://weibo.com/strawhatchan)**

# 概要
> **本文采用知识库的方式，记录Git以下各方面的零散知识点：**

1. 在不同系统中安装、卸载等程序层面的操作
2. 命令的作用及其理解
3. 工作流的组织
4. 应用过程中遇到的问题及其解决方案

# Git安装、卸载与使用



# Git命令



# Git工作流



# 问题及解决方案
- 合并分支
    - 情景描述：在VSCode中使用Terminal将tlv2分支Fast-forward合并后，将master推送到master，并继续修改tlv2分支且提交，但在push时VSCode提示该分支不存在upstream分支
    - 原因分析：可能是使用`git merge`合并分支并将master推送后，本地tlv2分支与远程tlv2分支之间的追踪关系被解除了
    - 解决方案：使用`git checkout <LocalBranchName>`切换`HEAD`指针指向，再使用`git branch -u <RemoteShortName>/<BranchName>`命令，在本地分支与远程分支之间重新建立追踪关系
- GitBook展示数学公式（commit：测试数学公式#7）
    - 情景描述：在`VSCode Version 1.23.1`中安装`Markdown All in One`插件，以便利用`$ math $`展示行内数学，以及利用`$$ math $$`使用整行数学公式，但在2018年05月24日完成“BookPython_DSS.md”提交并推送至Github和Gitbook后，发现在Github和Gitbook上无法展示数学公式
    - 原因分析：
        - gitbook.com暂时不支持数学公式，也不支持通过插件展示数学公式
        - 只有legacy.gitbook.com可以通过`mathjax`或者`katex`插件支持数学公式
        - 上述2个gitbook的插件需要使用2个`$`作为行内或块数学公式的标识符
        - VSCode中`Markdown All in One`插件使用`$ math $`支持行内公式，使用`$$  $$`支持块公式
        - 尽管`katex-plus`插件与VSCode中`Markdown All in One`插件的用法相同，但对于markdown语法中包含在行代码中的`$`符号可能出现识别错误
    - 解决方案：
        - 将托管于gitbook.com的书迁移至legacy.gitbook.com，并与github同步
        - 在legacy.gitbook.com中使用book.json文件安装并激活`mathjax`插件
        - 在VSCode中编辑数学公式时使用单个`$`符号展示数学公式，以便通过预览查看公式
        - 当全部编辑完成时，在VSCode中选中`$`符号，并使用`Ctrl+Shift+L`编辑所有`$`符号，使单个`$`符号变更为2个`$`符号，以使数学公式能在legacy.gitbook.com中展示