class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if s[0] == '0':
            return 0
        # prev of prev
        a = 1
        #       prev
        b = 1
        i = 1
        while i < len(s):
            # 如果当前是0，则前一个必须是1或者2，否则返回0
            if s[i] == '0':
                if s[i - 1] == '1' or s[i - 1] == '2':
                    b, a = a, b
                else:
                    return 0
            else:
                if 11 <= int(s[i - 1] + s[i]) <= 26:
                    b, a = a + b, b
                else:
                    a, b = b, b
            i += 1
        return b

