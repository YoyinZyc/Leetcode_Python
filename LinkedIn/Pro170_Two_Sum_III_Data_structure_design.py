'''
LinkedIn_Easy
10.13 1:03am
'''
class TwoSum(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = set()
        self.d = dict()

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.s.add(number)
        self.d[number] = self.d.get(number, 0) + 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for i, v in enumerate(self.s):
            if value - v == v and self.d[v] > 1:
                return True
            elif value - v != v and value - v in self.s:
                return True
        return False



        # Your TwoSum object will be instantiated and called as such:
        # obj = TwoSum()
        # obj.add(number)
        # param_2 = obj.find(value)