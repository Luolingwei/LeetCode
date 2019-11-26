
# 思路: 类似sorted array to Balanced BST, 找到doubly linkedlist的中点分别建立左右子树即可

class Solution:
    def convert(self,head):
        if not head: return None
        if not head.next: return TreeNode(head.val)
        slow,fast=head,head
        while fast and fast.next:
            slow,fast=slow.next,fast.next.next
        slow.prev.next=None
        slow.prev=None
        root=TreeNode(slow.val)
        root.right=self.convert(slow.next)
        root.left=self.convert(head)
        return root