'''
todo 52张牌,然后每个人随机14张,然后不重复
'''
import random

from sympy.abc import lamda

from Card import Card
from Suite import Suite


class Poker:
    def __init__(self):
        #  # 52张牌构成的列表
        self.cards = [Card(suite, face)
                      for suite in Suite
                      for face in range(1, 14)
                      ]
        # 添加大小王
        self.cards.append(Card(None, 0, is_joker=True))  # 小王
        self.cards.append(Card(None, 1, is_joker=True))  # 大王
        self.current = 0  # 记录发牌位置的属性

    def shuffle(self):
        """洗牌"""
        self.current = 0
        # todo 通过random模块的shuffle函数实现随机乱序
        random.shuffle(self.cards)

    def deal(self):
        """发牌"""
        card = self.cards[self.current]
        self.current += 1
        return card

    @property
    def has_next(self):
        """还有没有牌可以发"""
        return self.current < len(self.cards)


# 定义玩家
class Player:

    def __init__(self, name):
        self.name = name
        self.cards = []

    #     摸牌
    def add_card(self, card):
        self.cards.append(card)

    def arrange(self):
        """整理手上的牌"""
        self.cards.sort()


# 创建四个玩家
if __name__ == '__main__':
    players = [Player('东邪'),
               Player('西毒'),
               # Player('南帝'),
               Player('北丐'),
               Player('底牌')]
    # 随机地主👲
    player_value = '🧒'
    landlord_value = '👲'
    landlord_name = players[random.randint(0, 2)].name
    print(f'\r\n这一局的地主👲是：{landlord_name}')
    # 先洗牌
    poker = Poker()
    poker.shuffle()
    # 开始每个人发17张牌,然后底牌留三张
    for player in players:
        if player.name == '底牌':
            for _ in range(3):
                player.add_card(poker.deal())
        else:
            for _ in range(17):
                player.add_card(poker.deal())

    # 先拿出底牌，然后给到地主手上
    bottom_cards = players[3].cards
    print(f'底牌: ', end='')
    print(bottom_cards)
    match landlord_name:
        case '东邪':
            players[0].cards.extend(bottom_cards)
        case '西毒':
            players[1].cards.extend(bottom_cards)
        case '北丐:':
            players[2].cards.extend(bottom_cards)
        case _:
            description = '这局没地主哦'

    # 玩家整理手上的牌输出名字和手牌
    for player in players:
        if player.name == '底牌':
            continue
        player.arrange()
        # todo 三目运算符： 满足条件的结果 if landlord_name == player.name else 不满足条件的结果
        print(f'{landlord_value if landlord_name == player.name else player_value}{player.name}: ', end='')
        print(player.cards)
