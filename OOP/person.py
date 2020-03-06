import math
class Person:
    instances = []

    def __init__(self, name, age=18):
        self.name = name
        self.age = age
        self.job = ""
        self.level = 1
        self.work_place = None
        Person.instances.append(self)
        pass

    class WorkPlace:
        pass
    def get_job(self):
        return self.job
        pass
    def upgrade(self):
        self.level+= 1
        pass
    def calc_income(self):
        pass
    def calc_life_cost(self):
        pass
    def do_level(self, income):
        return income * math.sqrt(self.level * self.work_place.level)
        pass
    def calc(self):
        return  self.do_level(self.calc_income()) - self.calc_life_cost()
        pass

    @staticmethod
    def calc_all():
        sum =0
        for ins in Person.instances:
            sum += ins.calc()
            pass
        return sum
    pass