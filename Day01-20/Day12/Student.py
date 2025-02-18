class Student:
    """学生"""
    # 类属性
    species = "high school"

    #  name ,age,course_name 属于静态属性:特征
    # study,play 属于动态属性:方法
    #  __init__ todo 初始化构造方法:参数 (get/set)
    def __init__(self, name, age, sex):
        """初始化方法"""
        self.name = name
        self.age = age
        self.__sex = sex

    def study(self, course_name):
        """学习"""
        print(f'{self.name}{self.species}正在学习{course_name}.')

    def play(self):
        """玩耍"""
        print(f'{self.__sex}{self.name}正在玩游戏.')


    # todo 类方法（使用 @ classmethod 装饰器）：类方法的第一个参数是类本身（通常命名为cls）。
    # todo 静态方法（使用 @ staticmethod装饰器）：静态方法不依赖于实例或类，可以不传递任何参数。

    # 类方法
    @classmethod
    def common_species(cls):
        return f"All dogs belong to the species {cls.species}."

    # 静态方法
    @staticmethod
    def is_domestic():
        return "Dogs are domestic animals."


stu = Student("zs", "12", "man")
stu.study('Python')
stu.play()
