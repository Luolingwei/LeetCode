
# 思路: 分成三个部分分别进行操作并连接
# reverse(second)之后返回尾部节点，second此时变成尾部节点，可以直接使用
# reverse时头部不需要断开，但是尾部一定要断开，因为是判断reverse结束的条件

class Solution:
    def reverseBetween(self, head, m, n):
        def reverse(node):
            pre = None
            while node:
                newnode = node.next
                node.next = pre
                pre = node
                node = newnode
            return pre

        prehead = ListNode(0)
        prehead.next = head
        p = prehead

        for _ in range(m - 1):
            p = p.next

        first = p
        second = p.next

        for _ in range(n - m + 1):
            p = p.next

        third = p.next
        p.next = None

        first.next = reverse(second)
        second.next = third
        return prehead.next

