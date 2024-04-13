# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        nums = []

        def helper(root):
            if not root:
                return
            
            nums.append(root.val)
            
            helper(root.left)
            helper(root.right)
        
        helper(root)
        nums = sorted(nums)
        diff = []

        for i in range(1, len(nums)):
            diff.append(nums[i] - nums[i-1])
        
        return sorted(diff)[0]