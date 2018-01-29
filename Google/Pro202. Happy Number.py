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

