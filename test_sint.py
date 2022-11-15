from model_sint import *
from model_uint import *
import unittest

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
        self.assertEqual(test2.sint_sub(model_sint(0x0, 16)), model_sint(0xccb2, 17))
        self.assertEqual(test3.sint_sub(test4), model_sint(0x920de90671562700, 65))
        self.assertEqual(test4.sint_sub(test3), model_sint(0x16df216f98ea9d900, 65))
        self.assertEqual(test4.sint_sub(test3), model_sint(0x16df216f98ea9d900, 65))
        # test2.sint_sub(test1).print_bits()

    def test_mul(self):
        test1.sint_mul(test2).print_bits()
        # self.assertEqual(test1.sint_mul(test2), model_sint(0xea028354, 32))
    #     self.assertEqual(test3.sint_mul(test4), model_sint(0x5f7c3f3a3c3b3b04, 65))
    #     self.assertEqual(test4.sint_mul(test4), model_sint(0x1c7e5a2a5d0a2a04, 65))
    #     self.assertEqual(test5.sint_mul(test6), model_sint(0x2c6b1f6d8b6e1f4c90d8, 81))
    #     self.assertEqual(test6.sint_mul(test6), model_sint(0x1e7e8a1c3d0e8f6e6dbb4, 81))
    #     self.assertEqual(test7.sint_mul(test8), model_sint(0x2c7e5a2a5d0a2a04, 129))
    #     self.assertEqual(test8.sint_mul(test8), model_sint(0x17e7e5a2a5d0a2a04, 129))

if __name__=="__main__":
    unittest.main()