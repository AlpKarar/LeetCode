# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = [root.val]
        queue = [(root, 0)]
        cur_level = 0

        while queue:
            cur, level = queue.pop(0)

            if level > cur_level:
                if cur:
                    res.append(cur.val)
                
                cur_level = level

            if cur.right:
                queue.append((cur.right, level + 1))
            
            if cur.left:
                queue.append((cur.left, level + 1))
        
        return res