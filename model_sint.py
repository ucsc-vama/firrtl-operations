from model_uint import *

def two_comp(val, bits):
    val = val ^ ( (1 << bits) - 1)
    return (val +1)&((1<<bits)-1)

def signed_subtract(a,b):
    if b > a:
        return two_comp(b-a)
    return a - b


class model_sint:
    def __init__(self, value, bitsize):
        self.bitsize = bitsize
        self.value = value

    def __eq__ (self, other):
        if isinstance(other, model_uint) or isinstance(other, model_sint):
            if self.value == other.value and self.bitsize == other.bitsize:
                return True
        return False

    # for a and b, if MSB is 1, then find 2's complement
    # if MSB is 1, that means its negative, therefore do normal addition taking that into account
    # if reslt is negative, return 2's complement
    def sint_add(self, other):
        asig = (self.value >> (self.bitsize - 1)) & 1
        bsig = (other.value >> (other.bitsize - 1)) & 1
        maxbit=max(self.bitsize,other.bitsize)
        a = self.value
        b = other.value
        if asig == 1:
            a = two_comp(self.value, self.bitsize)
        if bsig == 1:
            b = two_comp(other.value, other.bitsize)
        if asig > bsig:
            val = signed_subtract(b,a)
        elif asig < bsig:
            val = signed_subtract(a,b)
        elif asig and bsig:
            val = a+b
            val = two_comp(val, maxbit+1)
        else:
            val = a + b
        return model_sint(val, maxbit+1)

    def sint_sub(self, other):
        val = self.value + two_comp(other.value, other.bitsize)
        return model_sint(val, max(self.bitsize,other.bitsize)+1)

    # if result is negative, return 2's complement
    # if val's MSB is 1, then find 2's complement. that is the real number
    # do operation with the real number. if MSB was 1, find 2's complement
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
