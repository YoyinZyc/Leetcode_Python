'''
Facebook_Easy
11.05 11:05pm
'''
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not num1:
            return num2
        if not num2:
            return num1

        ret = ''
        i = -1
        j = -1
        carrying = 0
        while i > -1 - len(num1) and j > -1 - len(num2):
            s = int(num1[i]) + int(num2[j]) + carrying
            ret = str(s % 10) + ret
            carrying = s // 10
            i -= 1
            j -= 1
        if i == -1 - len(num1) and j == -1 - len(num2):
            if carrying:
                return '1' + ret
            else:
                return ret
        elif i == -1 - len(num1):
            while j > -1 - len(num2):
                if not carrying:
                    return num2[:j + 1] + ret
                s = int(num2[j]) + carrying
                ret = str(s % 10) + ret
                carrying = s // 10

                j -= 1
        else:
            while i > -1 - len(num1):
                if not carrying:
                    return num1[:i + 1] + ret
                s = int(num1[i]) + carrying
                ret = str(s % 10) + ret
                carrying = s // 10

                i -= 1

        if carrying:
            return '1' + ret
        else:
            return ret