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

import random


class RandomizedCollection:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.loc = dict()
        self.nums = list()

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.nums.append(val)
        if val in self.loc:
            self.loc[val].append(len(self.nums) - 1)
            return False
        else:
            self.loc[val] = [len(self.nums) - 1]
            return True

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.loc:
            pos, last = self.loc[val].pop(), self.nums[-1]
            # 如果pos本来就是最后一位就不需要这个操作
            if pos < len(self.nums) - 1:
                # nums的最后一位改为要pop出的值
                self.nums[pos] = last
                # 把原本最后一位对应的数组中弹出index
                self.loc[last].remove(len(self.nums) - 1)
                # 更新index
                self.loc[last].append(pos)
            # 如果空了，弹出这个key
            if not self.loc[val]:
                self.loc.pop(val)
            self.nums.pop()
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.nums)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()



#更快的方法

import random


class RandomizedCollection(object):
    def __init__(self):
        # vals存储数， idxs存储数字对应的下标
        self.vals, self.idxs = [], collections.defaultdict(set)

    def insert(self, val):
        # 插入
        self.vals.append(val)
        self.idxs[val].add(len(self.vals) - 1)
        return len(self.idxs[val]) == 1

    def remove(self, val):
        if self.idxs[val]:
            # val对应的一个下标，数组最后一个数字
            out, ins = self.idxs[val].pop(), self.vals[-1]
            # 把最后一个数字放到val对应的位置
            self.vals[out] = ins
            # 把这个位置加进最后一个数字对应的map中
            self.idxs[ins].add(out)
            # 把其原先位置删除，注意要先添加再删除，这样就不用考虑本身是不是就是最后一个
            self.idxs[ins].discard(len(self.vals) - 1)
            # 弹出
            self.vals.pop()
            return True
        return False

    def getRandom(self):
        return random.choice(self.vals)