# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []

        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            nodes.append(root)
            inorder(root.right)

        def helper(start, end):
            if start > end:
                return None
            
            m = start + (end - start) // 2
            curNode = nodes[m]
            curNode.left = helper(start, m - 1)
            curNode.right = helper(m + 1, end)

            return curNode
        
        inorder(root)
        
        return helper(0, len(nodes) - 1)