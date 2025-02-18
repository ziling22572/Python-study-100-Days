"""todo 面向对象编程应用:例子1：扑克游戏"""
from Suite import Suite
from random import randint, random


# todo 扑克牌(花色,大小)
class Card:

    def __init__(self, suite, face, is_joker=False):
        self.suite = suite
        self.face = face
        # 大小王，没有花色
        self.is_joker = is_joker

    # todo __repr__ 是一个特殊方法（也叫魔术方法或双下方法）。它用于返回一个对象的字符串表示，并且通常应该提供一个 清晰、不歧义 的字符串，便于调试和展示对象 自动格式化展示
    def __repr__(self):
        suites = '♠♥♣♦'
        faces = ['', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        if self.is_joker:  # 如果是大小王 todo 0代表小王 1代表大王
            return '♞' if self.face == 0 else '♘'  # 小王用 ♞，大王用 ♘
        else:
            return f'{suites[self.suite.value]}{faces[self.face]}'

    # 定义比较规则 todo 没有大小王
    # def __lt__(self, other):  # 小于
    #     if self.face != other.face:  # 先比较点数
    #         return self.face < other.face
    #     return self.suite.value < other.suite.value  # 再比较花色

    # 定义比较规则 有大小王
    def __lt__(self, other):  # 小于
        if self.is_joker and other.is_joker:  # 如果都是大小王
            return self.face < other.face
        elif self.is_joker:  # 如果只有自己是大小王
            return False  # 大小王比其他牌都大
        elif other.is_joker:  # 如果只有对方是大小王
            return True
        else:  # 都不是大小王，按原有规则比较
            if self.face != other.face:  # 先比较点数
                return self.face < other.face
            return self.suite.value < other.suite.value  # 再比较花色

    def __eq__(self, other):  # 相等
        return self.face == other.face and self.suite.value == other.suite.value

# if __name__ == '__main__':
#     card1 = Card(Suite.SPADE, 5)
#     card2 = Card(Suite.HEART, 13)
#     print(card1)  # ♠5
#     print(card2)  # ♥K
#     card3 = Card(None, 0, True)
#     print(card3)
