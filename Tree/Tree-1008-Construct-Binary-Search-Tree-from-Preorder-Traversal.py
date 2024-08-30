# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def helper(root, val):
            if not root:
                return TreeNode(val)
            
            if root.val > val:
                root.left = helper(root.left, val)
            else:
                root.right = helper(root.right, val)
            
            return root
        
        root = helper(None, preorder[0])

        for i in range(1, len(preorder)):
            helper(root, preorder[i])
        
        return root