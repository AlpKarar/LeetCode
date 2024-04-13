# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = dict()

        def helper(root):
            if not root:
                return
            
            freq[root.val] = freq[root.val] + 1 if root.val in freq else 1

            helper(root.left)
            helper(root.right)

        helper(root)
        sortedFreq = sorted(freq.items(), key = lambda x: x[1])
        mode = sortedFreq[-1][1]
        result = [sortedFreq[-1][0]]

        for i in range(len(sortedFreq) - 2, -1, -1):
            if sortedFreq[i][1] == mode:
                result.append(sortedFreq[i][0])
            else:
                break

        return result