# do the binary calculation

def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    a = a[::-1]
    b = b[::-1]

    i = 0
    ret = ""
    bit, carry = 0, 0
    while i < len(a) or i < len(b):
        abit = a[i] if i < len(a) else 0
        bbit = b[i] if i < len(b) else 0
        bit = int(abit) + int(bbit) + carry
        if bit == 0 or bit == 1: carry = 0
        if bit == 2:
            bit, carry = 0, 1
        elif bit == 3:
            bit, carry = 1, 1
        ret += str(bit)
        i += 1
    if carry:
        return (ret + "1")[::-1]
    return ret[::-1]

# int(x, y) assume x is in y numeration and transfer x to decimal.
# bin -> transfer to binary with 0b at beginning
def addBinary(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]