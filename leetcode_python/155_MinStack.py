class MinStack(object):
              
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.smallest = []
        self.container = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.container.append(x)
        if len(self.smallest) == 0 or self.smallest[-1]>=x:
            self.smallest.append(x)
            

    def pop(self):
        """
        :rtype: None
        """
        poped = self.container.pop(-1)
        if poped == self.smallest[-1]:
            self.smallest.pop(-1)
        return poped
        

    def top(self):
        """
        :rtype: int
        """
        return self.container[-1] if self.container else None
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.smallest[-1] if self.smallest else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()