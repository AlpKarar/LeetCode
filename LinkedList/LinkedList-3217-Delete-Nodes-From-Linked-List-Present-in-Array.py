# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set = set(nums)
        prev = None
        temp = head
        res = head

        while temp:
            if temp.val in nums_set:
                if prev:
                    prev.next = temp.next
                else:
                    res = temp.next
            else:
                prev = temp
            
            temp = temp.next
        
        return res