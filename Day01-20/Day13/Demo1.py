# 牌面映射
card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

# 牌面集合
cards = ['♣8', '♠4', '♦10', '♠A', '♥3', '♣J', '♠9', '♣5', '♥10', '♦Q', '♣3', '♠2', '♦J']

# 提取花色和牌面，按牌面数字排序
def card_sort_key(card):
    # 获取牌面的值（例如 '8', 'A'）
    value = card[1:]  # 从第二个字符开始提取数字或字母
    return card_values.get(value, 0)  # 返回对应的数值

# 排序
sorted_cards = sorted(cards, key=card_sort_key)

# 输出排序后的牌
print(sorted_cards)