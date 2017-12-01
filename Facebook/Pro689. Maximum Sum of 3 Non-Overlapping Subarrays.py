'''
Facebook_Hard
11.9 11:39am
'''
from collections import deque

# 方法一
class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # Best single, double, and triple sequence found so far
        bestSeq = 0
        bestTwoSeq = [0, k]
        bestThreeSeq = [0, k, k * 2]

        # Sums of each window
        seqSum = sum(nums[0:k])
        seqTwoSum = sum(nums[k:k * 2])
        seqThreeSum = sum(nums[k * 2:k * 3])

        # Sums of combined best windows
        bestSeqSum = seqSum
        bestTwoSum = seqSum + seqTwoSum
        bestThreeSum = seqSum + seqTwoSum + seqThreeSum

        # Current window positions
        seqIndex = 1
        twoSeqIndex = k + 1
        threeSeqIndex = k * 2 + 1
        while threeSeqIndex <= len(nums) - k:
            # Update the three sliding windows
            seqSum = seqSum - nums[seqIndex - 1] + nums[seqIndex + k - 1]
            seqTwoSum = seqTwoSum - nums[twoSeqIndex - 1] + nums[twoSeqIndex + k - 1]
            seqThreeSum = seqThreeSum - nums[threeSeqIndex - 1] + nums[threeSeqIndex + k - 1]

            # Update best single window
            if seqSum > bestSeqSum:
                bestSeq = seqIndex
                bestSeqSum = seqSum

            # Update best two windows
            # 只有当两个加起来比之前大的时候才改变，不用担心重合
            if seqTwoSum + bestSeqSum > bestTwoSum:
                bestTwoSeq = [bestSeq, twoSeqIndex]
                bestTwoSum = seqTwoSum + bestSeqSum

            # Update best three windows
            if seqThreeSum + bestTwoSum > bestThreeSum:
                bestThreeSeq = bestTwoSeq + [threeSeqIndex]
                bestThreeSum = seqThreeSum + bestTwoSum

            # Update the current positions
            seqIndex += 1
            twoSeqIndex += 1
            threeSeqIndex += 1

        return bestThreeSeq
if __name__ == '__main__':
    s = Solution()
    s.maxSumOfThreeSubarrays([1,2,3,4,8,9,2,7,1,5],3)

# 方法2
class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        sum_l = []
        sum_l.append(sum(nums[:k]))
        for i in range(1, len(nums) - k + 1):
            sum_l.append(sum_l[-1] - nums[i - 1] + nums[i + k - 1])
        record = deque()
        last_record = [0, -1, 0, [-1, -1], 0, [-1, -1, -1]]
        for i in range(len(sum_l)):
            new_record = [v for v in last_record]
            if sum_l[i] > last_record[0]:
                new_record[0] = sum_l[i]
                new_record[1] = i
            if i >= k:
                prev = record.popleft()
                if last_record[2] < prev[0] + sum_l[i]:
                    new_record[2] = prev[0] + sum_l[i]
                    new_record[3] = [prev[1], i]
                if i >= 2 * k:
                    if last_record[4] < prev[2] + sum_l[i]:
                        new_record[4] = prev[2] + sum_l[i]
                        new_record[5] = [prev[3][0], prev[3][1], i]
            last_record = new_record
            record.append(new_record)
        return record[-1][-1]