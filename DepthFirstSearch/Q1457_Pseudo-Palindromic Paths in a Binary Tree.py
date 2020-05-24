# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 思路1: 用数组记录各个node的个数, 在叶子节点check奇数的个数是否<=1
# 向上合并加起来, O(nk)

# 思路2: 用bit记录各个node的个数, 用异或进行同样value的抵消
# 在叶子节点check是否只有一个1, 用bit&(bit-1)==0判断
# O(n)

class Solution:

    # def pseudoPalindromicPaths(self, root):
    #     def check(new_count):
    #         return sum(c & 1 for c in new_count) <= 1
    #
    #     def dfs(node, count):
    #         if not node: return 0
    #         new_count = count[:]
    #         new_count[node.val] += 1
    #         if not node.left and not node.right:
    #             return check(new_count)
    #         return dfs(node.left, new_count) + dfs(node.right, new_count)
    #
    #     return int(dfs(root, [0]*10))

    def pseudoPalindromicPaths(self, root):

        def dfs(node, bit):
            if not node: return 0
            bit^=1<<(node.val-1)
            if not node.left and not node.right:
                return bit&(bit-1)==0
            return dfs(node.left, bit) + dfs(node.right, bit)

        return int(dfs(root, 0))