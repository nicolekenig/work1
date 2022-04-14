from logicGate import *

if __name__ == '__main__':
    print(AND(1, 1))

    print("+---------------+----------------+")
    print(" | AND Truth Table | Result |")
    print(" A = False, B = False | A AND B =", AND(False, False), " | ")
    print(" A = False, B = True | A AND B =", AND(False, True), " | ")
    print(" A = True, B = False | A AND B =", AND(True, False), " | ")
    print(" A = True, B = True | A AND B =", AND(True, True), " | ")

    print(NAND(1, 0))

    print("+---------------+----------------+")
    print(" | NAND Truth Table | Result |")
    print(" A = False, B = False | A AND B =", NAND(False, False), " | ")
    print(" A = False, B = True | A AND B =", NAND(False, True), " | ")
    print(" A = True, B = False | A AND B =", NAND(True, False), " | ")
    print(" A = True, B = True | A AND B =", NAND(True, True), " | ")

    print(OR(0, 0))

    print("+---------------+----------------+")
    print(" | OR Truth Table | Result |")
    print(" A = False, B = False | A OR B =", OR(False, False), " | ")
    print(" A = False, B = True | A OR B =", OR(False, True), " | ")
    print(" A = True, B = False | A OR B =", OR(True, False), " | ")
    print(" A = True, B = True | A OR B =", OR(True, True), " | ")

    print(XOR(5, 5))

    print("+---------------+----------------+")
    print(" | XOR Truth Table | Result |")
    print(" A = False, B = False | A XOR B =", XOR(False, False), " | ")
    print(" A = False, B = True | A XOR B =", XOR(False, True), " | ")
    print(" A = True, B = False | A XOR B =", XOR(True, False), " | ")
    print(" A = True, B = True | A XOR B =", XOR(True, True), " | ")

    print(NOT(0))

    print("+---------------+----------------+")
    print(" | NOT Truth Table | Result |")
    print(" A = False | A NOT =", NOT(False), " | ")
    print(" A = True, | A NOT =", NOT(True), " | ")

    print(NOR(0, 0))

    print("+---------------+----------------+")
    print(" | NOR Truth Table | Result |")
    print(" A = False, B = False | A NOR B =", NOR(False, False), " | ")
    print(" A = False, B = True | A NOR B =", NOR(False, True), " | ")
    print(" A = True, B = False | A NOR B =", NOR(True, False), " | ")
    print(" A = True, B = True | A NOR B =", NOR(True, True), " | ")

    print(XNOR(1, 1))

    print("+---------------+----------------+")
    print(" | XNOR Truth Table | Result |")
    print(" A = False, B = False | A XNOR B =", XNOR(False, False), " | ")
    print(" A = False, B = True | A XNOR B =", XNOR(False, True), " | ")
    print(" A = True, B = False | A XNOR B =", XNOR(True, False), " | ")
    print(" A = True, B = True | A XNOR B =", XNOR(True, True), " | ")