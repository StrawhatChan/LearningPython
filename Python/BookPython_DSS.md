<!-- Grus, J., 2016: Data Science from Scratch: First Principles with Python. O'Reilly Media. -->
**本文“发表于微博自媒体”，微博：[@钻石草帽](https://weibo.com/strawhatchan)**

**本文为《Data Science from Scratch: First Principles with Python》的读书笔记**

# BuiltIn
## BuiltIn函数
- enumerate
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
- zip
	- 作用：根据不同迭代对象中相同的索引，以迭代的方式为序列中的所有元素生成tuple
	- 调用：`zip(*iterables)`
	- 说明：`*iterables`表示多个支持迭代的对象，所有对象不需要有相同的长度，根据相同索引并按照其中最少的索引生成tuple，如果其中任意1个迭代对象为空，则生产空tuple
```python
# 迭代对象长度相同
>>> x = [1, 2, 3]
>>> y = [4, 5, 6]
>>> zipped = zip(x, y)
>>> print(list(zipped))
[(1, 4), (2, 5), (3, 6)]
# 迭代对象长度不同
>>> x = [1, 2, 3]
>>> y = [4, 5]
>>> zipped = zip(x, y)
>>> print(list(zipped))
[(1, 4), (2, 5)]
# 迭代对象多余2个
>>> x = [1, 2, 3]
>>> y = [4, 5, 6]
>>> z = [7, 8, 9, 10]
>>> zipped = zip(x, y, z)
>>> print(list(zipped))
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
# 迭代对象中有1个为空
>>> x = [1, 2]
>>> y = []
>>> zipped = zip(x, y)
>>> print(list(zipped))
[]
```




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
- plot
	- 作用：画2维曲线
	- 调用：`pyplot.plot([x], [y], [options])`
	- 说明:`[options]`包括`color`（颜色）、`marker`（节点标记）、`linestyle`（线的形式）、`'g-'`或`'r-.'`或`'b:'`（同时设置线条颜色和样式，字母表示线条颜色，后面的符号表示线条样式）、`label='LabelName'`（`label=`为固定字符，`'LabelName'`为线条标签）
- legend
	- 作用：设置图例位置
	- 调用：`pyplot.legend(arguments)`
	- 说明：`arguments`可为`loc=num`（`loc=`为固定字符，`num`为数字，特别的，`loc=9`表示顶部中央）
- title
	- 作用：添加图标题
	- 调用格式：`pyplot.title("TitleName")`
- xlabel
	- 作用：添加x轴名称
	- 调用：`pyplot.xlabel("xLeabelName")`
- ylabel
	- 作用：添加y轴名称
	- 调用：`pyplot.ylabel("yLeabelName")`
- axis
	- 作用：调整x轴和y轴的取值范围
	- 调用：`pyplot.axis([num1, num2, num3, num4])`
	- 说明：`num1`和`num2`定义x轴取值范围，`num3`和`num4`定义y轴取值范围；使用时需谨慎，因为坐标轴如果不是从0开始，容易使人产生困惑
- show
	- 作用：显示所作的图
	- 调用：`pyplot.show()`
- bar
	- 作用：画条形图
	- 调用：`pyplot.bar([x], [y], [options])`
	- 说明：条形宽度的默认值为0.8，默认x轴图标签位于条形图正中，可以通过给`[x]`赋值调整x坐标轴来调整条形图的显示位置；`[options]`可为条形宽度，用数值表示
- xticks
	- 作用：修改x轴的图标签
	- 调用：`pyplot.xticks([x], [y])`
	- 说明：`[x]`为可选参数，`[y]`为必要参数，`[x]`可用于表示`[y]`中每一个标签的显示位置，默认位于条形图正中，但如果修改了x轴图标签的显示位置，此处做相同修改才可使标签位于每一个条形的正中
```python
# xticks说明示例
>>> from matplotlib import pyplot as plt
>>> movies = ['Annie Hall', 'Ben-Hur', 'Casablanca', 'Gandhi', 'West Side Story']
>>> num_oscars = [5, 11, 3, 8, 10]
>>> xs = [i for i, _ in enumerate(movies)]
>>> plt.bar(xs, num_oscars)
>>> plt.xticks([i for i, _ in enumerate(movies)], movies)
>>> plt.show()
# 如果xs对i做了修改，则xticks应对i做相同修改
>>> xs = [i + 0.1 for i, _ in enumerate(movies)]
>>> plt.xticks([i + 0.1 for i, _ in enumerate(movies)], movies)
```
- scatter
	- 作用：画散点图
	- 调用：`pyplot.scatter([x], [y])`
- annotate
	- 作用：在图中添加标记
	- 调用：`pyplot.annotate('LabelName', xy=(num1, num2), xytext=(num3, num4), [options])`
	- 说明：`'LabelName'`为标记名称；`xy=(num1, num2)`为需要添加标记的位置；`xytext=(num3, num4)`为标记文字出现的位置；`[options]`为其他对标记的控制选项

# 自定义函数
