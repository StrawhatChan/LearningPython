# -*- coding: utf-8 -*-
# Matthes, E., 2015: Python Crash Course[M]. San Francisco: No Starch Press.
# 本文件记录此书中第1部分，即基础知识部分的练习代码
# ============================================ ##
# Chapter 1
# -------------------------------------------- ##
# 简单输出
print("Hello Python interpreter")
print("Hello World")

# 变量输出
message = "Hello Python World"
print(message)
message = "Hello Python Crash Course World!"
print(message)
# ============================================ ##
# Chapter 2:变量和简单数据类型
# -------------------------------------------- ##
# 数据类型：字符
# -------------------------------------------- ##
"This is a string"
'This is also a string'
print('I told my friend, "Python is my favorite language!"')
print("The language 'Python' is named after Monty Python, not the snake.")
print("One of Python's strengths is its diverse and supportive community.")

# 方法：title()、upper()、lower()
name = "ada lovelace"
print(name.title())
name = "Ada Lovelace"
print(name.upper())
print(name.lower())

# 方法：concatenation使用"+"符号(去掉双引号)实现
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")
message = "Hello, " + full_name.title() + "!"
print(message)

# 方法：whitespace包括：\t：等价于tab;\n：另起一行;rstrip():去掉右边空格;lstrip()：去掉左边空格;strip()：去掉字符串两端的空格
print("Python")
print("\tPython")
print("Language:\nPython\nC\nJavaScript")
print("Language:\n\tPython\n\tC\n\tJavaScript")
favorite_language = "Python "
print(favorite_language.rstrip())
print(favorite_language)
favorite_language = favorite_language.rstrip()
print(favorite_language)
favorite_language = " Python"
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())

# 语法错误示例
message = "One of Python's strengths is its diverse community."
print(message)
message = 'One of Python's strengths is its diverse community.'
print(message)
# -------------------------------------------- ##
# 数据类型：数值
# -------------------------------------------- ##
# 数据类型：整数
print(2 + 3)
print(3 - 2)
print(2 * 3)
print(3 / 2)
print(3 ** 2)
print(3 ** 3)
print(10 ** 6)
print(2 + 3*4)
print((2 + 3) * 4)

# 数据类型：浮点
print(0.1 + 0.1)
print(0.2 + 0.2)
print(2 * 0.1)
print(2 * 0.2)
print(0.2 + 0.1)
print(3 * 0.1)

# 数值和字符混用时错误和正确的示例
age = 23
message1 = "message1 = Happy " + age + "rd Birthday!"
print(message1)
age = 23
message2 = "message2 = Happy " + str(age) + "rd Birthday!"
print(message2)

# Python的宗旨
import this
# ============================================ ##
# Chapter 3：List
# -------------------------------------------- ##
list示例：list、list元素的展示形式
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1].title())
print(bicycles[2].title())
print(bicycles[3].title())
print(bicycles[-1].title())

# 调用list元素
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

# 变更list元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# 增加list元素
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)
motorcycles = []
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# 插入list元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.insert(0,'ducati')
print(motorcycles)

# del语句删除list元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[1]
print(motorcycles)

# pop方法删除list元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

# remove方法删除list元素
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

# 使用sort方法永久排序list元素
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# 使用sorted函数暂时排序list元素
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the reverse sorted list:")
print(sorted(cars,reverse=True))
print("\nHere is the original list again:")
print(cars)

# 使用reverse方法排序list元素
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse() # 注意，reverse方法仅按照元素顺序永久倒序排列
print(cars)

# len函数获取list元素个数
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

# 索引错误示例
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[3])
print(motorcycles[-1])
motorcycles = []
print(motorcycles[-1])
# ============================================ ##
# Chapter 4：Working with lists
# -------------------------------------------- ##
# 可以修改的list
# -------------------------------------------- ##
# for loop的使用
# 示例1
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)
# 示例2
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician.title() + ", that was a great trick")
	print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")

# Indentation错误示例
# 示例1
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
print(magician)
# 示例2
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician.title() + ", that was a great trick")
print("I can't wait to see your next trick, " + magician.title() + ".\n")
# 示例3
message = "Hello Python world"
	print(message)
# 示例4
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician.title() + ", that was a great trick")
	print("I can't wait to see your next trick, " + magician.title() + ".\n")
	print("Thank you, everyone. That was a great magic show!")
