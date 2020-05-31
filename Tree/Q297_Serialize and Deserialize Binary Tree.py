# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# You may serialize the following tree:
#
#     1
#    / \
#   2   3
#      / \
#     4   5
#
# as "[1,2,3,null,null,4,5]"

# 思路: 先序遍历tree，然后以中左右的顺序deserialize，碰到'#'时，说明当前路径结束，返回None，构建另一支子树

from collections import deque
class Codec:

    # 返回list的解法
    # def serialize(self, root):
    #     data = []
    #     def preorder(node):
    #         if not node:
    #             data.append('#')
    #         else:
    #             data.append(node.val)
    #             preorder(node.left)
    #             preorder(node.right)
    #     preorder(root)
    #     return data
    #
    # def deserialize(self, data):
    #     def construct(data):
    #         while data:
    #             if data[0] == '#':
    #                 data.popleft()
    #                 return None
    #             root = TreeNode(data.popleft())
    #             root.left = construct(data)
    #             root.right = construct(data)
    #             return root
    #     queue = collections.deque(data)
    #     return construct(queue)


    # 返回string的解法
    def serialize(self, root):
        self.res = ""
        def preorder(node):
            if not node:
                self.res += "# "
                return
            self.res += str(node.val) + " "
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return self.res

    def deserialize(self, data):
        data = deque(data.split())
        def construct():
            if data[0] == "#":
                data.popleft()
                return None
            root = TreeNode(int(data.popleft()))
            root.left = construct()
            root.right = construct()
            return root
        return construct()
