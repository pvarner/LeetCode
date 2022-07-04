# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        iter1 = head
        iter2 = head
        count = 1
        
        while iter1.next != None:
            
            iter1 = iter1.next
            
            if (count % 2 == 0):
                iter2 = iter2.next
            
            count += 1
        
        if count % 2 == 0:
            return iter2.next
        else:
            return iter2
        