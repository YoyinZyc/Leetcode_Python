class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1
        cur = 1
        while i >= 0 and cur:
            digits[i], cur = (digits[i] + cur) % 10, (digits[i] + cur) // 10
            i -= 1
        if cur:
            digits.insert(0, 1)
        return digits
