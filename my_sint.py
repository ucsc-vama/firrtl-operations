from my_uint import *

class my_sint:
    def __init__(self, bitsize, value):
        self.bitsize = bitsize
        self.value = value

    def __eq__ (self, other):
        if isinstance(other, my_uint) or isinstance(other, my_sint):
            if self.value == other.value and self.bitsize == other.bitsize:
                return True
        return False
    
    def sint_add(self, other):
        return my_sint(max(self.bitsize,other.bitsize)+1, self.value+other.value)

    def sint_pad(self, n):
        if self.bitsize < n:
            return my_sint(n, self.value)
        else:
            return my_sint(self.bitsize, self.value)

    def sint_cat(self, other):
        return my_sint(self.bitsize + other.bitsize, (self.value << other.bitsize) | other.value)

    def sint_asuint(self):
        return my_uint(self.bitsize, self.value)

    def print_bits(self):
        result = "s(" + hex(self.value) + ")"
        print(result, self.bitsize)
