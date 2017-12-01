class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        return self.helper(s, wordDict, {})

    def helper(self, s, wordDict, record):
        if s in record:
            return record[s]
        l = []
        if not s:
            return []
        for word in wordDict:
            if s[:len(word)] == word:
                if len(word) == len(s):
                    l.append(word)
                else:
                    ret = self.helper(s[len(word)], wordDict, record)
                    for v in ret:
                        l.append(word + ' ' + v)
        record[s] = l
        return l
if __name__ == '__main__':
    s = Solution()
    s.wordBreak("catsanddog",
["cat","cats","and","sand","dog"])