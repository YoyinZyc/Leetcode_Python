import heapq as hq
from collections import defaultdict
class Solution(object):
    def accountsMerge(self, accounts):
        # 记录有没有visit过这个account
        visited_accounts = [False] * len(accounts)
        # account和email的map
        emails_accounts_map = defaultdict(list)
        res = []

        # Build up the graph. 定义map关系
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                emails_accounts_map[email].append(i)

        # DFS code for traversing accounts.
        def dfs(i, emails):
            if visited_accounts[i]:
                return
            visited_accounts[i] = True
            # 对account中的所有email遍历
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)
                # 递归
                for neighbor in emails_accounts_map[email]:
                    dfs(neighbor, emails)

        # Perform DFS for accounts and add to results.
        for i, account in enumerate(accounts):
            if visited_accounts[i]:
                continue
            name, emails = account[0], set()
            dfs(i, emails)
            res.append([name] + sorted(emails))
        return res


if __name__ == '__main__':
    s = Solution()
    s.accountsMerge([["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]])