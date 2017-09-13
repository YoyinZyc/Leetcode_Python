'''
Greedy_Easy
9.12 4:46pm
'''


class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i = 0
        j = 0
        print(1)
        while i<len(s) and j<len(g):
            if s[i] >= g[j]:
                i+=1
                j+=1
            else:
                i+=1
        return j


if __name__ == "__main__":
    g = [10, 9, 8, 7]
    s = [5, 6, 7, 8]
    solution = Solution()
    solution.findContentChildren(g, s)