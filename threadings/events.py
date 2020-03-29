from threading import Thread, Event, currentThread

import time

def f(e):
    print('{} is waiting for event.'.format(currentThread().getName()))
    value = e.wait()
    print('{} finished waiting.'.format(currentThread().getName()))

def g(e):
    time.sleep(1)
    e.set()
    print('{} set the event.'.format(currentThread().getName()))

e = Event()

t = Thread(name='t', target=f, args=(e,))
s = Thread(name='s', target=g, args=(e,))

t.start()
s.start()
print('####################')
print('####################')
from threading import Thread, Event, currentThread

import time

def f(e):
    print('{} is waiting for event.'.format(currentThread().getName()))
    value = e.wait(2)
    if value:
        print('other thread set the event')
    else:
        print('timeout finished')

def g(e, t):
    time.sleep(t)
    e.set()
    print('{} set the event.'.format(currentThread().getName()))

#timeout check

e = Event()

t = Thread(name='t', target=f, args=(e,))
s = Thread(name='s', target=g, args=(e,3))

t.start()
s.start()

t.join()
print('event value is {}'.format(e.isSet()))
s.join()

#regular check

e.clear()

t = Thread(name='t', target=f, args=(e,))
s = Thread(name='s', target=g, args=(e,1))

t.start()
s.start()

t.join()
print('event value is {}'.format(e.isSet()))
s.join()