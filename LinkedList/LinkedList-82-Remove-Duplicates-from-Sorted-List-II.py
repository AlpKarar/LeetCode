# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        prev = head
        cur = head.next

        if not cur:
            return prev

        duplicates = set()
        res = None
        last = None

        while cur:
            if cur.val == prev.val:
                duplicates.add(prev.val)
            elif prev.val not in duplicates:
                if not res:
                    res = prev
                    last = prev
                else:
                    last.next = prev
                    last = last.next
            
            prev = cur
            cur = cur.next
        
        if prev.val not in duplicates:
            if not res:
                res = prev
            else:
                last.next = prev
        elif last:
            last.next = None

        return res