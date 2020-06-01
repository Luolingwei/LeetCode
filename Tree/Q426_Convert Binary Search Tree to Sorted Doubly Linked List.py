
# 思路1: inorder取出所有nodes按顺序排列, 然后每个node和它前面和后面连接起来即可

# 思路2: in-place 递归解决, 计算出左右子树的循环链表，并将它们与root连接起来, 最后连接首尾即可

class Solution:

    # def treeToDoublyList(self, root):
    #     nodes = []
    #
    #     def inorder(node):
    #         if not node: return
    #         inorder(node.left)
    #         nodes.append(node)
    #         inorder(node.right)
    #
    #     inorder(root)
    #     if not nodes:
    #         return None
    #     N = len(nodes)
    #     for i in range(N):
    #         nodes[i].left = nodes[(i - 1) % N]
    #         nodes[i].right = nodes[(i + 1) % N]
    #     return nodes[0]

    def treeToDoublyList(self, root):
        if not root:
            return None
        pre = self.treeToDoublyList(root.left)
        nxt = self.treeToDoublyList(root.right)
        head = tail = root
        if pre:
            head = pre
            root.left = pre.left
            root.left.right = root
        if nxt:
            tail = nxt.left
            root.right = nxt
            nxt.left = root

        head.left = tail
        tail.right = head
        return head
