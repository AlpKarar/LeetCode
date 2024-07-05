# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        temp = head

        while temp and temp not in visited:
            visited.add(temp)
            temp = temp.next
        
        return temp