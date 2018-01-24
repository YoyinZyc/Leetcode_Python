'''
题意：给一个字符串判断这个字符串的各种combination中有没有能形成回文数列的
思路：
用一个dict存储每个字符对应的个数
'''
class Solution:
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        record = dict()
        for v in s:
            record[v] = record.get(v,0)+1
        has_odd = False
        for v in record:
            if record[v]%2 and has_odd:
                return False
            if record[v]%2:
                has_odd = True
        return True