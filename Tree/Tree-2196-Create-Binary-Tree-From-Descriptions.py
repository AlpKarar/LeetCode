# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = dict()

        for desc in descriptions:
            if desc[0] not in nodes:
                newNode = TreeNode(desc[0])
                nodes[desc[0]] = newNode
            
            if desc[1] not in nodes:
                newChildNode = TreeNode(desc[1])
                nodes[desc[1]] = newChildNode
            
            if desc[2] == 1:
                nodes[desc[0]].left = nodes[desc[1]]
            else:
                nodes[desc[0]].right = nodes[desc[1]]
        

        """
        children = set()

        for val in nodes:
            node = nodes[val]
            
            if node.left:
                children.add(node.left)
            
            if node.right:
                children.add(node.right)
        
        root = None

        for val in nodes:
            node = nodes[val]

            if node not in children:
                root = node
                break
        """
        
        node_vals = {val for val in nodes.keys()}
        
        for desc in descriptions:
            if desc[1] in node_vals:
                node_vals.remove(desc[1])

        return nodes[list(node_vals)[0]]