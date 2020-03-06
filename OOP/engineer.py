from person import *
import math
class Engineer(Person):
    def __init__(self, name , age):
        super(Engineer, self).__init__(name , age)
        self.job = 'engineer'

    def get_price(self):
        return int(math.floor(Consts.BASE_PRICE[self.job] * math.sqrt(Consts.MIN_AGE / self.age)))

    def calc_life_cost(self):
        return int(math.floor(Consts.BASE_COST[self.job] * math.sqrt(self.age / Consts.MIN_AGE)))

    def calc_income(self):
        return int(math.floor(Consts.BASE_INCOME[self.job][self.work_place.get_expertise()] * math.sqrt(Consts.MIN_AGE / self.age)))