# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = prehead = ListNode(0)

        while l1 and l2:
            if l1.val > l2.val:
                prehead.next = l2
                prehead = prehead.next
                l2 = l2.next
            else:
                prehead.next = l1
                prehead = prehead.next
                l1 = l1.next

        if not l1:
            prehead.next = l2
        if not l2:
            prehead.next = l1

        return root.next

