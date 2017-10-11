'''
BitManipulation_Easy
10.10 9:19pm
'''
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        reverse_d = {'0': 'f', '1': 'e', '2': 'd', '3': 'c', '4': 'b', '5': 'a', '6': '9', '7': '8', '8': '7', '9': '6',
                     'a': '5', 'b': '4', 'c': '3', 'd': '2', 'e': '1', 'f': '0'}
        if num >= 0:
            return self.helper(num)
        else:
            ret = self.helper(-num - 1).zfill(8)
            return ''.join([reverse_d[v] for v in ret])

    def helper(self, num):
        ret = ""
        while num > 0:
            n = num % 16
            if n >= 10:
                ret = str(chr(ord('a') + n - 10)) + ret
            else:
                ret = str(n) + ret
            num = num // 16
        return ret


