# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        middle = (0 + len(nums) - 1) // 2
        node = TreeNode(nums[middle])
        node.left = self.sortedArrayToBST(nums[:middle])
        node.right = self.sortedArrayToBST(nums[middle + 1:])
        return node
