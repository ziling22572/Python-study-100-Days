"""
todo 例子2：工资结算系统。
> **要求**：某公司有三种类型的员工，
分别是部门经理、程序员和销售员。
需要设计一个工资结算系统，根据提供的员工信息来计算员工的月薪。
其中，部门经理的月薪是固定15000元；
程序员按工作时间（以小时为单位）支付月薪，每小时200元；
销售员的月薪由1800元底薪加上销售额5%的提成两部分构成。
"""


class Employee:
    def __init__(self, name, salary=0):
        '''
        :param name: 名字
        :param salary: 薪资
        '''
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary


class Manager(Employee):
    def __init__(self, name, salary=15000):
        super().__init__(name, salary)

    # def get_salary(self):
    #     return self.salary


class Developer(Employee):
    # 每小时工钱
    fee_hour = 200

    def __init__(self, name, salary=0, working_hours=0):
        super().__init__(name, salary)
        self.working_hours = working_hours
        self.salary = self.working_hours * self.fee_hour

    # def get_salary(self):
    #     return self.salary


class Sale(Employee):
    start_money = 1800
    sale_percent = 0.05

    def __init__(self, name, salary=0, sale_amount=0):
        super().__init__(name, salary)
        self.sale_amount = sale_amount
        self.salary = round(self.sale_amount * self.sale_percent) + self.start_money


if __name__ == '__main__':
    m = Manager('曹操')
    print(f'{m.name}:{m.salary}💰')
    d = Developer('张辽', 0, 160)
    print(f'{d.name}:{d.salary}💰')
    s = Sale('张三丰', 0, 8000)
    print(f'{s.name}:{s.get_salary()}💰')

