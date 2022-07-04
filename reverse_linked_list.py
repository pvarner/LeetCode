# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        


        # if empty
        if head == None or head.next == None:
            return head
        
        prevNode = head
        curNode = head.next
        prevNode.next = None

        # if two element 
        if curNode != None:
            nextNode = curNode.next
        else:
            return curNode

        while True:
            curNode.next = prevNode
            if nextNode == None:
                return curNode
            
            prevNode = curNode
            curNode = nextNode
            nextNode = nextNode.next
            