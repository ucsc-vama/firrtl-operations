from my_sint import *
from my_uint import *

a = my_uint(1, 0x1)
b = my_uint(1, 0x0)
c = a.uint_sub(b)

c.print_bits()