# 示例5
magicians = ['alice', 'david', 'carolina']
for magician in magicians
	print(magician)

# 结合for loop和range函数创建数列
for value in range(1,5):
	print(value)
print("\n")
for value in range(1,6):
	print(value)

# 结合range函数和list函数创建数值list
numbers = list(range(1,6))
print(numbers)
even_numbers = list(range(2,11,2))
print(even_numbers)

# 结合for loop和append方法创建数值list
squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares)

# 针对list的简单统计
digits = range(0,10)
print(min(digits))
print(max(digits))
print(sum(digits))

# list comprehension的编写方式
squares = [value**2 for value in range(1,11)]
print(squares)

# 操作list的部分元素
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

# 使用for loop操作list部分元素
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())

# 复制list
# 有效的复制方法
my_foods = ['pizza', 'falafel', 'carrot cake']
freind_foods = my_foods[:]
my_foods.append('cannoli')
freind_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy freind's favorite foods are:")
print(freind_foods)
# 无效的复制方法
my_foods = ['pizza', 'falafel', 'carrot cake']
freind_foods = my_foods # 简单赋值的复制方式无效，它没有将2个list区分开
my_foods.append('cannoli')
freind_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy freind's favorite foods are:")
print(freind_foods)
# -------------------------------------------- ##
# 不可修改的list：tuple
# -------------------------------------------- ##
# 创建与引用
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
dimensions[0] = 250

# for loop展示tuple元素
dimensions = (200,50)
for dimension in dimensions:
	print(dimension)

# 通过对变量重新赋值来修改tuple的元素
dimensions = (200,50)
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)
dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)
# ============================================ ##
# Chapter 5： IF Statements
# -------------------------------------------- ##
# if和for loop综合示例
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

# 条件判断示例:区分大小写
car = 'Audi'
print(car == 'audi')
print(car.lower() == 'audi')

# 不等号!=的运用
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
	print("Hold the anchovies")

# 数值比较
age = 18
print(age == 18)
answer = 17
if answer != 42:
	print("That is not the correct answer. Please try again!")
age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)

# 使用and检查多个条件
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
age_1 = 22
print(age_0 >=21 and age_1 >= 21)
print((age_0 >= 21) and (age_1 >=21)) # 这是更易读的编写方式

# 使用or检查多个条件
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)
age_0 = 18
print(age_0 >=21 or age_1 >= 21)

# 使用in判断某个值是否在list中
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)
banned_users = ['andrew', 'carolian', 'david']
user = 'marie'
if user not in banned_users:
	print(user.title() + ", you can post a response if you wish")

# 布尔（Boolean expressions）表达式
game_active = True
can_edit = False

# if语句
age = 19
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")

# if-else语句
age = 17
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")
else:
	print("Sorry, you are too young to vote.")
	print("Please registered to vote as soon as you turn 18!")

if-elif-else语句
# 繁琐的编写方式
age = 12
if age <4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $5.")
else:
	print("Your admission cost is $10.")
# 简洁的编写方式
age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 5
else:
	price = 10
print("Your admission cost is $" + str(price) +".")

# 使用多个elif块
age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
else:
	price = 5
print("Your admission cost is $" + str(price) +".")

# 忽略else块
age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
elif age > 65:
	price = 5
print("Your admission cost is $" + str(price) +".")

# 独立if语句检测全部条件和if-elif-else语句检测到某个条件即跳出的比较
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
	print("Adding extra cheese.")
print("Finished making your pizza!")

# 使用if-elif语句与上述结果进行比较
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
	print("\nAdding mushrooms.")
elif 'pepperoni' in requested_toppings:
	print("\nAdding pepperoni.")
elif 'extra cheese' in requested_toppings:
	print("\nAdding extra cheese.")
print("Finished making your pizza!")

# if和lists的结合使用
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry, we are out of green peppers right now.")
	else:
		print("Adding " + requested_topping + ".")
print("\nFinishied making your pizza!")

# 执行for loop前检查list是否为空
requested_toppings = []
if requested_toppings: # 如果requested_toppings为空，返回False，否则返回Ture
	for requested_topping in requested_toppings:
		print("Adding " + requested_topping + '.')
	print("\nFinishied making your pizza!")
