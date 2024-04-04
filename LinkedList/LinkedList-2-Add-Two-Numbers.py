# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = l1, l2
        head = None
        cur = None
        rem = 0

        while cur1 or cur2 or rem > 0:
            curSum = (cur1.val if cur1 else 0) + (cur2.val if cur2 else 0) + rem

            if curSum >= 10:
                if not head:
                    head = ListNode(curSum - 10)
                    rem = 1
                    cur = head
                else:
                    cur.next = ListNode(curSum - 10)
                    rem = 1
                    cur = cur.next
            else:
                if not head:
                    head = ListNode(curSum)
                    rem = 0
                    cur = head
                else:
                    cur.next = ListNode(curSum)
                    rem = 0
                    cur = cur.next
            
            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None

        return head