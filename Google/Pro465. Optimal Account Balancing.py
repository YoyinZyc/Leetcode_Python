'''
题意：
类似于Splitwise

重点在于构建debit表
时间复杂度O（n！）
'''
class Solution(object):
    def minTransfers(self, transactions):
        # Compute net profit for every person.
        # 构建一个表，记录每个人现在的balance，
        personNetProfit = dict()
        for lender, borrower, amount in transactions:
            personNetProfit[lender] = personNetProfit.get(lender, 0) - amount
            personNetProfit[borrower] = personNetProfit.get(borrower, 0) + amount
        # Preserve unsettled people only.
        netProfit = []
        # 把不是0的人的加进去
        for amount in personNetProfit.values():
            if amount != 0:
                netProfit.append(amount)
        return self.traverse(netProfit, 0, 0)

    def traverse(self, netProfit, startIdx, numTrans):
        # Skip settled people.
        while startIdx < len(netProfit) and netProfit[startIdx] == 0:
            startIdx += 1
        if startIdx + 1 >= len(netProfit):
            return numTrans
        else:
            # 尝试去找正好相等的人，这样就不用递归了
            for i in range(startIdx + 1, len(netProfit)):
                # Greedy condition.
                if netProfit[startIdx] + netProfit[i] == 0:
                    netProfit[i] += netProfit[startIdx]
                    minNumTrans = self.traverse(netProfit, startIdx + 1, numTrans + 1)
                    netProfit[i] -= netProfit[startIdx]
                    return minNumTrans
            minNumTrans = sys.maxint
            # 否则还是要backtracking，每一个都要去试
            for i in range(startIdx + 1, len(netProfit)):
                # Non-greedy condition for possible closing out in the future.
                if netProfit[startIdx] * netProfit[i] < 0:
                    netProfit[i] += netProfit[startIdx]
                    minNumTrans = min(minNumTrans, self.traverse(netProfit, startIdx + 1, numTrans + 1))
                    # 回复之前的状态
                    netProfit[i] -= netProfit[startIdx]
            return minNumTrans