class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        record = dict()
        return self.helper(nums, target, record)

    def helper(self, nums, target, record):
        count = 0
        for v in nums:
            if target - v > 0:
                if target - v not in record:
                    record[target - v] = self.helper(nums, target - v, record)
                count += record[target - v]
            elif target == v:
                count += 1
        return count
if __name__ == '__main__':
    s = Solution()
    s.combinationSum4([1,2,3],4)