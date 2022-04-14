def AND(a, b):
    if a == 1 and b == 1:
        return True
    else:
        return False


def NAND(a, b):
    if a == 1 and b == 1:
        return False
    else:
        return True


def OR(a, b):
    if a == 1 or b == 1:
        return True
    else:
        return False


def XOR(a, b):
    if a != b:
        return 1
    else:
        return 0


def NOT(a):
    return not a


def NOR(a, b):
    if(a == 0) and (b == 0):
        return 1
    elif(a == 0) and (b == 1):
        return 0
    elif(a == 1) and (b == 0):
        return 0
    elif(a == 1) and (b == 1):
        return 0

