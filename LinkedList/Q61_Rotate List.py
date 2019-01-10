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
        node =test=head
        length=1
        while test.next:
            test=test.next
            length+=1
        for _ in range(k%length):
            while node.next:
                if not node.next.next:
                    temp=node
                node=node.next
            node.next=head
            head=node
            temp.next=None
        return node


