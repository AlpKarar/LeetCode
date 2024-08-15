# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        temp = head
        i = 1
        stack = []

        while i < right + 1:
            if i >= left:
                stack.append(temp)
            
            temp = temp.next
            i += 1

        l = 0
        r = len(stack) - 1

        while l < r:
            stack[l].val, stack[r].val = stack[r].val, stack[l].val
            l += 1
            r -= 1
        
        return head