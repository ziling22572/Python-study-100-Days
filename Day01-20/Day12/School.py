"""todo 动态属性"""
'''
如果不希望在使用对象时动态的为对象添加属性，可以使用 Python 语言中的`__slots__`魔法。对于`School`类来说，可以在类中指定`__slots__ = ('name', 'age')`，这样`Student`类的对象只能有`name`和`age`属性，如果想动态添加其他属性将会引发异常，代码如下所示。
'''


class School:
    # todo 固定属性集合,不能在外面补充参数
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = School('王大锤', 20)
# AttributeError: 'Student' object has no attribute 'sex'
stu.sex = '男'
