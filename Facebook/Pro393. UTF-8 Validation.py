'''
Facebook_Medium
11.06 10:54am
'''
class Solution:
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        count = 0
        for v in data:
            # print(v)
            if v >= 192:
                if count != 0:
                    return False
                elif v >= 248:
                    return False
                elif v >= 240:
                    count = 3
                elif v >= 224:
                    count = 2
                else:
                    count = 1
            elif v >= 128 :
                count -= 1
                # print(count)
                if count < 0:
                    return False
            elif count >0:
                return False
        return count == 0