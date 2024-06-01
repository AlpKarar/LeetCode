# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        isAllNone = True

        for i in range(len(lists)):
            if lists[i]:
                isAllNone = False
                break
        
        if isAllNone:
            return None
        
        nodes = []

        for root in lists:
            temp = root

            while temp:
                nodes.append(temp)
                temp = temp.next
        
        nodes = sorted(nodes, key = lambda node: node.val)
        res = None
        cur = None

        for i in range(len(nodes)):
            if not res:
                res = nodes[i]
                cur = res
            else:
                cur.next = nodes[i]
                cur = cur.next
        
        return res