from my_sint import *
from my_uint import *

# Variables
test1 = my_uint(1, 0x0)
test2 = my_uint(1, 0x1)
test3 = my_uint(2, 0x2)
test4 = my_uint(16, 0xcafe)
test5 = my_uint(16, 0xbebe)
test6 = my_uint(80, 0x234901234823ad3e9283)
test7 = my_uint(80, 0x3da3e90d8f93ab12d239)
test8 = my_uint(240, 0xada3e90d8f93bc7eab12ddf2331939a1340134f12349b10231aca924ade9)
test9 = my_uint(240, 0xd23aa349017b3ae3cba396810bef3910f931065a390bce31891009cee714)

# Run test on uint variables
def run_test():

        #ADD
        assert test1.uint_add(test2) == my_uint(2, 0x1)
        assert test2.uint_add(test3) == my_uint(3, 0x3)
        assert test4.uint_add(test5) == my_uint(17, 0x189bc)
        assert test7.uint_add(test8) == my_uint(241, 0xada3e90d8f93bc7eab12ddf2331939a1340134f160ed9a0fc14054378022)

        #SUB
        assert test3.uint_sub(test2) == my_uint(3, 0x1)
        assert test5.uint_sub(test1) == my_uint(17, 0xbebe)
        assert test7.uint_sub(test6) == my_uint(81, 0x1a5ae7ea476ffdd43fb6)
        assert test9.uint_sub(test8) == my_uint(241, 0x2496ba3b71e77e652090b88ed8d5ff6fc52fd16915c21d2f576360aa392b)

        #MUL
        assert test3.uint_mul(test2) == my_uint(3, 0x2)
        assert test5.uint_mul(test1) == my_uint(17, 0x0)
        assert test7.uint_mul(test6) == my_uint(160, 0x87efce0722fbc9512aafe0d33af9c8bb554152b)
        assert test9.uint_mul(test8) == my_uint(480, 0x8e983b10cefc08fd4b85dbe9517422d805d6ebbf80d66d15f6b73f2029c82edabf8cb30436c2b4abfeaea119aa6856856e4a8346d4d6a34e7248d534)

        #DIV
        assert test1.uint_div(test2) == my_uint(1, 0x0)
        assert test2.uint_div(test3) == my_uint(1, 0x0)
        assert test4.uint_div(test5) == my_uint(16, 0x1)
        assert test9.uint_div(test6) == my_uint(240, 0x5f53f78026545a5ee52bb010bdc7fc10b6d49cf9a)

        #REM
        assert test1.uint_rem(test2) == my_uint(1, 0x0)
        assert test2.uint_rem(test3) == my_uint(1, 0x1)
        assert test4.uint_rem(test5) == my_uint(16, 0xc40)
        assert test9.uint_rem(test6) == my_uint(80, 0x18b5f39130a9ab57d746)

        #LEFT THAN
        assert test1.uint_lt(test2) == my_uint(1, 0x1)
        assert test2.uint_lt(test2) == my_uint(1, 0x0)
        assert test4.uint_lt(test5) == my_uint(1, 0x0)
        
        #LESS THAN OR EQUAL
        assert test1.uint_leq(test2) == my_uint(1, 0x1)
        assert test2.uint_leq(test2) == my_uint(1, 0x1)
        assert test4.uint_leq(test5) == my_uint(1, 0x0)
        
        #GREATER THAN
        assert test1.uint_gt(test2) == my_uint(1, 0x0)
        assert test2.uint_gt(test2) == my_uint(1, 0x0)
        assert test4.uint_gt(test5) == my_uint(1, 0x1)
        
        #GREATER THAN OR EQUAL
        assert test1.uint_geq(test2) == my_uint(1, 0x0)
        assert test2.uint_geq(test2) == my_uint(1, 0x1)
        assert test4.uint_geq(test5) == my_uint(1, 0x1)

        #EQUAL
        assert test1.uint_eq(test2) == my_uint(1, 0x0)
        assert test2.uint_eq(test2) == my_uint(1, 0x1)
        assert test4.uint_eq(test5) == my_uint(1, 0x0)

        #NOT EQUAL
        assert test1.uint_neq(test2) == my_uint(1, 0x1)
        assert test2.uint_neq(test2) == my_uint(1, 0x0)
        assert test4.uint_neq(test5) == my_uint(1, 0x1)

        #PADDING
        assert test1.uint_pad(5) == my_uint(5, 0x0)
        assert test4.uint_pad(2) == my_uint(16, 0xcafe)

        #asSint (come back later
        #assert test1.uint_asSint() == my_sint(1, 0x0)
        #assert test2.uint_asSint() == my_sint(1, 0x0)
        #assert test4.uint_asSint() == my_sint(16, 0x0)
        #assert test9.uint_asSint() == my_sint(80, 0x0)

        #SHL
        assert test1.uint_shl(1) == my_uint(2, 0x0)
        assert test2.uint_shl(3) == my_uint(4, 0x8)
        assert test4.uint_shl(5) == my_uint(21, 0x195fc0)

        #SHR
        assert test2.uint_shr(1) == my_uint(1, 0x0)
        assert test3.uint_shr(3) == my_uint(1, 0x0)
        assert test5.uint_shr(5) == my_uint(11, 0x5f5)

        #DSHL
        assert test2.uint_dshl(test1) == my_uint(2, 0x1)
        assert test3.uint_dshl(test2) == my_uint(3, 0x2)
        assert test4.uint_dshl(test3) == my_uint(19, 0xcafc)
        assert test8.uint_dshl(test3) == my_uint(243, 0xada3e90d8f93bc7eab12ddf2331939a1340134f12349b10231aca924ade8)

        #DSHR
        assert test1.uint_dshr(test2) == my_uint(1, 0x0)
        assert test2.uint_dshr(test2) == my_uint(1, 0x0)
        assert test4.uint_dshr(test3) == my_uint(16, 0x32bf)
        assert test9.uint_dshr(test3) == my_uint(240, 0x348ea8d2405eceb8f2e8e5a042fbce443e4c41968e42f38c62440273b9c5)

        #NEG
        #assert test1.uint_neg() == my_sint(1, 0x0)
        #assert test2.uint_neg() == my_sint(1, 0x1)
        #assert test4.uint_neg() == my_sint(16, 0xc40)
        #assert test9.uint_neg() == my_sint(240, 0x12dc55cb6fe84c51c345c697ef410c6ef06cef9a5c6f431ce76eff63118ec)

        #NOT
        assert test1.uint_not() == my_uint(1, 0x1)
        assert test2.uint_not() == my_uint(1, 0x0)
        assert test4.uint_not() == my_uint(16, 0x3501)
        assert test9.uint_not() == my_uint(240, 0x2dc55cb6fe84c51c345c697ef410c6ef06cef9a5c6f431ce76eff63118eb)

        #AND
        assert test1.uint_and(test2) == my_uint(1, 0x0)
        assert test2.uint_and(test3) == my_uint(2, 0x0)
        assert test4.uint_and(test5) == my_uint(16, 0x8abe)
        assert test9.uint_and(test6) == my_uint(240, 0x210900210800090e8200)
        
        #OR
        assert test2.uint_or(test3) == my_uint(2, 0x3)
        assert test4.uint_or(test5) == my_uint(16, 0xfefe)
        assert test9.uint_or(test6) == my_uint(240, 0xd23aa349017b3ae3cba396810bef3910f931065a3b4bcf33c933adfef797)

        #XOR
        assert test1.uint_xor(test2) == my_uint(1, 0x1)
        assert test2.uint_xor(test3) == my_uint(2, 0x3)
        assert test4.uint_xor(test5) == my_uint(16, 0x7440)
        assert test9.uint_xor(test6) == my_uint(240, 0xd23aa349017b3ae3cba396810bef3910f931065a1a42cf12c133a4f07597)

        #ANDR
        assert test1.uint_andr() == my_uint(1, 0x0)
        assert test2.uint_andr() == my_uint(1, 0x1)
        assert test4.uint_andr() == my_uint(1, 0x0)
        assert test9.uint_andr() == my_uint(1, 0x0)

        #ORR
        assert test1.uint_orr() == my_uint(1, 0x0)
        assert test2.uint_orr() == my_uint(1, 0x1)
        assert test4.uint_orr() == my_uint(1, 0x1)
        assert test9.uint_orr() == my_uint(1, 0x1)

        #XORR
        assert test1.uint_xorr() == my_uint(1, 0x0)
        assert test2.uint_xorr() == my_uint(1, 0x1)
        assert test4.uint_xorr() == my_uint(1, 0x1)
        assert test9.uint_xorr() == my_uint(1, 0x0)
        
        #CAT
        assert test1.uint_cat(test2) == my_uint(2, 0x1)
        assert test2.uint_cat(test3) == my_uint(3, 0x6)
        assert test4.uint_cat(test5) == my_uint(32, 0xcafebebe)
        assert test9.uint_cat(test6) == my_uint(320, 0xd23aa349017b3ae3cba396810bef3910f931065a390bce31891009cee714234901234823ad3e9283)

        #BITS
        assert test1.uint_bits(5, 1) == my_uint(0, 0x0)
        assert test4.uint_bits(5, 1) == my_uint(5, 0x12)
        assert test9.uint_bits(5, 1) == my_uint(5, 0x14)

        #HEAD
        assert test1.uint_head(5) == my_uint(0, 0x0)
        assert test4.uint_head(5) == my_uint(5, 0x19)
        assert test9.uint_head(5) == my_uint(5, 0x1a)

        #TAIL
        assert test1.uint_tail(10) == my_uint(0, 0x0)
        assert test4.uint_tail(10) == my_uint(6, 0x3e)
        assert test9.uint_tail(10) == my_uint(230, 0x3aa349017b3ae3cba396810bef3910f931065a390bce31891009cee714)

        print("all tests completed")

def main():
    run_test()

if __name__=="__main__":
    main()