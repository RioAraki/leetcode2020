class Solution:
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        # corner case: hand = 0, wrong number of total cards in hands
        if len(hand) == 0 or len(hand) % W != 0:
            return False

        hand = sorted(hand)

        while len(hand) != 0:
            start = hand[0]
            count = 0

            while count < W:
                if start + count not in hand:
                    return False
                else:
                    hand.remove(start + count)
                    count += 1

        return True