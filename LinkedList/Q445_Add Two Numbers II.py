# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        x1,x2,head=0,0,ListNode(0)
        while l1:
            x1=10*x1+l1.val
            l1=l1.next
        while l2:
            x2=10*x2+l2.val
            l2=l2.next
        x=x1+x2
        while x:
            x,reminder=divmod(x,10)
            head.next,head.next.next=ListNode(reminder),head.next
        return head.next or head


