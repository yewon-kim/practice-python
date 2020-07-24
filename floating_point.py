print((0.1)*3) # 0.30000000000000004
print((0.1)*3 == 0.3) # False

from decimal import Decimal
print(Decimal('0.1')*3) # 0.3
print(Decimal('0.1')*3 == Decimal('0.3')) # True
print(Decimal('0.1')*3 == 0.3) # False

import math
print(math.isclose(0.1*3, 0.3)) # True

from fractions import Fraction
print(Fraction('1/10')*3) # 3/10
print(Fraction('1/10')*3 == Fraction('3/10')) # True