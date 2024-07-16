# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        store = dict()

        def helper(root, depth):
            if not root:
                return
            
            store[depth] = store.get(depth, []) + [root.val]
            
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)
        
        helper(root, 0)

        srt = sorted(store.items(), key = lambda x: x[0])

        return [item[1] for item in srt]