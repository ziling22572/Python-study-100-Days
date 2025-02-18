from enum import Enum


# 花色
class RoleEnum(Enum):
    """花色(枚举)"""
    SPADE, HEART, CLUB, DIAMOND = range(4)
    # todo 和下面👆等价
    MANAGER, CXY, SALES = {0, 1, 2}
