'''
不能连续偷两家

DP

'''
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        robPrev = 0
        jumpPrev = 0
        for i in range(len(nums)):
            robPrev, jumpPrev = jumpPrev + nums[i], max(robPrev,jumpPrev)
        return max(robPrev, jumpPrev)
'''
Follow up2:
环状房间
分rob第一间房和不rob两种情况
'''
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def helper(nums):
            robPrev = 0
            jumpPrev = 0
            for i in range(len(nums)):
                robPrev, jumpPrev = jumpPrev + nums[i], max(robPrev,jumpPrev)
            return max(robPrev, jumpPrev)
        if not nums:
            return 0
        return max(nums[0] + helper(nums[2:-1]), helper(nums[1:]))

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
Follow-up2:
二叉树
这个是DFS，不是DP
'''
class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node):
            if not node:
                return (0,0)
            left = helper(node.left)
            right = helper(node.right)
            return (max(left)+max(right), node.val + left[0] + right[0])
        return max(helper(root))
if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    s.rob(root)