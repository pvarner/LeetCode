# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        arr = set()
        
        while head and head.next:
            arr.add(head)
            
            if head.next in arr:
                return head.next
            
            head = head.next
            
        return None
            