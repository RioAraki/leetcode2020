# My failed solution. should be pretty close, only problem is that product(args*) requires multiple inputs but I dont know
# how to feed such multiple parameters input to it, I can only from an one element list



import itertools


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dct = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"],
               "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}

        return list(map(lambda x: "".join(x), itertools.product((dct[digits[i]] for i in range(len(digits))))))