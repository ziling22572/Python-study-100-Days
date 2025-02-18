import random
import string

from django.db.models.expressions import result

'''
 例子1：随机验证码: 设计一个生成随机验证码的函数，验证码由数字和英文大小写字母构成，长度可以通过参数设置。
'''

ALL_CHARS = string.digits + string.ascii_letters


# todo 当函数定义中使用 * 时，它意味着在 * 之后的所有参数都必须通过关键字参数的形式传递，而不能作为位置参数传递。也就是说，调用函数时必须明确指定参数名和对应的值。
# 给默认值code_len=6
def generate_code(*, code_len=6):
    """
    生成指定长度的验证码
    :param code_len: 验证码的长度(默认4个字符)
    :return: 由大小写英文字母和数字构成的随机验证码字符串
    """
    return ''.join(random.choices(ALL_CHARS, k=code_len))


#  错误的调用方式，不能使用位置参数，只能用关键字参数
# todo  generate_code(8)  # 这会引发 TypeError
print(generate_code(code_len=7))

'''
 例子1：判断素数:设计一个判断给定的大于1的正整数是不是质数的函数。质数是只能被1和自身整除的正整数（大于1），如果一个大于1的正整数$N$是质数，那就意味着在2到$N-1$之间都没有它的因子。
'''


def is_prime(num: int) -> bool:
    """
      判断一个正整数是不是质数
      :param num: 大于1的正整数
      :return: 如果num是质数返回True，否则返回False
    """
    if num < 2:
        print(f'请输入大于1的整数')
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        print(f'{num}：是个素数')
        return True


# a = int(input(f'请输入一个整数'))
# print(is_prime(a))

"""求最小公倍数"""


def lcm(x: int, y: int) -> int:
    return x * y // gcd(x, y)


"""求最大公约数"""


def gcd(x: int, y: int) -> int:
    while y % x != 0:
        x, y = y % x, x
    return x


# 最小公倍数等于除数和最后的商相乘，即。7*3*4=84
print(lcm(21, 28))  # 最小可以整除x,y的数
print(gcd(20, 12))  # 最大可以被x,y的整除的数:4


# todo 极差：最大值-最小值
def ptp(data):
    """极差（全距）"""
    return max(data) - min(data)


# todo 算术平均：所有数值相加/个数
def mean(data):
    """算术平均"""
    return sum(data) / len(data)


# todo 中位数：所有数值位于中间的那个数据，如果是偶数就取中间的两个/2,如果是奇数就取中间，前提是排好序了
def median(data):
    """中位数"""
    temp, size = sorted(data), len(data)
    if size % 2 != 0:
        return temp[size // 2]
    else:
        return mean(temp[size // 2 - 1:size // 2 + 1])


# todo 方差：方差的公式用于衡量一组数据的离散程度，表示数据与其平均值之间的偏差大小
'''


'''


# 总体方差用于描述整个数据集的离散程度。
# 样本方差用于估计总体方差。
# 方差越大，数据的波动性越大；方差越小，数据越集中。
def var(data, ddof=1):
    """方差"""
    x_bar = mean(data)
    temp = [(num - x_bar) ** 2 for num in data]
    return sum(temp) / (len(temp) - ddof)


# ** 0.5代表开根号√
# 标准差是方差的平方根，用于衡量数据分布的离散程度。与方差相比，标准差的单位和原始数据一致，因此更具直观性
def std(data, ddof=1):
    """标准差"""
    return var(data, ddof) ** 0.5


# todo 变异系数通过将标准差与均值的比值来表示。变异系数（Coefficient of Variation, 简称 CV）是衡量数据相对离散程度的一个无量纲指标，常用于比较不同数据集的波动性，尤其是在均值差异较大的情况下
def cv(data, ddof=1):
    """变异系数"""
    return std(data, ddof) / mean(data)


def describe(data):
    """输出描述性统计信息"""
    print(f'均值: {mean(data)}')
    print(f'中位数: {median(data)}')
    print(f'极差: {ptp(data)}')
    print(f'方差: {var(data)}')
    print(f'标准差: {std(data)}')
    print(f'变异系数: {cv(data, ddof=1)}')


demo_data = [1, 3, 4, 5, 6, 11, 88, 89, 90, 1000, 1111, 1112]
print(describe(demo_data))

# todo 例子5：双色球随机选号（红球 1-33 蓝球1-16）
RED_BALLS = [i for i in range(1, 34)]
BLUE_BALLS = [i for i in range(1, 17)]


# 获取指定组的双色球列表，红在前 蓝在后
def get_red_blue_balls():
    selected_balls = random.sample(RED_BALLS, 6)
    selected_balls.sort()
    # 选择一个
    selected_balls.append(random.choice(BLUE_BALLS))
    return selected_balls


def display(balls):
    """
    格式输出一组号码
    :param balls: 保存随机号码的列表
    """
    res = check_lottery(balls)
    for ball in balls[:-1]:
        print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
    print(f'\033[034m{balls[-1]:0>2d}\033[0m------------->中奖情况：{res}')


winning_numbers = [4, 11, 15, 24, 25, 33, 15]  # 中奖的号码

'''
一等奖：投注号码与当期开奖号码全部相同（顺序不限，下同），即中奖；
二等奖：投注号码与当期开奖号码中的6个红色球号码相同，即中奖；
三等奖：投注号码与当期开奖号码中的任意5个红色球号码和1个蓝色球号码相同，即中奖；
四等奖：投注号码与当期开奖号码中的任意5个红色球号码相同，或与任意4个红色球号码和1个蓝色球号码相同，即中奖；
五等奖：投注号码与当期开奖号码中的任意4个红色球号码相同，或与任意3个红色球号码和1个蓝色球号码相同，即中奖；
六等奖：投注号码与当期开奖号码中的1个蓝色球号码相同，即中奖。
'''


def check_lottery(user_numbers):
    # 假设用户输入的号码是一个包含7个数字的列表
    # 例如：user_numbers = [1, 2, 3, 4, 5, 6, 10]

    # 中奖号码是一个包含7个数字的列表
    # 例如：winning_numbers = [1, 2, 3, 4, 5, 6, 10]
    # print(f'当前号码：{user_numbers}')
    # 将红号和蓝号分开
    user_reds, user_blue = user_numbers[:6], user_numbers[6]
    winning_reds, winning_blue = winning_numbers[:6], winning_numbers[6]

    # 检查红号匹配数量情况
    red_matches = len(set(user_reds) & set(winning_reds))  # 交集，计算红号匹配数量

    # 判断中奖情况
    if set(user_numbers) == set(winning_numbers):  # 全部号码完全相同
        return "🐂一等奖！"
    elif red_matches == 6:  # 红号完全相同，蓝号不一定相同
        return "二等奖！"
    elif red_matches == 5 and user_blue == winning_blue:  # 5个红号和1个蓝号相同
        return "三等奖！"
    elif red_matches == 5 or (red_matches == 4 and user_blue == winning_blue):  # 5个红号或4个红号加1个蓝号相同
        return "四等奖！"
    elif red_matches == 4 or (red_matches == 3 and user_blue == winning_blue):  # 4个红号或3个红号加1个蓝号相同
        return "五等奖！"
    elif user_blue == winning_blue:  # 1个蓝号相同
        return "六等奖！"
    else:
        return "😭谢谢参与！"


n = int(input('生成几注号码: '))
for _ in range(n):
    display(get_red_blue_balls())
