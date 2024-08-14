"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        levels = dict()

        def helper(root, level):
            if not root:
                return
            
            levels[level] = levels.get(level, []) + [root.val]

            for child in root.children:
                helper(child, level + 1)

        helper(root, 0)

        return levels.values()