try:
    x = int(input())
except ValueError:
    print("input isn't number")

for i in range(4):
    try:
        if i == 0:
            1/0
        if i == 1:
            int("salam")
        if i == 2:
            "salam" + 1
        if i == 3:
            raise NameError('salam')
    except ZeroDivisionError:
        print("ZeroDivisionError called") # 1/0
    except TypeError:
        print("TypeError called") # "salam" + 1
    except ValueError:
        print("ValueError called") # int("salam")
    except (ZeroDivisionError, TypeError, ValueError):
        print("an error occurred")
    except NameError:
        print('an exception raised')

class A(Exception):
    pass
class C(A):
    pass
try:
    raise C
except A as e:
    print('exception found', type(e))
finally:
    print('finally is running')