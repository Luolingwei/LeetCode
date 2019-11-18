# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 思路: 从root dfs改变各个节点的值，并用set存储

class FindElements:
    def __init__(self, root):
        self.memo = set()
        def dfs(node, curv):
            if node:
                node.val = curv
                self.memo.add(node.val)
                dfs(node.left, 2 * curv + 1)
                dfs(node.right, 2 * curv + 2)
        dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.memo