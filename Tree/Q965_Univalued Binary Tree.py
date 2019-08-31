# Input: [2,2,2,5,2]
# Output: false

# 思路: dfs即可

class Solution:
    def isUnivalTree(self, root):
        def dfs(node):
            if not node: return True
            return node.val==root.val and dfs(node.left) and dfs(node.right)
        return dfs(root)