else:
	print("Are you sure you want a plain pizza?")

# 使用多个lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + ".")
	else:
		print("Sorry, we don't have " + requested_topping + '.')
print("\nFinishied making your pizza!")
# ============================================ ##
# Chapter 6： Dictionaries
# -------------------------------------------- ##
# 无嵌套字典
# -------------------------------------------- ##
# 字典示例，其核心特征是key-value对
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# 在字典中增加元素
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 创建空字典并增加元素
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# 修改字典中特定key的值
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

# 功能性示例
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

# 使用del语句永久删除字典中不再需要的key-value对
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

# 编写字典的一般方法
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python', #此处的逗号对程序运行无影响
	}
print("Sarah's favorite language is " +
	favorite_languages['sarah'].title() +
	".")

# 结合for语句和item方法实现字典key-value对的循环
# 示例1
user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
	}
for key, value in user_0.items():
	print("\nKey: " + key)
	print("Value: " + value)
for k, v in user_0.items():
	print("\nKey: " + k)
	print("Value: " + v)
# 示例2
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
for name, language in favorite_languages.items():
	print(name.title() + 
		"'s favorite language is " +
		language.title() +
		".")

# 使用key方法实现字典key的循环
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
print("Useing the keys() method: ")
for name in favorite_languages.keys():
	print(name.title())
print("\nDefault looping method: ")
for name in favorite_languages: # key是字典的默认循环内容
	print(name.title())
print("\nThis is another example: ")
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())
	if name in friends:
		print("  Hi " +
			name.title() +
			", I see your favoite language is " +
			favorite_languages[name].title() +
			"!")
print("\nFinding out if a particular person was polled: ")
if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")

# 结合sorted函数和keys方法，按顺序循环字典的key值
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
for name in sorted(favorite_languages.keys()):
	print(name.title() +
		", thank you for taking the poll.")

# 使用values方法返回字典中不包括key或去重后的value
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())
print("\nHere is Sorted Method： ")
for language in sorted(favorite_languages.values()):
	print(language.title())
print("\nLanguage without repetition: ")
for language in set(favorite_languages.values()):
	print(language.title())
# -------------------------------------------- ##
# 嵌套字典
# -------------------------------------------- ##
# 嵌套示例
alien_0 = {
	'color': 'green',
	'points': 5,
	}
aline_1 = {
	'color': 'yellow',
	'points': 10,
	}
alien_2 = {
	'color': 'red',
	'points': 15,
	}
aliens = [alien_0, aline_1, alien_2]
for alien in aliens:
	print(alien)

# 通过循环创建嵌套字典：字典在list中
aliens = []
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)
for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['point'] = 15
for alien in aliens[:5]:
	print(alien)
print("...")
print("Total number of aliens: " + str(len(aliens)))

# 创建嵌套字典：list在字典中
# 示例1
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
	}
print("You ordered a " + pizza['crust'] + "-curst pizza " + "with the following toppings:")
for topping in pizza['toppings']:
	print("\t" + topping)

# 示例2
favorite_languages = {
	'jen': ['python', 'rubu'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['pyhon', 'haskell'],
	}
for name, languages in favorite_languages.items():
	print("\n" + name.title() + "'s favoite languages are:")
	for language in languages:
		print("\t" + language.title())

# 创建嵌套字典：字典在字典中
users = {
	'aeinstein':{
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
		},
	'mcurie':{
		'first': 'marie',
		'last': 'curie',
		'location': 'paris',
		}
	}
for username, user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']
	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())
# ============================================ ##
# Chapter 7： User Input and While Loops
# -------------------------------------------- ##
# Input
# -------------------------------------------- ##
# Input字符
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
name = input("Please enter your name: ")
print("Hello, " + name + "!")
prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your firse name?"
name = input(prompt)
print("\nHello, " + name + "!")

# Input数值
age = input("How old are you?")
print(age)
print(age >= 18) # 错误的示例
age = int(age) # 使用int函数将字符转换为数值
print(age >= 18) # 正确的示例
height = input("How tall are you, in inches?")
height = int(height)
if height >= 36:
	print("\nYou're tall enough to ride!")
else:
	print("\nYou'll be able to ride when you're a little older.")

# 使用%符号做模运算（modulo operator）
number = input("Enter a number, and I'll tell you if it's enen or odd: ")
number = int(number)
if number % 2 == 0:
	print("\nThe number " + str(number) + " is even.")
