# Input: 1->2->3->4->5->6->NULL
# Output: 1->2->3->6->5->4->NULL

# 用快慢指针求出中点，然后reverse后面一半即可

class Solution:
    def reverseList(self, head):
        def reverse(node):
            pre = None
            while head:
                next_head = head.next
                head.next = pre
                pre = head
                head = next_head
            return pre
        fast=slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        slow.next=reverse(slow.next)
        return head