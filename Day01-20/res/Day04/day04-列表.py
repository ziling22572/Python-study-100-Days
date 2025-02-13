"""todo 常用数据结构之列表"""
'''
列表底层是一个可以动态扩容的数组，列表元素在计算机内存中是连续存储的
'''
import random

items1 = [35, 12, 99, 68, 55, 35, 87]
items2 = ['Python', 'Java', 'Go', 'Kotlin']
items3 = [100, 12.3, 'Python', True]
print(items1)  # [35, 12, 99, 68, 55, 35, 87]
print(items2)  # ['Python', 'Java', 'Go', 'Kotlin']
print(items3)  # [100, 12.3, 'Python', True]
items4 = list(range(1, 10))
print(items4)
# todo 数组直接可以相乘*2=items1*2，相加+=items1+items2 ，in 判断 'java' in items2
'''
可以使用`[]`运算符，通过在`[]`中指定元素的位置来访问该元素，这种运算称为索引运算。需要说明的是，`[]`的元素位置可以是`0`到`N - 1`的整数，也可以是`-1`到`-N`的整数，分别称为正向索引和反向索引，其中`N`代表列表元素的个数。
对于正向索引，`[0]`可以访问列表中的第一个元素，`[N - 1]`可以访问最后一个元素；对于反向索引，`[-1]`可以访问列表中的最后一个元素，`[-N]`可以访问第一个元素，代码如下所示。
'''
print(items1[0])  # 35
print(items1[-7])  # 35
'''
切片运算是形如`[start:end:stride]`的运算符，其中`start`代表访问列表元素的起始位置，`end`代表访问列表元素的终止位置（终止位置的元素无法访问），而`stride`则代表了跨度，简单的说就是位置的增量，
'''
print(items4[1:7:2])  # 索引从1到7（终止位置的元素无法访问，索引位置为7的无法访问），然后2个为跨度 [2, 4, 6]

# for index in range(len(items2)):
#     print(items2[index])


counters = [0] * 6  # [0,0,0,0,0,0]
# 模拟掷色子记录每种点数出现的次数
# todo _  只是用来占位。 表示我们不关心这些数字，只是单纯地执行循环。
# for _ in range(6000):
#     face = random.randrange(1, 7)
#     counters[face - 1] += 1 #对应的索引下值+1
# # 输出每种点数出现的次数
# for face in range(1, 7):
#     print(f'{face}点出现了{counters[face - 1]}次')

'''
我们可以用列表的`remove`方法从列表中删除指定元素，需要注意的是，如果要删除的元素并不在列表中，会引发`ValueError`错误导致程序崩溃，所以建议大家在删除元素时，先用之前讲过的成员运算做一个判断。
我们还可以使用`pop`方法从列表中删除元素，`pop`方法默认删除列表中的最后一个元素，当然也可以给一个位置，删除指定位置的元素。在使用`pop`方法删除元素时，如果索引的值超出了范围，会引发`IndexError`异常，导致程序崩溃。
除此之外，列表还有一个`clear`方法，可以清空列表中的元素。
'''

list_demo1 = ['Java', 'Python', 'Go', 'Kotlin', 'Python']
list_demo1.remove('Python')  # 默认删除第一个
list_demo1.pop()  # todo `pop`方法默认删除列表中的最后一个元素
list_demo_copy = list_demo1.copy()  # todo `pop`方法默认删除列表中的最后一个元素
list_demo_copy.append('vscode')  # todo 只能拼接单个对象
list_demo_copy.extend(['Idea', 'vue'])  # todo 拼接数组
# list_demo1.clear() # 清空元素
print(list_demo1)
print(list_demo_copy)

languages = ['Python', 'SQL', 'Java', 'C++', 'JavaScript']
if 'Java' in languages:
    languages.remove('Java')
if 'Swift' in languages:
    languages.remove('Swift')
print(languages)  # ['Python', 'SQL', C++', 'JavaScript']
languages.pop()
# 清掉对应的值，同时拿出来备份
temp = languages.pop(1)
print(temp)  # SQL
languages.append(temp)
print(languages)  # ['Python', C++', 'SQL']
languages.clear()
print(languages)  # []

# todo 统计次数 count(),索引开始 index（value,start）
items = ['Python', 'Java', 'Java', 'C++', 'Kotlin', 'Python']
print(items.index('Python'))  # 0
# 从索引位置1开始查找'Python'
print(items.index('Python', 1))  # 5
print(items.count('Python'))  # 2
print(items.count('Kotlin'))  # 1
print(items.count('Swfit'))  # 0
# 从索引位置3开始查找'Java'
# print(items.index('Java', 3)) #ValueError: 'Java' is not in list

# todo 元素排序【sort()】和反转【reverse()】

'''
下面👇两种写法
'''
items_1 = []
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        items.append(i)

items_11 = [i for i in range(1, 100) if i % 3 == 0 or i % 5 == 0]

# todo 嵌套列表 2维数组
scores = [[95, 83, 92], [80, 75, 82], [92, 97, 90], [80, 78, 69], [65, 66, 89]]
print(scores[0]) #[95, 83, 92]
print(scores[0][1]) #83



red_balls = [i for i in range(1, 34)]
blue_balls = [i for i in range(1, 17)]
# 从红色球列表中随机抽出6个红色球（无放回抽样）
selected_balls = random.sample(red_balls, 6)
# 对选中的红色球排序
selected_balls.sort()
# 输出选中的红色球
for ball in selected_balls:
    print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
# 从蓝色球列表中随机抽出1个蓝色球
blue_ball = random.choice(blue_balls)
# 输出选中的蓝色球
print(f'\033[034m{blue_ball:0>2d}\033[0m')
