[Pro Git(2nd)](https://git-scm.com/book/en/v2)
=========================
**Version 2.1.61, 2018-05-15**

## 第0章 结构
1. 章节
	- 第1章（Getting Started）：介绍版本控制系统（Version Control System，VCSs）及其产生和流行的原因；Git下载、安装和配置
	- 第2章（Git Basics）：与Git使用相关的基础知识，包括80%的案例中要经常使用的知识；学会克隆；了解项目历史、修改文件等；
	- 第3章（Git Branching）：Git的杀手级应用：分支模型（branching model）
	- 第4章（Git on the Server）：Git的服务器应用
	- 第5章（Distributed Git）：使用Git完成不同的工作流
	- 第6章（Github）：Github的深度应用
	- 第7章（Git Tools）：Git高级命令
	- 第8章（Customizing Git）：自定义Git环境
	- 第9章（Git and Other System）：处理Git和其他的VCSs
	- 第10章（Git Internals）：深入理解Git的内部机制
2. 附件
	- 附件A（Git in Other Environments）：在不同环境中使用Git的例子
	- 附件B（Embedding Git in your Applications）：像`libgit2`和`JGit`这类提升效率的Git工具
	- 附件C（Git Commands）：Git命令
3. 索引（Index）

## 第1章 Getting Started
1. 版本控制的特征
	- 一个系统
	- 记录文件随时间的变化
	- 可以回溯至特定历史版本
2. 版本控制的类型
	- 本地版本控制系统：从一个文件夹直接复制到另一个文件夹
		- 优点：简单
		- 缺点：容易混淆不同的文件夹；错误覆盖不想覆盖的文件
	- RCS：通过补丁（patchs）实现版本控制
	- 中心化版本控制（Centralized Version Control Systems）：
		- 优点：中心服务器存储所有版本并分配权限；每个人都知道其他人在做什么
		- 缺点：中心服务器宕机，则无法工作；中心服务器数据丢失，则无法恢复数据
	- 分布式版本控制（Distributed Version Control Systems）：复制全部文件至客户端；远程协作；可执行多种类型的工作流；操作本地文件；Git使用`SHA-1 hash`检查所有文件，以使Git知道所有文件的任何修改，同时也意味着不会丢失任何数据，另外一种保证不丢失数据的机制是，Git只向其数据库中增加数据（这与删除文件中的数据是2个完全不同的概念）
3. Git基础
	- Git与其他VCS的区别在于如何理解数据
		- 其他VCS将数据理解为文件和文件随时间的改变
		- Git将数据理解为微型文件系统（miniature filesystem）的快照流（stream of snapshots），即每次提交，Git获取所有文件的快照，并存储快照关系（reference to snapshot），但是，如果文件未发生改变，则Git不保存这些文件，仅保存连接到源文件的链接
	- Git中的3种关键状态
		- Committed意味着数据已安全地存储至本地数据库
		- Modified意味着已修改文件，但尚未将修改后的数据存储至本地数据库
		- Staged意味着已将修改文件的当前版本标记为进入下一个提交快照的状态
	- Git工作流
		- 修改工作树中的文件
		- 选择哪些修改进入下一个提交
		- 提交所有选择的修改
	- Git设置
		- config文件：通常为`/etc/gitconfig`、`~/.gitconfig`、`$XDG_CONFGI_HOME/git/config`或者`$GIT_DIR/config`这4个文件的其中一个或多个，其中，`~/.gitconfig`一般通过命令行设置属性后创建
		- 设置用户：`git config --global user.name <name>`设置用户名，`git config --global user.email <email address>`设置邮箱地址
		- `git help <verb>`或者`man git-<verb>`获取帮助
		- 通过`git <verb> (-h | -help)`获取特定命令简要帮助

## 第2章 Git Basics
1. 获取Git repository的2种方式及其初始化：
	- 将本地文件夹转换为Git repository
		- 在终端命令行中切换至拟初始化文件夹
		- 切换完成后，在终端输入`git init`创建`.git`子文件夹，在这个时点项目中的任何文件尚未被追踪
		- 使用`git add <files>`命令添加需要被追踪的文件，然后使用`git commit`命令提交，此时，版本控制启动
	- 从其他位置克隆已经存在的Git repository
		- 使用`git clone <URL | SSH> (CustomDirName)`语法从指定位置克隆已存在的repository至本地，完成克隆后，文件夹中包含`.git`子文件夹
	- repository中的文件必定处于被追踪和未被追踪这2种状态的一种，而被追踪的文件有未修改、已修改和Staged共3种状态
	- 使用`git status [-s]`命令检测是否被追踪、是否已修改、是否被提交等状态，如果加上`-s`参数，则文件状态可能显示为` M`、`M `、`MM`、`A `、`??`，这5中文件状态标记符号都有2列，第1列表示staging区域，第2列表示工作树的状态，具体含义如下（忽略下划线）：
		- `_M`已修改但未处于staged状态
		- `M_`已修改且已处于staged状态
		- `MM`已修改且已处于staged状态但后续又做了修改且后续修改尚未处于staged状态
		- `A_`新文件且已处于staged状态
		- `??`尚未被追踪
2. 忽略文件
	- 对于某些不需要被自动添加或者显示状态的文件，通过“忽略”的方式使其既不处于被追踪状态，也不处于未被追踪状态
	- 使用`cat .gitignore`在项目根目录下创建`.gitignore`文件
	- 编辑`.gitignore`文件的规则
		- 空白行或者以`#`开头的行将被忽略
		- 标准glob样式（glob patterns）在整个工作树中都起作用，glob样式可以像简单的正则表达式一样在shell中使用，比如，`*`表示0或者更多的字符；`[abc]`表示所有在方括号中的字符；`?`表示任意单个字符；`[0-9]`或者`a/**/z`匹配任意一个在这2个字符之间的字符
		- 以`/`开头避免递归
		- 以`/`结尾表示目录
		- 以`!`否定样式
	- Github汇集了一些常用[.gitignore文件](https://github.com/github/gitignore)
	- 在一些简单的示例中，只在根目录下有`.gitignore`文件，但也可以在子目录中创建`.gitignore`文件，所有的`.gitignore`文件都只应用于该文件及其子文件夹
	- 更多关于`.gitignore`的细节，通过`man gitignore`查阅
3. 常用命令
	- 查阅变动。使用`git diff`命令获取对被追踪文件的完整修改情况，使用`git diff --help`查阅该命令的帮助
	- 提交。如果staging区域已经就绪，即所有新增和已修改的文件均使用`git add`命令添加至staging区域，可使用`git commit`命令进行提交修改，添加`-a`参数可以跳过`git add`部分，直接提交全部已追踪的文件，但必须注意，这一操作可能将不需要提交的文件提交
	- 移除文件。使用`git rm`命令将文件从staging区域移除，下次提交后，文件将不会出现在未追踪文件中；如果仅使用`rm`命令，只是简单地将文件从工作目录中移除，需要将文件加入staging区域并提交后才能达到移除效果；对于已增加至staging区域，但又希望移除的文件，需要添加`-f`参数
	- 修改名称。使用`git mv (<OldName NewName>)`修改文件名称，该命令是3条命令的集合，即`mv`命令（修改名称）、`git rm`命令（将原文件名称从追踪文件中移除）、`git add`将新文件名加入追踪文件中；必须注意，Git不自动追踪文件名称的变化
	- 查阅提交历史。使用`git log [options]`查阅全部提交历史
		- 使用`git log --pretty=format:'"'<自定义格式化内容>'"' [options]`按照自定义格式化输出提交历史，格式化内容代码如下：
		- `%H`提交历史hash
		- `%h`简写的提交历史hash
		- `%T`树hash
		- `%t`简写的树hash
		- `%P`父hash
		- `%p`简写的父hash
		- `%an`作者名称
		- `%ae`作者邮件地址
		- `%ad`作者日期
		- `%ar`作者日期（相对）
		- `%cn`提交者名称
		- `%ce`提交者邮件地址
		- `%cd`提交日期
		- `%cr`提交日期（相对）
		- `%s`主题
	- 撤销提交。使用`git commit --amend`命令将最近1次的提交从提交历史中剔除，并将新的提交放入提交历史中
	- 撤销stage。使用`git reset HEAD <file>`命令将错误放入staging区域的文件移出staging区域
	- 撤销文件修改。使用`git checkout -- <file>`将已修改的文件还原成前次提交状态
4. 远程工作
	- 远程repository是托管在网络上的项目版本，但可以在本地对文件进行修改、提交等操作
	- 使用`git clone <URL | SSH>`远程克隆文件至本地，并将分支命名为`origin`，同时，默认跟踪远程master分支
	- 使用`git remote`进行远程管理
		- 使用`git remote -v`查阅远程项目情况
		- 使用`git remote add <RemoteShortName> <URL>`添加新的远程repository
		- 使用`git remote show <RemoteShortName>`查阅特定远程项目信息
		- 使用`git remote rename <OldName> <NewName>`重命名远程项目名称，该命令同时修改远程追踪分支名称
		- 使用`git remote (remove | rm) <RemoteShortName>`移除远程特定项目，所有该项目下的远程分支和配置都将被删除
	- 使用`git fetch <RemoteShortName>`远程拉取特定分支的全部项目数据，注意，该命令仅下载数据，不会将远程版本与本地版本合并
	- 使用`git pull`远程拉取全部项目数据并与本地版本合并
	- 使用`git push <RemoteShortName> <Branch>`将特定版本推送到远程分支
5. 标签
	- 使用`git tag [-l | --list] [options]`列出标签
	- 标签有2类，一类是不可更改的轻量标签（lightweight），另一类是包含诸多信息的注释标签（annotated）
		- 轻量标签：设置方法为`git tag <TagName>`，即不包含任何`-a`、`-m`等可选项
		- 注释标签：设置方法为`git tag -a <TagName> -m '"'TagMessage'"'`
		- 设置后通过`git show <TagName>`显示标签信息
	- 可随时添加标签，使用`git tag -a <TagName> <hash>`为特定的提交添加标签
	- 远程添加标签，使用`git push <RemoteShortName> <TagName>`为远程特定项目的提交添加标签，如果需要将多个标签同时提交远程端，则使用`git push <RemoteShortName> --tags`
	- 使用`git checkout <TagName>`检查标签，但必须小心使用这种方法，因为，这种方法使repository处于"detached HEAD"状态，该种状态下，所有的修改和提交除非使用hash指定分支进行提交，否则将不属于任何分支，也无法达到
6. 别号（Aliases）
	- 将Git的命令与其他名称连接，以便使用自定义名称使用该命令
	- `git config --global alias.unstage 'reset HEAD --'`该命令的含义是，执行该命令后可使用`git unstage`命令替代`git reset HEAD --`命令

## 第3章 Git Branching
分支的目标是在不阻断开发的前提下，从主干开出一条分支进行开发，避免与主干发生混淆。Git鼓励频繁的分支和合并工作流，正是这一具有杀手级特性的分支模型使Git得以广泛使用。
1. 每个提交将增加2个对象保存至Git的数据库中，1个提交对象和1个树对象；其中，提交对象包含树对象信息，并且提交对象包含的内容都有对应的hash值，具体内容如下：
	- 1个指向所有staged内容的指针（1个包含所有文件的树对象）
	- 指向父提交的1个或多个指针
	- 作者名称、电子邮件地址
	- 提交者输入的关于提交的描述信息
根据上述对提交的理解，Git的分支实质是指向提交的、轻量的、可移动的指针。默认的分支名称为`master`，但仅为普通分支，没有任何特殊意义。
2. 使用`git branch <BranchName>`创建分支，其实质是创建1个指向**当前提交**的新指针
	- Git通过1个名为`HEAD`的特殊指针确定**当前提交**
	- 创建分支后，`HEAD`指针的指向保持不变，不自动跳转至新分支- 使用`git checkout <BranchName>`调整`HEAD`指针指向的分支，调整分支包含2个动作：
		- 将`HEAD`移动至指定分支
		- 当前工作目录变更为指定分支的工作目录，亦即从新版本跳转至旧版本，或者从旧版本跳转至新版本
	- 切换分支前，如果在staging区域存在尚未提交的修改，那么Git将阻止分支切换
还可以采用另一种方法创建分支并同时将`HEAD`调整至该分支，即`git checkout -b <BranchName>`
3. 分支与合并
	- 如果沿着A分支创建A1分支后做修改，并最终将A1分支与A分支合并，这种方式称为Fast-forward，可采用以下步骤实现
		- 使用`git checkout -b A1`创建A1分支并将`HEAD`指针调整至A1
		- 修改A1内容并提交
		- 将`HEAD`指针调整至A
		- 使用`git merge A1`合并A和A1共2个分支，其实质是将A分支指针指向的对象向前移动至A1分支指针指向的对象
		- 由于A和A1这2个分支指针指向的对象完全相同，A1指针已无意义，使用`git branch -d A1`删除A1指针
	- 如果A和A1分支均源自同一个父节点，修改A1内容后须将A和A1合并，这种方式称为Merge，可采用以下步骤实现
		- 使用`git checkout <BranchName>`将`HEAD`指针切换至A分支的父分支，再创建A1分支并将`HEAD`指针调整至A1
		- 修改A1内容并提交
		- 将`HEAD`指针调整至A
		- 使用`git merge A1`合并A和A1共2个分支，其实质是创建A和A1分支合并后的新节点，并将A分支指针指向该新节点，但A1分支指针仍指向A1
		- A和A1分支已合并，A1分支已无价值，删除A1分支
	- 如果2个不同分支都对同一个文件的同一内容做了不同的修改，合并时将发生冲突，可采用以下步骤解决合并冲突
		- 使用`git status`查询产生冲突的位置和原因
		- 通过选择发生冲突一方的内容或者统一冲突内容来解决合并冲突
		- 可以借助`git mergetool`这一图形化工具解决合并冲突
	- 分支管理
		- 使用`git branch`命令查询全部分支，有`*`的分支表示`HEAD`指针指向的当前分支
		- 使用`git branch -v`查询所有分支的最后一次提交
		- 使用`git branch --merged`查询已经合并过（merged into）的分支，使用`git branch --no-merged`查询未合并过的分支
		- 使用`git branch -d <BranchName>`删除分支，使用`git branch -D <BranchName>`强制删除分支
4. 分支工作流
	- 长跑分支（Long-Running Branches）
		- 仅保持1个稳定版本
		- 线性分支工作流
		- 除稳定版本外，其他所有分支都是为了测试
	- 主题分支（Topic Branches）
		- 适用于任意大小的项目
		- 每个分支都是为1个特定目的开发，完成后即删除
		- 多主题同时开发
5. 远程分支
	- 远程关联（Remote Reference）是指向远程repository的指针，包含分支、标签等内容
	- 使用`git ls-remote <RemoteShortName>`或者`git remote show <RemoteShortName>`查阅远程分支信息
	- 远程追踪分支（Remote-Tracking Branches）关联远程分支的状态，Git确保其准确反映远程的repository，就像书签；它的表达形式是`<RemoteShortName>/<BranchName>`
	- 当远程克隆1个repository时，Git创建了1个形如`<RemoteShortName>/<BranchName>`的远程分支指针，同时创建1个本地分支指针并下载远程端文件，以便进行本地操作
	- 如果同时有多个服务器开发当前项目，并且进度不同，可使用`git fetch <RemoteShortName>`拉取不同服务器上的文件，每次拉取都只是为远程分支创建1个与该服务器及其开发版本对应的远程分支指针，而不会在本地存储任何文件
	- 当希望将本地分支传送至拥有写入权限的远程端时，使用`git push <RemoteShortName> <BranchName>`或者`git push <RemoteShortName> <BranchName>:<BranchName>`推送至远程分支
	- 每次向远程推送时可能会被要求输入用户名和密码，为避免每次都都需要输入，可使用`git config --global credential.helper cache`将用户名和密码在内存中保存几分钟
	- 使用`git checkout -b <BranchName> <RemoteShortName>/<BranchName>`或者`git checkout --track <RemoteShortName>/<BranchName>`将任意本地分支作为远程分支的追踪分支（Tracking Branch），其中，追踪的远程分支又称为上有分支（upstream branch），而在追踪分支下使用`git pull`，Git将自动识别fetch和merge的远程分支，并执行fetch和merge这2个操作，应谨慎使用`git pull`，因为它混用2个操作，而不是分别执行2个操作，容易造成混乱；如果希望改变追踪分支的上游分支，则使用`git branch -u <RemoteShortName>/<BranchName>`
	- `@{u}`或者`@{upstream}`与`origin/master`等价
	- 使用`git branch -vv`查询追踪分支的设置情况；在情况信息中`ahead`表示自最近1次fetch开始，本地尚未推送到上游分支的提交数量，而`behind`表示表示自最近1次fetch开始，本地尚未从上游分支拉取的提交数量
	- 使用`git push <RemoteShortName> --delete <BranchName>`删除远程分支，该操作仅删除服务器上的指针，而不是删除服务器上的文件
6. 变基（rebasing）
	- 






## 版本记录
1. v1.0.0