'''
Google_Medium
10.11 1:07pm
'''
class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        mask = 0
        final = 0
        for i in range(31, -1, -1):
            mask |= 1 << i
            prefix_set = {v & mask for v in nums}
            guess = final | 1 << i
            for v in prefix_set:
                if v ^ guess in prefix_set:
                    final = guess
                    break
        return final
