"""from datetime import time
t = time(17, 21, 20, 2021)
print(t , "# ", type(t))
"""
"""
from datetime import date
d = date(2019, 5, 23)
print(d.year, d.month, d.day)
"""

from datetime import datetime
dt = datetime(1, 2, 3, 4, 5, 6, 7)
print(dt.year, dt.month, dt.day, dt.minute )
print()
print(datetime.now())