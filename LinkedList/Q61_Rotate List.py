# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p=node=head
        length=1
        while p.next:
            p=p.next
            length+=1
        carry=length-k%length-1
        while carry:
            node=node.next
            carry-=1
        p.next=head
        head=node.next
        node.next=None
        return head