# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        def helper(root):
            if not root:
                return []
            
            return helper(root.left) + [root.val] + helper(root.right)
        
        arr1 = helper(root1)
        arr2 = helper(root2)
        i = 0
        j = 0
        res = []

        while i < len(arr1) and j < len(arr2):
            if arr1[i] > arr2[j]:
                res.append(arr2[j])
                j += 1
            else:
                res.append(arr1[i])
                i += 1
        
        while i < len(arr1):
            res.append(arr1[i])
            i += 1
        
        while j < len(arr2):
            res.append(arr2[j])
            j += 1
        
        return res