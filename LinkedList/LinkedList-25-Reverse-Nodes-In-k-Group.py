# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        stack = []
        temp = head
        i = 0

        while temp:
            stack.append(temp)
            temp = temp.next
            i += 1

            if i % k == 0:
                substack = []

                for _ in range(k):
                    substack.append(stack.pop())
                
                for j in range(k - 1):
                    substack[j].next = substack[j + 1]
                
                substack[-1].next = temp
                
                if len(stack) > 0:
                    stack[-1].next = substack[0]
                
                stack += substack

        return stack[0]