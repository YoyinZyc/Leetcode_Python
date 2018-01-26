'''
设计一个event queue。
要求给 定一个event，判断在这个 event之前的一个固定时间段里 有没有出现大于k个event。
event可能是按时间顺序来也可 能是随机来

random:
用heap
顺序：
一个长度为k的queue，小于k，加入；大于k，弹出老的，放入新的
'''
import heapq
from collections import deque
class EventQueue(object):
    def __init__(self,k,time):
        self.queue = deque()
        self.k = k
        self.time = time

    def random_add(self,e):
        if len(self.queue) >= self.k:
            heapq.heappush(self.queue, e)
            i = self.queue.index(e)
            if i < self.k:
                return False
            elif e - self.queue[i-self.k] <= self.time:
                return True
            else:
                return False
        else:
            heapq.heappush(self.queue, e)
        return False
    def add(self,e):
        if len(self.queue) >= self.k:
            first = self.queue[0]
            self.queue.popleft()
            self.queue.append(e)
            if e-first <= self.time:
                return True
            else:
                return False
        else:
            self.queue.append(e)
            return False
if __name__ == '__main__':
    e = EventQueue(3,20)
    es = [1,2,4,7,50]
    for v in es:
        print(e.add(v))