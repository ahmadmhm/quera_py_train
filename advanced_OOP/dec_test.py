from functools import wraps
import random
from django.core.cache import cache as _cache


def cache(*args, **kwargs):

    func = None
    if len(args) == 1 and __builtins__.callable(args[0]):
        func = args[0]

    if func:
        seconds = 60  # default values

    if not func:
        seconds = kwargs.get('seconds')

    def callable(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            cache_key = [func, args, kwargs]
            result = _cache.get(cache_key)
            if result:
                return result
            result = func(*args, **kwargs)
            _cache.set(cache_key, result, timeout=seconds)
            return result
        return wrapped

    return callable(func) if func else callable


@cache(seconds=60)
def function_to_wrap(bits=128):
    return random.getrandbits(bits)

@cache
def function_to_wrap2(bits=128):
    return random.getrandbits(bits)


if __name__ == "__main__":
    print (function_to_wrap()  )# prints '47141457794590517513826129394479136255'
    print (function_to_wrap()  )# prints '47141457794590517513826129394479136255' also (cached)
    print (function_to_wrap2(32))  # prints '2202905596'
    print (function_to_wrap2(32))  # prints '2202905596' also (cached)