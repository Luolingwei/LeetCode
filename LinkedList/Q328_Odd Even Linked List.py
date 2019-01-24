# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd,even=ListNode(0),ListNode(0)
        odd_head,even_head=odd,even
        flag=1
        while head:
            if flag%2==1:
                odd.next=head
                odd=odd.next
            else:
                even.next=head
                even=even.next
            head=head.next
            flag+=1
        even.next=None
        odd.next=even_head.next
        return odd_head.next




