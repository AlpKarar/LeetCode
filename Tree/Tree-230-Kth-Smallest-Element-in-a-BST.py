# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = [0]
        
        def helper(root):
            if not root:
                return 0
            
            left = helper(root.left)
            res[0] += 1

            if res[0] == k:
                return root.val

            right = helper(root.right)

            return left or right

        return helper(root)