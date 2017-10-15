'''
LinkedIn_Medium
10.14 6:41pm
'''

class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        index_word1 = 0
        index_word2 = 0
        visited_word1 = False
        visited_word2 = False
        i = 0
        while not visited_word1 or not visited_word2:
            if words[i] == word1 and words[i] == word2:
                if visited_word1:
                    index_word2 = i
                    visited_word2 = True
                else:
                    index_word1 = i
                    visited_word1 = True
            elif words[i] == word1:
                index_word1 = i
                visited_word1 = True
            elif words[i] == word2:
                index_word2 = i
                visited_word2 = True
            i += 1

        distance = abs(index_word1 - index_word2)
        while i < len(words):
            if words[i] == word1 and words[i] == word2:
                if index_word1 < index_word2:
                    index_word1 = i
                else:
                    index_word2 = i
                distance = min(distance, abs(index_word1 - index_word2))
            elif words[i] == word1:
                index_word1 = i
                distance = min(distance, abs(index_word1 - index_word2))
            elif words[i] == word2:
                index_word2 = i
                distance = min(distance, abs(index_word1 - index_word2))
            i += 1
        return distance