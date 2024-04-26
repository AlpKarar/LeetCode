# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        def helper(root, target, curDepth, parent):
            if not root:
                return (0, None)
            
            if root.val == target:
                return (curDepth, parent)

            leftSide = helper(root.left, target, curDepth + 1, root)
            rightSide = helper(root.right, target, curDepth + 1, root)
            
            if leftSide[0] > rightSide[0]:
                return leftSide
            
            return rightSide
        
        first = helper(root, x, 0, root)
        second = helper(root, y, 0, root)

        return first[0] == second[0] and first[0] > 1 and first[1] != second[1]