'''
Facebook_Hard
11.06 5:15pm
'''
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        if s.isspace():
            return False
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        j = len(s) - 1
        while j >= 0 and s[j] == ' ':
            j -= 1
        if s[i] == '+' or s[i] == '-':
            print(4)
            return self.helper(s[1 + i:j + 1])

        return self.helper(s[i:j + 1])

    def helper(self, s):
        if s == '.':
            return False
        has_e = False
        has_dot = False
        has_opt = False
        has_n_befor_e = False
        for i in range(len(s)):
            if s[i] == ' ':
                return False
            elif s[i] == '.':
                if has_dot:
                    return False
                else:
                    has_dot = True
            elif s[i] == '+' or s[i] == '-':
                if not has_e or has_opt:
                    return False
                has_opt = True
            elif s[i] == 'e':
                if has_e:
                    return False
                if not s[i + 1:]:
                    return False
                if s[i + 1] == '+' or s[i + 1] == '-':
                    return s[i + 2:].isdigit() and has_n_befor_e
                return s[i + 1:].isdigit() and has_n_befor_e
            elif not s[i].isdigit():
                return False
            else:
                has_n_befor_e = True
        return True
