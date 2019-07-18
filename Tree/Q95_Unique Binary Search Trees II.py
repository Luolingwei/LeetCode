# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 思路: 左子树和右子树的值域范围由root的val决定, 用memo记录已经生成的(i,j)范围的树集合.

class Solution:
    def __init__(self):
        self.memo={}
    def generateTrees(self, n):
        if not n: return []
        def generate(i,j):
            if (i,j) not in self.memo:
                ans=[]
                for val_root in range(i,j+1):
                    for left in generate(i,val_root-1):
                        for right in generate(val_root+1,j):
                            root=TreeNode(val_root)
                            root.left=left
                            root.right=right
                            ans+=[root]
                self.memo[(i,j)]=ans or [None]
            return self.memo[(i,j)]
        return generate(1,n)