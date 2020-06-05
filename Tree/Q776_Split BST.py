
# 思路: 分成大于和小于等于v的两部分, 并且保持结构, recursive解决
# 如果v大于等于root.val, 那么左边和root都是小于等于v, split右边, 把low的部分放到root.right, 返回root和high
# 如果v小于root.val, 那么右边和root都是大于v, split左边, 把high的部分放到root.left, 返回low和root

class Solution:

    def splitBST(self, root, V: int):
        if not root:
            return None,None
        if root.val<=V:
            low,high = self.splitBST(root.right,V)
            root.right = low
            return root,high
        else:
            low,high = self.splitBST(root.left,V)
            root.left = high
            return low,root