import os
import datetime
import sys

src = sys.argv[1]
dst = sys.argv[2]

print(src)
print(dst)
if not os.path.exists(dst):
    os.makedirs(dst)
    pass