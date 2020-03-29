from threading import Thread, Lock

class Counter:
    def __init__(self):
        self.lock = Lock()
        self.value = 0

    def increment(self):
        self.lock.acquire()
        self.value += 1
        self.lock.release()

def f():
    global counter
    for i in range(200000):
        counter.increment()

def test():
    global counter
    counter = Counter()

    t = Thread(target=f)
    s = Thread(target=f)

    t.start()
    s.start()

    t.join()
    s.join()

for i in range(1, 5):
    test()
    print("in test {}: value of a is {} and must be {}".format(i, counter.value, 200000*2))