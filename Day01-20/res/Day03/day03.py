"""循环结构"""
# todo for-in循环 while continue break
import time

'''
- `range(101)`：可以用来产生`0`到`100`范围的整数，需要注意的是取不到`101`。
- `range(1, 101)`：可以用来产生`1`到`100`范围的整数，相当于是左闭右开的设定，即`[1, 101)`。
- `range(1, 101, 2)`：可以用来产生`1`到`100`的奇数，其中`2`是步长（跨度），即每次递增的值，`101`取不到。
- `range(100, 0, -2)`：可以用来产生`100`到`1`的偶数，其中`-2`是步长（跨度），即每次递减的值，`0`取不到。
'''
# for i in range(3600):
#     print('hello, world')
#     time.sleep(1)

# todo 从1到100的偶数求和
print(sum(range(2, 101, 2)))

# todo  打印9*9乘法口诀表
for i in range(1, 10):
    for j in range(1, 10):
        if i > j:
            continue
        print(f'{i}×{j}={i * j}', end='\t')
    print()

# todo 找出100以内的素数：素数指的是大于1，只能被1和自身整除的大于1的整数
not_su = []
all_num = []
for s in range(2, 101):
    if s != 2:
        all_num.append(s)
    for i in range(2, s):
        if s % i == 0:
            not_su.append(s)
            break
su = list(set(all_num) - set(not_su))
result = [num for num in all_num if num not in set(not_su)]
print(su)
print(result)

# **提示**：两个数的最大公约数是两个数的公共因子中最大的那个数。
# x = int(input('x = '))
# y = int(input('y = '))
# for i in range(x, 0, -1):
#     if x % i == 0 and y % i == 0:
#         print(f'最大公约数: {i}')
#         break

# 例子2：斐波那契数列 0,1,1,2,3,5,8,13,21
a, b = 0, 1
for _ in range(20):
    a, b = b, a + b
    print(a)