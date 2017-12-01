class Solution:
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        # 先判断a是不是0，如果是则按照b的正负就可以线性输出
        if a == 0:
            if b >= 0:
                return [b * v + c for v in nums]
            else:
                return [b * v + c for v in nums][::-1]
        # 最高点
        sigma = -b / (a * 2)
        begin = 0
        end = len(nums) - 1
        ret = []
        # 二项式搜索找到找到sigma介于哪两个数之间
        while begin <= end:
            mid = (begin + end) // 2
            if nums[mid] > sigma:
                end = mid - 1
            else:
                begin = mid + 1
        # i是下届，j是上届
        i = end
        j = begin
        # 把数字加进ret
        while i >= 0 and j <= len(nums) - 1:
            if abs(sigma - nums[i]) > abs(sigma - nums[j]):
                ret.append(a * (nums[j] ** 2) + b * nums[j] + c)
                j += 1
            else:
                ret.append(a * (nums[i] ** 2) + b * nums[i] + c)
                i -= 1
        while i >= 0:
            ret.append(a * (nums[i] ** 2) + b * nums[i] + c)
            i -= 1
        while j <= len(nums) - 1:
            ret.append(a * (nums[j] ** 2) + b * nums[j] + c)
            j += 1
        # 如果a小于0，说明要reverse ret
        if a < 0:
            return ret[::-1]
        return ret




