# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return -1
        
        res = [float("inf"), float("inf")]

        def helper(root):
            if not root:
                return
            
            if root.val < res[0]:
                res[1] = res[0]
                res[0] = root.val
            elif root.val < res[1] and root.val != res[0]:
                res[1] = root.val
            
            helper(root.left)
            helper(root.right)
        
        helper(root)

        if res[1] == float("inf"):
            return -1

        print(res)
        return res[1]