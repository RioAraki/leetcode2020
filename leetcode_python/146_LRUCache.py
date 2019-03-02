class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.lru = []
        self.dct = collections.defaultdict(int)
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dct.keys():
            return -1
        
        pos = self.lru.index(key)
        self.lru = [self.lru[pos]] + self.lru[:pos] + self.lru[pos+1:]
        
        return self.dct[key]
            

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.lru:
            if len(self.lru) == self.capacity:
                self.dct.pop(self.lru[-1])       
            self.lru = [key] + self.lru[:self.capacity-1]
            
        else:
            pos = self.lru.index(key)
            self.lru = [self.lru[pos]] + self.lru[:pos] + self.lru[pos+1:]
            
        self.dct[key] = value    
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)