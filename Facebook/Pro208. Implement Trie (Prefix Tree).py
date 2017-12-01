class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.subtrie = dict()
        self.isWord = False
        self.val = ''

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if not word:
            self.isWord = True
            return
        if word[0] not in self.subtrie:
            t = Trie()
            t.val = word[0]
            self.subtrie[word[0]] = t
        self.subtrie[word[0]].insert(word[1:])

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        t = self
        for v in word:
            if v in t.subtrie:
                t = t.subtrie[v]
            else:
                return False
        return t.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        t = self
        for v in prefix:
            if v in t.subtrie:
                t = t.subtrie[v]
            else:
                return False
        return True

        # Your Trie object will be instantiated and called as such:
        # obj = Trie()
        # obj.insert(word)
        # param_2 = obj.search(word)
        # param_3 = obj.startsWith(prefix)
    