# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        temp1 = l1

        while temp1:
            num1 += str(temp1.val)
            temp1 = temp1.next
        
        num2 = ""
        temp2 = l2

        while temp2:
            num2 += str(temp2.val)
            temp2 = temp2.next
        
        num3 = str(int(num1) + int(num2))
        stack = [int(num3[i]) for i in range(len(num3) - 1, -1, -1)]
        head = None
        cur = None

        while stack:
            if not head:
                head = ListNode(int(stack.pop()))
                cur = head
            else:
                cur.next = ListNode(int(stack.pop()))
                cur = cur.next
        
        return head