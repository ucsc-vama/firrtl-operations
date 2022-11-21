from model_uint import *

def two_comp(val, bits):
    val = val ^ ( (1 << bits) - 1)
    return (val +1)&((1<<bits)-1)

def signed_subtract(a,b,bits):
    if b > a:
        return two_comp(b-a, bits)
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
            val = signed_subtract(b,a, maxbit+1)
        elif asig < bsig:
            val = signed_subtract(a,b, maxbit+1)
        elif asig and bsig:
            val = a+b
            val = two_comp(val, maxbit+1)
        else:
            val = a + b
        return model_sint(val, maxbit+1)

    def sint_sub(self, other):
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
            val = a+b
            val = two_comp(val, maxbit+1)
        elif asig < bsig:
            val = a+b
        elif asig and bsig:
            val = signed_subtract(b,a,maxbit+1)
        else:
            val = signed_subtract(a,b,maxbit+1)
        val = self.value + two_comp(other.value, other.bitsize)
        return model_sint(val, max(self.bitsize,other.bitsize)+1)

    # if result is negative, return 2's complement
    # if val's MSB is 1, then find 2's complement. that is the real number
    # do operation with the real number. if MSB was 1, find 2's complement
    def sint_mul(self, other):
        asig = (self.value >> (self.bitsize - 1)) & 1
        bsig = (other.value >> (other.bitsize - 1)) & 1
        a = self.value
        b = other.value
        if asig == 1:
            a = two_comp(self.value, self.bitsize)
        if bsig == 1:
            b = two_comp(other.value, other.bitsize)
        val = a * b
        if asig ^ bsig:
            val = two_comp(val, self.bitsize+other.bitsize)
        return model_sint(val, self.bitsize + other.bitsize)

    def sint_div(self, other):
        if other.value == 0:
            print("ERROR: divide by zero")
            return model_sint(0, self.bitsize)
        asig = (self.value >> (self.bitsize - 1)) & 1
        bsig = (other.value >> (other.bitsize - 1)) & 1
        a = self.value
        b = other.value
        if asig == 1:
            a = two_comp(self.value, self.bitsize)
        if bsig == 1:
            b = two_comp(other.value, other.bitsize)
        val = int(a / b)
        if asig ^ bsig:
            val = two_comp(val, self.bitsize+1)
        return model_sint(val, self.bitsize + 1)

    def sint_mod(self, other):
        if other.value == 0:
            print("ERROR: divide by zero")
            return model_sint(0, self.bitsize)
        asig = (self.value >> (self.bitsize - 1)) & 1
        bsig = (other.value >> (other.bitsize - 1)) & 1
        minsize = min(self.bitsize, other.bitsize)
        a = self.value
        b = other.value
        if asig == 1:
            a = two_comp(self.value, self.bitsize)
        if bsig == 1:
            b = two_comp(other.value, other.bitsize)
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
        pass

    def tohex(self):
        mask = (1<<self.bitsize)-1
        return hex(mask & self.value)

    def print_bits(self):
        result = "s("
        result += str(hex(self.value))#self.tohex()
        result += ")"
        print(self.bitsize, result)
