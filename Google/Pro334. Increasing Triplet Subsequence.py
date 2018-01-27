'''
题意：看nums中有没有的3个递增的sequence

'''
class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 记录first和second数的index
        a = -1
        b = -1
        for i, v in enumerate(nums):
            # 如果没有a，或者v比a对应的位置小
            if a == -1 or v < nums[a]:
                a = i
            # 如果v大于a的位置且b没有或者v比b位置小
            elif v > nums[a] and (b == -1 or v < nums[b]):
                b = i
            # b存在且v大于b
            elif b != -1 and v > nums[b]:
                return True
        return False
