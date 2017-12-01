class Solution:
    """
    @param: : a number
    @param: : digit needed to be rorated
    @return: a number
    """

    def leftRotate(self, n, d):
        # write code here
        binstr = str(bin(n))[2:].zfill(32)
        d = d%32
        binstr = binstr[d:]+binstr[:d]
        return int(binstr,2)