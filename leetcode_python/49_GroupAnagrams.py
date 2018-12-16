import collections

def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    a = collections.defaultdict(list)
    for i in strs:
        a[str(sorted(i))].append(i)
    return [a[x] for x in a]
