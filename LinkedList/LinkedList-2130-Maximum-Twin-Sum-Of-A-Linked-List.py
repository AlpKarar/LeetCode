# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []
        temp = head

        while temp:
            stack.append(temp.val)
            temp = temp.next
        
        res = 0
        l = 0
        r = len(stack) - 1

        while l < r:
            res = max(res, stack[l] + stack[r])
            l += 1
            r -= 1
        
        return res