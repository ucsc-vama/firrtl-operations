from my_sint import *
import math

class my_uint:
    def __init__(self, bitsize, value):
        self.bitsize = bitsize
        self.value = value

    def __eq__ (self, other):
        if isinstance(other, my_uint) or isinstance(other, my_sint):
            if self.value == other.value and self.bitsize == other.bitsize:
                return True
        return False

    def uint_add(self, other):
        return my_uint(max(self.bitsize,other.bitsize)+1, self.value+other.value)

    def uint_sub(self, other):
        comp = self.value - other.value
        size = max(self.bitsize, other.bitsize)
        if (comp < 0):
            result = (abs(comp) ^ ((1<<size)-1))+1#2s complement
            result += (1<<size)
            return my_uint(size+1, result)
        else:
            return my_uint(size+1, comp)

    def uint_mul(self, other):
        return my_uint(self.bitsize+other.bitsize, self.value*other.value)

    def uint_div(self, other): #division rouding down
        if other.value != 0:
            return my_uint(self.bitsize, self.value//other.value)

    def uint_rem(self, other):
        if other.value != 0:
            return my_uint(min(self.bitsize, other.bitsize), self.value % other.value)

    def uint_lt(self, other):
        if self.value < other.value:
            return my_uint(1, 1)
        return my_uint(1,0)

    def uint_leq(self,other):
        if self.value <= other.value:
            return my_uint(1,1)
        return my_uint(1,0)

    def uint_gt(self,other):
        if self.value > other.value:
            return my_uint(1,1)
        return my_uint(1,0)

    def uint_geq(self,other):
        if self.value >= other.value:
            return my_uint(1,1)
        return my_uint(1,0)

    def uint_eq(self,other):
        if self.value == other.value:
            return my_uint(1,1)
        return my_uint(1,0)
    
    def uint_neq(self,other):
        if self.value != other.value:
            return my_uint(1,1)
        return my_uint(1,0)

    def uint_pad(self, n):
        if self.bitsize < n:
            return my_uint(n, self.value)
        else:
            return my_uint(self.bitsize, self.value)

    def uint_asUint(self):
        return my_uint(self.bitsize, self.value)

    def uint_asSint(self): #
        return my_sint(self.bitsize, self.value)
    
    def uint_shl(self, n):
        num = self.value << n
        return my_uint(self.bitsize+n, num)

    def uint_shr(self, n):
        num = self.value >> n
        return my_uint(max(self.bitsize-n, 1), num)

    def uint_dshl(self, other):
        num = self.value << other.value
        return my_uint(self.bitsize + 2**other.bitsize -1, num)

    def uint_dshr(self, other): 
        num = self.value >> other.value
        return my_uint(self.bitsize, num)

    def uint_cvt(self): #
        return my_sint(self.bitsize+1, self.value)

    def uint_neg(self): #
        result = 0
        for i in range(self.bitsize):
            result |= ((~self.value>>i)&1) << i
        result += 1
        result |= (1<<self.bitsize)
        return my_sint(self.bitsize+1, result)

    def uint_not(self):
        result = 0
        for i in range(self.bitsize):
            result |= ((~self.value>>i)&1) << i
        return my_uint(self.bitsize, result)

    def uint_and(self, other):
        return my_uint(max(self.bitsize,other.bitsize), self.value & other.value)

    def uint_or(self, other):
        return my_uint(max(self.bitsize,other.bitsize), self.value | other.value)

    def uint_xor(self, other):
        return my_uint(max(self.bitsize,other.bitsize), self.value ^ other.value)
    
    def uint_andr(self):
        result = 1
        for i in range(self.bitsize):
            bit_i = (self.value & (1<<i))>>i
            result = result & bit_i
        return my_uint(1, result)
    
    def uint_orr(self):
        result = 0
        for i in range(self.bitsize):
            bit_i = (self.value & (1<<i))>>i
            result = result | bit_i
        return my_uint(1, result)

    def uint_xorr(self):
        result = 0
        for i in range(self.bitsize):
            bit_i = (self.value & (1<<i))>>i
            result = result ^ bit_i
        return my_uint(1, result)

    def uint_cat(self,other):
        return my_uint(self.bitsize+other.bitsize, (self.value<<other.bitsize)|other.value)

    def uint_bits(self, hi, lo):
        if hi > lo and hi < self.bitsize:
            return my_uint(hi-lo+1, (self.value>>lo)&(2**(hi-lo+1)-1))
        return my_uint(0,0)

    def uint_head(self, n):
        if n > 0 and n <= self.bitsize:
            return my_uint(n, self.value>>(self.bitsize-n))
        return my_uint(0,0)

    def uint_tail(self, n):
        if self.bitsize > n:
            return my_uint(self.bitsize-n, self.value & (2**(self.bitsize-n)-1))
        return my_uint(0,0)

    def tohex(self):
        mask = (1<<self.bitsize)-1
        return hex(mask & self.value)

    def print_bits(self):
        result = "u("
        result += str(hex(self.value))#self.tohex()
        result += ")"
        print(self.bitsize, result)
