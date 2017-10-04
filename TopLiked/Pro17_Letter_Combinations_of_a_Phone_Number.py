'''
TopLiked_Medium
9.28 12:29pm
'''

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {'1': ['*'], '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        if not digits:
            return []
        return self.helper(d, digits)

    def helper(self, d, digits):
        if len(digits) == 1:
            return d[digits[0]]
        ret = []
        l = self.helper(d, digits[1:])
        l_d = d[digits[0]]
        for v in l:
            for v2 in l_d:
                ret.append(v2 + v)
        return ret



