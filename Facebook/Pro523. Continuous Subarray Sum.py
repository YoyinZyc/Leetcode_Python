'''
Facebook_Medium
11.9 11:24pm
'''
class Solution:
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        if k < 0:
            k = -k
        if k == 0:
            for i in range(1, len(nums)):
                if nums[i] == 0 and nums[i - 1] == 0:
                    return True
            return False
        if k == 1:
            return True
        record = dict()
        record[nums[0] % k] = []
        record[nums[0] % k].append(0)
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            if not nums[i] % k:
                return True
            remain = nums[i] % k
            if remain in record:
                if record[remain][0] < i - 1:
                    return True
                else:
                    record[remain].append(i)
            else:
                record[remain] = [i]
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.checkSubarraySum([-2, -2, 8],6))


