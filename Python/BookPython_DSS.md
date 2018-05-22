<!-- Grus, J., 2016: Data Science from Scratch: First Principles with Python. O'Reilly Media. -->
> **本文“发表于微博自媒体”，微博：[@钻石草帽](https://weibo.com/strawhatchan)**

**本文为《Data Science from Scratch: First Principles with Python》的读书笔记**

-----------------

# 重要原则
- 充分理解数据，尽可能测试每一个属性，观察其对相关性的影响，避免辛普森悖论
- 相关不是因果
- 正确理解p-value的价值
- 贝叶斯推断不仅数学原理复杂，而且存在主观性缺陷
- 机器学习是完成对数据收集、理解、清理和整理后才做的工作

# 预备知识
预备知识的内容结构:
- 概念
- 数学

## 概念
概念的内容结构：
- 数据科学
- 模型
- 机器学习

### 数据科学
- 主要内容是把商业问题转换为数据问题，然后收集数据、理解数据、清理数据、整理数据格式，再执行机器学习

### 模型
- 针对存在于不同变量之间的数学或概率联系的一种规范

### 机器学习
- 概念
	- 创建并使用那些由学习数据而得出的模型，也可以称为预测建模或数据挖掘，目标是用已存在的数据来开发可用来对新数据预测多种可能结果的模型
- 模型分类
	- 可分为有监督的模型（有正确答案可供学习）
	- 无监督模型（没有正确答案）
	- 半监督模型（部分有正确答案）
	- 在线模型（根据新加入数据做持续调整）
- 拟合
	- 拟合的实质是模型构建及其参数估计
	- 过拟合（overfitting，一个训练数据上表现良好，但对任何新数据的泛化能力却很差的模型），明显复杂的模型会导致过拟合，解决方法是使用不同的数据来训练和测试模式，如用三分之二的数据训练，用剩余三分之一的数据测试
		- 出错类型1：如果划分训练数据集和测试数据集的目的是判断模型，训练和测试数据集中的共有模式可能无法泛化至大型数据集上；解决方案是，调整训练模型，或重新划分训练集和测试集
		- 出错类型2：如果划分训练集和测试集的目的不仅仅是判断模型，而是选择模型，并且以“在测试集上表现最好的模型”为选择依据，那么，测试集本质上是另一个训练集，无法达到划分训练集和测试集的目的，解决方案是，将数据划分为3部分，1个用来建模的训练集、1个为在训练好的模型上进行选择的验证集、1个用来判断最终模型的测试集
	- 欠拟合（underfitting，产生的模型在训练数据上没有好的表现）
- 正确性
	- 建立模型做二元判断
		- 有4类可能的结果，即将**预测的真假**和**事实的真假**表示为矩阵，：（预测真，事实真）、（预测真，事实假）、（预测假，事实真）、（预测假，事实假）
		- （预测真，事实假）为统计中的第1类错误，（预测假，事实真）为统计中的第2类错误
		- 为后续说明便利，假设4类结果的判断次数依次为pt、pf、npf、npt
	- 准确率（accuracy）是指在所有判断的次数中判断正确的比例，即（pt + npt）/（pt + pf + npf + npt）
	- 查准率（precision）是指“预测真”的判断准确率pt/（pt + pf）
	- 查全率（recall）是指“事实真”时作出“预测真”的判断比例pt/（pt + npf）
	- FI得分，是指[查准率和查全率的调和平均值](https://en.wikipedia.org/wiki/Harmonic_mean)
	- 模型的选择通常是查准率和查全率之间的权衡，也是第1类错误和第2类错误之间的权衡
- 特征
	- 特征的严肃定义是，提供给模型的任何输入
	- 也可以这样理解，从数据中提取最少的因素来界定所要研究的问题
	- 还可以这样理解，数据如果没有足够特征，则可能欠拟合；如果特征太多，则容易过拟合
- 偏倚和方差
	- 偏倚是指测量值对真值的偏离；方差是指样本各个值对样本平均值的偏离
	- 如果低偏倚和高方差对应过拟合，高偏倚和低方差对应欠拟合
	- 如果模型有高偏倚，则加入更多的特征；如果有高方差，既可以移除特征，也可以获取更多数据
	- 偏倚和方差的权衡是思考过拟合和欠拟合的另一种角度
- 参考资料
	- [Coursera的机器学习课程](https://www.coursera.org/learn/machine-learning)
	- [加州理工学院的机器学习课程](https://work.caltech.edu/telecourse.html)
	- [《The Elements of Statistical Learning》](https://web.stanford.edu/~hastie/ElemStatLearn/)这本数学化的教材

## 数学
- 随机性
- 向量及其运算
- 矩阵及其运算
- 相关分析
- 线性代数
	- 导数的理解与计算
- 概率论
	- 独立性
	- 条件概率
	- 贝叶斯定理
	- 随机变量
	- 连续分布
	- 离散分布
	- 正态分布
	- 密度函数
	- 分布函数
	- 中心极限定理
	- 贝叶斯推断
- 假设检验
	- 零假设与替代假设
		- 零假设H0：代表默认的立场
		- 替代假设H1：代表与零假设对比的立场
	- 显著性：犯第1类错误概率
		- 第1类错误：原假设正确，但拒绝了原假设
		- 第2类错误：原假设错误，但没有拒绝原假设
	- 置信区间：重复很多次实验，其中90%-99%的“真”参数会落在观测到的置信区间内
	- p-hacking
		- 本质是质疑统计学中p值的价值，[The Extent and Consequences of P-Hacking in Science](http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002106)这篇文章中给出了p-hacking定义，即通过对数据、统计方法的选择，使统计分析结果从不显著变为显著；另一篇更早的关于p-hacking的文章[Scientific method: Statistical errors](https://www.nature.com/news/scientific-method-statistical-errors-1.14700)发表于《Nature》上；《American Scientist》也有一篇讨论因p-hacking引起可能的统计危机的文章[The Statistical Crisis in Science](https://www.americanscientist.org/article/the-statistical-crisis-in-science#)；美国统计学会也发表一篇名为[Statement on Statistical Significance and P-Values](http://www.amstat.org/asa/files/pdfs/P-ValueStatement.pdf)的声明，确定了使用P值的6条原则
		- 解决方案：要在审查数据之前确定假设，要在做假设之前整理好数据，牢记p值不是靠直觉得出；替代方案是贝叶斯推断
	- 贝叶斯推断
		- 思路：将未知参数作为随机变量，从参数的先验分布出发，利用数据和贝叶斯定理计算更新后的后验分布，不再对检验本身给出概率推断，而是对参数本身给出概率推断
		- 这种检验方式有争议，部分源于复杂的数学原理，部分源于先验分布的主观性
- 梯度下降（gradient descent）
	- 解决最优化问题，如“最小化模型残差”，适用于从零开始逐步解决问题
	- 梯度理论
		- 梯度在微积分中表示偏导数向量，为计算最大或最小可能值提供方向，在这个方向上，函数增长或减少最快
		- 最大化函数的算法，首先从1个随机初始点开始计算梯度，既可以是最大化方向，也可以是最小化方向，当在梯度方向上跨越一小步后，再从1个新的初始点重复这个过程，直至梯度变得非常小
		- 该算法存在局限；当函数存在全局极值时，该方法可能找到它；但如果存在多个局部极值时，这种方法可能找不到，因为，计算会陷入死循环
	- 梯度实现
		- 以x变动t时，函数差商的极限来定义梯度
		- 初始值的选取可使用随机数
		- 确定移动的步长有3种常用方法：第1种，固定步长；第2种，随时间逐步减小的步长；第3种每一步都通过最小化目标函数的值来选择合适的步长；其中，第3种方法的计算代价最大
	- scikit-learn中有梯度计算模块
- 参考资料
	- [Introduction to Probability](http://www.dartmouth.edu/~chance/teaching_aids/books_articles/probability_book/amsbook.mac.pdf)

# 算法
## K近邻算法
- 最近邻分类（nearset neighbors classification）思想：确定目标后，选择1个或多个维度，参照个体行为被这些维度影响或刻画的程度，观察最接近个体的邻居比观察所有的邻居会得到更好的预测结果
- 模型仅要求某种距离概念以及一种彼此接近的点具有相似性质的假设，没有多少数学假设和复杂处理，这种思想有意忽略大量信息，预测只依赖最接近它的点
- 最近邻算法不能帮助理解所观察到的任意现象的产生机制
- 出现并列结果时的处理方法
	- 随机选择获胜者
	- 根据距离加权并选择加权的获胜者
	- 减少k值直到找到唯一的获胜者
- 高维空间中，因为空间过于巨大，导致最邻近的2个点的距离并不比点和点的平均距离小，这意味着2个点邻近没有价值
- [scikit-learn库中有许多邻近模型](http://scikit-learn.org/stable/modules/neighbors.html)

## 朴素贝叶斯算法
- 利用贝叶斯定理计算条件概率
- 基本假设是，各条件之间相互独立（这是一个极端假设）
- 由于该算法涉及接近于0的浮点数计算，而计算机不擅长处理这类浮点数，也就是可能产生下溢（underflow）问题，因而经常使用$e^{log}$的等效形式
- 伪记数（pseudo count）
	- 当某个条件在训练集中不出现时，将会导致该条件的条件概率永远为0，使用伪记数作为平滑技术避免这种情况的发生
	- 通过$P(X_i|S) = \frac{(k + \text{含有某个条件的数量})}{(2k + \text{总数量})}$公式实现，$P(X_i|\lnot S)$采用类似的处理方法
- [scikit-learn库](http://scikit-learn.org/stable/modules/naive_bayes.html)提供了一个名为BernoulliNB的模型，可实现朴素贝叶斯算法以及基于该算法的变种

## 简单线性回归


# 实践提示
- 获取数据
	- 对于csv文件，必须使用二进制模式处理，具体见[Stack Overflow的讨论](http://stackoverflow.com/questions/4249185/using-python-to-append-csv-files)
	- 从HTML中获取数据需要用到以下库
		- [BeautifulSoup库](https://www.crummy.com/software/BeautifulSoup/)
		- [requests库](http://docs.python-requests.org/en/master/)
		- 为使用这2个库，可能需要安装第3方解析器`html5lib`，如需要，使用`pip`命令安装即可
		- [Scrapy](http://scrapy.org/)是网络抓取方面具有更全特性的库
		- 抓取网页信息时必须了解网站对网页抓取的政策，通常置于**robots.txt文件**中，必须认真阅读，特别是不允许抓取的项目以及抓取间隔和数量的限制
	- 语料库
		- [SpamAssassin垃圾邮件公共语料库](https://spamassassin.apache.org/publiccorpus/)是一个关于垃圾邮件的语料库
- 应用程序接口（Application Programming Interface，API）
	- 允许请求结构化数据
	- 通常需要验证，但也有不需要的，例如Github
	- 寻找API
		- 查阅特定网站的开发者部分或API部分，并以*python__api*搜索相应的库，例如`Rotten Tomatoes`库，以及针对*Klout*、*Yelp*、*IMDB*等多个API封装
		- 查阅有Python封装的API列，可参阅[Python API](http://www.pythonapi.com/)和[Python for Beginners](http://www.pythonforbeginners.com/development/list-of-python-apis/)
		- 查阅不一定有Python封装的API名录，可查阅[Programmable Web](http://www.programmableweb.com/)
- HTTP
	- 因为HTTP是一种转换文本协议，通过API请求的数据需要串行化（serialized）地转换为字符串格式，需要使用JavaScript对象符号，即JavaScript Object Notation，JSON），它与字典很相似，通过引入Python的`json`模块，可以将JSON对象反串行化（deserialized）为Python的对象；如果通过API获取的数据是XML格式，则可以用`BeautifulSoup`从中获取数据
- 日期解析
	- 由于存在多种日期格式，并且Python自身的日期解析器并不强调，需要安装其他包，比如`dateutil`
- 研究问题的步骤
	- 明确需要研究的问题
	- 获取数据
	- 探索数据（作图、转换数据类型、查看变化）
	- 整理数据（分组或聚类、降维）
	- 建模求解
	- Pandas是Python清理、整理、处理和利用数据的主要工具，**Python for Data Analysis**是学习Pandas的最好途径

# 微博发布
- [x] 重要原则
- [x] 预备知识
- [ ] 算法
- [ ] 实践提示