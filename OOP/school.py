from work_place import *
import math
class School(WorkPlace):
    def __init__(self, name):
        super(School, self).__init__(name)
        self.expertise = 'school'

    def calc_capacity(self):
        self.capacity = int(math.floor(math.sqrt(self.level)))

    def calc_costs(self):
        return  int(Consts.BASE_PLACE_COST * math.floor(math.sqrt(self.level)))
