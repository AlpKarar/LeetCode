# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        
        tempHead = head
        prev = None
        cur = head

        while cur:
            if cur.val == val:
                if not prev:
                    tempHead = cur.next
                else:
                    prev.next = cur.next
            else:
                prev = cur
            
            cur = cur.next
        
        return tempHead