# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prehead=ListNode(0)
        prehead.next=head
        while head and head.next:
            if head.next.val>head.val:
                head=head.next
                continue
            node=head.next
            head.next=head.next.next
            pre=prehead
            while pre.next and pre.next.val<node.val:
                pre=pre.next
            node.next =pre.next
            pre.next=node
        return prehead.next
