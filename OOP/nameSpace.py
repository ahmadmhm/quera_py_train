def f():
    # non-local scope for inner functions

    msg = "salam"

    def test_local():
        msg = "khoobi?"
        print("in function: " + msg)

    def test_nonlocal():
        nonlocal msg
        msg = "chetori?"
        print("in function: " + msg)

    def test_global():
        global msg
        msg = "chera?!"
        print("in function: " + msg)

    test_local()
    print(msg)
    test_nonlocal()
    print(msg)
    test_global()
    print(msg)
    pass


f()
print(msg)

class Game1:
    pass

game = Game1()
print(type(game))
print(type(Game1))

class Person1:
    pass
p1 = Person1()
p2 = Person1()
p1.name = 'mohamadreza'
p1.age = 18
print(p1.name, p1.age)
# print(p2.name)

class Game:
    def set_money(self, x):
        self.money = x

    def get_money(self):
        return self.money

game = Game()
game.set_money(4)
print(game.get_money())
Game.set_money(game, 5)
print(game.money)

class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

p1 = Person("Ali", 12)
p2 = Person("Amir")
print(p1.name, p1.age)
print(p2.name, p2.age)

class Game:
    goal_money = 3000

    def set_money(self, x):
        self.money = x

    def get_money(self):
        return self.money


print("Game.goal_money:", Game.goal_money)
Game.max_people_count = 20
print("Game.max_people_count:", Game.max_people_count)
game = Game()
game.goal_money = 2000
print("game.goal_money:", game.goal_money)
print("Game.goal_money:", Game.goal_money)
del game.goal_money
print("game.goal_money:", game.goal_money)

class Sample:
    goal_money = 3000

    def __init__(self):
        pass

    @staticmethod
    def increase_goal_money(value):
        Sample.goal_money += value


sample = Sample()
print(Sample.goal_money)
Sample.increase_goal_money(100)
print(sample.goal_money)

class Sample:
    def __init__(self, x):
        self.__x = x

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x


sample = Sample(2)
print(sample.get_x())
sample.set_x(20)
print(sample.get_x())
print(dir(sample))
# print(sample.__x) has error
print(sample._Sample__x)