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
        # self.assertEqual(test2.sint_add(test2), model_sint(0x19964, 17))
        # self.assertEqual(test5.sint_add(test6), model_uint("0x12f5b0e0a8d0f3c2b1e2", 81))
        # self.assertEqual(test7.sint_add(test8), model_uint("0x12a8c1b5e7e5b8c5d8e5c6f9b0e9a9b1", 129))

if __name__=="__main__":
    unittest.main()