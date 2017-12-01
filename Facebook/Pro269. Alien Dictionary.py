from collections import deque
class Solution:
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if not words:
            return ''
        if len(words) == 1:
            return words[0]
        # after：记录所有在这个letter后面的letter
        d1 = {}
        # before：记录所有在这个letter前面的letter
        d2 = {}
        q = deque()
        i = 0
        # 记录一共有多少个word
        letter_num = 0
        while i < len(words):
            # 对于第一个word，不需要比较，直接把word加入d1，d2
            if i == 0:
                for v in words[i]:
                    if v not in d1:
                        d1[v] = set()
                        letter_num += 1
                    if v not in d2:
                        d2[v] = set()
            else:
                j = 0
                # 循环长度选择words[i]words[i-1]中小的那一个
                while j < len(words[i - 1]) and j < len(words[i]):
                    if words[i][j] != words[i - 1][j]:
                        # 更新上一个word的after
                        d1[words[i - 1][j]].add(words[i][j])
                        # 当前letter不在d1，d2中，加入
                        if words[i][j] not in d1:
                            d1[words[i][j]] = set()
                            letter_num += 1
                        if words[i][j] not in d2:
                            d2[words[i][j]] = set()
                        # 更新当前word的before
                        d2[words[i][j]].add(words[i - 1][j])
                        break
                    j += 1
                # 把剩下的letter加入
                while j < len(words[i]):
                    if words[i][j] not in d1:
                        d1[words[i][j]] = set()
                        letter_num += 1
                    if words[i][j] not in d2:
                        d2[words[i][j]] = set()
                    j += 1
            i += 1
        # 把所有没有before的letter入队列
        for k in d2.keys():
            if not d2[k]:
                q.append(k)
        ans = ''
        while q:
            ans += q.popleft()
            after = d1[ans[-1]]
            for v in after:
                d2[v].remove(ans[-1])
                if not d2[v]:
                    q.append(v)
        # 当q为空了，且所有letter都进入了ans，然后ans，否则就是有环，返回空
        if letter_num == len(ans):
            return ans
        return ''