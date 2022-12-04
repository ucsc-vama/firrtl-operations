from model_uint import *

def two_comp(val, bits):
    val = val ^ ( (1 << bits) - 1)
    val = (val +1)&((1<<bits)-1)# mask
    return val

def signed_subtract(a,b,bits):
    if b > a:
        return two_comp(b-a, bits)
    return a - b
    
def signed_add(a,b,bits):
    if a + b < 0:
        return two_comp(b-a, bits)
    return a + b 

def signed(x,w):
    if (x >= 0):
        return x
    else:
        return 2**w + x

def utos(x, w):
    if (x >= 2**(w-1)):#negative, then remove MSB
        return (x - 2**w)*-1
    else:
        return x

class model_sint:
    def __init__(self, value, bitsize):
        self.sign = (value >> (bitsize - 1)) & 1
        self.bitsize = bitsize
        # self.value = value
        if self.sign:
            self.value = two_comp(value, bitsize)
        else:
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
        maxbit=max(self.bitsize,other.bitsize)
        if self.sign and other.sign:
            val = two_comp(self.value + other.value, maxbit+1)
        elif self.sign and not other.sign:
            val = signed_subtract(other.value, self.value, maxbit+1)
        elif not self.sign and other.sign:
            val = signed_subtract(other.value, self.value, maxbit+1)
        else: # not self.sign and not other.sign:
            val = self.value + other.value
        return model_sint(val, maxbit+1)

    def sint_sub(self, other):
        maxbit=max(self.bitsize,other.bitsize)
        if self.sign and other.sign:
            val = signed_subtract(self.value, other.value, maxbit+1)
        elif self.sign and not other.sign:
            val = two_comp(self.value + other.value, maxbit+1)
        elif not self.sign and other.sign:
            val = other.value + self.value
        else: # not self.sign and not other.sign:
            val = signed_subtract(self.value, other.value, maxbit + 1)
        return model_sint(val, maxbit+1)
        

    # if result is negative, return 2's complement
    # if val's MSB is 1, then find 2's complement. that is the real number
    # do operation with the real number. if MSB was 1, find 2's complement
    def sint_mul(self, other):
        val = self.value * other.value
        if self.sign ^ other.sign:
            val = two_comp(val, self.bitsize+other.bitsize)
        return model_sint(val, self.bitsize + other.bitsize)

    def sint_div(self, other):
        if other.value == 0:
            print("ERROR: divide by zero")
            return model_sint(0, self.bitsize)
        val = int(self.value / other.value)
        if self.sign ^ other.sign:
            val = two_comp(val, self.bitsize+1)
        return model_sint(val, self.bitsize + 1)

    def sint_mod(self, other):
        if other.value == 0:
            print("ERROR: divide by zero")
            return model_sint(0, self.bitsize)
        minsize = min(self.bitsize, other.bitsize)
        r = a % b
        if asig and bsig:
            r = two_comp(r,minsize)
        return model_sint(r, minsize)

    def sint_lt(self, other):
        asig = (self.value >> (self.bitsize - 1)) & 1
        bsig = (other.value >> (other.bitsize - 1)) & 1
        if asig and not bsig:
            return model_sint(0x1, 1)
        if not asig and bsig:
            return model_sint(0x0, 1)
        a = self.value
        b = other.value
        if asig == 1:
            a = two_comp(self.value, self.bitsize)
        if bsig == 1:
            b = two_comp(other.value, other.bitsize)
        if not asig and not bsig:
            if a < b:
                return model_sint(0x1, 1)
            return model_sint(0x0, 1)
        else:
            if a > b:
                return model_sint(0x1, 1)
            return model_sint(0x0, 1)

    def sint_leq(self, other):
        asig = (self.value >> (self.bitsize - 1)) & 1
        bsig = (other.value >> (other.bitsize - 1)) & 1
        if asig and not bsig:
            return model_sint(0x1, 1)
        if not asig and bsig:
            return model_sint(0x0, 1)
        a = self.value
        b = other.value
        if asig == 1:
            a = two_comp(self.value, self.bitsize)
        if bsig == 1:
            b = two_comp(other.value, other.bitsize)
        if not asig and not bsig:
            if a <= b:
                return model_sint(0x1, 1)
            return model_sint(0x0, 1)
        else:
            if a >= b:
                return model_sint(0x1, 1)
            return model_sint(0x0, 1)

    def sint_gt(self, other):
        asig = (self.value >> (self.bitsize - 1)) & 1
        bsig = (other.value >> (other.bitsize - 1)) & 1
        if not asig and bsig:
            return model_sint(0x1, 1)
        if asig and not bsig:
            return model_sint(0x0, 1)
        a = self.value
        b = other.value
        if asig == 1:
            a = two_comp(self.value, self.bitsize)
        if bsig == 1:
            b = two_comp(other.value, other.bitsize)
        if not asig and not bsig:
            if a <= b:
                return model_sint(0x1, 1)
            return model_sint(0x0, 1)
        else:
            if a >= b:
                return model_sint(0x1, 1)
            return model_sint(0x0, 1)
        

    def tohex(self):
        mask = (1<<self.bitsize)-1
        return hex(mask & self.value)

    def print_bits(self):
        result = "s("
        result += hex(self.value)#self.tohex()
        result += ")"
        print(self.bitsize, result)
