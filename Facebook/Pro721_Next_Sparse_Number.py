class Solution:
    """
    @param: : a number
    @return: return the next sparse number behind x
    """

    def nextSparseNum(self, x):
        # write your code here
        binstr = str(bin(x))[2:]
        i = len(binstr)-1
        while i >= 0:
            if binstr[i] == '1':
                j = i
                while j >= 0 and binstr[j] == '1':
                    j-=1
                if j != i-1:
                    if j == -1:
                        return int('1' + len(binstr) * '0', 2)
                    binstr = binstr[:j] + '1' + (len(binstr)-j-1) * '0'
                i = j
            else:
                i-=1
        return int(binstr,2)