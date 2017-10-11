
'''
Google_Easy
10.9 12:44pm
'''
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[0] == 0:
            return [1]
        i = -1
        ret = [1]
        while i >= 0 - len(digits):
            s = ret[0] + digits[i]
            ret[0] = s % 10
            ret.insert(0, s // 10)
            i -= 1
        if ret[0] == 0:
            return ret[1:]
        return ret


