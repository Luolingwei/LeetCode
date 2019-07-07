# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 思路: 如果节点的父节点被删除而自己未被删除，将其加入results，通过参数parent_deleted将当前节点是否删除传给子节点，以判断是否将子节点加入ans
# 如果删除，当前节点返回None，否则返回node. 这样将原来的deleted node与父节点拆断，但是这里并没有将deleted node与子节点的连接断开，但是并不影响此题的答案

class Solution:
    def delNodes(self, root, to_delete):
        to_delete,ans=set(to_delete),[]
        def dfs(node,parent_deleted):
            if not node: return None
            deleted=node.val in to_delete
            if parent_deleted and not deleted:
                ans.append(node)
            node.left=dfs(node.left,deleted)
            node.right=dfs(node.right,deleted)
            return None if deleted else node
        dfs(root,True)
        return ans