'''
Facebook_Hard
11.05 4:56pm
'''
class Solution:
    '''
    //num：原始string；
target: 原始target
mul_v: 如果下一个是*，前一个的用于*的值
temp_v: 当前expression 的值
temp_v: 当前expression
Ans: 返回数组
start_i: 当前的I
    '''
    def helper(self, num, target, mul_v, temp_v, temp_e, ans, start_i):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        ret = []
        if start_i == len(num):
            if temp_v == target:
                ans.add(temp_e)
            return

        for i in range(start_i, len(num)):
            #             '000001'只有第一个0判断
            if i != start_i and num[start_i] == '0':
                break
            val = int(num[start_i:i + 1])
            if not start_i:
                self.helper(num, target, val, temp_v + val, temp_e + str(val), ans, i + 1)
            else:
                self.helper(num, target, val, temp_v + val, temp_e + '+' + str(val), ans, i + 1)
                self.helper(num, target, 0 - val, temp_v - val, temp_e + '-' + str(val), ans, i + 1)
                self.helper(num, target, mul_v * val, (temp_v - mul_v) + mul_v * val, temp_e + '*' + str(val), ans,
                            i + 1)

    def addOperators(self, num, target):
        ans = set()
        self.helper(num, target, 1, 0, '', ans, 0)
        return list(ans)