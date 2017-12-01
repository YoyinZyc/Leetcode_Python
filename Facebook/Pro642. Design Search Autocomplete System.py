class AutocompleteSystem:
    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.d = dict()
        self.begin = Trie('')

        for i, v in enumerate(sentences):
            self.begin.insert(v, v, times[i])
            self.d[v] = times[i]
        self.t = self.begin
        self.input_s = ''
        # for v in sentences:

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        ans = []
        if c == '#':
            self.d[self.input_s] = self.d.get(self.input_s,0)+1
            self.begin.insert(self.input_s, self.input_s, self.d[self.input_s])
            # self.begin.times[self.input_s] = 1
            self.t = self.begin
            self.input_s = ''
            return ans
        self.input_s += c
        if not self.t:
            return ans
        if c in self.t.next:
            self.t = self.t.next[c]
            words = self.t.words
            words.sort()
            i = 0
            while i < len(words) and i < 3:
                ans.append(words[i][1])
                i+=1
        else:
            self.t = None
        return ans

class Trie(object):
    def __init__(self, val):
        self.next = {}
        self.val = val
        self.words = []
        # self.times = times

    def insert(self, ful_word, word, times):
        # self.words.append(ful_word)
        if [1-times, ful_word] in self.words:
            self.words.remove([1 - times, ful_word])
        self.words.append([0-times,ful_word])
        if word:
            if word[0] in self.next:
                t = self.next[word[0]]
            else:
                t = Trie(word[0])
                self.next[word[0]] = t
            t.insert(ful_word, word[1:], times)