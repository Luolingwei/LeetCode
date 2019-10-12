
# 思路: 判断每个node是否为single node，如果是，返回其左/右子树prune的结果，以此删除该节点

class Solution:
    def prune(self,root):
        if not root: return None
        if (not root.left and root.right) or (not root.right and root.left):
            return self.prune(root.left or root.right)
        root.left=self.prune(root.left)
        root.right=self.prune(root.right)
        return root