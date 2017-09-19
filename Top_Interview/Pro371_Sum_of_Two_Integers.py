'''
Top_Interview_Easy
9.18 4:58pm
'''


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        a =str(bin(a))
        b = str(bin(b))
        if a[0] != '-':
            a = '0'*(34-len(a))+a[2:]

        else:
            a = self.reverse('0'*(35-len(a))+a[3:])
        if b[0] != '-':
            b = '0'*(34-len(b))+b[2:]
        else:
            b = self.reverse('1'*(35-len(b))+b[3:])

        print(a)
        print(b)
        sum = self.add(a,b)
        print(sum)
        if sum[0] == '1':

            return int('-'+self.reversed(sum),2)
        else:
            return int(sum, 2)

    def add(self, a, b):
        i = 0
        index = 0
        sum = ''
        while i < 32:
            if a[-1-i] == '0' and b[-1-i] == '0':
                if index == 1:
                    sum = '1'+sum
                    index = 0
                else:
                    sum = '0' + sum
            elif a[-1-i] == '1' and b[-1-i] == '1':
                if index == 1:
                    sum = '1'+sum
                    index = 1
                else:
                    sum = '0' + sum
                    index = 1
            else:
                if index == 1:
                    sum = '0'+sum
                    index = 1
                else:
                    sum = '1' + sum
            i+=1
        return sum

    def reverse(self, a):
        reverse = ''
        for i in range(32):
            if a[i] == '0':
                reverse += '1'
            else:
                reverse += '0'
        return self.add(reverse,'0'*31+'1')