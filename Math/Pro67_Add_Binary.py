'''
Math_Easy
9.17 10:43pm
'''


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ret=''
        n = 0
        i = -1
        while(i >= 0-len(a) and i >= 0-len(b)):
            add = int(a[i])+int(b[i])+n
            if add == 3:
                ret = '1'+ret
                n = 1
            elif add == 2:
                ret = '0'+ret
                n = 1
            elif add == 1:
                ret = '1'+ret
                n = 0
            else:
                ret = '0'+ret
                n = 0
            i-=1
        if len(a) == len(b):
            if n == 1:
                ret = '1'+ret
        elif len(a) > len(b):
            if n == 1:
                while i >= 0-len(a):
                    add = n+int(a[i])
                    if add == 2:
                        ret = '0'+ret
                        n = 1
                    elif add == 1:
                        ret = '1' + ret
                        n = 0
                    else:
                        ret = '0'+ret
                        n = 0
                    i-=1
                if n==1:
                    ret='1'+ret
            else:
                ret = a[:i+1]+ret
        else:
            if n == 1:
                while i >= 0-len(b):
                    add = n+int(b[i])
                    if add == 2:
                        ret = '0'+ret
                        n = 1
                    elif add == 1:
                        ret = '1' + ret
                        n = 0
                    else:
                        ret = '0'+ret
                        n = 0
                    i-=1
                if n==1:
                    ret='1'+ret

            else:
                ret = b[:i+1]+ret
        return ret