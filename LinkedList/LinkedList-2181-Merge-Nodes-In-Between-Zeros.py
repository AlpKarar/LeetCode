# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head.next

        tempSum = 0
        resHead = None
        tempNode = None

        while cur:
            if cur.val != 0:
                tempSum += cur.val
            elif not resHead:
                resHead = ListNode(tempSum)
                tempNode = resHead
                tempSum = 0
            else:
                tempNode.next = ListNode(tempSum)
                tempNode = tempNode.next
                tempSum = 0
            
            cur = cur.next
        
        return resHead