**本文“发表于微博自媒体”，微博：[@钻石草帽](https://weibo.com/strawhatchan)**

# 概要
**本文采用知识库的方式，记录Python官方或第3方以下各方面的零散知识点：**

1. 在不同系统中安装、卸载等程序层面的操作
2. 库、包、模块、函数、类型等的安装、卸载、定义、应用、理解
3. 编程范式与技巧
4. 应用过程中遇到的问题及其解决方案

# 安装、卸载与使用




# BuiltIn
## BuiltIn函数
1. enumerate
	- 作用：以迭代的方式为序列中的所有元素生成带序号的tuple
	- 调用：`enumerate(iterable, 'start='number)`
	- 说明：`iterable`必须是支持迭代的对象，例如list；`start=`为可选的固定字符；`number`为数字，如0、1、2等
```python
# 输出tuple
>>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> print(list(enumerate(seasons)))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>> print(list(enumerate(seasons，start=3)))
[(3, 'Spring'), (4, 'Summer'), (5, 'Fall'), (6, 'Winter')]
# 输出序号列表(注意for后的下划线)
>>> xs = [i + 0.1 for i, _ in enumerate(seasons)]
>>> print(xs)
[0.1, 1.1, 2.1, 3.1]
# 输出值列表(注意for后的下划线)
>>> ys = [season + '+' for _, season in enumerate(seasons)]
>>> print(ys)
['Spring+', 'Summer+', 'Fall+', 'Winter+']
```
2. 




# 第3方库-matplotlib
记录matplotlib库的安装与使用。
## 安装
### Ubuntu系统
1. 直接用`apt-get`安装，在终端输入`sudo apt-get install python3-matplotlib`
2. 使用pip（Python包管理工具）安装
	- 在终端输入`(pip | pip3) install matplotlib`，其中，`pip`命令安装Python2下的包，`pip3`命令安装Python3下的包
	- pip安装后无法直接使用`matplotlib`库，还需要安装依赖，终端输入`sudo apt-get build-dep python-matplotlib`并根据提示完成安装，更多细节可查阅[matplotlib官网文档](https://matplotlib.org/contents.html)

## 使用
### 显示中文图例

### pyplot
1. plot
	- 作用：画2维曲线
	- 调用：`pyplot.plot([x], [y], [options])`
	- options:`color`, `marker`, `linestyle`
2. title
	- 作用：添加图标题
	- 调用格式：`pyplot.title("TitleName")`
3. ylabel
	- 作用：添加y轴标记
	- 调用：`pyplot.ylabel("yLeabelName")`
4. show
	- 作用：显示所作的图例
	- 调用：`pyplot.show()`





# 参考资料
1. Grus, J., 2016: Data Science from Scratch. O'Reilly Media.
2. Matthes, E., 2015: Python Crash Course. San Francisco: No Starch Press.
3. [Python官方帮助文档](https://docs.python.org/3/)