# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        temp = head
        stack = []

        while temp:
            stack.append(temp.val)
            temp = temp.next
        
        res = 0
        i = 0

        while stack:
            res += stack.pop() * (2 ** i)
            i += 1
        
        return res