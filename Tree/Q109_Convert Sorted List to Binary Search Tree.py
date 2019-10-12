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
    def sortedListToBST(self, head):
        def getnums(head):
            nums=[]
            while head:
                nums.append(head.val)
                head=head.next
            return nums
        def buildBST(nums):
            if not nums: return None
            mid=len(nums)//2
            root=TreeNode(nums[mid])
            root.left=buildBST(nums[:mid])
            root.right=buildBST(nums[mid+1:])
            return root
        return buildBST(getnums(head))