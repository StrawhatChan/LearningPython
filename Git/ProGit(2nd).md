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
	- 使用`cat .gitignore`在项目根目录下浏览`.gitignore`文件
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
		- 使用`git remote set-url <RemoteShortName> <httpsURL | sshURL>`变更本地分支与远程分支的传输协议，例如以前为`https://`可修改为`SSHurl`
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
	- Git中有2种整合分支的方式，一种是Merge，另一种是rebase
	- 假设A和A1分支均源自同一个父节点，目标是修改A1内容后须将A和A1合并；使用merge的机制是：创建1个新节点，指向A的指针调整为指向新节点，A1继续存在且原A1指针仍指向A1；rebase的机制见下，它与merge的机制不同，但结果相同，并且比merge有更清晰的历史
		- 将`HEAD`指针指向A1
		- 使用`git rebase A`创建1个新节点，A1消失，指向A1的指针调整为指向新节点，原A指针仍指向A
		- 将`HEAD`指针指向A
		- 使用`git merge A1`执行fast-forward合并，完成合并后，A和A1的指针均指向新节点
		- 删除A1分支
	- 假设A1是A的分支，A2是A1的分支，3个分支都开发了几个版本，现希望保留A1分支，但将A1以A为基础链至A分支之后，采用以下步骤实现：
		- 使用`git rebase --onto A A1 A2`设定上述变基
		- 将`HEAD`指针指向A
		- 使用`git merge A2`将A2分支变成以A为基础，同时将A分支指针指向的对象调整为A2分支指针指向的对象
		- 如果在此基础上还希望将A1分支的基础变为A，使用`git rebase A A1`设置变基
		- 将`HEAD`指针指向A
		- 使用`git merge A1`实现变基，同时将A分支指针指向的对象调整为A1分支指针指向的对象
		- A1和A2分支已无价值，删除
	- 在多人合作的项目执行变基，有可能让其他使用者因不清楚发生了什么而产生困惑，这是变基的一项风险；如果认为可能遇到这种情况，通过使用`git fetch`和`git rebase <RemoteShortName>/<BranchName>`命令或者直接使用`git pull --rebase`命令，Git将通过对比提交的SHA-1值判断：1.哪些是我们独立的分支；2.哪些是没有合并的提交；3.哪些没有被写入目标分支；4.将前述判断应用至`<RemoteShortName>/<BranchName>`的上端
	- 必须注意，变基将改变repository的提交历史，是在抹掉部分修改历史，是否执行变基取决于你对提交历史的理解，如果认为提交历史是已发生事项的完整记录，则不应使用变基，因为它会抹掉历史；如果认为提交历史只是完成项目的故事记录，仅用于说清楚项目故事，则应该使用变基，以使故事变得简洁明了

## 第4章 Git的服务器应用
1. 协议（protocols）：Git利用4种不同的协议传输数据，分别是Local、HTTP、Secure Shell（SSH）和Git
	- 使用`git clone ["file://"]<LocalFilePath>`克隆本地项目，比如，`git clone /srv/git/project.git`或者`git clone file:///srv/git/project.git`，其中`file://`类似`http://`
		- 使用`git remote add <LocalShortName> <LocalFilePath>`将本地repository添加至Git项目，即可像操作远程项目一样操作本地项目
	- 使用`git clone [http:// | https://]`克隆HTTP或HTTPs协议下的项目
	- 使用`git clone ssh://[user@]server:project.git`克隆SSH协议下的项目
2. SSH权限控制
	- 为每个成员设置账户
	- 创建1个git用户，将每个成员的SSH公钥放入`~/.ssh/`文件夹中，将写入权限授给每个用户
	- 从LDAP服务器或其其他中心化控制器为SSH服务器分发写入授权
