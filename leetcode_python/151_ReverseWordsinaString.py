# 2019-03-02

def reverseWords(self, s: str) -> str:
    return " ".join( filter(lambda x: x != "", s.strip().split(" ")[::-1]))