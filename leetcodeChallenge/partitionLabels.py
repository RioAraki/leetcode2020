class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        letterList = []
        for i in range(26):
            letterList.append([len(S), 0])
        for i in range(len(S)):
            letterList[ord(S[i])-ord('a')][0] = min(letterList[ord(S[i])-ord('a')][0], i)
            letterList[ord(S[i])-ord('a')][1] = max(letterList[ord(S[i])-ord('a')][1], i)
        
        i = 0;
        res = []
        while i < len(S):
            start = letterList[ord(S[i])-ord('a')][0]
            end = letterList[ord(S[i])-ord('a')][1]
            isChanged = 1
            while (isChanged):
                isChanged = 0
                tmp = end
                for j in range(start, end):
                    if letterList[ord(S[j])-ord('a')][1] > end:
                        end = letterList[ord(S[j])-ord('a')][1]
                        isChanged = 1
            # print(start, end)
            res.append(end - start + 1)
            start = end + 1
            i = end + 1
        return res
            
                
            