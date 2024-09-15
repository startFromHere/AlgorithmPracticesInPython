# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1, h2 = list1, list2
        myHead = ListNode()
        h = myHead
        while h1 or h2:
            if not h2 or (h1 and h1.val < h2.val):
                h.next = h1
                h1 = h1.next
            else:
                h.next = h2
                h2 = h2.next
            h = h.next
        return myHead.next

        