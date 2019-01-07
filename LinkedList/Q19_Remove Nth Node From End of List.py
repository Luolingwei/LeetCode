# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l1=l2=head
        for _ in range(n):
            l2=l2.next
        if not l2:
            return head.next
        while l2.next:
            l1=l1.next
            l2=l2.next
        l1.next=l1.next.next
        return head
