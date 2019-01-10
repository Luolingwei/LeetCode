# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prehead = ListNode(float('inf'))
        prehead.next = head
        last = prehead
        node = head
        while node and node.next:
            node=node.next
            while node and node.val==last.next.val:
                node=node.next
            if last.next.next==node:
                last=last.next
            else:
                last.next=node
        return prehead.next
