# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        temp = head
        stack = []
        resHead = None
        resTemp = None

        while temp:
            if temp.val < x:
                if resTemp:
                    resTemp.next = ListNode(temp.val)
                    resTemp = resTemp.next
                else:
                    resHead = ListNode(temp.val)
                    resTemp = resHead
            else:
                if stack:
                    stack[-1].next = ListNode(temp.val)
                    stack.append(stack[-1].next)
                else:
                    stack.append(ListNode(temp.val))
            
            temp = temp.next
        
        if resTemp and stack:
                resTemp.next = stack[0]
        elif not resTemp and stack:
            resHead = stack[0]

        return resHead