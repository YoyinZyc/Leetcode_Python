'''
题意：
给一个字符串，要求找到所以把其中连续的++替换成--的结果
For example, given s = "++++", after one move, it may become one of the following states:
[
  "--++",
  "+--+",
  "++--"
]

'''
class Solution:
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        i = 0
        ret = []
        while i < len(s)-1:
            if s[i]=='+' and s[i+1] == '+':
                ret.append(s[:i] + '--' + s[i+2:])
            i+=1
        return ret