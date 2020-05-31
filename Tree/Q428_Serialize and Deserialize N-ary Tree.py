
# 思路: 和Binary Tree类似, 仍然preorder进行serialize
# 不同的是, 多叉树的关键不再是左右子树是否为空, 而是有多少个children
# serialize时, children加完后, 加入一个标识符"#"表示这个root的children已经没有了
# 第一个节点为root, 递归建立children, 最后遇到"#"结束children添加, pop出"#", 返回root即可

from collections import deque

class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        res = []

        def preorder(node):
            if not node:
                return
            res.append(str(node.val))
            for c in node.children:
                preorder(c)
            res.append("#")

        preorder(root)
        return " ".join(res)

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if not data: return None
        data = deque(data.split())

        def construct():
            root = Node(data.popleft(), [])
            while data[0] != "#":
                root.children.append(construct())
            data.popleft()
            return root

        return construct()