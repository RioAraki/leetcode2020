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

#=================

# Better solution:
# 1. built a doubly linked list with key and value, act as a queue, add and remove using doubly linked list is o(1) because each of them would record prev and next
# 2. built a hashmap (dictionary) to save all key/value pairs since get operation in hashmap is o(1)
class Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = dict() 
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dic:
            cur = self.dic[key]
            self._remove(cur)
            self._add(cur)
            return cur.value
        return -1
                
    def put(self, key: int, value: int) -> None:
        # key exists, update the value, move 
        
        if key in self.dic:
            self._remove(self.dic[key])
        n = Node(key, value)
        self._add(n)
        self.dic[key] = n
        
        if len(self.dic) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]
    
    # remove a node from the doubly linked list
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
    
    # add a node to the doubly linked list
    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail