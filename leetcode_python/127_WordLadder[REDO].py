# 2019-01-08： REDO, got the rough idea. Does not make it by my own

def ladderLength(self, beginWord, endWord, wordList):
	"""
	:type beginWord: str
	:type endWord: str
	:type wordList: List[str]
	:rtype: int
	"""
	# set up a dictionary with key as the word with * in a character, value as the corresponding words
	# eg: "m*d": mid, mad, mud

	# then do a bfs to find the connection

    dct = collections.defaultdict(list)
    
    for word in wordList:
        for i in range(len(word)):
            dct[word[:i]+'*'+word[i+1:]].append(word)
    
    q, visited = collections.deque([(beginWord, 1)]), set()
    
    while q:
        word, length = q.popleft()
        if word == endWord:
            return length
        visited.add(word)
        
        for i in range(len(word)):
            s = word[:i]+"*"+word[i+1:]
            neigh = dct.get(s, [])
            for nei in neigh:
                if nei not in visited:
                    q.append((nei, length+1))
    return 0