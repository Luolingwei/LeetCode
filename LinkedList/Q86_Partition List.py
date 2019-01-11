# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        prehead1,prehead2=ListNode(0),ListNode(0)
        p=prehead1
        q=prehead2
        while head:
            if head.val<x:
                p.next=head
                p=p.next
            else:
                q.next=head
                q=q.next
            head=head.next
        q.next=None
        p.next=prehead2.next
        return prehead1.next

