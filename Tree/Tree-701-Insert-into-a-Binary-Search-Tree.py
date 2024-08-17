# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def helper(root, val):
            if not root:
                return TreeNode(val)

            if root.val > val:
                if root.left:
                    helper(root.left, val)
                else:
                    root.left = TreeNode(val)
            else:
                if root.right:
                    helper(root.right, val)
                else:
                    root.right = TreeNode(val)
            
            return root

        return helper(root, val)