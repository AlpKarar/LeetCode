# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        res = []
        
        def findRoots(root, is_root):
            if not root:
                return
            
            is_root_deleted = root.val in to_delete_set

            if is_root and not is_root_deleted:
                res.append(root)
            
            root.left = findRoots(root.left, is_root_deleted)
            root.right = findRoots(root.right, is_root_deleted)

            return None if is_root_deleted else root
        
        findRoots(root, True)

        return res