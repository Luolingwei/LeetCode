# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Solution 1 recursive 40 ms
    # def reverseList(self, head):
    #     if not head or not head.next:
    #         return head
    #     new_head=self.reverseList(head.next)
    #     head.next.next=head
    #     head.next=None
    #     return new_head

    # Solution 2 iterative
    def reverseList(self, head):
        pre=None
        while head:
            next_head=head.next
            head.next=pre
            pre=head
            head=next_head
        return pre