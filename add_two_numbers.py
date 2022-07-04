# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        num1 = 0
        num2 = 0
        scalar = 1
        root = listSum = ListNode()
        
        while l1:
            num1 += l1.val * scalar
            l1 = l1.next
            scalar *= 10
           
        scalar = 1
        
        while l2:
            num1 += l2.val * scalar
            l2 = l2.next
            scalar *= 10
            
        sum = num1 + num2
        
        listSum.val = sum%10
        
        while (sum // 10) > 0:
            listSum.next = ListNode()
            listSum = listSum.next
            sum = sum // 10
            listSum.val = sum%10
            
        
        return root