# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverse(self,head):
        if not head or not head.next:
            return head
        new_head=self.reverse(head.next)
        head.next.next=head
        head.next=None
        return new_head

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        reversed=self.reverse(slow)
        while reversed and head:
            if reversed.val!=head.val:
                return False
            reversed=reversed.next
            head=head.next
        return True
