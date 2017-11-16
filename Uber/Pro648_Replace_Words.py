'''
Uber_Medium
10.29 6:34pm
'''

class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        if not dict:
            return sentence
        root = Trie()
        for v in dict:
            trie = root
            for v1 in v:
                if v1 not in trie.d:
                    trie.d[v1] = Trie()
                trie = trie.d[v1]
            trie.isRoot = True
        ret = ''
        i = 0
        l = sentence.split(' ')
        for v in l:
            ret += ' '
            trie = root
            i = 0
            add_value = ''
            find = False
            while i < len(v):
                if v[i] in trie.d:
                    # add_value += v[i]
                    if trie.d[v[i]].isRoot:
                        # ret += add_value
                        find = True
                        break
                    trie = trie.d[v[i]]
                else:
                    break
                i += 1
            if not find:
                ret += v
            else:
                ret += v[:i + 1]
        return ret[1:]


class Trie(object):
    def __init__(self):
        self.isRoot = False
        self.d = dict()