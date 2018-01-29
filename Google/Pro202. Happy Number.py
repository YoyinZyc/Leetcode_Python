'''
Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        record = [n]
        while True:
            if n == 1:
                return True
            temp = 0
            for v in str(n):
                temp += int(v) ** 2
            if temp in record:
                return False

            record.append(temp)
            n = temp

