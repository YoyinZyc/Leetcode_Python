class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
        ans = list()
        for i in range(len(nums)-2):
            if i ==0 or nums[i] != nums[i-1]:
                j = i+1
                k = len(nums)-1
                while j < k:
                    if nums[j] + nums[k] == 0-nums[i]:
                        ans.append([nums[i], nums[j], nums[k]])
                        while j < k and nums[j] == nums[j+1]:
                            j+=1
                        j+=1
                        while k > j and nums[k] == nums[k-1]:
                            k-=1
                        k-=1
                    elif nums[j] + nums[k] < 0-nums[i]:
                        j+=1
                    else:
                        k-=1
        return ans