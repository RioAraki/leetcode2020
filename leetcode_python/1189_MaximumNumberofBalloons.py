class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        textCnt = collections.Counter(text)
        return min(textCnt["b"], textCnt["a"], textCnt["l"]//2,textCnt["o"]//2,textCnt["n"])