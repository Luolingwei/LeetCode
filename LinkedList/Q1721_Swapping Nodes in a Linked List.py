
# 思路: 交换第k个和倒数第k个节点, 倒数第k个即正数L-k个
# 用一个节点先走k步，然后两个节点一起走到头, 前面的节点会停在L-k个节点处

class Solution:
    def swapNodes(self, head, k: int):
        prehead = ListNode(0)
        prehead.next = head
        p = q = prehead
        for _ in range(k):
            q = q.next
        left = q
        while q:
            p = p.next
            q = q.next
        p.val, left.val = left.val, p.val
        return prehead.next