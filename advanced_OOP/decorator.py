def decorator(validate):
    def result(func):
        def check_validate(*args, **kwargs):
            if not validate(*args, **kwargs):
                return 'error'
            return func(*args, **kwargs)
        return check_validate
    return result
def validator(*args, **kwargs):

    return True
    pass
@decorator(validator)
def f(x,y):
   return x*4 + y


d = f(4,3)
print(d)
#https://stackoverflow.com/questions/15299878/how-to-use-python-decorators-to-check-function-arguments
#python custom decorator with arguments and validation