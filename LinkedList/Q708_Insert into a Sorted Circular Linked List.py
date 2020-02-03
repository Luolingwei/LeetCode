
# 思路: 从头结点往下找，找到位于中间的情况p.val<=insertVal<=p.next.val
# 或者位于两头的情况p.val>p.next.val and (insertVal>=p.val or insertVal<=p.next.val)

class Solution:
    def insert(self, head: 'Node', insertVal):
        if not head:
            newnode=Node(insertVal)
            newnode.next=newnode
            return newnode
        p,flag=head,1
        while flag:
            if p.val<=insertVal<=p.next.val: break
            if p.val>p.next.val and (insertVal>=p.val or insertVal<=p.next.val): break
            p=p.next
            if p==head: flag=0
        newnode=Node(insertVal)
        newnode.next=p.next
        p.next=newnode
        return head