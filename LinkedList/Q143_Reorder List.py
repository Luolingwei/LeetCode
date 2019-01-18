# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import collections
class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        queue=collections.deque()
        while head:
            queue.append(head)
            head=head.next
        prehead,index=ListNode(0),0
        head=prehead
        while queue:
            if index%2==0:
                head.next=queue.popleft()
            else:
                head.next=queue.pop()
            head=head.next
            index+=1
        head.next=None