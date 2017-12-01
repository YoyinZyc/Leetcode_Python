class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 要sort的array的开始坐标
        begin = -1
        # 要sort的array的结束坐标
        end = 0
        i = 1
        # 要sort的array中的最小值
        min_before = nums[0]
        # array中的最大值
        max_before = nums[0]
        while i < len(nums):
            # 如果比最大值大，说明不需要sort，改变max
            if nums[i] >= max_before:
                max_before = nums[i]
            # 如果比最大值小，说明要sort
            else:
                # 改变end
                end = i
                # 如果begin=-1说明这是第一次遇见要sort的地方，挪动begin直至begin的值比nums[i]大；改变min
                if begin == -1:
                    begin += 1
                    while nums[begin] <= nums[i]:
                        begin += 1
                    min_before = nums[i]
                # 如果不是第一次，当当前值比min小的时候，说明begin还要左移，移begin改min
                else:
                    if nums[i] < min_before:
                        while begin >= 0 and nums[begin] > nums[i]:
                            begin -= 1
                        begin += 1
                        min_before = nums[i]
            i += 1
        # 返回的时候要判断begin是不是等于-1，如果是说明原本就是递增数列，返回0，不是返回end-begin+1
        return end - begin + 1 if begin != -1 else 0



