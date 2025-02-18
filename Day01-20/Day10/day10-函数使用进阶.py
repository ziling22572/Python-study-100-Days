""" todo 函数使用进阶 """
'''
“一等函数”指的就是函数可以赋值给变量，函数可以作为函数的参数，函数也可以作为函数的返回值。把一个函数作为其他函数的参数或返回值的用法，我们通常称之为“高阶函数”。
'''
# todo 提供与运算符对应的函数，可以让你将运算符作为参数传递给高阶函数。# 用于进行简单的比较、数学运算和逻辑运算等。
import operator
# todo functools 模块提供了一些高阶函数和工具，用于简化函数的创建和使用。它常用于装饰器、函数式编程和优化等方面。
# 主要功能：
# functools.partial()：创建函数的部分应用（即，固定部分参数的函数）。
# functools.reduce()：对序列进行累积操作。
# functools.lru_cache()：为函数添加缓存，优化计算。
# functools.wraps()：用于装饰器，保持原函数的元数据（如 __name__, __doc__ 等）。
import functools


# todo  高阶函数:我们回到之前讲过的一个例子，设计一个函数，传入任意多个参数，对其中`int`类型或`float`类型的元素实现求和操作。我们对之前的代码稍作调整，让整个代码更加紧凑一些，如下所示。


# 只接受位置参数 *args。
# args 是一个元组，包含所有传递给函数的位置参数。
# 不支持关键字参数。,name='1111' 会报错
def calc1(*args):
    items = list(args)
    result = 0
    for item in items:
        if type(item) in (int, float):
            result += item
    return result


# 同时接受位置参数 *args 和关键字参数 **kwargs。
# args 是一个元组，包含所有传递给函数的位置参数。
# kwargs 是一个字典，包含所有传递给函数的关键字参数（键值对形式）。
# kwargs.values() 提取关键字参数的值，并将它们与位置参数合并到 items 列表中。
def calc2(*args, **kwargs):
    # 位置参数+获取关键字参数的值
    items = list(args) + list(kwargs.values())
    result = 0
    for item in items:
        if type(item) in (int, float):
            result += item
    return result


def add(x, y):
    return x + y


def mul(x, y):
    return x * y


def calc(init_value, op_func, *args, **kwargs):
    items = list(args) + list(kwargs.values())
    result = init_value
    for item in items:
        if type(item) in (int, float):
            result = op_func(result, item)
    return result


# 递归相乘或者相加
def digui(init_value, max_value, op_func):
    result = init_value
    for i in range(1, max_value):
        result = op_func(result, i)
        # print(result)
    return result


def is_even(num):
    """判断num是不是偶数"""
    return num % 2 == 0


def square(num):
    """求平方"""
    return num ** 2


print(calc1(1, 2, 3, 4, 'KEY', 2.111))
print(calc2(1, 2, 3, 4, 'KEY', 2.111, name='11', k=12))
# todo 传递函数
print(calc(0, add, 1, 2, 3, 4, 'KEY', 2.111))
print(calc(0, mul, 1, 2, 3, 4, 'KEY', 2.111))
# 1*2*3...9=362880
print(f'递归✖️后值：{digui(1, 10, operator.mul)}')

old_nums = [35, 12, 8, 99, 60, 52]
# todo filter() 内置函数，它用于过滤掉不符合条件的元素，保留符合条件的元素,filter() 返回一个[迭代器]，所以它的结果是一个类似列表的对象，但并没有直接返回一个列表。
# todo map() 内置函数 函数用于对可迭代对象中的每个元素应用一个函数，并返回一个新的[迭代器]
new_nums = list(map(square, filter(is_even, old_nums)))
# print(list(map(square,old_nums)))
print(new_nums)

# int 默认按照小-大排序 字符串默认按照a-z
old_strings = ['in', 'apple', 'zoo', 'waxberry', 'pear']
old_ints = [1, 3, 2, 0, -1]
# 通过长度排
new_strings = sorted(old_strings, key=len)
# reverse=True todo 代表反转从大到小排
new_ints = sorted(old_ints, reverse=True)
print(new_strings)  # ['in', 'zoo', 'pear', 'apple', 'waxberry']
print(new_ints)  # ['in', 'zoo', 'pear', 'apple', 'waxberry']

'''
Lambda函数: 匿名函数 lambda x: 赋值|判断|计算
格式=> lambda x: x % 2 == 0 或者 x ** 2
'''

# todo 在 Python 中，lambda 表达式是用于创建匿名函数的一种简洁方式。【lambda 表达式总是返回一个单一的值】，它的语法结构如下：
# lambda arguments: expression
# arguments 是输入的参数，可以是一个或多个。
# expression 是在函数体内计算并返回的表达式，必须是一个单一的表达式。
# todo # 这是无效的 lambda 表达式，[语法错误]   lambda x, y: x = y + 1
# todo lambda x, y: x + y  等价于： def add(x, y):  return x + y

old_nums = [35, 12, 8, 99, 60, 52]
new_nums = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, old_nums)))
print(new_nums)

# 使用 functools.reduce 来做累积操作
numbers = [1, 2, 3, 4]
result = functools.reduce(lambda x, y: x + y, numbers)  # 计算 1 + 2 + 3 + 4
print(result)  # 输出 10

# 用一行代码实现计算阶乘的函数 todo 下面也是一个函数，传递的参数为：n ,阶乘结果作为返回值 初始值为：1
fac = lambda n: functools.reduce(operator.mul, range(2, n + 1), 1)
print(fac(10))  # 3628800

# 用一行代码实现判断素数的函数
# todo all 函数用于检查从 2 到 sqrt(n)（包括整数部分）之间的每个数 i，是否都不能整除 n。如果 n 可以被某个数 i 整除（即 n % i == 0），all 返回 False，否则返回 True，表示 n 是素数。
is_sushu = lambda x: x > 1 and all(map(lambda f: x % f, range(2, int(x ** 0.5) + 1)))
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

print(is_sushu(4))
print(is_prime(4))


'''
偏函数
偏函数是指固定函数的某些参数，生成一个新的函数，这样就无需在每次调用函数时都传递相同的参数。
在 Python 语言中，我们可以使用`functools`模块的`partial`函数来创建偏函数。
例如，`int`函数在默认情况下可以将字符串视为十进制整数进行类型转换，如果我们修修改它的`base`参数，就可以定义出三个新函数，分别用于将二进制、八进制、十六进制字符串转换为整数，代码如下所示。
'''
# 分别用于将二进制、八进制、十六进制字符串转换为整数
# TODO 下面也是一种函数：偏函数
int2 = functools.partial(int, base=2)
int8 = functools.partial(int, base=8)
int16 = functools.partial(int, base=16)
print(int2('1111'))
print(int8('1111'))
print(int16('111F'))