else:
	print("\nThe number " + str(number) + " is odd.")
# -------------------------------------------- ##
# while循环
# -------------------------------------------- ##
# while示例
current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1 # 等价于current_number = current_number + 1

# 退出while循环
# 示例1：不保存输入内容
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
	message = input(prompt)
	print(message)
# 示例2：保存输入内容
prompt = "\nTell me something, and I will repeat it back to you:\nEnter 'quit' to end the program."
message = ['action']
while message[-1] != 'quit':
	message.append(input(prompt))
	print(message)

# 使用flag退出while循环
# 示例1：不保存输入内容
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
active = True
while active:
	message = input(prompt)
	if message == 'quit':
		active = False
	else:
		print(message)
# 示例2：保存输入内容
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
active = True
message = []
while active:
	message.append(input(prompt))
	if message[-1] == 'quit':
		active = False
	else:
		print(message)

# 使用break退出while循环
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"
while True:
	city = input(prompt)
	if city == 'quit':
		break
	else:
		print("I'd love to go to " + city.title() + "!")

# 在循环中使用continue忽略其后的语句，继续执行循环
current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 ==0:
		continue
	print(current_number)

# 使用while将一个list的元素移动到另一个list
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	print("Verifying user: " + current_user.title())
	confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())

# 结合while循环和remove方法，从list中删除全部特定值
pets = ['dog',
		'cat',
		'dog',
		'goldfish',
		'cat',
		'rabbit',
		'cat',
		]
print(pets)
while 'cat' in pets:
	pets.remove('cat')
print(pets)

# 使用while循环和input在字典中存储数据
responses = {}
polling_active = True
while polling_active:
	name = input("\nWhat is your name?")
	response = input("Which mountain would you like to climb someday?")
	responses[name] = response
	repeat = input("Would you like to let another person respond?(yes/ no)")
	if repeat == 'no':
		polling_active = False
print("\n--- Poll Results ---")
for name, response in responses.items():
	print(name.title() + " would like to climb " + response.title() + ".")
# ============================================ ##
# Chapter 8： Functions
# -------------------------------------------- ##
# 定义函数示例
def greet_user():
	print("Hello!")
greet_user()

# 包含变量参数的函数
def greet_user(username):
	print("Hello, " + username.title() + "!")
greet_user('jesse')
greet_user('sarah')

# 函数中的positional arguments：按顺序输入的参数
def describe_pet(animal_type, pet_name):
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')
describe_pet('harry', 'hamster') # 函数按照参数位置输出
describe_pet('dog', 'willie')

# 函数中的keyword arguments：不用考虑参数顺序
def describe_pet(animal_type, pet_name):
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

# 函数中参数变量的默认值
def describe_pet(pet_name, animal_type='dog'):
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')
describe_pet(animal_type='hamster', pet_name='harry')

# 调用函数时使用return value保存结果但不直接输出
# 示例1
def get_formatted_name(first_name, last_name):
	full_name = first_name + ' ' + last_name
	return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
# 示例2
def get_formatted_name(first_name, middle_name, last_name):
	full_name = first_name + ' ' + middle_name + ' ' + last_name
	return full_name.title()
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

# 设定可选参数
def get_formatted_name(first_name, last_name, middle_name=''):
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()
musician = get_formatted_name('john', 'hooker')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

# 函数返回字典
def build_person(first_name, last_name):
	person = {'First': first_name.title(), 'Last': last_name.title()}
	return person
musician = build_person('jimi', 'hendrix')
print(musician)
def build_person(first_name, last_name, age=''):
	person = {'Fist': first_name.title(), 'Last': last_name.title()}
	if age:
		person['Age'] = age
	return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)

# 在函数中使用while循环
# 无限循环示例
def get_formatted_name(first_name, last_name):
	full_name = first_name + ' ' + last_name
	return full_name.title()
while True: # 这是一个无限循环
	print("\nPlease tell me your name:")
	f_name = input("First name: ")
	l_name = input("Last name: ")
	formatted_name = get_formatted_name(f_name, l_name)
	print("\nHello, " + formatted_name + "!")
# 非无限循环示例
def get_formatted_name(first_name, last_name):
	full_name = first_name + ' ' + last_name
	return full_name.title()
