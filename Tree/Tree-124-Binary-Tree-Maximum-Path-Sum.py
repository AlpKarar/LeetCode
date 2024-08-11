# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        cur_max = [-1001]

        def helper(root):
            if not root:
                return 0
            
            left = helper(root.left)
            right = helper(root.right)
            cur = cur_max[0]

            if max(left, right) + root.val > cur:
                cur = max(left, right) + root.val
            
            if left + right + root.val > cur:
                cur = left + right + root.val

            if root.val > cur:
                cur = root.val

            cur_max[0] = cur
            
            if left < 0 and right < 0:
                return root.val
            
            return max(left, right) + root.val
        
        res = helper(root)

        return cur_max[0] if res < cur_max[0] else res