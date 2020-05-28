
# 思路1: 用全局变量flag记录是否找到目标节点
# 如果flag=1(找到目标节点)且self.res尚未找到则记录res
# O(n)

# 思路2: 用node的值替代flag, 找到第一个比p.val大的节点即可
# O(n)

# 思路3: recursive, 如果p.val>=root.val, 那么successor不可能存在左边, 去右边找
# 否则在左边找, 左边没找到即返回root
# 同样的道理可求predecessor
# O(h)

# 思路4: iterative, 找successor, 如果p.val>=root.val, 往右边增加node的值, 一直到p.val<root.val
# 即找到第一个比p.val大的node, 然后试图往左减小, 更靠近p.val, 如果左边没有, 直接返回res记录的最后一个root
# 同样的道理可求predecessor
# O(h)

class Solution:
    # def inorderSuccessor(self, root, p):
    #     self.flag, self.res = 0, None
    #     def inorder(node):
    #         if node:
    #             inorder(node.left)
    #             if self.flag and not self.res:
    #                 self.res = node
    #                 return
    #             if node == p:
    #                 self.flag = 1
    #             inorder(node.right)
    #     inorder(root)
    #     return self.res

    # def inorderSuccessor(self, root, p):
    #     self.res = None
    #     def inorder(node):
    #         if node:
    #             inorder(node.left)
    #             if node.val>p.val and not self.res:
    #                 self.res = node
    #                 return
    #             inorder(node.right)
    #     inorder(root)
    #     return self.res

    # def inorderSuccessor(self, root, p):
    #     if not root: return None
    #     if root.val <= p.val:
    #         return self.inorderSuccessor(root.right, p)
    #     else:
    #         l = self.inorderSuccessor(root.left, p)
    #         return l if l else root

    def inorderSuccessor(self, root, p):
        res = None
        while root:
            if p.val>=root.val:
                root=root.right
            else:
                res = root
                root=root.left
        return res