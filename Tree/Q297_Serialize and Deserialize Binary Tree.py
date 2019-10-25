# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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

import collections
class Codec:

    def serialize(self, root):
        data = []
        def inorder(node):
            if not node:
                data.append('#')
            else:
                data.append(node.val)
                inorder(node.left)
                inorder(node.right)
        inorder(root)
        return data

    def deserialize(self, data):
        def construct(data):
            while data:
                if data[0] == '#':
                    data.popleft()
                    return None
                root = TreeNode(data.popleft())
                root.left = construct(data)
                root.right = construct(data)
                return root
        queue = collections.deque(data)
        return construct(queue)



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))