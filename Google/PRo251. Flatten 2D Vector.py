'''
题意：
For example,
Given 2d vector =

[
  [1,2],
  [3],
  [4,5,6]
]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].

思路：
注意可能有这样的输入[[],[]], 所以在init方法里要排除空
'''
class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.l = vec2d
        i = 0
        # 去空
        while i < len(self.l):
            if self.l[i]:
                i+=1
            else:
                self.l.pop(i)
        self.next_v = 0

    def next(self):
        """
        :rtype: int
        """
        return self.next_v

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.l:
            self.next_v = self.l[0].pop(0)
            if not self.l[0]:
                self.l.pop(0)
            return True
        return False

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())