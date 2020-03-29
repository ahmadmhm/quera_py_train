from threading import Thread, Lock

def synchronized(f):
    lock = Lock()
    def ret(*args, **kwargs):
        lock.acquire()
        res = f(*args, **kwargs)
        lock.release()
        return res
    return ret
    pass
a = 0

@synchronized
def f():
    global a
    for i in range(300000):
        a = a + 1


t = Thread(target=f)
s = Thread(target=f)

t.start()
s.start()

t.join()
s.join()

print(" *** ", a)