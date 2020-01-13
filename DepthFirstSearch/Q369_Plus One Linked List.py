# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 思路: dfs搜索返回True或False代表当前位是否溢出

class Solution:
    # Solution 1 construct LinkedList
    # def plusOne(self, head):
    #     n=0
    #     while head:
    #         n=n*10+head.val
    #         head=head.next
    #     m=n+1
    #     newhead=ListNode(0)
    #     while m:
    #         node=ListNode(m%10)
    #         node.next=newhead.next
    #         newhead.next=node
    #         m=m//10
    #     return newhead.next

    # Solution 2 dfs
    def plusOne(self, head):
        def dfs(node):
            if not node.next or dfs(node.next):
                if node.val+1>9:
                    node.val=0
                    return True
                else:
                    node.val+=1
            return False
        if dfs(head):
            newhead=ListNode(1)
            newhead.next=head
            return newhead
        return head