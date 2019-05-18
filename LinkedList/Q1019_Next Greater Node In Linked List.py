# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 思路: 用stack存储当前仍未找到最近最大值的数，每次进来一个数，stack pop比它小的，并将当前值作为pop出的相应数字的ans

class Solution:
    def nextLargerNodes(self, head):
        ans,stack=[],[]
        i=0
        while head:
            while stack and stack[-1][1]<head.val:
                ans[stack.pop()[0]]=head.val
            stack.append((i,head.val))
            ans.append(0)
            i,head=i+1,head.next
        return ans