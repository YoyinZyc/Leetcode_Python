'''
s1，s2
判断s2中是否包含s1的各种permutation

思路：
滑动窗口
'''
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # 记录是s1的情况
        record = dict()
        for v in s1:
            record[v] = record.get(v, 0) + 1
        i = 0
        j = 0
        while i < len(s2):
            # 如果v在record中且record[v]>0
            if s2[i] in record and record[s2[i]]:
                record[s2[i]] -= 1
                i += 1
                # 判断是否全覆盖
                if i - j == len(s1):
                    return True
            # 如果v不在record中，移动j到i
            elif s2[i] not in record:
                while j < i:
                    record[s2[j]] += 1
                    j += 1
                i += 1
                j = i
            # 如果record[v] = 0, 移动j到record[v] > 0; i不变
            elif not record[s2[i]]:
                while j < i and not record[s2[i]]:
                    record[s2[j]] += 1
                    j += 1

        return False