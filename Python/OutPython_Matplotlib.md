**本部分为Python第3方库matplotlib的安装、应用与理解，“发表于微博自媒体”，微博：[@钻石草帽](https://weibo.com/strawhatchan)**

# 安装
### Ubuntu系统
1. 直接用`apt-get`安装，在终端输入`sudo apt-get install python3-matplotlib`
2. 使用pip（Python包管理工具）安装
	- 在终端输入`(pip | pip3) install matplotlib`，其中，`pip`命令安装Python2下的包，`pip3`命令安装Python3下的包
	- pip安装后无法直接使用`matplotlib`库，还需要安装依赖，终端输入`sudo apt-get build-dep python-matplotlib`并根据提示完成安装，更多细节可查阅[matplotlib官网文档](https://matplotlib.org/contents.html)

# 应用
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


# 理解