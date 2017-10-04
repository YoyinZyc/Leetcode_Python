'''
TopLiked_Medium
9.29 9:11pm
'''

class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node("")

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        i = 0
        while i < len(word) and word[i] in node.v_l:
            node = node.l[node.v_l.index(word[i])]
            if i == len(word) - 1:
                node.k = 1
            i += 1
        if i < len(word):
            while i < len(word) - 1:
                next_node = Node(word[i])
                node.addNext(next_node)
                node = next_node
                i += 1
            node.addNext(Node(word[i], k=1))

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        i = 0
        while i < len(word) and word[i] in node.v_l:
            node = node.l[node.v_l.index(word[i])]
            i += 1
        if node.k == 1 and i == len(word):
            return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        i = 0
        while i < len(prefix) and prefix[i] in node.v_l:
            node = node.l[node.v_l.index(prefix[i])]
            i += 1
        if i == len(prefix):
            return True
        return False


class Node(object):
    def __init__(self, value, k=0):
        self.v = value
        self.k = k
        # 注意这边的初始化，如果是在init函数外面就会成为static变量
        self.l = []
        self.v_l = []
        print(self.v_l)

    def setKey(self, key):
        self.k = key

    def addNext(self, node):
        self.l.append(node)
        self.v_l.append(node.v)

        # Your Trie object will be instantiated and called as such:
        # obj = Trie()
        # obj.insert(word)
        # param_2 = obj.search(word)
        # param_3 = obj.startsWith(prefix)