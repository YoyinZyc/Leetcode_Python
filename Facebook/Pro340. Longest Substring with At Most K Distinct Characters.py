class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        record = dict()
        i = 0
        j = 0
        max_l = 0
        while j < len(s):
            if s[j] in record:
                record[s[j]] += 1
            else:
                record[s[j]] = 1
            if len(record) > k:
                max_l = max(max_l, j-i)
                while len(record) > k:
                    record[s[i]]-=1
                    if not record[s[i]]:
                        record.pop(s[i])
                    i+=1
            j+=1
        max_l = max(max_l, j-i)
        return max_l