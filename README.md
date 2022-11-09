Firrtl operations ![Build Status](https://github.com/ucsc-vama/firrtl-operations/actions/workflows/run_test.yaml/badge.svg)
=====================
This repo tests several primitive operations referenced in chapter 7 of [firrtl](https://github.com/freechipsproject/firrtl) [spec](https://github.com/ucb-bar/firrtl/blob/master/spec/spec.pdf). Most notably, unsigned-int and signed-int are templated by bit width and bit value. 

Test the repo by running test.py:

    $ python -m unittest -v test_uint.py
    $ python -m unittest -v test_uint.py
