# introspection :: خودآزمایی
#dir
class A:
    def hello(self):
        b = 100
        print(dir())
        pass
    num = 0

a = A()
a.hello()
print(dir(a))

# type 1.type of var 2.define new type ==> (name, (object, ),{'age': 4, 'height': 130, 'name': 'default', 'set_name': set_name})
print(type(a))
def set_name(self, name):
    self.name = name
    pass
Kid = type('MyNewType', (object,), {'age': 4, 'height': 130, 'name': 'default', 'set_name': set_name})
b = Kid()
print(b.age)
b.set_name('ahmad')
print(b.name)

# isinstance( object , [class]) ::is object instance of the class?? True or false

class A:
    pass
class B(A):
    pass
class C:
    pass
a = B()
print(isinstance(a , A))
print(isinstance(a , B))
print(isinstance(a , C))
print(isinstance(a , (A ,C)))

#  issubclass() first class from secon class
class A(list):
    pass
class B(A):
    pass
class C:
    pass
print(issubclass(A, list))
print(issubclass(C, A))

# inspect
import inspect
print(inspect.isclass(A))

#  reflection
    # getattr
class A:
    def __init__(self, age, name):
        self.age = age
        self.name = name
a = A(22, 'amir')
print(getattr(a, 'age'))
s = input()
print(getattr(a, s))
s = input()
print(getattr(a, s, 'eshteb zadi'))
    # setattr()
class T:
    pass
t = T()
setattr(a, 'name', 'ahmad')
setattr(a, 'age', 25)
print(a.name + " , " + str(a.age))

class A:
    def __init__(self):
        self.attrs = {'name': 'amir', 'age': 12, 'grade': 'A'}

    def __getattr__(self, attr):
        if attr in self.attrs:
            return self.attrs[attr]
        def f():
            return getattr(self, attr[4:])

        return f

a = A()

print(a.get_name())
print(a.get_age())
print(a.get_grade())
print(a.get_grad())

#  getattr(object, attribute) == object.__getattr__(attribute)
#attribute is a string