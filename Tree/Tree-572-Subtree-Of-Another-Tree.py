# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def findSubRoot(root):
            if not root:
                return []
            
            cur = []

            if root.val == subRoot.val:
                cur.append(root)
            
            return findSubRoot(root.left) + findSubRoot(root.right) + cur
        
        def compareNodes(node1, node2):
            if not node1 and not node2:
                return True
            
            if not node1 or not node2:
                return False
            
            return (node1.val == node2.val
                    and compareNodes(node1.left, node2.left)
                    and compareNodes(node1.right, node2.right))

        candidate_subRoots = findSubRoot(root)

        for candidate_subRoot in candidate_subRoots:
            if compareNodes(subRoot, candidate_subRoot):
                return True
        
        return False