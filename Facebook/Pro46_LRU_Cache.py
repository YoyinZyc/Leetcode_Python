'''
Facebook_Hard
10.2 6:43pm
'''
from collections import deque


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.d = dict()
        self.q = deque()

    def get(self, key):
        """1
        :type key: int
        :rtype: int
        """
        if key in self.q:
            self.q.remove(key)
            self.q.appendleft(key)
            return self.d[key]
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        self.d[key] = value
        if key in self.q:
            self.q.remove(key)
            self.q.appendleft(key)
        else:
            if self.capacity:
                self.q.appendleft(key)
                self.capacity -= 1
            else:
                self.q.pop()
                self.q.appendleft(key)



                # Your LRUCache object will be instantiated and called as such:
                # obj = LRUCache(capacity)
                # param_1 = obj.get(key)
                # obj.put(key,value)