# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 思路:先用stack或者number将两个数存起来，然后相加，最后构造LinkedList

class Solution:
    # Solution 1 stack 88 ms
    # def addTwoNumbers(self, l1, l2):
    #     def read(node):
    #         stack=[]
    #         while node:
    #             stack.append(node.val)
    #             node=node.next
    #         return stack
    #     s1,s2=read(l1),read(l2)
    #     carry,head=0,ListNode(0)
    #     while s1 or s2 or carry:
    #         carry=carry+(s1 or [0]).pop()+(s2 or [0]).pop()
    #         carry,remider=divmod(carry,10)
    #         node=ListNode(remider)
    #         node.next=head.next
    #         head.next=node
    #     return head.next

    # Solution 2 number 80 ms
    def addTwoNumbers(self, l1, l2):
        def read(node):
            p=0
            while node:
                p=p*10+node.val
                node=node.next
            return p
        p1,p2=read(l1),read(l2)
        p,head=p1+p2,ListNode(0)
        while p:
            p,reminder=divmod(p,10)
            node=ListNode(reminder)
            node.next=head.next
            head.next=node
        return head.next or head