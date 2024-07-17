# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        i = 0
        prev = None
        cur = list1

        while i < a:
            prev = cur
            cur = cur.next
            i += 1
        
        first = prev

        while i < b:
            i += 1
            cur = cur.next
        
        second = cur.next

        last_node_list2 = list2

        while last_node_list2.next:
            last_node_list2 = last_node_list2.next
        
        head = list1

        if first:
            first.next = list2
        else:
            head = list2
        
        last_node_list2.next = second

        return head