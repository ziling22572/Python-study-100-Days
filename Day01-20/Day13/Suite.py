# 枚举
from enum import Enum


# 花色
class Suite(Enum):
    """花色(枚举)"""
    # SPADE, HEART, CLUB, DIAMOND = range(4)
    # todo 和下面👆等价
    SPADE, HEART, CLUB, DIAMOND = {0, 1, 2, 3}

# suite = Suite.SPADE
# # 值
# print(suite.value) # 0,1,2,3
# print(suite.name) # SPADE 字符串
