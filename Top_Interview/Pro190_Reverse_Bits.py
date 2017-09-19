'''
Top_Interview_Easy
9.18 3:50pm
'''


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = str(bin(n))
        n = '0'*(34-len(n))+n[2:]
        v = 0
        # print(n)
        for i in range(len(n)):
            if n[i] == '1':
                v+=pow(2,i)
        return v