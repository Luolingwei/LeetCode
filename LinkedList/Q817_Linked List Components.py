# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 思路: 遍历链表，如果找到在G中的节点，将剩下的连接着的同时遍历掉，ans+1.

class Solution:
    def numComponents(self, head, G):
        S,ans=set(G),0
        while head:
            if head.val in S:
                ans+=1
                while head and head.val in S:
                    head=head.next
            else:
                head=head.next
        return ans