'''
题意：
删去string中的重复字符，且使得String的字典序最小
'''
from collections import deque


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 记录string中每个字符出现的次数
        count = [0 for i in range(26)]
        # 记录这个字符是否在stack中
        visit = [False for i in range(26)]
        # 更新count
        for v in s:
            count[ord(v) - ord('a')] += 1
        stack = deque()


        for v in s:
            # count和visit中的指针
            i = ord(v) - ord('a')
            # 因为到了这个字符，所以把这个字符的count-1
            count[i] -= 1
            # 如果这个字符已经在栈中，则continue；因为为了字典序最小，相同的字符保留最左边的
            if visit[i]:
                continue
            # 当栈不为空且栈顶比当前字符大且栈顶的那个字符在当前位置之后还有，即不是最后一个
            while stack and ord(stack[-1]) > ord(v) and count[ord(stack[-1]) - ord('a')] > 0:
                # 把栈顶弹出，visit设置为false
                visit[ord(stack[-1]) - ord('a')] = False
                stack.pop()
            # 入栈
            stack.append(v)
            # visit为True
            visit[i] = True
        # 把栈中的字符join起来
        return ''.join(list(stack))


if __name__ == '__main__':
    s = Solution()
    s.removeDuplicateLetters("edebbed")