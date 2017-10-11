'''
Google_Hard
10.10 12:17pm
'''
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        record = [[0 for i in range(len(nums))] for j in range(len(nums))]
        for i in range(1, len(nums) + 1):
            for j in range(0, len(nums) - i + 1):

                for k in range(j, j + i):
                    last_burst = nums[k] * self.get_value(nums, j - 1) * self.get_value(nums, j + i)
                    if k != j:
                        last_burst += record[j][k - 1]
                    if k != j + i - 1:
                        last_burst += record[k + 1][j + i - 1]
                    record[j][j + i - 1] = max(record[j][j + i - 1], last_burst)
        print(record)
        return record[0][len(nums) - 1]

    def get_value(self, nums, i):
        if i < 0 or i >= len(nums):
            return 1
        else:
            return nums[i]