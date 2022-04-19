from gates.INVERTER import *
from gates.multibitAND import *
from gates.multibitNAND import *
from gates.multibitNOR import *
from gates.multibitOR import *
from gates.multibitXOR import *

if __name__ == '__main__':
    # ------------ AND TEST ------------
    # print('------------ AND TEST ------------')
    # test_multi_and = multibitAND([0,0,0],'test_and4' )
    # print(test_multi_and.get_output())

    # ------------ INVERTER (NOT) TEST ------------
    # print('------------ INVERTER (NOT) TEST ------------')
    # test_not = INVERTER(0,'test_not')
    # print(test_not.get_output())

    # ------------ NAND TEST ------------
    # print('------------ NAND TEST ------------')
    # test_multi_nand = multibitNAND([0,0,0], 'test_nand')
    # print(test_multi_nand.get_output())

    # ------------ OR TEST ------------
    # print('------------ OR TEST ------------')
    # test_multi_or = multibitOR([1,1,1],'test_or')
    # print(test_multi_or.get_output())

    # ------------ NOR TEST ------------
    # print('------------ NOR TEST ------------')
    # test_multi_nor = multibitNOR([1,1,1],'test_nor')
    # print(test_multi_nor.get_output())

    # ------------ XOR TEST ------------
    print('------------ XOR TEST ------------')
    test_multi_xor = multibitXOR([0,0,0], 'test_xor')
    print("in:[0,0,0]  out:0", test_multi_xor.get_output() == 0)
    print()
    test_multi_xor = multibitXOR([0, 0, 1], 'test_xor')
    print("in:[0,0,1]  out:1", test_multi_xor.get_output() == 1)
    print()
    test_multi_xor = multibitXOR([0, 1, 0], 'test_xor')
    print("in:[0,1,0]  out:1", test_multi_xor.get_output() == 1)
    print()
    test_multi_xor = multibitXOR([0, 1, 1], 'test_xor')
    print("in:[0,1,1]  out:0", test_multi_xor.get_output() == 0)
    print()
    test_multi_xor = multibitXOR([1, 0, 0], 'test_xor')
    print("in:[1,0,0]  out:1", test_multi_xor.get_output() == 1)
    print()
    test_multi_xor = multibitXOR([1, 0, 1], 'test_xor')
    print("in:[1,0,1]  out:0", test_multi_xor.get_output() == 0)
    print()
    test_multi_xor = multibitXOR([1, 1, 0], 'test_xor')
    print("in:[1,1,0]  out:0", test_multi_xor.get_output() == 0)
    print()
    test_multi_xor = multibitXOR([1, 1, 1], 'test_xor')
    print("in:[1,1,1]  out:1", test_multi_xor.get_output() == 1)
    print()



