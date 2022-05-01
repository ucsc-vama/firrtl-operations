from my_sint import *
from my_uint import *

a = my_uint(240, 0xada3e90d8f93bc7eab12ddf2331939a1340134f12349b10231aca924ade9)
b = my_uint(2, 0x2)
c = a.uint_dshl(b)

c.print_bits()