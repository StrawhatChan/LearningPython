> **本文“发表于微博自媒体”，微博：[@钻石草帽](https://weibo.com/strawhatchan)**

[The Python Library Reference](https://docs.python.org/3/library/index.html)
============================

# BuiltIn函数
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
# 迭代对象多于2个
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

