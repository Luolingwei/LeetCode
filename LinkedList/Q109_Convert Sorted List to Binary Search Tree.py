# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def numsToBST(self,nums):
        if not nums:
            return None
        if len(nums)==1:
            return TreeNode(nums[0])
        curVal=nums[len(nums)//2]
        curNode=TreeNode(curVal)
        curNode.left=self.numsToBST([n for n in nums if n<curVal])
        curNode.right=self.numsToBST([n for n in nums if n>curVal])
        return curNode

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        nums=[]
        while head:
            nums.append(head.val)
            head=head.next
        return self.numsToBST(nums)
