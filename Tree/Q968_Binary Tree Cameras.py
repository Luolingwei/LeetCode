# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 思路: 一共有三种节点: 未被cover的点(0)，被cover的点(2)，放置camera的点(1)
# 如果left和right存在未被cover的(0)，当前加入camera，变为camera(1)
# 否则，如果left和right存在camera(1)，则当前节点已被cover(2)
# 否则，如果left和right都是被cover节点(2)，则当前节点不放置camera，留为0

class Solution:
    def minCameraCover(self, root):
        self.cameras=0
        def dfs(root):
            if not root: return 2
            left,right=dfs(root.left),dfs(root.right)
            if left==0 or right==0:
                self.cameras+=1
                return 1
            if left==1 or right==1:
                return 2
            return 0
        return (dfs(root)==0)+self.cameras