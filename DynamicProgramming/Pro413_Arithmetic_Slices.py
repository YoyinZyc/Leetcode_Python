'''
DP_Medium
9.21 10:24am
'''

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        sub = A[1]-A[0]
        count = 1
        i = 2
        ret = 0
        while i < len(A):
            if A[i]-A[i-1] == sub:
                count+=1
            else:
                sub = A[i]-A[i-1]
                if count >= 2:
                    ret += (count*(count-1)) / 2
                count = 1
            i+=1
        if count >= 2:
            ret += (count * (count-1))/2
        return ret
