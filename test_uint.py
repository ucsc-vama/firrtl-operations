import sint
import uint
import unittest

# Variables
test1 = uint.model_uint(0x0, 1)
test2 = uint.model_uint(0x1, 1)
test3 = uint.model_uint(0x2, 2)
test4 = uint.model_uint(0xcafe, 16)
test5 = uint.model_uint(0xbebe, 16)
test6 = uint.model_uint(0x234901234823ad3e9283, 80)
test7 = uint.model_uint(0x3da3e90d8f93ab12d239, 80)
test8 = uint.model_uint(0xada3e90d8f93bc7eab12ddf2331939a1340134f12349b10231aca924ade9, 240)
test9 = uint.model_uint(0xd23aa349017b3ae3cba396810bef3910f931065a390bce31891009cee714, 240)

# Run test on uint variables
class TestOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(test1.uint_add(test2), uint.model_uint(0x1, 2))
        self.assertEqual(test2.uint_add(test3), uint.model_uint(0x3,3))
        self.assertEqual(test4.uint_add(test5), uint.model_uint(0x189bc,17))
        self.assertEqual(test7.uint_add(test8), uint.model_uint(0xada3e90d8f93bc7eab12ddf2331939a1340134f160ed9a0fc14054378022, 241))

    def test_sub(self):
        self.assertEqual(test3.uint_sub(test2), uint.model_uint(0x1, 3))
        self.assertEqual(test5.uint_sub(test1), uint.model_uint(0xbebe, 17))
        self.assertEqual(test7.uint_sub(test6), uint.model_uint(0x1a5ae7ea476ffdd43fb6, 81))
        self.assertEqual(test9.uint_sub(test8), uint.model_uint(0x2496ba3b71e77e652090b88ed8d5ff6fc52fd16915c21d2f576360aa392b, 241))

    def test_mul(self):
        self.assertEqual(test3.uint_mul(test2), uint.model_uint(0x2, 3))
        self.assertEqual(test5.uint_mul(test1), uint.model_uint(0x0, 17))
        self.assertEqual(test7.uint_mul(test6), uint.model_uint(0x87efce0722fbc9512aafe0d33af9c8bb554152b, 160))
        self.assertEqual(test9.uint_mul(test8), uint.model_uint(0x8e983b10cefc08fd4b85dbe9517422d805d6ebbf80d66d15f6b73f2029c82edabf8cb30436c2b4abfeaea119aa6856856e4a8346d4d6a34e7248d534, 480))

    def test_div(self):
        self.assertEqual(test1.uint_div(test2), uint.model_uint(0x0, 1))
        self.assertEqual(test2.uint_div(test3), uint.model_uint(0x0, 1))
        self.assertEqual(test4.uint_div(test5), uint.model_uint(0x1, 16))
        self.assertEqual(test9.uint_div(test6), uint.model_uint(0x5f53f78026545a5ee52bb010bdc7fc10b6d49cf9a, 240))

    def test_rem(self):
        self.assertEqual(test1.uint_rem(test2), uint.model_uint(0x0,1))
        self.assertEqual(test2.uint_rem(test3), uint.model_uint(0x1,1))
        self.assertEqual(test4.uint_rem(test5), uint.model_uint(0xc40,16))
        self.assertEqual(test9.uint_rem(test6), uint.model_uint(0x18b5f39130a9ab57d746, 80))

    def test_lt(self):
        self.assertEqual(test1.uint_lt(test2), uint.model_uint(0x1,1))
        self.assertEqual(test2.uint_lt(test2), uint.model_uint(0x0,1))
        self.assertEqual(test4.uint_lt(test5), uint.model_uint(0x0,1))
        
    def test_leq(self):
        self.assertEqual(test1.uint_leq(test2), uint.model_uint(0x1,1))
        self.assertEqual(test2.uint_leq(test2), uint.model_uint(0x1,1))
        self.assertEqual(test4.uint_leq(test5), uint.model_uint(0x0,1))
        
    def test_gt(self):
        self.assertEqual(test1.uint_gt(test2), uint.model_uint(0x0,1))
        self.assertEqual(test2.uint_gt(test2), uint.model_uint(0x0,1))
        self.assertEqual(test4.uint_gt(test5), uint.model_uint(0x1,1))
        
    def test_geq(self):
        self.assertEqual(test1.uint_geq(test2), uint.model_uint(0x0,1))
        self.assertEqual(test2.uint_geq(test2), uint.model_uint(0x1,1))
        self.assertEqual(test4.uint_geq(test5), uint.model_uint(0x1,1))

    def test_eq(self):
        self.assertEqual(test1.uint_eq(test2), uint.model_uint(0x0,1))
        self.assertEqual(test2.uint_eq(test2), uint.model_uint(0x1,1))
        self.assertEqual(test4.uint_eq(test5), uint.model_uint(0x0,1))

    def test_neq(self):
        self.assertEqual(test1.uint_neq(test2), uint.model_uint(0x1,1))
        self.assertEqual(test2.uint_neq(test2), uint.model_uint(0x0,1))
        self.assertEqual(test4.uint_neq(test5), uint.model_uint(0x1,1))

    def test_pad(self):
        self.assertEqual(test1.uint_pad(5), uint.model_uint(0x0,5))
        self.assertEqual(test4.uint_pad(2), uint.model_uint(0xcafe,16))

    # #def test_asSint(self):
    #     #self.assertEqual(test1.uint_asSint(), my_sint(1, 0x0))
    #     #self.assertEqual(test2.uint_asSint(), my_sint(1, 0x0))
    #     #self.assertEqual(test4.uint_asSint(), my_sint(16, 0x0))
    #     #self.assertEqual(test9.uint_asSint(), my_sint(80, 0x0))

    def test_shl(self):
        self.assertEqual(test1.uint_shl(1), uint.model_uint(0x0,2))
        self.assertEqual(test2.uint_shl(3), uint.model_uint(0x8,4))
        self.assertEqual(test4.uint_shl(5), uint.model_uint(0x195fc0,21))

    def test_shr(self):
        self.assertEqual(test2.uint_shr(1), uint.model_uint(0x0,1))
        self.assertEqual(test3.uint_shr(3), uint.model_uint(0x0,1))
        self.assertEqual(test5.uint_shr(5), uint.model_uint(0x5f5,11))

    def test_dshl(self):
        self.assertEqual(test2.uint_dshl(test1), uint.model_uint(0x1,2))
        self.assertEqual(test3.uint_dshl(test2), uint.model_uint(0x4,3))
        self.assertEqual(test4.uint_dshl(test3), uint.model_uint(0x32bf8,19))
        self.assertEqual(test8.uint_dshl(test3), uint.model_uint(0x2b68fa4363e4ef1faac4b77c8cc64e684d004d3c48d26c408c6b2a492b7a4,243))

    def test_dshr(self):
        self.assertEqual(test1.uint_dshr(test2), uint.model_uint(0x0,1))
        self.assertEqual(test2.uint_dshr(test2), uint.model_uint(0x0,1))
        self.assertEqual(test4.uint_dshr(test3), uint.model_uint(0x32bf,16))
        self.assertEqual(test9.uint_dshr(test3), uint.model_uint(0x348ea8d2405eceb8f2e8e5a042fbce443e4c41968e42f38c62440273b9c5,240))

    #def test_neg(self):
        #self.assertEqual(test1.uint_neg(), my_sint(1, 0x0))
        #self.assertEqual(test2.uint_neg(), my_sint(1, 0x1))
        #self.assertEqual(test4.uint_neg(), my_sint(16, 0xc40))
        #self.assertEqual(test9.uint_neg(), my_sint(240, 0x12dc55cb6fe84c51c345c697ef410c6ef06cef9a5c6f431ce76eff63118ec))

    def test_not(self):
        self.assertEqual(test1.uint_not(), uint.model_uint(0x1, 1))
        self.assertEqual(test2.uint_not(), uint.model_uint(0x0,1))
        self.assertEqual(test4.uint_not(), uint.model_uint(0x3501,16))
        self.assertEqual(test9.uint_not(), uint.model_uint(0x2dc55cb6fe84c51c345c697ef410c6ef06cef9a5c6f431ce76eff63118eb, 240))

    def test_and(self):
        self.assertEqual(test1.uint_and(test2), uint.model_uint(0x0,1))
        self.assertEqual(test2.uint_and(test3), uint.model_uint(0x0,2))
        self.assertEqual(test4.uint_and(test5), uint.model_uint(0x8abe,16))
        self.assertEqual(test9.uint_and(test6), uint.model_uint(0x210900210800090e8200,240))
        
    def test_or(self):
        self.assertEqual(test2.uint_or(test3), uint.model_uint(0x3,2))
        self.assertEqual(test4.uint_or(test5), uint.model_uint(0xfefe,16))
        self.assertEqual(test9.uint_or(test6), uint.model_uint(0xd23aa349017b3ae3cba396810bef3910f931065a3b4bcf33c933adfef797,240))

    def test_xor(self):
        self.assertEqual(test1.uint_xor(test2), uint.model_uint(0x1,1))
        self.assertEqual(test2.uint_xor(test3), uint.model_uint(0x3,2))
        self.assertEqual(test4.uint_xor(test5), uint.model_uint(0x7440,16))
        self.assertEqual(test9.uint_xor(test6), uint.model_uint(0xd23aa349017b3ae3cba396810bef3910f931065a1a42cf12c133a4f07597,240))

    def test_andr(self):
        self.assertEqual(test1.uint_andr(), uint.model_uint(0x0,1))
        self.assertEqual(test2.uint_andr(), uint.model_uint(0x1,1))
        self.assertEqual(test4.uint_andr(), uint.model_uint(0x0,1))
        self.assertEqual(test9.uint_andr(), uint.model_uint(0x0,1))

    def test_orr(self):
        self.assertEqual(test1.uint_orr(), uint.model_uint(0x0,1))
        self.assertEqual(test2.uint_orr(), uint.model_uint(0x1,1))
        self.assertEqual(test4.uint_orr(), uint.model_uint(0x1,1))
        self.assertEqual(test9.uint_orr(), uint.model_uint(0x1,1))

    def test_xorr(self):
        self.assertEqual(test1.uint_xorr(), uint.model_uint(0x0,1))
        self.assertEqual(test2.uint_xorr(), uint.model_uint(0x1,1))
        self.assertEqual(test4.uint_xorr(), uint.model_uint(0x1,1))
        self.assertEqual(test9.uint_xorr(), uint.model_uint(0x0,1))
        
    def test_cat(self):
        self.assertEqual(test1.uint_cat(test2), uint.model_uint(0x1,2))
        self.assertEqual(test2.uint_cat(test3), uint.model_uint(0x6,3))
        self.assertEqual(test4.uint_cat(test5), uint.model_uint(0xcafebebe,32))
        self.assertEqual(test9.uint_cat(test6), uint.model_uint(0xd23aa349017b3ae3cba396810bef3910f931065a390bce31891009cee714234901234823ad3e9283,320))

    def test_bits(self):
        self.assertEqual(test1.uint_bits(5, 1), uint.model_uint(0x0,1))
        self.assertEqual(test4.uint_bits(5, 1), uint.model_uint(0x1f,5))
        self.assertEqual(test9.uint_bits(5, 1), uint.model_uint(0xa,5))
        self.assertEqual(test5.uint_bits(1,1), uint.model_uint(0x1,1))

    def test_head(self):
        self.assertEqual(test1.uint_head(5), uint.model_uint(0x0,1))
        self.assertEqual(test4.uint_head(5), uint.model_uint(0x19,5))
        self.assertEqual(test9.uint_head(5), uint.model_uint(0x1a,5))
        self.assertEqual(test9.uint_head(0), uint.model_uint(0x0,0))

    def test_tail(self):
        self.assertEqual(test1.uint_tail(0), uint.model_uint(0x0,1))
        self.assertEqual(test3.uint_tail(2), uint.model_uint(0x0,0))
        self.assertEqual(test4.uint_tail(10), uint.model_uint(0x3e,6))
        self.assertEqual(test9.uint_tail(10), uint.model_uint(0x3aa349017b3ae3cba396810bef3910f931065a390bce31891009cee714,230))

if __name__=="__main__":
    unittest.main()