class Solution:
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        ret = []
        # 注意这里吧lower-1和upper+1放进nums，因为lower和upper两个边界是包含的，所有要放-1和+1
        nums.insert(0,lower-1)
        nums.append(upper+1)
        i = 1
        # 循环判断后一个和前一个
        while i < len(nums):
            if nums[i] - nums[i-1] == 2:
                ret.append(str(nums[i]-1))
            elif nums[i] - nums[i-1] > 2:
                ret.append(str(nums[i-1]+1)+'->'+str(nums[i]-1))
            i+=1
        return ret