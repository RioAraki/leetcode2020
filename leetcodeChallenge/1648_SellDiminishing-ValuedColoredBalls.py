# sort the list in reverse order
# remove balls from big to small
# care big integer multiplication, use Fraction

from fractions import Fraction

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        
        def equalDiffSum(head, tail):
            head = Fraction(head)
            tail = Fraction(tail)
            return int((head + tail) * (tail - head + 1) / 2)
        
        inventory.sort(reverse = True)
        inventory += [0]
        res = 0
        multiplier = 1
        for i in range(len(inventory)-1):
            if orders == 0:
                break
            if i+1 < len(inventory):
                if inventory[i] > inventory[i+1]:
                    diff = (inventory[i] - inventory[i+1]) * multiplier
                    if orders >= diff:
                        orders -= diff
                        res += equalDiffSum(inventory[i+1] + 1, inventory[i]) * multiplier
                    elif orders < diff:
                        quotient = orders // multiplier
                        remainder = orders % multiplier
                        res += equalDiffSum(inventory[i] - quotient + 1, inventory[i]) * multiplier
                        orders -= quotient * multiplier
                        res += (inventory[i] - quotient) * remainder
                        orders -= remainder
                        break
                multiplier += 1
                      
                        
        return res % (10**9 + 7)
                        
                    