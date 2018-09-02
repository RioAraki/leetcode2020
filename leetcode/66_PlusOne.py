# string -> transfer whole list as one int + 1 -> back to str, split each one -> each transfer to int, put in a list

def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    return [int(x) for x in str(int("".join([str(x) for x in digits])) + 1)]

# increment last bit by 1 and move backward depends on the carry

def betterPlusOne(digits):
    carry = 1
    for i in range(len(digits)-1,-1,-1):
        if carry == 0: break
        digits[i], carry = (digits[i] + carry, 0) if digits[i] < 9 else (0, 1)
        print(digits[i], carry)
    if carry == 1:
        return [1]+digits
    return digits

digits = [6,7,8,9]
print(betterPlusOne(digits))