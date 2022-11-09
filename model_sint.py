from model_uint import *

def two_comp(val, bits):
    val = val ^ ( (1 << bits) - 1)
    return (val +1)&((1<<bits)-1)

class model_sint:
    def __init__(self, value, bitsize):
        self.bitsize = bitsize
        self.value = value

    def __eq__ (self, other):
        if isinstance(other, model_uint) or isinstance(other, model_sint):
            if self.value == other.value and self.bitsize == other.bitsize:
                return True
        return False

    def sint_add(self, other):
        print(str(hex(two_comp(self.value, self.bitsize))))
        print(str(hex(two_comp(other.value, other.bitsize))))
        asig = (self.value >> (self.bitsize - 1)) & 1
        bsig = (other.value >> (other.bitsize - 1)) & 1
        maxlength = max(self.bitsize,other.bitsize)
        minlength = min(self.bitsize,other.bitsize)
        if asig ^ bsig: # different signs
            val = (self.value + other.value) & ((1<<minlength)-1)
        else: #same sign
            val = self.value + other.value
        return model_sint(val, maxlength+1)

    def sint_sub(self, other):
        val = self.value + two_comp(other.value, other.bitsize)
        return model_sint(val, max(self.bitsize,other.bitsize)+1)

    def sint_mul(self, other):
        val = self.value * other.value
        return model_sint(val, self.bitsize + other.bitsize)

    def tohex(self):
        mask = (1<<self.bitsize)-1
        return hex(mask & self.value)

    def print_bits(self):
        result = "s("
        result += str(hex(self.value))#self.tohex()
        result += ")"
        print(self.bitsize, result)
