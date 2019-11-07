
# Solution 1: 2-pass. 先构建整个tree的copy，然后inorder搜索Tree，用copy中的node重新构建一次
# Solution 2: 1-pass, 动态赋值，暂时没有的node先置为0，访问到每个节点时修改值

import collections
class Solution:

    # def copyRandomTree(self, root):
    #     copy = {}
    #     def inorder_copy(node):
    #         if node:
    #             inorder_copy(node.left)
    #             copy[node] = TreeNode(node.val)
    #             inorder_copy(node.right)
    #     def preorder_make(node):
    #         if node:
    #             curNode=copy[node]
    #             curNode.random=copy[node.random]
    #             curNode.left=preorder_make(node.left)
    #             curNode.right=preorder_make(node.right)
    #             return curNode
    #     inorder_copy(root)
    #     return preorder_make(root)

    def copyRandomTree(self, root):
        copy = collections.defaultdict(lambda : TreeNode(0))
        def preorder_make(node):
            if node:
                curNode=copy[node]
                curNode.val=node.val
                curNode.random=copy[node.random]
                curNode.left=preorder_make(node.left)
                curNode.right=preorder_make(node.right)
                return curNode
        return preorder_make(root)