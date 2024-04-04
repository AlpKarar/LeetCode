# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        
        if not list2:
            return list1
        
        temp1 = list1
        temp2 = list2
        head = None
        cur = None

        while temp1 and temp2:
            if head:
                if temp1.val > temp2.val:
                    cur.next = ListNode(temp2.val)
                    temp2 = temp2.next
                else:
                    cur.next = ListNode(temp1.val)
                    temp1 = temp1.next

                cur = cur.next
            else:
                if temp1.val > temp2.val:
                    head = ListNode(temp2.val)
                    temp2 = temp2.next
                else:
                    head = ListNode(temp1.val)
                    temp1 = temp1.next
                
                cur = head
        
        while temp1:
            cur.next = ListNode(temp1.val)
            temp1 = temp1.next
            cur = cur.next
        
        while temp2:
            cur.next = ListNode(temp2.val)
            temp2 = temp2.next
            cur = cur.next

        return head