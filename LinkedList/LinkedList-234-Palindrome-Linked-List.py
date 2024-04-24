# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        
        stack = []
        l = head
        r = head.next

        while r and r.next:
            stack.append(l.val)
            l = l.next
            r = r.next.next
        
        if r and not r.next:
            stack.append(l.val)

        l = l.next

        while stack:
            if l.val != stack.pop():
                return False
            
            l = l.next
        
        return True