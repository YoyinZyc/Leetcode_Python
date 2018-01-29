'''
题意：
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3

也是利用了减的那个思想
'''
from collections import deque
class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        # self.count = 0
        self.l = deque()
        self.l.append(0)
    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.l.append(self.l[-1]+val)
        if len(self.l)-1 > self.size:
            return (self.l[-1]-self.l[-1-self.size]) / self.size
        else:
            return self.l[-1] / (len(self.l)-1)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)