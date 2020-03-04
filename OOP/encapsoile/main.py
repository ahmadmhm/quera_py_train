import test
test.print_test()
x = test.Test(4)
x.print()
print(test.a)

import test
test.a = 20
test = 4

from test import a

from test import print_test , Test
print_test()

from math import sin as cos
from math import cos as sin
from math import pi as p
print(sin(p))
print(cos(p/2))