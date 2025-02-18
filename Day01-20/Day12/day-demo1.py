# 导入 Student.py 文件中的 Student 类 todo import 类名
from Student import Student
from Clock import Clock
from Point import Point
from Triangle import Triangle
import time

if __name__ == '__main__':
    # 调用初始化方法
    stu = Student("zs", "12", "man")
    stu.study('Python')
    stu.play()
    # todo 这里可以动态加属性
    stu.dept = "python"
    print(stu.dept)
    # print(stu.sex)  # todo AttributeError: 'Student' object has no attribute '__sex'

    p1 = Point(1, 2)
    print(p1)
    p2 = Point(-1, 3)
    print(p2)
    print(f'p1和p2两点之间的距离为{p1.distance_to(p2)}')

    # 创建时钟对象
    clock = Clock(23, 59, 58)
    while True:
        # 给时钟对象发消息读取时间
        print(clock.show())
        # 休眠1秒钟
        time.sleep(1)
        # 给时钟对象发消息使其走字
        clock.run()

