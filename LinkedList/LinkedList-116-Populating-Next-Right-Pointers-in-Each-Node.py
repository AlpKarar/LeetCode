"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        queue = [(root, 0)]
        level = 0
        prevNode = None

        while queue:
            curNode, curLevel = queue.pop(0)

            if level != curLevel:
                level += 1
                prevNode = curNode
            elif prevNode:
                prevNode.next = curNode
                prevNode = curNode

            
            if curNode and curNode.left:
                queue.append((curNode.left, curLevel + 1))
            
            if curNode and curNode.right:
                queue.append((curNode.right, curLevel + 1))

        return root