
# 思路: dfs搜索，对每个节点返回None或其本身，如果left和right为None且val==target，返回None

class Solution:
    def removeLeafNodes(self, root, target):
        def dfs(node):
            if not node: return None
            node.left=dfs(node.left)
            node.right=dfs(node.right)
            if not node.left and not node.right and node.val==target:
                return None
            return node
        return dfs(root)