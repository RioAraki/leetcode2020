class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        lst1 = version1.split(".")
        lst2 = version2.split(".")
        minlen = min(len(lst1), len(lst2))
        for i in range(minlen):
            v1 = int(lst1[i].lstrip("0")) if lst1[i].lstrip("0") != "" else 0
            v2 = int(lst2[i].lstrip("0")) if lst2[i].lstrip("0") != "" else 0
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1 
        lst1 = lst1[minlen:]
        lst2 = lst2[minlen:]
        
        if len(list(filter(lambda x: x != "", [x.lstrip("0") for x in lst1]))):
            return 1
        elif len(list(filter(lambda x: x != "", [x.lstrip("0") for x in lst2]))):
            return -1
        return 0