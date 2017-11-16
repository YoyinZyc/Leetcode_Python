'''
Facebook_Medium
11.06 11：29pm
'''
from collections import deque


class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie('')

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if node.l[index]:
                node = node.l[index]
            else:
                node.l[index] = Trie(word[i])
                node = node.l[index]
        node.isWord = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.helper(word, self.root)

    def helper(self, word, node):
        if not word:
            return node.isWord
        i = 0
        while i < len(word):
            if word[i] == '.':
                for j in range(26):
                    if node.l[j] and self.helper(word[i + 1:], node.l[j]):
                        return True
                return False
            else:
                if node.l[ord(word[i]) - ord('a')]:
                    node = node.l[ord(word[i]) - ord('a')]
                else:
                    return False
            i += 1
        return node.isWord


class Trie(object):
    def __init__(self, v):
        self.v = v
        self.isWord = False
        self.l = [0 for _ in range(26)]
        # Your WordDictionary object will be instantiated and called as such:
        # obj = WordDictionary()
        # obj.addWord(word)
        # param_2 = obj.search(word)


# 方法2
class WordDictionary(object):
    def __init__(self):
        self.word_dict = collections.defaultdict(list)

    def addWord(self, word):
        if word:
            self.word_dict[len(word)].append(word)

    def search(self, word):
        if not word:
            return False
        if '.' not in word:
            return word in self.word_dict[len(word)]
        for v in self.word_dict[len(word)]:
            # match xx.xx.x with yyyyyyy
            for i, ch in enumerate(word):
                if ch != v[i] and ch != '.':
                    break
            else:
                return True
        return False