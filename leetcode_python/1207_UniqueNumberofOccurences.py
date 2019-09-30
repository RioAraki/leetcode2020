def uniqueOccurrences(self, arr: List[int]) -> bool:
  cnt = collections.Counter(arr)
  return len(cnt.values()) == len(set(cnt.values()))
