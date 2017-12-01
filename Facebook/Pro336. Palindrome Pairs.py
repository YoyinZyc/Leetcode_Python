class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        record = dict()
        ret = []
        for i, v in enumerate(words):
            record[v] = i
        for i, v in enumerate(words):
            j = 0
            while j < len(v) + 1:
                s1 = v[:j]
                s2 = v[j:]
                if self.isPalindrome(s1):
                    if s2[::-1] in record and record[s2[::-1]] != i:
                        ret.append([record[s2[::-1]], i])
                if self.isPalindrome(s2):
                    if s1[::-1] in record and record[s1[::-1]] != i and len(s2) != 0:
                        ret.append([i, record[s1[::-1]]])
                j += 1
        return ret

    def isPalindrome(self, s):
        if not s:
            return True
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True