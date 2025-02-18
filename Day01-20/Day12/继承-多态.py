class Person:
    """人"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name}正在吃饭.')

    def sleep(self):
        print(f'{self.name}正在睡觉.')


# todo 继承
class Student(Person):
    def __init__(self, age, name, score, bj):
        super().__init__(name, age)
        self.score = score
        self.bj = bj

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}.')


'''
在这个例子中，Animal 类有一个 speak 方法，它是一个抽象方法（通过 raise NotImplementedError 来模拟）。每个子类（如 Dog, Cat, Bird）都实现了 speak 方法，因此它们的 speak 方法表现出不同的行为。

dog.speak() 返回 "Woof"
cat.speak() 返回 "Meow"
bird.speak() 返回 "Tweet"
尽管我们用相同的方法名 speak，每个类根据自身的实现给出了不同的输出，这就是多态。 
'''
#todo  尽管我们用相同的方法名speak，每个类根据自身的实现给出了不同的输出，这就是 多态。 类似java中的接口不同实现


# 父类：动物类
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

# 子类：狗类
class Dog(Animal):
    def speak(self):
        return "Woof"

# 子类：猫类
class Cat(Animal):
    def speak(self):
        return "Meow"

# 子类：鸟类
class Bird(Animal):
    def speak(self):
        return "Tweet"

# 创建不同的动物对象
dog = Dog()
cat = Cat()
bird = Bird()

# 调用相同的接口方法
animals = [dog, cat, bird]

for animal in animals:
    print(animal.speak())