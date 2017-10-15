'''
LinkedIn_Medium
10.12 2:54pm
'''

class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """

        nums = [i for i in range(1, maxChoosableInteger + 1)]
        nums = tuple(nums)
        if sum(nums) < desiredTotal:
            return False
        record = dict()
        return self.helper(nums, desiredTotal, True, record)

    def helper(self, nums, total, desire, record):
        for i, v in enumerate(nums):
            if v >= total:
                if desire:
                    return True
                else:
                    return False
            result = True
            if i == 0:
                if not (nums[1:], total - v) in record:
                    record[(nums[1:], total - v)] = self.helper(nums[1:], total - v, not desire, record)
                result = record[(nums[1:], total - v)]
            else:
                if not (nums[0:i] + nums[i + 1:], total - v) in record:
                    record[(nums[0:i] + nums[i + 1:], total - v)] = self.helper(nums[0:i] + nums[i + 1:], total - v,
                                                                                not desire, record)
                result = record[(nums[0:i] + nums[i + 1:], total - v)]
            if desire and result:
                return True
            elif not desire and not result:
                return False
        if desire:
            return False
        else:
            return True



