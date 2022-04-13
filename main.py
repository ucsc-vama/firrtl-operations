from my_sint import *
from my_uint import *

a = my_uint(16, 0xf3)
b = my_uint(16, 0x3)
c = a.uint_sub(b)

c.print_bits()