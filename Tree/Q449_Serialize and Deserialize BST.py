# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 和 Q297不一样的是，这里增加了BST的性质，而且题目要求“The encoded string should be as compact as possible”，所以这里可以不存储空节点，利用BSY的性质进行Deserialize.

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def helper(root):
            if root:
                vals.append(root.val)
                helper(root.left)
                helper(root.right)
        vals=[]
        helper(root)
        return vals

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # 用BST的性质对节点进行分割和判断，而不是用空节点'#'了
        def helper(MinVal,MaxVal):
            if data and MinVal<data[0]<MaxVal:
                val=data.pop(0)
                root=TreeNode(val)
                root.left=helper(MinVal,val)
                root.right=helper(val,MaxVal)
                return root

        return helper(float('-inf'),float('inf'))


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))