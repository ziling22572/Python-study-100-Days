class Triangle:
    class_variable = 0

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # todo 静态方法:当你需要将一个功能封装在类中，但该功能并不依赖于类或实例的属性时，可以使用静态方法。例如：数学运算、工具函数等。
    # 静态方法不访问类的属性或实例的属性。
    # 它和普通函数一样，只是定义在类中的方法。
    # 静态方法可以在没有实例化对象的情况下调用。
    @staticmethod
    def is_valid(a, b, c):
        """判断三条边长能否构成三角形(静态方法)"""
        return a + b > c and b + c > a and a + c > b

    # cls 参数代表类本身
    # todo 类方法可以访问类的属性，但不能直接访问实例属性。
    # 类方法的第一个参数是类本身（cls），而不是实例对象。
    # 类方法通常用于操作类级别的属性，或者创建和修改类的状态。
    @classmethod
    def is_valid1(cls):
        cls.class_variable += 1
        print(f"Class variable: {cls.class_variable}")

    @property
    def perimeter(self):
        """计算周长"""
        return self.a + self.b + self.c

    @property
    def area(self):
        """计算面积"""
        p = self.perimeter / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


t = Triangle(1, 2, 5)
print(t.is_valid(1, 2, 5))
print(f'周长: {t.perimeter}')
print(f'面积: {t.area}')
