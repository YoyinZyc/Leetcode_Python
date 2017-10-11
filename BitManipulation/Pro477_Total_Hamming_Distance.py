'''
BitManipulation_Medium
10.10 10:14pm
'''
class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        total = 0
        for bit in range(32):
            count_0 = 0
            count_1 = 0
            for n in nums:
                if n & 2 ** (bit):
                    count_1 += 1
                else:
                    count_0 += 1
            total += count_0 * count_1
        return total