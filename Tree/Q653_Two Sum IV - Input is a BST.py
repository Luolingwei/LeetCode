# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 思路1: dfs,dic存储已遍历的节点值
# 思路2: bfs, 同样用dic存储已遍历的节点值
# 思路3: inorder取出所有值，然后two pointers寻找target

class Solution:
    # Solution 1 dfs 92 ms
    # def findTarget(self, root, k):
    #     dic=set()
    #     def dfs(root):
    #         if root:
    #             if k-root.val in dic:
    #                 return True
    #             dic.add(root.val)
    #             return dfs(root.left) or dfs(root.right)
    #     return dfs(root)==True

    # Solution 2 bfs 80 ms
    def findTarget(self, root, k):
        if not root: return False
        bfs,dic=[root],set()
        while bfs:
            node=bfs.pop(0)
            if k-node.val in dic: return True
            dic.add(node.val)
            if node.left: bfs.append(node.left)
            if node.right: bfs.append(node.right)
        return False

    # Solution 3 inorder 92 ms
    # def findTarget(self, root, k):
    #     nums=[]
    #     def inorder(root):
    #         if root:
    #            inorder(root.left)
    #            nums.append(root.val)
    #            inorder(root.right)
    #     inorder(root)
    #     l,r=0,len(nums)-1
    #     while l<r:
    #         n=nums[l]+nums[r]
    #         if n>k:
    #             r-=1
    #         elif n<k:
    #             l+=1
    #         else:
    #             return True
    #     return False