import sint
import uint
import unittest

testa = sint.model_sint(0x1, 1)
testb = sint.model_sint(0x0, 1)
test0 = sint.model_sint(0xa, 4)
test00 = sint.model_sint(0x9, 4)
test000 = sint.model_sint(0x9, 4)
test0000 = sint.model_sint(0x3, 4)
test1 = sint.model_sint(0x6dba, 16)
test2 = sint.model_sint(0xccb2, 16)
test3 = sint.model_sint(0x71088d1c4a5c4a02, 64)
test4 = sint.model_sint(0xdefaa415d9062302, 64)
test5 = sint.model_sint(0x381c1fe6bca6875922fe, 80)
test6 = sint.model_sint(0xefbe8ae0d38ab7f36dda, 80)
test7 = sint.model_sint(0x6e0939370acc19daec06e9c13db50674, 128)
test8 = sint.model_sint(0xbeb828fdbac591dba8e38eeb433f563d, 128)
test9 = sint.model_sint(0x381c1fe6bca6875922fe381c1fe6bca6875922fe, 158)


class TestOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(test1.sint_add(test2), sint.model_sint(0x3a6c, 17))
        self.assertEqual(test2.sint_add(test2), sint.model_sint(0x19964, 17))
        self.assertEqual(test3.sint_add(test4), sint.model_sint(0x5003313223626d04, 65))
        self.assertEqual(test4.sint_add(test4), sint.model_sint(0x1bdf5482bb20c4604, 65))
        self.assertEqual(test5.sint_add(test6), sint.model_sint(0x27daaac790313f4c90d8, 81))
        self.assertEqual(test6.sint_add(test6), sint.model_sint(0x1df7d15c1a7156fe6dbb4, 81))
        self.assertEqual(test7.sint_add(test8), sint.model_sint(0x2cc16234c591abb694ea78ac80f45cb1, 129))
        self.assertEqual(test8.sint_add(test8), sint.model_sint(0x17d7051fb758b23b751c71dd6867eac7a, 129))

    def test_sub(self):
        self.assertEqual(test1.sint_sub(test2), sint.model_sint(0xa108, 17))
        self.assertEqual(test2.sint_sub(test1), sint.model_sint(0x15ef8, 17))
        self.assertEqual(test2.sint_sub(sint.model_sint(0x0, 16)), sint.model_sint(0x1ccb2, 17))
        self.assertEqual(test3.sint_sub(test4), sint.model_sint(0x920de90671562700, 65))
        self.assertEqual(test4.sint_sub(test3), sint.model_sint(0x16df216f98ea9d900, 65))
        self.assertEqual(test1.sint_sub(test4), sint.model_sint(0x021055bea26fa4ab8, 65))
        self.assertEqual(test4.sint_sub(test6), sint.model_sint(0x010415419d08b2112b528, 81))

    def test_mul(self):
        self.assertEqual(test1.sint_mul(test2), sint.model_sint(0xea028354, 32))
        self.assertEqual(test3.sint_mul(test4), sint.model_sint(0xf16b880f2bad048691fd4b72a0e2da04, 128))
        self.assertEqual(test5.sint_mul(test6), sint.model_sint(0xfc6fe531cae4d5f834f4831b7dc6f5fbfee7f24c, 160))
        self.assertEqual(test7.sint_mul(test8), sint.model_sint(0xe3f0c77f6f1ce87a5d5735256c8addf7a2a5210cf49a1af0917e727f76d981a4, 256))

    def test_div(self):
        self.assertEqual(test1.sint_div(test2), sint.model_sint(0x1fffe,17))
        self.assertEqual(test3.sint_div(test4), sint.model_sint(0x1fffffffffffffffd,65))
        self.assertEqual(test3.sint_div(test1), sint.model_sint(0x107b710ae332f,65))
        self.assertEqual(test4.sint_div(test2), sint.model_sint(0xa4c48cb11e2b,65))

    def test_mod(self):
        self.assertEqual(test1.sint_mod(test2), sint.model_sint(0x71e,16))
        self.assertEqual(test3.sint_mod(test4), sint.model_sint(0xdf8795dd56eb308,64))
        self.assertEqual(test3.sint_mod(test1), sint.model_sint(0x16dc,16))
        self.assertEqual(test4.sint_mod(test2), sint.model_sint(0xe51c,16))

    def test_lt(self):
        self.assertEqual(test1.sint_lt(test2), sint.model_sint(0x0,1))
        self.assertEqual(test3.sint_lt(test4), sint.model_sint(0x0,1))
        self.assertEqual(test6.sint_lt(test5), sint.model_sint(0x1,1))
        self.assertEqual(test2.sint_lt(test4), sint.model_sint(0x0,1))
        self.assertEqual(test4.sint_lt(test2), sint.model_sint(0x1,1))

    def test_leq(self):
        self.assertEqual(test1.sint_leq(test2), sint.model_sint(0x0,1))
        self.assertEqual(test3.sint_leq(test4), sint.model_sint(0x0,1))
        self.assertEqual(test6.sint_leq(test6), sint.model_sint(0x1,1))

    def test_gt(self):
        self.assertEqual(test1.sint_gt(test2), sint.model_sint(0x1,1))
        self.assertEqual(test3.sint_gt(test4), sint.model_sint(0x1,1))
        self.assertEqual(test6.sint_gt(test5), sint.model_sint(0x0,1))
        self.assertEqual(test2.sint_gt(test4), sint.model_sint(0x1,1))
        self.assertEqual(test4.sint_gt(test2), sint.model_sint(0x0,1))
        self.assertEqual(test3.sint_gt(test3), sint.model_sint(0x0,1))
        self.assertEqual(test1.sint_gt(test3), sint.model_sint(0x0,1))

    def test_geq(self):
        self.assertEqual(test1.sint_geq(test2), sint.model_sint(0x1,1))
        self.assertEqual(test3.sint_geq(test4), sint.model_sint(0x1,1))
        self.assertEqual(test6.sint_geq(test5), sint.model_sint(0x0,1))
        self.assertEqual(test2.sint_geq(test4), sint.model_sint(0x1,1))
        self.assertEqual(test4.sint_geq(test2), sint.model_sint(0x0,1))
        self.assertEqual(test3.sint_geq(test3), sint.model_sint(0x1,1))

    def test_eq(self):
        self.assertEqual(test1.sint_eq(test1), sint.model_sint(0x1,1))
        self.assertEqual(test2.sint_eq(test1), sint.model_sint(0x0,1))

    def test_neq(self):
        self.assertEqual(test1.sint_neq(test1), sint.model_sint(0x0,1))
        self.assertEqual(test2.sint_neq(test1), sint.model_sint(0x1,1))
        
    def test_pad(self):
        self.assertEqual(test1.sint_pad(3), sint.model_sint(0x6dba,16))
        self.assertEqual(test1.sint_pad(18), sint.model_sint(0x6dba,18))
        self.assertEqual(test2.sint_pad(20), sint.model_sint(0xfccb2,20))
        self.assertEqual(test3.sint_pad(200), test3.sint_pad(100).sint_pad(200))

    def test_asUInt(self):
        self.assertEqual(test1.sint_asUInt(), uint.model_uint(0x6dba,16))
        self.assertEqual(test2.sint_asUInt(), uint.model_uint(0xccb2,16))

    def test_asSInt(self):
        self.assertEqual(test1.sint_asSInt(), sint.model_sint(0x6dba,16))
        self.assertEqual(test2.sint_asSInt(), sint.model_sint(0xccb2,16))

    def test_shl(self):
        self.assertEqual(test1.sint_shl(0), test1)
        self.assertEqual(test1.sint_shl(4), sint.model_sint(0x6dba0,20))
        self.assertEqual(test3.sint_shl(8), sint.model_sint(0x71088d1c4a5c4a0200,72))
        self.assertEqual(test5.sint_shl(60), sint.model_sint(0x381c1fe6bca6875922fe000000000000000,140))

    def test_shr(self):
        self.assertEqual(test1.sint_shr(0), test1)
        self.assertEqual(test1.sint_shr(8), sint.model_sint(0x6d,8))
        self.assertEqual(test3.sint_shr(16), sint.model_sint(0x71088d1c4a5c,48))
        self.assertEqual(test5.sint_shr(24), sint.model_sint(0x381c1fe6bca687,56))
        self.assertEqual(test7.sint_shr(48), sint.model_sint(0x6e0939370acc19daec06,80))
        self.assertEqual(test7.sint_shr(128), sint.model_sint(0x0,1))
    
    def test_dshl(self):
        testa.sint_dshl(uint.model_uint(0x0,1)).print_bits()
        self.assertEqual(test1.sint_dshl(sint.model_sint(0x0,1)), sint.model_sint(0x6dba,17))
        self.assertEqual(test1.sint_dshl(sint.model_sint(0x4,4)), sint.model_sint(0x6dba0,31))

    def test_dshr(self):
        self.assertEqual(test1.sint_dshr(sint.model_sint(0x0,1)), sint.model_sint(0x6dba,16))
        self.assertEqual(test1.sint_dshr(sint.model_sint(0x4,4)), sint.model_sint(0x06db,16))
        self.assertEqual(test3.sint_dshr(sint.model_sint(0x8,4)), sint.model_sint(0x71088d1c4a5c4a,64))

    def test_neg(self):
        self.assertEqual(test1.sint_neg(), sint.model_sint(0x19246,17))
        self.assertEqual(test3.sint_neg(), sint.model_sint(0x18ef772e3b5a3b5fe,65))
        self.assertEqual(test5.sint_neg().sint_neg(), test5.sint_pad(82))
        self.assertEqual(test6.sint_neg(), sint.model_sint(0x1041751f2c75480c9226, 81))
        self.assertEqual(test4.sint_neg().sint_neg(), test4.sint_pad(66))

    def test_not(self):
        self.assertEqual(test1.sint_not(), uint.model_uint(0x9245,16))
        self.assertEqual(test2.sint_not(), uint.model_uint(0x334d,16))
        self.assertEqual(test7.sint_not(), uint.model_uint(0x91f6c6c8f533e62513f9163ec24af98b,128))
        self.assertEqual(test9.sint_not(), uint.model_uint(0x07e3e019435978a6dd01c7e3e019435978a6dd01, 158))
        self.assertEqual(test00.sint_not(), uint.model_uint(0x6,4))

    def test_and(self):
        self.assertEqual(test1.sint_and(test2), sint.model_sint(0x4cb2,16))
        self.assertEqual(test5.sint_and(test6), sint.model_sint(0x281c0ae09082875120da,80))

    def test_or(self):
        self.assertEqual(test1.sint_or(test2), sint.model_sint(0xedba,16))
        self.assertEqual(test5.sint_or(test6), sint.model_sint(0xffbe9fe6ffaeb7fb6ffe,80))

    def test_xor(self):
        self.assertEqual(test1.sint_xor(test2), sint.model_sint(0xa108,16))
        self.assertEqual(test5.sint_xor(test6), sint.model_sint(0xd7a295066f2c30aa4f24,80))

    def test_andr(self):
        self.assertEqual(test00.sint_andr(), sint.model_sint(0x0, 1))
        self.assertEqual(test1.sint_andr(), sint.model_sint(0x0, 1))
        self.assertEqual(test2.sint_andr(), sint.model_sint(0x0, 1))
        self.assertEqual(test5.sint_andr(), sint.model_sint(0x0, 1))
        self.assertEqual(test9.sint_andr(), sint.model_sint(0x0, 1))
        self.assertEqual(uint.model_uint(0x0,16).uint_not().uint_asSint().sint_andr(), sint.model_sint(0x1, 1))

    def test_orr(self):
        self.assertEqual(test00.sint_orr(), sint.model_sint(0x1, 1))
        self.assertEqual(test1.sint_orr(), sint.model_sint(0x1, 1))
        self.assertEqual(test2.sint_orr(), sint.model_sint(0x1, 1))
        self.assertEqual(test5.sint_orr(), sint.model_sint(0x1, 1))
        self.assertEqual(test9.sint_orr(), sint.model_sint(0x1, 1))
        self.assertEqual(sint.model_sint(0x0,16).sint_orr(), sint.model_sint(0x0, 1))
        self.assertEqual(sint.model_sint(0x0,69).sint_orr(), sint.model_sint(0x0, 1))
        self.assertEqual(sint.model_sint(0x0,16).sint_andr(), sint.model_sint(0x0, 1))
        self.assertEqual(sint.model_sint(0x0,69).sint_andr(), sint.model_sint(0x0, 1))

    def test_xorr(self):
        self.assertEqual(test00.sint_xorr(), sint.model_sint(0x0, 1))
        self.assertEqual(test1.sint_xorr(), sint.model_sint(0x0, 1))
        self.assertEqual(test2.sint_xorr(), sint.model_sint(0x0, 1))
        self.assertEqual(test3.sint_xorr(), sint.model_sint(0x1, 1))
        self.assertEqual(test4.sint_xorr(), sint.model_sint(0x1, 1))
        self.assertEqual(test5.sint_xorr(), sint.model_sint(0x0, 1))
        self.assertEqual(test9.sint_xorr(), sint.model_sint(0x0, 1))

    def test_cat(self):
        self.assertEqual(test1.sint_cat(test2), sint.model_sint(0x6dbaccb2, 32))
        self.assertEqual(test00.sint_cat(test0000), sint.model_sint(0x93, 8))
        self.assertEqual(test9.sint_cat(test5), sint.model_sint(0x381c1fe6bca6875922fe381c1fe6bca6875922fe381c1fe6bca6875922fe, 238))

    def test_bits(self):
        self.assertEqual(test1.sint_bits(15,3), uint.model_uint(0x0db7, 13))
        self.assertEqual(test3.sint_bits(32,13), uint.model_uint(0x252e2, 20))
        self.assertEqual(test6.sint_bits(72,59), uint.model_uint(0x37d1, 14))
        self.assertEqual(test9.sint_bits(102,72), uint.model_uint(0x5922fe38, 31))

    def test_head(self):
        self.assertEqual(test0000.sint_head(3), uint.model_uint(0x1,3))
        self.assertEqual(test1.sint_head(3), uint.model_uint(0x3,3))
        self.assertEqual(test9.sint_head(63), uint.model_uint(0x70383fcd794d0eb2,63))

    def test_tail(self):
        self.assertEqual(test0000.sint_tail(3), uint.model_uint(0x1,1))
        self.assertEqual(test1.sint_tail(3), uint.model_uint(0x0dba,13))
        self.assertEqual(test6.sint_tail(79), uint.model_uint(0x0,1))
        self.assertEqual(test9.sint_tail(63), uint.model_uint(0x22fe381c1fe6bca6875922fe,95))

if __name__=="__main__":
    unittest.main()