from collections import deque


class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stack = deque()
        ans = [0 for _ in range(n)]
        last_end = 0
        for v in logs:
            l = v.split(':')
            # 如果stack为空，则直接压入栈，并更新last_end
            if not stack:
                stack.append(int(l[0]))
                last_end = int(l[2])
                continue
            # 如果是start，则栈顶的时间加上当前开始的减去last，并更新last，压入栈
            if l[1] == 'start':
                ans[stack[-1]] += int(l[2]) - last_end
                last_end = int(l[2])
                stack.append(int(l[0]))
            # 如果是end，则栈顶的时间加上当前开始的减去last然后+1，pop出栈顶，更新last为当前时间+1
            else:
                ans[stack.pop()] += int(l[2]) - last_end + 1
                last_end = int(l[2]) + 1
        return ans
