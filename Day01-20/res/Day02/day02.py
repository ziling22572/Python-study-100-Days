"""Python语言中的运算符"""
import math

# todo 1、运算符、分支结构（if elif else match-case`）
'''
| 运算符                                                       | 描述                           |
| ------------------------------------------------------------ | ------------------------------ |
| `[]`、`[:]`                                                 | 索引、切片                  |
| `**`                                                         | 幂                             |
| `~`、`+`、`-`                                              | 按位取反、正号、负号         | 
| `*`、`/`、`%`、`//`                                       | 乘、除、模(取余)、整除            |
| `+`、`-`                                                    | 加、减                        |
| `>>`、`<<`                                                  | 右移、左移                    |
| `&`                                                          | 按位与                         |
| `^`、`|`                                                   | 按位异或、按位或              |
| `<=`、`<`、`>`、`>=`                                      | 小于等于、小于、大于、大于等于 |
| `==`、`!=`                                                   | 等于、不等于                  |
| `is`、`is not`                                               | 身份运算符                     |
| `in`、`not in`                                                | 成员运算符                     |
| `not`、`or`、`and`                                             | 逻辑运算符                     |
| `=`、`+=`、`-=`、`*=`、`/=`、`%=`、`//=`、`**=`、`&=`、`|=`、`^=`、`>>=`、`<<=` | 赋值运算符       |
'''

x = 5  # 二进制表示为 0000 0101
print(x ** 2)  # 输出:25
print(5 % 3)  # 取余：输出:2
print(5 // 3)  # 取整：输出:1

# todo 【位运算】
result = ~x  # 按位取反后变为 1111 1010 再转成二进制
'''
按位取反的规则: 对于一个(正负)整数 x：按位取反的结果是： -x - 1
'''
print(result)  # 输出 -6，如果是-5，则对应的是：4

'''
总结公式
对于任意整数 x 和位移量 n：
右移 x >> n 等价于将 x 除以 2^n 并向下取整（相当于去掉低 n 位）。
左移 x << n 等价于将 x 乘以 2^n（相当于增加高 n 位）。
'''
print(5 >> 3)  # 数字 5 的二进制表示为 0000 0101。向右移动 3 位后，结果为 0000 0000（右侧被移出的部分丢弃，左侧补 0）。转换为十进制值为 0。
print(5 << 3)  # 数字 5 的二进制表示为 0000 0101。向左移动 3 位后，结果为 0010 1000（左侧被移出的部分丢弃，右侧侧补 0）。转换为十进制值为 32+8=40。

'''
& 是按位与（bitwise AND）运算符。它的作用是对两个整数的二进制表示逐位进行“与”操作。只有当两个对应的二进制位都为 1 时，结果的该位才是 1，否则为 0。
总结公式
对于任意两个整数 x 和 y，按位与运算 x & y 的规则是：
如果 x 和 y 对应的二进制位都为 1，则结果的该位为 1。
否则，结果的该位为 0。
'''
#   0101   # 5 的二进制
# & 0011   # 3 的二进制
# ------
#   0001   # 结果 转成十进制：1
print(5 & 3)

'''
`^`、`|` 按位异或、按位或  
对于任意两个整数 x 和 y：
按位异或 x ^ y 的规则是：对应位相同时为 0，不同时为 1。
按位或 x | y 的规则是：对应位中任意一个为 1 时为 1，只有都为 0 时为 0。
'''
#   0110   # 结果 转成十进制：2+4
print(5 ^ 3)
#   0111   # 结果 转成十进制：4+2+1
print(5 | 3)

flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag0
print('flag0 =', flag0)  # flag0 = True
print('flag1 =', flag1)  # flag1 = True
print('flag2 =', flag2)  # flag2 = False
print('flag3 =', flag3)  # flag3 = False
print('flag4 =', flag4)  # flag4 = True
print('flag5 =', flag5)  # flag5 = False
print(flag1 and not flag2)  # True
print(1 > 2 or 2 == 3)  # False

# todo 华氏温度转摄氏度
# f = float(input('请输入华氏温度: '))
# c = (f - 32) / 1.8
# print('%.1f华氏度 = %.1f摄氏度' % (f, c))


# todo 输入半径计算圆的周长和面积
# r = float(input('请输入圆的半径: '))
# # π
# pi=math.pi
# s=round(pi*(r**2),2)
# print(f'圆的面积：{s}' )

# todo 判断闰年
# year = int(input('请输入年份: '))
# is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
# print(f'{is_leap = }')

# todo BMI计算器
height = float(input('身高(cm)：'))
weight = float(input('体重(kg)：'))
bmi = weight / (height / 100) ** 2
print(f'{bmi = :.1f}')
if bmi < 18.5:
    print('你的体重过轻！')
elif bmi < 24:
    print('你的身材很棒！')
elif bmi < 27:
    print('你的体重过重！')
elif bmi < 30:
    print('你已轻度肥胖！')
elif bmi < 35:
    print('你已中度肥胖！')
else:
    print('你已重度肥胖！')

# todo match-case
status_code = int(input('响应状态码: '))
match status_code:
    case 400:
        description = 'Bad Request'
    case 401:
        description = 'Unauthorized'
    case 403:
        description = 'Forbidden'
    case 404:
        description = 'Not Found'
    case 405:
        description = 'Method Not Allowed'
    # todo 带有`_`的`case`语句在代码中起到通配符的作用，上面都没有匹配到的情况往这里走
    case _:
        description = 'Unknown Status Code'
print('状态码描述:', description)
