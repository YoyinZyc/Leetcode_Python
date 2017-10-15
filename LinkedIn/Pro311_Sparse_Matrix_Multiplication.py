'''
LinkedIn_Medium
10.11 8:57pm
'''
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        B = zip(*B)
        ret = [[0 for _ in range(len(B))] for _ in range(len(A))]
        # print(ret)
        for i, l1 in enumerate(A):
            if not l1.count(0) == len(l1):
                for j, l2 in enumerate(B):

                    if not l2.count(0) == len(l2):

                        for k in range(len(l1)):
                            # print(i)
                            ret[i][j] += (l1[k] * l2[k])

        return ret
