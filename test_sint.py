from model_sint import *
from model_uint import *
import unittest

test000 = model_sint(0x9, 4)
test0 = model_sint(0xa, 4)
test00 = model_sint(0x9, 4)
test1 = model_sint(0x6dba, 16)
test2 = model_sint(0xccb2, 16)
test3 = model_sint(0x71088d1c4a5c4a02, 64)
test4 = model_sint(0xdefaa415d9062302, 64)
test5 = model_sint(0x381c1fe6bca6875922fe, 80)
test6 = model_sint(0xefbe8ae0d38ab7f36dda, 80)
test7 = model_sint(0x6e0939370acc19daec06e9c13db50674, 128)
test8 = model_sint(0xbeb828fdbac591dba8e38eeb433f563d, 128)


class TestOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(test1.sint_add(test2), model_sint(0x3a6c, 17))
        self.assertEqual(test2.sint_add(test2), model_sint(0x19964, 17))
        self.assertEqual(test3.sint_add(test4), model_sint(0x5003313223626d04, 65))
        self.assertEqual(test4.sint_add(test4), model_sint(0x1bdf5482bb20c4604, 65))
        self.assertEqual(test5.sint_add(test6), model_sint(0x27daaac790313f4c90d8, 81))
        self.assertEqual(test6.sint_add(test6), model_sint(0x1df7d15c1a7156fe6dbb4, 81))
        self.assertEqual(test7.sint_add(test8), model_sint(0x2cc16234c591abb694ea78ac80f45cb1, 129))
        self.assertEqual(test8.sint_add(test8), model_sint(0x17d7051fb758b23b751c71dd6867eac7a, 129))

    def test_sub(self):
        self.assertEqual(test1.sint_sub(test2), model_sint(0xa108, 17))
        self.assertEqual(test2.sint_sub(test1), model_sint(0x15ef8, 17))
        self.assertEqual(test2.sint_sub(model_sint(0x0, 16)), model_sint(0x1ccb2, 17))
        self.assertEqual(test3.sint_sub(test4), model_sint(0x920de90671562700, 65))
        self.assertEqual(test4.sint_sub(test3), model_sint(0x16df216f98ea9d900, 65))
        self.assertEqual(test1.sint_sub(test4), model_sint(0x021055bea26fa4ab8, 65))
        self.assertEqual(test4.sint_sub(test6), model_sint(0x010415419d08b2112b528, 81))

    def test_mul(self):
        self.assertEqual(test1.sint_mul(test2), model_sint(0xea028354, 32))
        self.assertEqual(test3.sint_mul(test4), model_sint(0xf16b880f2bad048691fd4b72a0e2da04, 128))
        self.assertEqual(test5.sint_mul(test6), model_sint(0xfc6fe531cae4d5f834f4831b7dc6f5fbfee7f24c, 160))
        self.assertEqual(test7.sint_mul(test8), model_sint(0xe3f0c77f6f1ce87a5d5735256c8addf7a2a5210cf49a1af0917e727f76d981a4, 256))

    def test_div(self):
        self.assertEqual(test1.sint_div(test2), model_sint(0x1fffe,17))
        self.assertEqual(test3.sint_div(test4), model_sint(0x1fffffffffffffffd,65))
        self.assertEqual(test3.sint_div(test1), model_sint(0x107b710ae332f,65))
        self.assertEqual(test4.sint_div(test2), model_sint(0xa4c48cb11e2b,65))

    def test_mod(self):
        self.assertEqual(test1.sint_mod(test2), model_sint(0x71e,16))
        self.assertEqual(test3.sint_mod(test4), model_sint(0xdf8795dd56eb308,64))
        self.assertEqual(test3.sint_mod(test1), model_sint(0x16dc,16))
        self.assertEqual(test4.sint_mod(test2), model_sint(0xe51c,16))

    def test_lt(self):
        self.assertEqual(test1.sint_lt(test2), model_sint(0x0,1))
        self.assertEqual(test3.sint_lt(test4), model_sint(0x0,1))
        self.assertEqual(test6.sint_lt(test5), model_sint(0x1,1))
        self.assertEqual(test2.sint_lt(test4), model_sint(0x0,1))
        self.assertEqual(test4.sint_lt(test2), model_sint(0x1,1))

    def test_leq(self):
        self.assertEqual(test1.sint_leq(test2), model_sint(0x0,1))
        self.assertEqual(test3.sint_leq(test4), model_sint(0x0,1))
        self.assertEqual(test6.sint_leq(test6), model_sint(0x1,1))

    def test_gt(self):
        self.assertEqual(test1.sint_gt(test2), model_sint(0x1,1))
        self.assertEqual(test3.sint_gt(test4), model_sint(0x1,1))
        self.assertEqual(test6.sint_gt(test5), model_sint(0x0,1))
        self.assertEqual(test2.sint_gt(test4), model_sint(0x0,1))
        self.assertEqual(test4.sint_gt(test2), model_sint(0x1,1))

if __name__=="__main__":
    unittest.main()