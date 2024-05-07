# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(nums):
            if len(nums) == 0:
                return None
            
            maxVal = 0
            index = 0

            for i in range(len(nums)):
                if nums[i] > maxVal:
                    maxVal = nums[i]
                    index = i
            
            leftRoot = helper(nums[:index])
            rightRoot = helper(nums[index + 1:])

            return TreeNode(maxVal, leftRoot, rightRoot)

        return helper(nums)