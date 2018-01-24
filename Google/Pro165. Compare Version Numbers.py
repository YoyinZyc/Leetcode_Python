'''
对比version no
可能有1.0.0.0和1.0对比的情况
'''
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        # split & 转换为int
        v1 = map(int, version1.split('.'))
        v2 = map(int, version2.split('.'))
        i = 0
        # 按位对比大小
        while i < len(v1) and i < len(v2):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
            i += 1
        # 如果长度一样，返回0
        if i == len(v1) and i == len(v2):
            return 0
        # 如果v2长
        elif i == len(v1):
            # 如果v2剩下都是0，返回0
            if not any(v2[i:]):
                return 0
            # 否则v2>v1,返回-1
            return -1
        # 同理v1
        else:
            if not any(v1[i:]):
                return 0
            return 1