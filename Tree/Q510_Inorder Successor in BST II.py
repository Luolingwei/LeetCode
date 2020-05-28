
# 思路: 给定node, 先向右找到比它大的第一个, 然后向左尽量缩小,
# 如果没有right, 那么需要向上找, 一直向上回溯parent, 直到找到一个向右拐的点, 即之前的都是它的左子树, 这个点比node大

class Solution:
    def inorderSuccessor(self, node):
        if not node.right:
            while node.parent and node.parent.right==node:
                node=node.parent
            return node.parent
        res = node.right
        while res.left:
            res = res.left
        return res