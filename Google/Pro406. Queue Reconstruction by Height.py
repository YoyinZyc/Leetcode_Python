'''
题意：
Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
给了一堆人
(x,y): x是身高，y是x前面有几个人
排序
时间复杂度应该都是n^2
'''

'''
思路1：先排序，然后插入
'''
class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort()
        ret = [0 for _ in range(len(people))]
        for v in people:
            count = 0
            i = 0
            # 遇到空位和大于自己的+1，直到等于v[1]
            while i < len(people) and count < v[1]:
                if not ret[i] or ret[i][0] >= v[0]:
                    count += 1
                i += 1
            # 找到下一个空位，插入
            while i < len(people) and ret[i]:
                i += 1
            ret[i] = v
        return ret

'''
思路2：
利用list的插入特性，
排序按照h降序，k升序，然后按顺序插入
Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

ex：为了让(5,0)在(7,0)后面插入
排序：
[[7,0], [7,1], [6,1], [5,0], [5,2], [4,4]]
'''
class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        for p in sorted(people, key=lambda x: (-x[0], x[1])):
            res.insert(p[1], p)
        return res


