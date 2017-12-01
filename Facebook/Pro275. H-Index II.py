class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        left = 0
        right = len(citations) - 1
        length = len(citations)
        while left <= right:
            mid = (left + right) // 2
            if citations[mid] == length - mid:
                return length - mid
            if citations[mid] > length - mid:
                right = mid - 1
            elif citations[mid] < length - mid:
                left = mid + 1
        return length - left
