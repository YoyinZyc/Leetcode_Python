
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



# 双向DFS
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        beginSet = set()
        endSet = set()
        visited = set()
        beginSet.add(beginWord)
        endSet.add(endWord)
        alp = 'abcdefghijklmnopqrstuvwxyz'
        length = 1
        while beginSet and endSet:
            if len(beginSet) > len(endSet):
                swap = beginSet
                beginSet = endSet
                endSet = swap

            temp = set()
            for word in beginSet:
                for i in range(len(word)):
                    for v in alp:
                        findWord = word[:i] + v + word[i + 1:]
                        if findWord in endSet:
                            return length + 1

                        if findWord not in visited and findWord in wordList:
                            temp.add(findWord)
                            visited.add(findWord)
            beginSet = temp
            length += 1
        return 0


if __name__ == '__main__':
    s = Solution()
    s.ladderLength("hit",
"cog",
["hot","dot","dog","lot","log"])