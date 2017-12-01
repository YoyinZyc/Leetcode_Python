class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = dict()
        s = 0
        max_length = 0
        for i,v in enumerate(nums):
            if v == 0:
                s-=1
            else:
                s+=1
            if s == 0:
                max_length = max(max_length, i+1)
            else:
                if s in d:
                    max_length = max(max_length, i-d[s])
                else:
                    d[s] = i
        return max_length