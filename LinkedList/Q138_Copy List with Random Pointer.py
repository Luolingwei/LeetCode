
# 思路1: 用HashTable存每个节点的copy，构造新LinkedList时，直接取用next和random O(2n)
# 相当于建立起了原链表和新链表的一一对应的copy关系，注意用copy.get，因为到链表尾部会get(null)

# 思路2: 一边建立LinkedList一边赋值，如果dic中没有暂时置为0, 当访问到该节点时，修改对应的val，此时需手动添加None

import collections
class Solution:
    # Solution 1 O(2n)
    # def copyRandomList(self, head):
    #     copy={}
    #     m=n=head
    #     while m:
    #         copy[m]=ListNode(m.val)
    #         m=m.next
    #     while n:
    #         copy[n].next=copy.get(n.next)
    #         copy[n].random=copy.get(n.random)
    #         n=n.next
    #     return copy[head]

    # Solution 2 O(n)
    def copyRandomList(self, head):
        copy=collections.defaultdict(lambda: ListNode(0))
        copy[None]=None
        m=head
        while m:
            copy[m].val=m.val
            copy[m].next=copy[m.next]
            copy[m].random=copy[m.random]
            m=m.next
        return copy[head]