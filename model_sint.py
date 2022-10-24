from model_uint import *

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
        truelength = max(self.bitsize,other.bitsize)
        val = (self.value + other.value) & (1<<truelength)-1
        return model_sint(val, truelength+1)


    def tohex(self):
        mask = (1<<self.bitsize)-1
        return hex(mask & self.value)

    def print_bits(self):
        result = "u("
        result += str(hex(self.value))#self.tohex()
        result += ")"
        print(self.bitsize, result)
