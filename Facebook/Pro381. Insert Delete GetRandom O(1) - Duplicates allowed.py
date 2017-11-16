'''
Facebook_Hard
11.06 11:26am
'''
import random
class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = dict()
        self.l = []

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.l.append(val)
        if val in self.d:
            self.d[val] += 1
            return False
        else:
            self.d[val] = 1
            return True


    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.d:
            self.d[val] -= 1
            if not self.d[val]:
                self.d.pop(val)
            self.l.remove(val)
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.l[random.randrange(len(self.l))]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()



#更快的方法

import random


class RandomizedCollection(object):
    def __init__(self):
        self.vals, self.idxs = [], collections.defaultdict(set)

    def insert(self, val):
        self.vals.append(val)
        self.idxs[val].add(len(self.vals) - 1)
        return len(self.idxs[val]) == 1

    def remove(self, val):
        if self.idxs[val]:
            out, ins = self.idxs[val].pop(), self.vals[-1]
            self.vals[out] = ins
            self.idxs[ins].add(out)
            self.idxs[ins].discard(len(self.vals) - 1)
            self.vals.pop()
            return True
        return False

    def getRandom(self):
        return random.choice(self.vals)