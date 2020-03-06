def f(g):
    h(10)
    return g
def h(a):
    print(a)
f(h)(100)
g = print
g("salam")

def poly_builder(ls):
    def p(x):
        ret = 0
        for i in range(len(ls)):
            ret += ls[i] * (x**i)
        return ret
    return p

f = poly_builder([1, 1]) # x + 1
print(f(-1))
f = poly_builder([-7, 1, 1]) # x^2 + x - 2
print(f(5))
import math

def fact(n):
    if n == 0:
        return 1
    return fact(n-1)*n

a = []
for i in range(0, 100):
    a.append(0)
    if i%2 == 0:
        continue
    a[i] = 1.0/fact(i)
    if int(i/2)%2 == 1:
        a[i] *= -1

sin = poly_builder(a)

print('math sin: ')
print(math.sin(math.pi/6))
print('our sin: ')
print(sin(math.pi/6))

class A:
    def __call__(self, x):
        return x**2
a = A()
print(a(20))
def int_check_decorator(f):
    def g(x):
        if type(x) != int:
            raise Exception('koraa argument should be int')
        return f(x)
    return g
@int_check_decorator
def f(a):
    return a+a

# print(f('salam'))

def return_value_for_10(f):
    return f(10)

@return_value_for_10
def f(a):
    return a+a

print(f)

calls = {}

def call_count_decorator(func):

    calls[func.__name__] = 0

    def ret(*args, **kwargs):
        calls[func.__name__] += 1
        return func(*args, **kwargs)

    return ret

@call_count_decorator
def f(x):
    pass

@call_count_decorator
def g(x, y):
    pass

@call_count_decorator
def h():
    pass

f(1)
f('a')
f('salam')
g(1, 2)
g(2, 2)
h()
h()
for k, v in calls.items():
    print(k + ": " + str(v))

def decorator_builder(check_class):
    def type_checker(func):
        def ret(x):
            if not isinstance(x, check_class):
                return "Argument must be " + check_class.__name__
            else:
                return func(x)
        return ret
    return type_checker

@decorator_builder(int)
def f(x):
    return 2**x

@decorator_builder(type("salam"))
def g(x):
    return x + " khoobi?"

print('f:')
print(f('salam'))
print(f(1))

print('g:')
print(g('salam'))
print(g(1))

class decorator:

    def __init__(self, msg):
        self.msg = msg

    def __call__(self, func):
        def ret():
            print(self.msg)
            return func()
        return ret

dec = decorator('salam')

@dec
def f():
    pass

@decorator('hello')
def g():
    pass

f()
g()
