class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        new_head=self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return new_head

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        prehead=ListNode(0)
        prehead.next=head
        if not head or not head.next:
            return head
        p,third=prehead,None
        for _ in range(m-1):
            p=p.next
        first=p
        q=p.next
        for _ in range(n-m):
            q=q.next
        third=q.next
        q.next=None

        second=self.reverseList(p.next)
        first.next=second
        while second.next:
            second=second.next
        second.next=third

        return prehead.next

