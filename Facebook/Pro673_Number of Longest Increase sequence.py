class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        # record中记录到当前点，最长的subsequence的长度以及个数，首位肯定为(1,1)
        record = [(1, 1)]
        # 最长的subsequence的长度
        max_l = 1
        i = 1
        while i < len(nums):
            j = i - 1
            # 记录最长的length
            max_len = 1
            # 记录个数
            max_count = 1
            while j >= 0:
                if nums[i] > nums[j]:
                    if record[j][0] + 1 > max_len:
                        max_len = record[j][0] + 1
                        max_count = record[j][1]
                    elif record[j][0] + 1 == max_len:
                        max_count += record[j][1]
                j -= 1
            # 更新max_L
            max_l = max(max_len, max_l)
            record.append((max_len, max_count))
            i += 1
        # 把record中所有v[0] = max_l的sequencde的长度加起来，返回count
        count = 0
        for v in record:
            if v[0] == max_l:
                count += v[1]
        return count

