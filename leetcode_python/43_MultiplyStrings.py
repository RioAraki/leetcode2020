from itertools import product


def multiply(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """

    # You cannot transfer the whole inputs to integer, but read inputs letter by letter and transfer each of them is allowed.
    # In other words, write a multiplication algorithm.

    def strNum(num):
        lst = []
        cnt = 0
        for i in range(len(num) - 1, -1, -1):
            lst.append(int(num[i]) * (10 ** cnt))
            cnt += 1
        return lst

    lst1, lst2 = strNum(num1), strNum(num2)
    return str(sum([x[0] * x[1] for x in product(lst1, lst2)]))