import functions
from threading import Thread
def solve():
    for i in range(1,5):
        t = Thread(name=i, target=functions.f[i])
        t.start()
        t.join()
    for i in range(1,3):
        t = Thread(name=i, target=functions.g[i])
        t.start()
        t.join()

    t = Thread(name=1, target=functions.h[1])
    t.start()
    t.join()

    pass
# solve()
