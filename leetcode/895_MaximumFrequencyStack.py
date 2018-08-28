# correct but TLE

# A dictionary to keep track of the num of elements in the stack
# A list to keep track of the index of elements in the stack

import operator
class TLEFreqStack:

    def __init__(self):
        self.dct = {}
        self.lst = []
    def push(self, x):
        """
        :type x: inta
        :rtype: void
        """
        if x in self.dct:
            self.dct[x] += 1
        else:
            self.dct[x] = 1
        self.lst.append(x)

# find max val in the dict
# find key with the max val that has largest index
# pop this key from list and decrement the value of it by 1

# how to improve:
# better data structure? priority queue?

    def pop(self):
        """
        :rtype: int
        """
        maxVal = max(self.dct.items(), key= operator.itemgetter(1))[1]
        # print("maxVal: ", maxVal)
        maxKeyList = list(filter(lambda x: x[1] == maxVal, self.dct.items()))
        # print("maxKeyList: ", maxKeyList)
        popIndex = len(self.lst)-1 - min([self.lst[::-1].index(pair[0]) for pair in maxKeyList])
        # print("popIndex: ", popIndex)
        self.dct[self.lst[popIndex]] -= 1
        return self.lst.pop(popIndex)

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()

if __name__ == "__main__":
    freq = TLEFreqStack()
    freq.push(5)
    freq.push(7)
    freq.push(5)
    freq.push(7)
    freq.push(4)
    freq.push(5)
    print(freq.dct, freq.lst)
    print(freq.pop())
    print(freq.pop())
    print(freq.pop())
    print(freq.pop())
    print(freq.dct, freq.lst)