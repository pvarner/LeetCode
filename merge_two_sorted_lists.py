# Definition for singly-linked list.

class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        root = node

        if list1 == None:
            return list2
        elif list2 == None:
            return list1

        while True:
            if list1.val > list2.val:
                node.val = list2.val
                list2 = list2.next
            else:
                node.val = list1.val
                list1 = list1.next

            if list1 == None:
                while list2 != None:
                    node.next = ListNode()
                    node = node.next
                    node.val = list2.val
                    list2 = list2.next
                return root
            elif list2 == None:
                while list1 != None:
                    node.next = ListNode()
                    node = node.next
                    node.val = list1.val
                    list1 = list1.next
                return root

            node.next = ListNode()
            node = node.next