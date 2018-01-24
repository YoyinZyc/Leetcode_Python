'''
题意：
给出key的个数，要求找到手机屏幕解锁的方式的个数
Each pattern must connect at least m keys and at most n
注意：If the line connecting two consecutive keys in the pattern passes through
any other keys, the other keys must have previously selected in the pattern.
No jumps through non selected key is allowed.
'''

class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 关于jump
        pass_record = {(1, 3): 2, (3, 1): 2, (1, 9): 5, (9, 1): 5, (1, 7): 4, (7, 1): 4, (3, 7): 5, (7, 3): 5,
                       (3, 9): 6, (9, 3): 6, (7, 9): 8, (9, 7): 8, (2, 8): 5, (8, 2): 5, (4, 6): 5, (6, 4): 5}
        record = [0 for i in range(n)]
        record[0] = 9

        def helper(path):
            if len(path) == n:
                return
            for v in range(1, 10):
                if v not in path:
                    if not ((path[-1], v) in pass_record and pass_record[(path[-1], v)] not in path):
                        # 相关的record递增
                        record[len(path)] += 1
                        helper(path + [v])

        for i in range(9):
            helper([i + 1])
        # sum m-n的那部分
        return sum(record[m - 1:n])
