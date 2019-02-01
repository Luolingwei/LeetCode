# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        size,ans=0,[]
        p=q=pointer=root
        while p:
            size+=1
            p=p.next
        base,carry=divmod(size,k)
        for i in range(carry):
            for j in range(base):
                pointer=pointer.next
            copy=pointer.next
            pointer.next=None
            ans.append(q)
            pointer=q=copy
        for i in range(k-carry):
            if not pointer:
                ans.append(None)
                continue
            for j in range(base-1):
                pointer=pointer.next
            copy=pointer.next
            pointer.next=None
            ans.append(q)
            pointer=q=copy
        return ans
