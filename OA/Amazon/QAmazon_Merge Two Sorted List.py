class Solution:
    def mergeTwoLists(self, l1, l2):
        root=pre=ListNode(0)
        while l1 and l2:
            if l1.val<l2.val:
                pre.next=l1
                l1=l1.next
            else:
                pre.next=l2
                l2=l2.next
            pre=pre.next
        if l1:
            pre.next=l1
        if l2:
            pre.next=l2
        return root.next