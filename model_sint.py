from model_uint import *

class model_sint:
    def __init__(self, bitsize, value):
        self.bitsize = bitsize
        self.value = value

    def __eq__ (self, other):
        if isinstance(other, model_uint) or isinstance(other, model_sint):
            if self.value == other.value and self.bitsize == other.bitsize:
                return True
        return False

    def sint_add(self, other):
        return model_uint(self.value+other.value, max(self.bitsize,other.bitsize)+1)
