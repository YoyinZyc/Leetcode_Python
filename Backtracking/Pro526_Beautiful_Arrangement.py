#Medium
#9.12 2:19

class Solution(object):
    count = 0;
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        l = []
        for i in range(N):
            l.append(i+1)
        self.helper(l, 1, N)
        return self.count
    def helper(self, l, index, N):
        if index == N+1:
            self.count+=1
        for i in range(len(l)):
            if l[i] % index == 0 or index % l[i] == 0:
                temp = l[i]
                l.remove(temp)
                self.helper(l, index+1, N)
                l.insert(i, temp)
