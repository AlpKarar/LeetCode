# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        stack = []
        temp = head

        while temp:
            stack.append(temp)
            temp = temp.next
        
        stack[k - 1].val, stack[-k].val = stack[-k].val, stack[k - 1].val

        return stack[0]