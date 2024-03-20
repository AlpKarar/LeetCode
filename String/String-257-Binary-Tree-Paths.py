# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []

        def helper(cur, curStr):
            if not cur:
                return
            
            if not cur.left and not cur.right:
                curStr += str(cur.val)
                result.append(curStr)
                return

            curStr += str(cur.val) + "->"

            helper(cur.left, curStr)
            helper(cur.right, curStr)

        helper(root, "")

        return result
    
# Beats 60.94%