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