'''
题意：有一个时间HH：MM；要求用之前时间里面出现的数字组成另一个时间，且这个时间在当前时间的后面，也可以是下一天
Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39,
which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.

Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.

'''
class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        hs = list()
        ms = list()
        l = list(time)
        l = list(set(l[:2] + l[3:]))
        # 排序时间中的数字；然后排列组合肯定就是从小到大了且没有重复
        l.sort()
        h = int(time[:2])
        m = int(time[3:])

        for i in l:
            for j in l:
                t = int(i + j)
                if t < 24:
                    hs.append(t)
                if t < 60:
                    ms.append(t)

        if max(hs) <= h and max(ms) <= m:
            return str(min(hs)).zfill(2) + ':' + str(min(ms)).zfill(2)
        elif max(ms) <= m:
            # hs.sort()
            return str(hs[hs.index(h) + 1]).zfill(2) + ':' + str(min(ms)).zfill(2)
        else:
            # ms.sort()
            return str(h).zfill(2) + ':' + str(ms[ms.index(m) + 1]).zfill(2)

