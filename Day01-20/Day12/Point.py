# 定义一个类描述平面上的点
class Point:

    def __init__(self, x, y):
        """初始化方法
                :param x: 轴坐标
                :param y: 轴坐标
                """
        self.x = x
        self.y = y

    # TODO 计算两个点之间的距离(向量)
    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx ** 2 + dy ** 2) ** 0.5

    # # 调用对象的__str__魔法方法
    def __str__(self):
        return f'({self.x}, {self.y})'
