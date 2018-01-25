'''
给个array，写个类似java里的iterator class，实现next()和hasNext()。array的even position是count，
odd position是number。比如 [3, 5, 0, 1]， 不停call next() 需要得到 [5, 5, 5]
'''
class ArrayIterator(object):
    def __init__(self, nums):
        self.nums = nums
        self.currentTimeIndex = 0
        self.currentValue = self.nums[1]
    def hasNext(self):
        while self.currentTimeIndex < len(self.nums) and not self.nums[self.currentTimeIndex]:
            self.currentTimeIndex+=2
        if self.currentTimeIndex >= len(self.nums):
            return False
        self.currentValue = self.nums[self.currentTimeIndex+1]
        return True
    def next(self):
        self.nums[self.currentTimeIndex] -= 1
        return self.currentValue
if __name__ == '__main__':
    i = ArrayIterator(nums = [0,2,4,1,0,3,0,2,1,8])
    while i.hasNext():
        print(i.next())