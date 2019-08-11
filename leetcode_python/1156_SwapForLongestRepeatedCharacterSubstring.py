import collections

class Solution(object):
    def maxRepOpt1(text):
        """
        :type text: str
        :rtype: int
        """
        n = len(text)
        if n < 2:
            return n

        # loop through the text, if previous and next char is the same and is different from cur, check if swap could be better.

        # a b c
        # a == b == c -> search for group
        # go to the end of group and check if next.next == cur
        # if so try to swap next with a value of cur

        longest = 1

        group = collections.defaultdict(list)

        start, end = 0, 0

        for i in range(n - 1):
            if text[i] != text[i + 1]:
                end = i
                group[text[i]].append((start, end))
                start = i + 1
            elif text[i] == text[i + 1]:
                end += 1

        if text[n - 1] != text[n - 2]:
            group[text[n - 1]].append((n - 1, n - 1))
        else:
            group[text[n - 1]].append((start, n - 1))

        for letter in group.values():
            size = len(letter) > 2
            if len(letter) == 1:
                longest = max(longest, letter[0][-1] - letter[0][0] + 1)
            for i in zip(letter[:-1], letter[1:]):
                if i[1][0] - i[0][-1] == 2:
                    if size:
                        longest = max(longest, i[1][-1] - i[0][0] + 1)
                    else:
                        longest = max(longest, i[1][-1] - i[0][0])
                else:
                    longest = max(longest, i[1][-1] - i[1][0] + 2, i[0][-1] - i[0][0] + 2)
        return longest










