import os
import datetime
import sys
print(sys.argv)
a = os.getcwd()
print(a)
os.listdir()
os.rename('os.py', 'os.py')
b = os.walk('..')
print(list(b))
print(os.path.exists('project'))
os.path.basename('os.py')
t = os.path.getmtime('os.py')
print( datetime.datetime.fromtimestamp(t).year)