
# 思路1: 找到下一个大于等于target的node和上一个小于等于target的node, 取差值最小的
# O(h)

# 思路2: 从上往下, 一直向target靠拢, 并记录最小差值
# O(h)

class Solution:
    # def closestValue(self, root, target):
    #     def prenode(root):
    #         res = None
    #         while root:
    #             if root.val > target:
    #                 root = root.left
    #             else:
    #                 res = root
    #                 root = root.right
    #         return float('-inf') if not res else res.val
    #
    #     def nextnode(root):
    #         res = None
    #         while root:
    #             if root.val < target:
    #                 root = root.right
    #             else:
    #                 res = root
    #                 root = root.left
    #         return float('inf') if not res else res.val
    #
    #     return min(prenode(root), nextnode(root), key=lambda x: abs(x - target))


    def closestValue(self, root, target):
        res = root.val
        while root:
            if abs(root.val-target)<abs(res-target):
                res = root.val
            if root.val>target:
                root=root.left
            else:
                root=root.right
        return res