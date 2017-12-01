class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        left_max = 0
        right_max = 0
        result = 0
        while left<right:
            if height[left] < height[right]:
                if height[left] < left_max:
                    result += left_max-height[left]
                left_max = max(left_max,height[left])
                left+=1
            else:
                if height[right] < right_max:
                    result += right_max-height[right]
                right_max = max(right_max,height[right])
                right-=1
        return result