3. 生成SSH钥匙对
	- 使用`ssh-keygen [options] "your_email@example.com"`命令后根据提示生成SSH钥匙对
	- 生成的钥匙对为`PrivateKeyName`和`PublicKeyName.pub`，其中`PrivateKeyName`与`PublicKeyName`名称相同，区别在于，公钥有`.pub`后缀，私钥没有
	- 钥匙对如果没有存储在`~/.ssh`文件夹中，可将钥匙对剪切至该文件夹；在Ubuntu系统中，`~/.ssh`的路径全称为`/home/username/.ssh`
	- 在不同操作系统中生成SSH钥匙对的细节可查阅[Github帮助](https://help.github.com/articles/generating-ssh-keys)
4. 创建SSH服务器并授权的步骤
	- 创建1个新的git用户
		- `sudo adduser git`
		- `su git`
		- `cd`
		- `mkdir .ssh && chmod 700 .ssh`
		- `touch .ssh/authorized_keys && chmod 600 .ssh/authorized_keys`，其中，`authorized_keys`可换成其他名称
	- 将所有公钥全部复制到`~/.ssh/authorized_keys`文件夹中
	- 设置空的repository
		- `cd <GitPath>`
		- `git init -bare`
	- 假设其他用户做了修改，需要将修改推送到刚刚创建的SSH中，在其他用户在他们本地做了提交后
		- 使用`git remote add origin git@gitserver:<GitPath>`添加新创建的远程项目
		- 使用`git push origin master`将提交推送至SSH服务器上
	- 上述操作同时赋予所有授权用户登陆SSH服务器并获取Shell的权限，为禁止其登陆服务器并获取shell，只允许这些用户对repository进行操作，则执行以下操作
		- 安装`git-shell`工具
		- 使用`which git-shell`寻找位置
		- 将git-shell文件复制到`/etc/shells`文件夹中，如果没有`shells`文件夹，则自行创建
		- 使用`sudo chsh <UserName> -s <shell>`禁止用户登陆SSH服务器并获取shell
		- 使用`git help shell`获取更多帮助信息
5. 其他服务器类型：
	- Daemon，明文传输，通过`git daemon`命令可设置明文传送的Git协议
	- Smart HTTP，既可以像SSH授权传输数据，也可以像`git://`或者`daemon`明文传输数据
	- GitWeb，是基于web的可视化Git界面，依赖于`lighttpd`或者`webrick`这类轻量级的web服务，通常情况下，Linux系统安装了`lighttpd`，可在项目文件夹中使用`git instaweb --httpd=webrick`运行
	- GitLab，是开源的Git服务方案，基于数据备份的web应用，安装、设置、维护等信息可查阅[Gitlab官方网站](https://gitlab.com/)
	- 如果不想自建服务器，也可以使用第3方服务器，第3方服务器列表可查阅[Git wiki](https://git.wiki.kernel.org/index.php/GitHosting)；[Github](https://github.com/)是最大的第3方Git托管服务器

## 第5章 Distributed Git
本章通过对“私人项目、2人、单一项目开发”，“私人项目、多人、无写入权限、并行开发”，“公共项目、多人、无写入权限、并行开发”，“公共项目、多人、拥有所有权限的项目主导、并行开发”这4类情景的描述，与工作流相结合，介绍Git的使用。其中，“公共项目、多人、无写入权限、并行开发”介绍对Github上托管的公共项目作出贡献的方法。
1. 分布式工作流能在Git上发生作用的2个关键特征：
	- 多团队可平行开发；多个团队或开发人员可平行开发，并且可在开发后进行合并
	- 控制多人同时推送；假设多人获取同一个repository并同时开发该项目后，如果其中1人已经将开发内容推送至服务器，Git将提示另1人无法直接推送其独立的开发内容，只有先拉取服务器上的最新版本内容才可继续推送
	- 支持各种合作模式；每个开发人员同时有多个公共repository，对于其自身的repository拥有读、写权限，而对于其他的仅有读取权限，如果开发人员需要对他人的repository进行开发，可先克隆、再修改、然后推送至克隆的repository、最后向原作者发送拉取和合并请求，理论上说，任何项目都可以由所有开发人员进行开发，既可以有管理层级，也可以没有
2. 项目贡献
	- 描述项目贡献效率的变量有4个
		- 活跃的贡献者数量，包括贡献者人数和贡献频次2个方面
		- 工作流选择
		- 提交权限
		- 可能的外部贡献方法
	- Git项目组在[Git的Github页面](https://github.com/git/git)下的`Documentation/SubmittingPatches`文件中提供了提交补丁的指引
3. `rerere`特性
	- `rerere`表示“reuse recorded resolution”
	- 是合并冲突的解决方案
	- 工作机制为，Git记录一系列成功合并的过程，如果观察到某个冲突是曾经解决过的冲突，`rerere`将直接使用最近一次的解决方案消除冲突，而不会对冲突做任何提示
	- 使用`git config --global rerere.enabled true`命令启用`rerere`特性
	- 使用`git rerere`命令进行缓存
4. 版本签名
	- 使用`git tag -s <VersionNumber> -m 'VersionMessage'`签名标签
	- 签名标签需要使用`GnuPG`，一个基于RSA算法的可加密、可签名钥匙对
		- 使用`sudo apt-get install gnupg`安装`gnupg`
		- 使用`gpg --gen-key`生成钥匙对，文件存储于`~/.gnupg`文件夹内
		- 上传公钥至服务器（例如[Ubuntu服务器](http://keyserver.ubuntu.com/)、[PGP Public Key Server](https://pgp.key-server.io/)、[MIT服务器](https://pgp.mit.edu/)、[赛门铁克服务器](https://keyserver.pgp.com/vkd/GetWelcomeScreen.event)，如果只用于在Git中签名标签，则无需上传服务器，因为Git自带分发公钥的解决方案，即将公钥作为blob保存在repository中，并添加标签直接指向这些内容），然后使用`gpg --fingerprint [用户ID | 邮件地址]`生成公钥指纹
		- 使用`gpg --import <PrivateKeyName>`导入私钥
		- 获取更多关于`gpg`的帮助使用`gpg --help`
		- GnuPG的介绍和常用功能可参考[阮一峰的博客文章](http://www.ruanyifeng.com/blog/2013/07/gpg.html)
	- 使用`gpg --list-keys`查看已有密钥信息
	- 使用`gpg -a --export <密钥特征值> | git hash-object -w --stdin`为GPG密钥生成1个hash对象指向该密钥
	- 使用`git tag -a <TagName> <hashValue>`将标签指向密钥hash值
	- 使用`git push --tags`将所有标签推送至远程分支
	- 使用`git show <TagName> | gpg --import`验证标签
5. 其他命令
	- 使用`git describe <BranchName>`将返回最近提交的标签、该提交以前的提交次数以及提交的SHA-1值
	- 使用`git archive <BranchName> --prefix='<ProjectName>' | gzip > 'ArchiveName'.tar.gz`或者`git archive <BranchName> --prefix='<ProjectName>' --format=zip > 'ArchiveName'.zip`
	- 使用`git shortlog --no-merges <BranchName> --not <VersionNumber>`列出所有提交的摘要

## 第6章 Github
本章主要介绍Github的使用，采用“遇到问题再解决问题”的学习策略，需要提及的是Github基本流程：
- Fork项目
- 从master创建1个分支
- 项目开发
- 将分支推送至自己的Github项目
- 在Github上打开1个拉取请求（pull request）
- 讨论或者进一步修改并提交
- 项目所有者合并或者关闭拉取请求

## 第7章 Git Tools



## 第8章 Customizing Git



## 第9章 Git and Other Systems



## 第10章 Git Internals











## 版本记录
1. 2018年05月19日，v1.0.0