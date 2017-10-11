
'''
Facebook_Medium
10.8 9:03pm
'''
from collections import deque


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if not endWord in wordList:
            return 0
        q = deque()
        q2 = deque()
        q.append(beginWord)
        visited_set = []
        level = 1
        while q:
            word = q.popleft()
            i = 0
            while i < len(word):
                for c in range(ord('a'), ord('a') + 26):
                    char = chr(c)
                    find_s = list(word)
                    find_s[i] = char
                    find_s = ''.join(find_s)
                    # print(find_s)

                    if find_s == endWord:
                        return level + 1
                    if find_s in wordList and not find_s in visited_set:
                        visited_set.append(find_s)
                        q2.append(find_s)
                i += 1
            if not q:
                level += 1
                temp = q
                q = q2
                q2 = temp

        return 0



        # if __name__ == '__main__':
        #     s = Solution()
        #     s.ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"])