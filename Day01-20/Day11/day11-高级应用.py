""" todo 函数高级应用 """
'''
1、装饰器 ：装饰器是“**用一个函数装饰另外一个函数并为其提供额外的能力**”的语法现象
2、递归调用 
3、函数语法糖 @lru_cache()
'''
import time
import random
from functools import wraps
from functools import lru_cache


# todo 通用执行xx函数耗时
def record_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 在执行被装饰的函数之前记录开始时间
        start = time.time()
        # 执行被装饰的函数并获取返回值
        result = func(*args, **kwargs)
        # 在执行被装饰的函数之后记录结束时间
        end = time.time()
        # 计算和显示被装饰函数的执行时间
        print(f'{func.__name__}执行时间: {end - start:.2f}秒')
        # 返回被装饰函数的返回值
        return result

    return wrapper


@record_time
def download(filename):
    """下载文件"""
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成.')


@record_time
def upload(filename):
    """上传文件"""
    print(f'开始上传{filename}.')
    time.sleep(random.random() * 8)
    print(f'{filename}上传完成.')


# todo @record_time 注解
# download('MySQL从删库到跑路.avi')
# upload('Python从入门到住院.pdf')
# # download = record_time(download)
# # upload = record_time(upload)
#
# # 取消装饰器的作用不记录执行时间     # todo 通过__函数名__
# download.__wrapped__('MySQL必知必会.pdf')
# upload.__wrapped__('Python从新手到大师.pdf')

"""
递归调用: 1*2*3*4...
"""


def fac(n):
    if n in (0, 1):
        return n
    return n * fac(n - 1)


print(fac(5))  # 120


# 递归调用函数入栈
# 5 * fac(4)
# 5 * (4 * fac(3))
# 5 * (4 * (3 * fac(2)))
# 5 * (4 * (3 * (2 * fac(1))))
# 停止递归函数出栈
# 5 * (4 * (3 * (2 * 1)))
# 5 * (4 * (3 * 2))
# 5 * (4 * 6)
# 5 * 24
# 120

# todo 斐波那契 1,1,2,3,5
# todo 再举一个之前讲过的生成斐波那契数列的例子，因为斐波那契数列前两个数都是`1`，从第三个数开始，每个数是前两个数相加的和，

def fb1(n):
    if n in (1, 2):
        return 1
    return fb1(n - 1) + fb1(n - 2)


# fb1(4)+fb1(3)=fb1(3)+fb1(2)=fb1(2)+fb1(1)
print(fb1(5))

# todo `lru_cache`函数是一个装饰器函数，我们将其置于上面的函数`fib2`之上，它可以缓存该函数的执行结果从而避免在递归调用的过程中产生大量的重复运算，这样代码的执行性能就有“飞一般”的提升。
# lru_cache`函数是一个带参数的装饰器，所以上面第4行代码使用装饰器语法糖时，`lru_cache`后面要跟上圆括号。todo  `lru_cache`函数有一个非常重要的参数叫`maxsize`，它可以用来定义缓存空间的大小，默认值是128。
@lru_cache()
def fib2(n):
    a, b = 0, 1
    for _ in range(n):
        # 初始时a = 0 和b = 1。
        # 执行a, b = b, a + b        时：
        # 右边的b, a + b计算成(1, 1)。
        # 然后左边的a, b 分别赋值为1和1。todo 先赋值a=b保留b赋值前的值,然后b=a+b
        a, b = b, a + b
    return a

print(fib2(5))
# n=1时 a=1 b=1
# n=2时 a=1 b=2
# n=3时 a=2 b=3
# n=4时 a=3 b=5
# n=5时 a=5 b=8
