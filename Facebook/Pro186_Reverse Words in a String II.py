class Solution:
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        # 先把整个str翻转
        self.reverse(str, 0, len(str) - 1)
        i = 0
        j = 0
        # 再把每个单词翻转
        while i < len(str):
            if str[i] == ' ':
                self.reverse(str, j, i - 1)
                j = i + 1
            i += 1
        # 最后还要翻转了最后一个word
        self.reverse(str, j, i - 1)

    def reverse(self, str, i, j):
        while i < j:
            str[i], str[j] = str[j], str[i]
            i += 1
            j -= 1
