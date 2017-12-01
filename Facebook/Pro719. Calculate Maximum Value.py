class Solution:
    """
    @param: : the given string
    @return: the maximum value
    """

    def calcMaxValue(self, str):
        # write your code here
        if not str:
            return 0
        res = int(str[0])
        i = 1
        while i < len(str):
            if str[i] == '0' or str[i] == '1' or res <= 1:
                res += int(str[i])
            else:
                res *= int(str[i])
            i+=1
        return res