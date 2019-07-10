# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 思路: 在判断数组是否是中序遍历的基础上修改即可，当左孩子的值不匹配时，交换左右孩子，将root加入ans，进入子节点判断，如果仍然不匹配，则返回False
# 如果最终为True，说明可以通过flip匹配，返回ans，否则返回[-1]

class Solution:
    def flipMatchVoyage(self, root, voyage):
        self.index,ans=0,[]
        def dfs(root):
            if not root: return True
            if root.val!=voyage[self.index]: return False
            self.index+=1
            if root.left and root.left.val!=voyage[self.index]: #如果左边和右边的不相等，交换左右孩子
                ans.append(root.val)
                root.left,root.right=root.right,root.left
            return dfs(root.left) and dfs(root.right)
        return ans if dfs(root) else [-1]