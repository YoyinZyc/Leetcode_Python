'''
Facebook_Easy
11.4 11:47
'''
class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return self.helper(s, False)

    def helper(self, s, delete):
        if not s:
            return True
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                if delete:
                    return False
                else:
                    if j - i == 1:
                        return True
                    else:

                        if s[i + 1] == s[j] and s[i] == s[j - 1]:
                            return self.helper(s[i + 2:j], True) or self.helper(s[i + 1:j - 1], True)
                        elif s[i] == s[j - 1]:
                            j -= 1
                            delete = True
                        elif s[i + 1] == s[j]:
                            i += 1
                            delete = True
                        else:
                            return False
            else:
                i += 1
                j -= 1
        return True
