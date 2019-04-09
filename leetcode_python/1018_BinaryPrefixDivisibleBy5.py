def prefixesDivBy5(self, A: List[int]) -> List[bool]:
    res = []
    bin = ""
    for i in A:
        bin += str(i)
        res.append(int(bin,2)%5 == 0) 
    return res

# https://leetcode.com/problems/binary-prefix-divisible-by-5/discuss/265601/Detailed-Explanation-using-Modular-Arithmetic-O(n)
# append one extra bit to a binary number
# Use the fact that (ab + c)%d is same as ((a%d)(b%d) + c%d)%d.
def prefixesDivBy5(self, A):
        for i in range(1, len(A)):
            A[i] += A[i - 1] * 2 % 5
        return [x % 5 == 0 for x in A]