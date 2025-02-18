""" todo 面向对象 """
'''
1:类和对象:**封装**、**继承**和**多态**
2:可见性和属性装饰器 :以`__`开头的属性`__name`相当于是私有的,外面无法访问,内部可以正常访问
3:静态方法 @staticmethod (在类加载前优先加载)和类方法(普通方法)
4:@property :方法作为类属性 
5:继承和多态
'''


# todo 类
class Student1:
    """学生"""
    species = "high school"

    #  name ,age,course_name 属于静态属性:特征
    # study,play 属于动态属性:方法
    #  __init__ todo 初始化构造方法:参数 (get/set)
    def __init__(self, name, age, sex):
        """初始化方法"""
        self.name = name
        self.age = age
        # 外部无法访问 可以赋值
        self.__sex = sex

    def study(self, course_name):
        """学习"""
        print(f'{self.name}正在学习{course_name}.')

    def play(self):
        """玩耍"""
        print(f'{self.name}正在玩游戏.')

        # 类方法

        # todo 类方法（使用 @ classmethod 装饰器）：类方法的第一个参数是类本身（通常命名为cls）。

    @classmethod
    def common_species(cls):
        return f"All dogs belong to the species {cls.species}."

        # todo 静态方法（使用 @ staticmethod装饰器）：静态方法不依赖于实例或类，可以不传递任何参数。

    # 静态方法
    @staticmethod
    def is_domestic():
        return "Dogs are domestic animals."
