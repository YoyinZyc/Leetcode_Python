'''
Uber_Hard
10.29 6:34pm
'''
class AllOne(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d_value = dict()
        self.d_key = dict()

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if key in self.d_value:
            self.d_key[self.d_value[key]].remove(key)
            if not self.d_key[self.d_value[key]]:
                self.d_key.pop(self.d_value[key])
        self.d_value[key] = self.d_value.get(key, 0) + 1
        self.d_key[self.d_value[key]] = self.d_key.get(self.d_value[key], [])
        self.d_key[self.d_value[key]].append(key)

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key in self.d_value:
            self.d_key[self.d_value[key]].remove(key)
            if not self.d_key[self.d_value[key]]:
                self.d_key.pop(self.d_value[key])
            self.d_value[key] -= 1
            if self.d_value[key] > 0:
                self.d_key[self.d_value[key]] = self.d_key.get(self.d_value[key], [])
                self.d_key[self.d_value[key]].append(key)
            else:
                self.d_value.pop(key)

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if not self.d_key:
            return ""
        return self.d_key[max(self.d_key.keys())][0]

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if not self.d_key:
            return ""
        # print(self.d_key)
        return self.d_key[min(self.d_key.keys())][0]


        # Your AllOne object will be instantiated and called as such:
        # obj = AllOne()
        # obj.inc(key)
        # obj.dec(key)
        # param_3 = obj.getMaxKey()
        # param_4 = obj.getMinKey()