while True: 
	print("\nPlease tell me your name:")
	print("(enter 'q' at any time to quit)")
	f_name = input("First name: ")
	if f_name == 'q':
		break
	l_name = input("Last name: ")
	if l_name == 'q':
		break
	formatted_name = get_formatted_name(f_name, l_name)
	print("\nHello, " + formatted_name + "!")

# 将List内容传递给函数
def greet_users(names):
	for name in names:
		msg = "Hello " + name.title() + "!"
		print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# 将list传递给函数后修改list
# 不使用函数
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
while unprinted_designs:
	current_design = unprinted_designs.pop()
	print("Printing model: " + current_design.title())
	completed_models.append(current_design)
print("\nThe following models have been printed:")
for completed_model in completed_models:
	print(completed_model.title())
# 使用函数
def print_models(unprinted_designs, completed_models):
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print("Printing model: " + current_design.title())
		completed_models.append(current_design)
def show_completed_models(completed_models):
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model.title())
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print("\n*** Beginning another example ***")
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron'] # 不修改原list的示例
completed_models = []
print_models(unprinted_designs[:], completed_models) # 避免函数修改list：使用[:]传递原list的副本
show_completed_models(completed_models)
print("\n--- Checking unprinted_designs list ---")
print(unprinted_designs)

# 定义一个不确定（Arbitrary）数量变量参数的函数
# 示例1
def make_pizza(*toppings):
	print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
# 示例2
def make_pizza(*toppings):
	print("\nMaking a pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# 确定参数（positional）和不确定数量参数（Arbitrary）混合的函数
def make_pizza(size, *toppings):
	print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra')

# 包含关键字的不确定数量参数函数
def build_profile(first, last, **user_info):
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
# ============================================ ##
# Chapter 9： Classes
# -------------------------------------------- ##
# 创建类（class）示例
class Dog():
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def sit(self):
		print(self.name.title() + " is now sitting.")
	def roll_over(self):
		print(self.name.title() + " rolled over!")
my_dog = Dog('willie', 6) # 创建一个例
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit() # 引用类中创建的方法
my_dog.roll_over()
my_dog = Dog('willie', 6) # 创建第1个例
your_dog = Dog('lucy', 3) # 创建第2个例
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()

# 创建1个新的类和方法，并为特定属性设置默认值，然后引用创建的方法
class Car():
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")
	def update_odometer(self, mileage): # 设置修改方法
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an adometer!")
	def increment_odometer(self, miles):
		self.odometer_reading += miles
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23 # 直接赋值修改默认值
my_new_car.read_odometer()
my_new_car.update_odometer(27) # 通过类的方法修改默认值
my_new_car.read_odometer()
my_new_car.update_odometer(26) # 测试修改方法中的if条件
my_new_car.read_odometer()
my_used_car = Car('subaru', 'outback', 2013) # 创建新例
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500) # 使用新设方法修改属性默认值
my_used_car.read_odometer()
my_used_car.increment_odometer(100) # 使用新设方法增加属性值
my_used_car.read_odometer()

# 类的继承机制
class Car(): # 父类
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")
	def update_odometer(self, mileage): # 设置修改方法
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an adometer!")
	def increment_odometer(self, miles):
		self.odometer_reading += miles
	def fill_gas_tank(self, tanknum):
		print("This car needs " + str(tanknum) + " gas tank!")
class ElectricCar(Car): # 子类
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery_size = 70
	def describe_battery(self): # 定义子类的方法
		print("This car has a " + str(self.battery_size) + "-KWh battery.")
	def fill_gas_tank(self):
		print("This car doesn't need a gas tank!")
my_tesla = ElectricCar('tesla', 'model s', 2016)		
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery() # 验证子类的方法
my_tesla.fill_gas_tank() # 验证子类覆盖父类方法

# 将类作为属性使用
class Car(): # 父类
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
class Battery():
	def __init__(self, battery_size=70):
		self.battery_size = battery_size
	def describe_battery(self):
		print("This car has a " + str(self.battery_size) + "-KWh battery.")
	def get_range(self):
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)
class ElectricCar(Car): # 子类
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery = Battery()
my_tesla = ElectricCar('tesla', 'model s', 2016)		
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
# ============================================ ##
# Chapter 10： Files and Exceptions
# -------------------------------------------- ##
# 文件读写
# -------------------------------------------- ##
# 文件地址
pi_digits = 'pcc/chapter_10/pi_digits.txt'
pi_million_digits = 'pcc/chapter_10/pi_million_digits.txt'
programming = 'pcc/chapter_10/programming.txt'
alice = 'pcc/chapter_10/alice.txt'
numbersjson = 'pcc/chapter_10/numbers.json'
usernames = 'pcc/chapter_10/usernames.json'

