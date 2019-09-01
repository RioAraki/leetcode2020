# TLE

class DinnerPlates:

    def __init__(self, capacity: int):
        self.dct = collections.defaultdict(list)
        self.status = collections.defaultdict(int)
        self.capacity = capacity
        self.fulfill = []
    def push(self, val: int) -> None:
        # check if there are empty spaces in the stack before
        #  if there is fill the leftmost one space, update dct and status
        #  if not open a new stack to save the new plate
        #  corner case: initial
        
        n = len(self.status)
        first = n
        # print(self.dct, self.status, val)
        for i in range(n):
            if self.status[i] != self.capacity:
                first = i
                break
        else:
            self.dct[n].append(val)
            self.status[n] += 1
            
        # empty space existed in stacks before
        if first < n:
            self.dct[first].append(val)
            self.status[first] += 1

        
    def pop(self) -> int:
        n = len(self.status)
        for i in range(n-1, -1, -1):
            if self.status[i] > 0:
                break
        # cannot pop anything from the stacks
        else:
            return -1

        self.status[i] -= 1
        ret = self.dct[i].pop(-1)
        # if the last stack is empty, we could eliminate this stack
        if i == n-1 and self.status[i] == 0:
            del self.status[i]
            del self.dct[i]
        
        
        return ret
                     

    def popAtStack(self, index: int) -> int:
        stackLen = self.status[index]
        if stackLen == 0:
            return -1
        else:
            self.status[index] -= 1
            return self.dct[index].pop(-1)


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)