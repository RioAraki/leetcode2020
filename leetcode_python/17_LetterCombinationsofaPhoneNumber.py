# mind the usage of *

import itertools


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "": return []
        dct = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"],
               "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}

        return list(map(lambda x: "".join(x), itertools.product(*[dct[digits[i]] for i in range(len(digits))])))

# another solution, not fancy but works well.
class Solution:
  def letterCombinations(self, digits):
      """
      :type digits: str
      :rtype: List[str]
      """
      teleDct = {"2":["a","b","c"],
                "3":["d", "e", "f"],
                "4":["g","h","i"],
                "5":["j","k","l"],
                "6":["m", "n", "o"],
                "7":["p","q","r","s"],
                "8":["t", "u", "v"],
                "9":["w","x","y","z"]}
      
      ret = []
      for i in digits:
          if len(ret) == 0:
              for letter in teleDct[i]:
                  ret.append(letter)
          else:
              tmp = ret
              ret = []
              for j in tmp:
                  for letter in teleDct[i]:
                      ret.append(j+letter)
      return ret