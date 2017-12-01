class Solution(object):
    # 方法一：先reverse，然后遇见空格判断有没有cache的word，如果没有就跳过，如果有就把word放进返回的str中
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        s = s[::-1]
        s += ' '
        word = ''
        ret= ''
        i = 0
        j = 0
        while i < len(s):
            if s[i] == ' ' and word != '':
                ret += (word + ' ')
                word = ''
            elif s[i] != ' ':
                # 每次给word中添加字符是逆向添加的
                word = s[i]+word
            i+=1
        return ret[:-1] if ret != '' else ''
    # 方法二：直接用split，然后reverse list，然后join
    def reverseWords(self, s):
        r = s.split()
        r = list(reversed(r))
        return " ".join(r)