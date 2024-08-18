# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        oddTemp = None
        evenHead = None
        evenTemp = None
        temp = head
        i = 1

        while temp:
            if i % 2 != 0:
                if not oddTemp:
                    oddTemp = temp
                else:
                    oddTemp.next = temp
                    oddTemp = oddTemp.next
            else:
                if not evenTemp:
                    evenTemp = temp
                    evenHead = temp
                else:
                    evenTemp.next = temp
                    evenTemp = evenTemp.next
            
            temp = temp.next
            i += 1
        
        if oddTemp:
            oddTemp.next = evenHead
        
        if evenTemp:
            evenTemp.next = None

        return head