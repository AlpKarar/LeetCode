# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        stack = []
        temp = head

        while temp:
            stack.append(temp)
            temp = temp.next
        
        n = len(stack)

        if n < k:
            for node in stack:
                node.next = None

            return stack + [None] * (k - n)
        
        i = n // k
        rem = n % k
        res = [head]

        while i < n:
            if rem > 0:
                res.append(stack[i + 1])
                stack[i].next = None
                rem -= 1
                i += 1
            else:
                res.append(stack[i])
                stack[i - 1].next = None
            
            i += n // k

        return res