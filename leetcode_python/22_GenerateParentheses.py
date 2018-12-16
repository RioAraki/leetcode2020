class Solution:
    def generateParenthesis(self, n):
        # p is the current string, left, right are numbers of ( ) we could put in p, parens returns the final solution
        def generate(p, left, right, parens=[]):
            print(p, left, right)
            # if there are still "left" left, add left to p
            if left:         generate(p + '(', left - 1, right)
            # add num of right > left , add right to p
            if right > left: generate(p + ')', left, right - 1)

            # once right has been used, ther must be no left and right left
            if not right:    parens += p,

            return parens

        return generate('', n, n)