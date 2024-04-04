# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        temp = head
        stack = []

        while temp:
            stack.append(temp)
            temp = temp.next
        
        newHead = stack.pop()
        temp = newHead

        while stack:
            temp.next = stack.pop()
            temp = temp.next
        
        temp.next = None

        return newHead