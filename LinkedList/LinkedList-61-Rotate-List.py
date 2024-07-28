# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        
        stack = []
        temp = head

        while temp:
            stack.append(temp)
            temp = temp.next
        
        k %= len(stack)

        if k == 0:
            return head
        
        stack[-k-1].next = None
        stack[-1].next = stack[0]

        return stack[-k]