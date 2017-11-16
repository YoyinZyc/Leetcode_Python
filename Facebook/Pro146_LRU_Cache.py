from collections import OrderedDict

class LRUCache(object):
    def __init__(self, capacity):
        self.array = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.array:
            value = self.array[key]
            del self.array[key]
            self.array[key] = value
            return value
        else:
            return -1

    def put(self, key, value):
        if key in self.array:
            # Delete existing key before refreshing it
            # del self.array[key]
            self.array.pop(key)
        elif len(self.array) >= self.capacity:
            # Delete oldest
            self.array.popitem(last=False) //这个相当于把要删除的放在dict的首位
            # self.array.pop(k)
        self.array[key] = value