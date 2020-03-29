import threading

def f():
    print('thread is working')


t = threading.Thread(target=f)
t.start()

def ft(i):
    print('thread with id={} is working'.format(i))


for i in range(0, 3):
    threading.Thread(target=ft, args=(i,)).start()
from threading import Thread
def fd(i, name='default'):
    print('thread named {} with id={} is working'.format(name, i))
for i in range(0, 3):
    Thread(target=fd, args=(i,), kwargs={'name': '{}{}{}'.format(i, i, i)}).start()

print('####################')
def f():
    print('current thread is: ' + threading.currentThread().getName())

print(threading.currentThread().getName())

Thread(target=f)
Thread(name='salam', target=f).start()
Thread(name='khoobi', target=f).start()
Thread(target=f).start()

import threading, time
from threading import Thread

def f():
    print('(' + threading.currentThread().getName() + ') started')
    time.sleep(5)
    print('(' + threading.currentThread().getName() + ') finished')


t = Thread(name = 'non-daemon', target=f)

#t.setDaemon(True)

t.start()
print('####################')
import threading, time
from threading import Thread

def f():
    print('(' + threading.currentThread().getName() + ') started')
    time.sleep(5)
    print('(' + threading.currentThread().getName() + ') finished')


t = Thread(name = 'daemon', target=f)

# t.setDaemon(True)

t.start()
print('####################')

def f():
    print('(' + threading.currentThread().getName() + ') started')
    time.sleep(5)
    print('(' + threading.currentThread().getName() + ') finished')
t = Thread(target=f)
t.start()
t.join()
print('salam')
print(t.isAlive())
print("---------------------")

t = Thread(target=f)
t.start()
t.join(1.0)
print('khoobi?')
print(t.isAlive())
print("---------------------")

t = Thread(target=f)
t.start()
print('che khabar?')
print(t.isAlive())
print("---------------------")
print('####################')
print('####################')
import threading
import time
from threading import Thread

def f(i):
    print('(' + threading.currentThread().getName() + ') is starting')
    time.sleep(i)
    print('(' + threading.currentThread().getName() + ') is finishing')


ls = []
for i in range(1, 5):
    ls.append(Thread(name='t'+str(i), target=f, args=(i,)))

for t in ls:
    t.start()

time.sleep(3)

for t in threading.enumerate():
    print(t.getName() + " is alive now!")