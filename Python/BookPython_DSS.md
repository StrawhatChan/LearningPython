<!-- Grus, J., 2016: Data Science from Scratch: First Principles with Python. O'Reilly Media. -->
**本文“发表于微博自媒体”，微博：[@钻石草帽](https://weibo.com/strawhatchan)**

**本文为《Data Science from Scratch: First Principles with Python》的读书笔记**

## 重要原则
- 充分理解数据，尽可能测试每一个属性，观察其对相关性的影响，避免辛普森悖论
- 相关不是因果
- 正确理解p-value的价值
- 贝叶斯推断不仅数学原理复杂，而且存在主观性缺陷

## 预备知识
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
		- 本质是质疑统计学中p值的价值，[The Extent and Consequences of P-Hacking in Science](http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002106)这篇文章中给出了p-hacking定义，即通过对数据、统计方法的选择，使统计分析结果从不显著变为显著；另一篇更早的关于p-hacking的文章[Scientific method: Statistical errors](https://www.nature.com/news/scientific-method-statistical-errors-1.14700)发表于《Nature》上；《American Scientist》也有一篇讨论因p-hacking引起可能的统计危机的文章[The Statistical Crisis in Science](https://www.americanscientist.org/article/the-statistical-crisis-in-science#)；美国统计学会也发表一篇名为[Statement on Statistical Significance and P-Values](http://www.amstat.org/asa/files/pdfs/P-ValueStatement.pdf)的声明，确定了使用P值的6条原则。
		- 解决方案：要在审查数据之前确定假设，要在做假设之前整理好数据，牢记p值不是靠直觉得出；替代方案是贝叶斯推断。
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

## 实践提示
- 获取数据
	- 对于csv文件，必须使用二进制模式处理，具体见[Stack Overflow的讨论](http://stackoverflow.com/questions/4249185/using-python-to-append-csv-files)
	- 从HTML中获取数据需要用到以下库
		- [BeautifulSoup库](https://www.crummy.com/software/BeautifulSoup/)
		- [requests库](http://docs.python-requests.org/en/master/)
		- 为使用这2个库，可能需要安装第3方解析器`html5lib`，如需要，使用`pip`命令安装即可
		- [Scrapy](http://scrapy.org/)是网络抓取方面具有更全特性的库
		- 抓取网页信息时必须了解网站对网页抓取的政策，通常置于**robots.txt文件**中，必须认真阅读，特别是不允许抓取的项目以及抓取间隔和数量的限制
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