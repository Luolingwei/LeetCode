# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotate_k(self,head,nexthead,k): #反转并连接链表
        currTail=nexthead
        for _ in range(k):
            temp=head.next
            head.next=currTail
            currTail=head
            head=temp
        return currTail

    def get_next(self,head,k):
        node=head
        for _ in range(k-1):
            if not node:
                break
            node=node.next
        return node

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        nexthead=self.get_next(head,k)
        if not nexthead:
            return head
        return self.rotate_k(head,self.reverseKGroup(nexthead.next,k),k)