# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        queue = [(root, 1)]
        tempLevel = 1
        tempSum = 0
        mx = -sys.maxsize - 1
        res = 0

        while queue:
            node, level = queue.pop(0)

            if level > tempLevel:
                if tempSum > mx:
                    mx = tempSum
                    res = tempLevel

                tempLevel = level
                tempSum = 0
            
            tempSum += node.val
            
            if node.left:
                queue.append((node.left, level + 1))
            
            if node.right:
                queue.append((node.right, level + 1))
        
        if tempSum > mx:
            mx = tempSum
            res = tempLevel

        return res