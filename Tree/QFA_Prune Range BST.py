
# 思路: 判断每个node是否在范围内，如果不在，利用BST的性质直接删除左子树或者右子树，如果在范围内，分别对左右剪枝并返回给root，返回root

class Solution:
    def prune(self,root,start,end):
        if not root: return None
        if root.val>end:
            return self.prune(root.left,start,end)
        if root.val<start:
            return self.prune(root.right,start,end)
        root.left=self.prune(root.left,start,end)
        root.right=self.prune(root.right,start,end)
        return root