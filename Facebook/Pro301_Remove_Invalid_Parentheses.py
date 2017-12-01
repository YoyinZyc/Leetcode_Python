'''
Facebook_Hard
11.3 3:35pm
'''
from collections import deque
class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        self.helper(ans, s, 0, 0, ['(', ')'])
        return ans

    def helper(self, ans, s, start_i, start_j, pair):
        print(s)
        count = 0
        for i in range(start_i, len(s)):
            if s[i] == pair[0]:
                count += 1
            elif s[i] == pair[1]:
                count -= 1
            if count >= 0:
                continue
            for j in range(start_j, i + 1):
                if s[j] == pair[1] and (j == start_j or s[j - 1] != pair[1]):
                    if j == 0:
                        new_s = s[1:]
                    else:
                        new_s = s[0:j] + s[j + 1:]
                    self.helper(ans, new_s, i, j, pair)
            return

        s = s[::-1]
        if pair[0] == '(':
            self.helper(ans, s, 0, 0, [')', '('])
        else:
            ans.append(s)

    def follow_up(self, s):
        count = 0
        i = 0
        # left -> right
        while i < len(s):
            if s[i] == '(':
                count += 1
            elif s[i] == ')':
                count -= 1
            if count >= 0:
                i+=1
            else:
                if i == 0:
                    s = s[1:]
                else:
                    s = s[0:i]+s[i+1:]
                count = 0
        if count == 0:
            return s
        # right->left
        if count > 0:
            count = 0
            s = s[::-1]
            i = 0
            while i <len(s):
                if s[i] == ')':
                    count += 1
                elif s[i] == '(':
                    count -= 1
                if count >= 0:
                    i += 1
                else:

                    if i == 0:
                        s = s[1:]
                    else:
                        s = s[0:i] + s[i + 1:]
                    count = 0
        return s[::-1]
    # one pass, use stack to store the index
    def follow2(self, s):
        q = deque()
        for i in range(len(s)):
            if s[i] == '(':
                q.append(i)
            elif s[i] == ')':
                while q:
                    if s[q[-1]] == ')' or s[q[-1]] == '(':
                        break
                    else:
                        q.pop()
                if not q:
                    q.append(i)

                if s[q[-1]] == ')':
                    q.append(i)
                else:
                    q.pop()
        ret = ''
        last_i = 0
        for v in q:
            if v == 0:
                continue
            ret += s[last_i:v]
            last_i = v+1
        return ret

if __name__ == '__main__':
    s = Solution()
    print(s.removeInvalidParentheses("())(()"))