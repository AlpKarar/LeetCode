# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def helper(start, end):
            subtreeRoots = []

            if start > end:
                subtreeRoots.append(None)
            else:
                for val in range(start, end + 1):
                    leftSubtrees = helper(start, val - 1)
                    rightSubtrees = helper(val + 1, end)

                    for leftSubtree in leftSubtrees:
                        for rightSubtree in rightSubtrees:
                            subtreeRoots.append(TreeNode(val, leftSubtree, rightSubtree))
            
            return subtreeRoots
        
        return helper(1, n)