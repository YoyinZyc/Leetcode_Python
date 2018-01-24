'''
题意：
给2个数列，要求zigzag输出
v1 = [1, 2]
v2 = [3, 4, 5, 6]
 [1, 3, 2, 4, 5, 6]

follow-up
k个list

思路：
先转换为deque，然后popleft
'''
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v1 = v1
        self.v2 = v2
        self.i = 0
        self.j = 0

    def next(self):
        """
        :rtype: int
        """
        if self.i == 1:
            self.i = 0
            self.j+=1
            if self.j-1 >= len(self.v2):
                self.j+=1
                return self.v1[self.j-1]
            else:
                return self.v2[self.j-1]
        else:
            self.i = 1
            if self.j >= len(self.v1):
                self.j+=1
                return self.v2[self.j-1]
            else:
                return self.v1[self.j]

    def hasNext(self):
        """
        :rtype: bool
        """
        return (self.i == 1 and (self.j < len(self.v2) or self.j+1 < len(self.v1)))or (self.i == 0 and (self.j < len(self.v1) or self.j < len(self.v2)))
# Your ZigzagIterator object will be instantiated and called as such:
'''
follow-up
'''
from collections import deque
class ZigzagIterator2(object):

    def __init__(self, vs):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        # 转换为deque
        vs = [deque(v) for v in vs]
        self.vs = vs
        # 指向下一个
        self.current = 0
        # 下一个value
        self.next_val = 0
    def next(self):
        """
        :rtype: int
        """
        return self.next_val

    def hasNext(self):
        """
        :rtype: bool
        """
        i = 0
        # 循环找到下一个，一共循环的次数是vs的长度
        while i < len(self.vs):
            if self.vs[(i+self.current) % len(self.vs)]:
                self.next_val = self.vs[(i+self.current) % len(self.vs)].popleft()
                self.current = (i+self.current) % len(self.vs)+1
                return True
            i+=1
        return False


if __name__ == '__main__':
    vs = [[1,2],[3,4,5,6],[7,8,9]]
    v1 = [1,2]
    v2 = [3,4,5,6]
    i, v = ZigzagIterator2(vs), []
    while i.hasNext():
        print(i.next())