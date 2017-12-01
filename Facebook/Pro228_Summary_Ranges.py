class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        i = 0
        j = 1
        ret = []
        while j < len(nums):
            if nums[j]-nums[j-1] > 1:
                if nums[j-1] == nums[i]:
                    ret.append(str(nums[i]))
                else:
                    ret.append(str(nums[i])+'->'+str(nums[j-1]))
                i = j
            j+=1
        if i == j-1:
            ret.append(str(nums[i]))
        else:
            ret.append(str(nums[i])+'->'+str(nums[j-1]))
        return ret