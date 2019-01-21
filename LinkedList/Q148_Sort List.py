# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
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
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        slow=fast=head
        while fast and fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next
        second=slow.next
        slow.next=None
        return self.mergeTwoLists(self.sortList(head),self.sortList(second))