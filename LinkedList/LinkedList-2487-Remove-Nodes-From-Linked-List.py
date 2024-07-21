# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curMax = [0]
        res = []

        def helper(node):
            if not node:
                return
            
            helper(node.next)

            if node.val >= curMax[0]:
                curMax[0] = node.val
                res.append(node)
        
        helper(head)

        for i in range(len(res) - 1, 0, -1):
            res[i].next = res[i-1]
        
        return res[-1]