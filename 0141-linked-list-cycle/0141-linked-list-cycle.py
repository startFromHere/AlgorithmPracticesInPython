# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s, q = head, head
        while q != None:
            if q.next == None:
                return False
            q = q.next.next
            s = s.next
            if s == q:
                return True
        return False
        
        