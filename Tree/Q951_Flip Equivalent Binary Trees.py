# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# T(n) = a*T(n/b) + n^c
# T(n) = 4*T(n/2)
# a = 4, b = 2, c = 0, logb(a) > c
# T(n) = n^2

class Solution:

    # 思路1: 递归比较左右子树
    def flipEquiv(self, root1, root2):
        if not root1 or not root2:
            return root1==root2
        if root1==root2: return True
        else:
            return root1.val==root2.val and \
                   (self.flipEquiv(root1.left,root2.left) and self.flipEquiv(root1.right,root2.right)
                    or self.flipEquiv(root1.left,root2.right) and self.flipEquiv(root1.right,root2.left))

    # 思路2: stack iterative, 比较每一个node, 根据r1, r2的child是否匹配决定append左右子树的顺序
    def flipEquiv(self, root1, root2):
        s1, s2 = [root1], [root2]
        while s1 and s2:
            r1, r2 = s1.pop(), s2.pop()
            if not r1 or not r2:
                if r1 != r2:
                    return False
                else:
                    continue

            if r1.val != r2.val: return False

            if r1.left == r2.left == None or r1.left and r2.left and r1.left.val == r2.left.val:
                s1 += [r1.left, r1.right]
            else:
                s1 += [r1.right, r1.left]
            s2 += [r2.left, r2.right]
        return not s1 and not s2