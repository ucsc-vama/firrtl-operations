import uint
from math import *

def two_comp(val, bits):
    val = val ^ ( (1 << bits) - 1)
    val = (val +1)&((1<<bits)-1)# mask
    return val

def signed_subtract(a,b,bits):
    if b > a:
        return two_comp(b-a, bits)
    return a - b
    
# def signed_add(a,b,bits):
#     if a + b < 0:
#         return two_comp(b-a, bits)
#     return a + b 

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
    
def getbitsize(value):
    if value == 0:
        return 1
    return ceil(log2(value+1))

class model_sint:
    def __init__(self, value, bitsize=None):
        self.type = "sint"
        if bitsize == None:
            self.bitsize = getbitsize(value)
        elif bitsize <= 0:
                # print("incorrect bitsize")
                self.bitsize=1
        else:
            self.bitsize = bitsize
        self.sign = (value >> (self.bitsize - 1)) & 1
        self.realval = value
        if self.sign:
            self.value = two_comp(value, self.bitsize)
        else:
            self.value = value

    def __eq__ (self, other):
        if isinstance(other, uint.model_uint) or isinstance(other, model_sint):
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
            val = signed_subtract(self.value, other.value, maxbit+1)
        else: # not self.sign andnot  other.sign:
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
        r = self.value % other.value
        if self.sign and other.sign:
            r = two_comp(r,minsize)
        return model_sint(r, minsize)

    def sint_lt(self, other):
        if self.sign and not other.sign:
            return model_sint(0x1, 1)
        if not self.sign and other.sign:
            return model_sint(0x0, 1)
        if not self.sign and not other.sign:
            if self.value < other.value:
                return model_sint(0x1, 1)
            return model_sint(0x0, 1)
        else:
            if self.value > other.value:
                return model_sint(0x1, 1)
            return model_sint(0x0, 1)

    def sint_leq(self, other):
        if self.sign and not other.sign:
            return model_sint(0x1, 1)
        if not self.sign and other.sign:
            return model_sint(0x0, 1)
        if not self.sign and not other.sign:
            if self.value <= other.value:
                return model_sint(0x1, 1)
            return model_sint(0x0, 1)
        else:
            if self.value >= other.value:
                return model_sint(0x1, 1)
            return model_sint(0x0, 1)

    def sint_gt(self, other):
        if self.sign and not other.sign:
            return model_sint(0x0, 1)
        if not self.sign and other.sign:
            return model_sint(0x1, 1)
        if not self.sign and not other.sign:
            if self.value > other.value:
                return model_sint(0x1, 1)
            return model_sint(0x0, 1)
        else:
            if self.value < other.value:
                return model_sint(0x1, 1)
            return model_sint(0x0, 1)
        
    def sint_geq(self,other):
        if self.sign and not other.sign:
            return model_sint(0x0, 1)
        if not self.sign and other.sign:
            return model_sint(0x1, 1)
        if not self.sign and not other.sign:
            if self.value >= other.value:
                return model_sint(0x1, 1)
            return model_sint(0x0, 1)
        else:
            if self.value <= other.value:
                return model_sint(0x1, 1)
            return model_sint(0x0, 1)

    def sint_eq(self, other):
        if self.value == other.value and self.sign == other.sign:
            return model_sint(0x1, 1)
        return model_sint(0x0, 1)

    def sint_neq(self, other):
        if self.value == other.value  and self.sign == other.sign:
            return model_sint(0x0, 1)
        return model_sint(0x1, 1)

    def sint_pad(self, n):
        if n < 0:
            print("ERROR: pad size must be positive")
            return self
        if n <= self.bitsize:
            return self
        if self.sign == 0:
            return model_sint(self.value, n)
        extend = (1 << (n-self.bitsize)) - 1
        realval = two_comp(self.value, self.bitsize)
        val = (extend << self.bitsize) | realval
        return model_sint(val, n)

    def sint_asUInt(self):#cant figure out the difference between asUInt and cvt
        if self.sign:
            val = two_comp(self.value, self.bitsize)
        else:
            val = self.value
        return uint.model_uint(val, self.bitsize)

    def sint_asSInt(self):
        return self

    def sint_shl(self, n):
        # if self.sign:
        #     val = two_comp(self.value, self.bitsize)
        # else:
        #     val = self.value
        val = self.value << n
        return model_sint(val, self.bitsize + n)

    def sint_shr(self, n):
        # if self.sign:
        #     val = two_comp(self.value, self.bitsize)
        # else:
        #     val = self.realval
        val = self.value >> n
        return model_sint(val, self.bitsize - n)

    def sint_dshl(self, shift):
        val = self.realval
        newsize =  self.bitsize + 2**shift.bitsize-1
        val = self.value << shift.value
        if self.sign:
            # extend = ((1 << (newsize-self.bitsize))-1) << self.bitsize
            extend = 1 << self.bitsize
            val = val | extend
        # val <<= shift.value
        return model_sint(val, newsize)

    def sint_dshr(self, shift):
        val = self.realval
        val >>= shift.value
        if self.sign:
            extend = ((1 << shift.value)-1) << (self.bitsize-shift.value)
            val = val | extend
        return model_sint(val, self.bitsize)

    def sint_cvt(self): #cant figure out the difference between asUInt and cvt
        return self

    def sint_neg(self):
        val = two_comp(self.realval, self.bitsize)
        if not self.sign:
            val = val | (1<<self.bitsize)
        return model_sint(val, self.bitsize+1)

    def sint_not(self):
        result = 0
        for i in range(self.bitsize):
            result |= ((~self.realval>>i)&1) << i
        return uint.model_uint(result, self.bitsize)

    def sint_and(self, other):
        result = 0
        maxbits = max(self.bitsize, other.bitsize)
        a = model_sint(self.realval, self.bitsize).sint_pad(maxbits)
        b = model_sint(other.realval, other.bitsize).sint_pad(maxbits)
        for i in range(maxbits):
            result |= ((a.realval>>i)&1 & (b.realval>>i)&1) << i
        return model_sint(result, maxbits)

    def sint_or(self, other):
        result = 0
        maxbits = max(self.bitsize, other.bitsize)
        a = model_sint(self.realval, self.bitsize).sint_pad(maxbits)
        b = model_sint(other.realval, other.bitsize).sint_pad(maxbits)
        for i in range(maxbits):
            result |= ((a.realval>>i)&1 | (b.realval>>i)&1) << i
        return model_sint(result, maxbits)

    def sint_xor(self, other):
        result = 0
        maxbits = max(self.bitsize, other.bitsize)
        a = model_sint(self.realval, self.bitsize).sint_pad(maxbits)
        b = model_sint(other.realval, other.bitsize).sint_pad(maxbits)
        for i in range(maxbits):
            result |= ((a.realval>>i)&1 ^ (b.realval>>i)&1) << i
        return model_sint(result, maxbits)

    def sint_andr(self):
        result = 1
        for i in range(self.bitsize):
            bit_i = (self.realval & (1<<i))>>i
            result = result & bit_i
        return model_sint(result, 1)

    def sint_orr(self):
        result = 0
        for i in range(self.bitsize):
            bit_i = (self.realval & (1<<i))>>i
            result = result | bit_i
        return model_sint(result, 1)

    def sint_xorr(self):
        result = 0
        for i in range(self.bitsize):
            bit_i = (self.realval & (1<<i))>>i
            result = result ^ bit_i
        return model_sint(result, 1)

    def sint_cat(self, other):
        if other.value == 0:
            return model_sint((self.realval<<other.bitsize), self.bitsize+other.bitsize)
        return model_sint((self.realval<<other.bitsize)|other.realval, self.bitsize+other.bitsize)

    def sint_bits(self, hi, lo):
        if hi > lo and hi < self.bitsize:
            return uint.model_uint((self.realval>>lo)&(2**(hi-lo+1)-1), hi-lo+1)
        if hi == lo:
            return uint.model_uint(0,0)
        return uint.model_uint(0,1)

    def sint_head(self, n):
        if n >= 0 and n <= self.bitsize:
            return uint.model_uint(self.realval>>(self.bitsize-n), n)
        return uint.model_uint(0,1)

    def sint_tail(self, n):
        if n == self.bitsize:
            return uint.model_uint(0,0)
        if self.bitsize > n:
            return uint.model_uint(self.realval & (2**(self.bitsize-n)-1), self.bitsize-n)
        print("tail: this should not happen")
        return uint.model_uint(0,0)

    def tohex(self):
        mask = (1<<self.bitsize)-1
        return hex(mask & self.value)

    def print_bits(self):
        result = "s("
        result += hex(self.realval)#self.tohex()
        result += ")"
        print(self.bitsize, result)
