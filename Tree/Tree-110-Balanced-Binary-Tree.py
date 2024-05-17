# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        subHeights = dict()

        def findHeights(root):
            if not root:
                return 0
            
            leftHeight = findHeights(root.left)
            rightHeight = findHeights(root.right)

            subHeights[root] = {
                "left": leftHeight,
                "right": rightHeight
            }

            return 1 + max(leftHeight, rightHeight)
        
        def helper(root):
            if not root:
                return True
            
            if subHeights[root]["left"] == 0 and subHeights[root]["right"] == 0:
                return True

            return (abs(subHeights[root]["left"] - subHeights[root]["right"]) <= 1 and
                    helper(root.left) and
                    helper(root.right))
        
        findHeights(root)

        return helper(root)