# Example 1:
# Input: [1,null,0,0,1]
# Output: [1,null,0,null,1]

# 思路: dfs每个节点，如果某节点为0且左右都为None(为空或已经删除)，那么return None删除当前节点，否则保留

class Solution:
    def pruneTree(self, root):
        def dfs(node):
            if not node: return None
            node.left,node.right=dfs(node.left),dfs(node.right)
            if not node.left and not node.right and not node.val:
                return None
            return node
        return dfs(root)