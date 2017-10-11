'''
BitManipulation_Medium
10.11 12:08am
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = ""
        for i in range(32):
            count_1 = 0
            for v in nums:
                if v & 2 ** i:
                    count_1 += 1
            if count_1 % 3:
                ret = "1" + ret
            else:
                ret = '0' + ret
        if ret[0] == '1':
            return -1 - int(ret, 2) ^ (2 ** 32 - 1)
        return int(ret, 2)
