'''
题意:
给一组string
要求判断这个String matrix的每行每列是否相同

思路：
不能用zip
因为会有这种情况
Input:
[
  "abcd",
  "bnrt",
  "crm",
  "dt"
]

Output:
true

'''
class Solution:
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        # 先判断words中最长的word的长度是否和word的总个数相等
        max_len = 0
        for v in words:
            max_len = max(max_len, len(v))
        if len(words) != max_len:
            return False
        i = 0
        while i < len(words):
            j = i+1
            while j < len(words):
                # 对应的位置都为空或者对应位置的字符相同
                if (j >= len(words[i]) and i >= len(words[j])) or (j < len(words[i]) and i < len(words[j]) and words[i][j] == words[j][i]):
                    j+=1
                else:
                    return False
            i+=1
        return True