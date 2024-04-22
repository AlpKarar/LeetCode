# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        
        res = head
        l = head
        r = head.next

        while r:
            temp = ListNode(self.gcd(max(l.val, r.val), min(l.val, r.val)))
            temp.next = r
            l.next = temp
            l = r
            r = r.next
        
        return res
    
    def gcd(self, bigger, smaller):
        if smaller == 0:
            return bigger
        
        return self.gcd(smaller, bigger % smaller)