# 打开、读取文件内容后输出其内容
with open(pi_digits) as file_object:
	contents = file_object.read()
	print(contents)
	print(contents.rstrip()) # rstrip方法去掉了字符右边的空白字符

# 分行读取文件内容
with open(pi_digits) as file_object: # 方法1
	for line in file_object:
		print(line.rstrip())
with open(pi_digits) as file_object: # 方法2
	lines = file_object.readlines()
for line in lines:
	print(line.rstrip())


# 操作文件内容
with open(pi_digits) as file_object: # 方法2
	lines = file_object.readlines()
pi_string = ''
for line in lines:
	pi_string += line.strip()
print(pi_string)
print(len(pi_string))

# 操作大文件：小数点后100万位的pi
with open(pi_million_digits) as file_object:
	lines = file_object.readlines()
pi_string = ''
for line in lines:
	pi_string += line.strip()
print(pi_string[:52] + "...")
print(len(pi_string))
birthday = input("Enter your birthday, in the form mmddyy:")
if birthday in pi_string:
	print("Your birthday appears in the first million digits of pi!")
else:
	print("Your birthday does not appear in the first million digits of pi.")

# 将内容写入或覆盖原文件内容
with open(programming, 'w') as file_object:
	file_object.write("I love programming.\n")
	file_object.write("I love creating new games.\n")

# 将内容加入文件
with open(programming, 'a') as file_object:
	file_object.write("I also love finding meaning in large datasets.\n")
	file_object.write("I love creating apps that can run in a browser.\n")
# -------------------------------------------- ##
# Exceptions
# -------------------------------------------- ##
# try-except代码块示例
try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero!")

# try-except-else代码块
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
	first_number = input("\nFirst number:")
	if first_number == 'q':
		break
	second_number = input("Second number:")
	if second_number == 'q':
		break
	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("You can't divide by 0!")
	else: # 当try没有发生错误时执行
		print(answer)

# 无法找到文件的示例
alice = 'alice.txt'
try:
	with open(alice) as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	msg = "Sorry, the file " + alice + " does not exist."
	print(msg)

# 分析文本
title = "Alice in Wonderland" # 简单示例
print(title.split()) # split方法将文本分割为单词并存入list中
try:
	with open(alice) as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	msg = "Sorry, the file " + alice + " does not exist."
	print(msg)
else:
	words = contents.split()
	num_words = len(words)
	print("The file " + alice + " has about " + str(num_words) + " words.")

# 使用pass语句以静默方式处理错误
alice = 'alice.txt'
try:
	with open(alice) as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	pass
# -------------------------------------------- ##
# Storying Data
# -------------------------------------------- ##
# 使用json.dump方法写入文件
import json
numbers = [2, 3, 5, 7, 11, 13, 15]
with open(numbersjson, 'w') as f_obj:
	json.dump(numbers, f_obj)

# 使用json.load方法读取文件
import json
with open(numbersjson) as f_obj:
	numbers = json.load(f_obj)
print(numbers)

# 使用json存储用户数据
import json
username = input("What is your name?")
with open(usernames, 'w') as f_obj:
	json.dump(username, f_obj)
	print("We'll remember you when you come back, " + username + "!")

# 使用json读取用户数据
import json
with open(usernames) as f_obj:
	contents = json.load(f_obj)
	print("Welcome back, " + contents + "!")

# 合并存储和读取用户数据
import json
try:
	with open(usernames) as f_obj:
		username = json.load(f_obj)
except FileNotFoundError:
	username = input("What is your name?")
	with open(usernames, 'w') as f_obj:
		json.dump(username,f_obj)
		print("We'll remember you when you come back, " + username + "!")
else:
	print("Welcome back, " + username + "!")
# ============================================ ##
# Chapter 11： Testing your Code
# -------------------------------------------- ##
# 暂不学习，待必要时再学习