'''
search leftbound, leaf, rightbound, rightbound need to be append is reverse order.
'''

class Solution:
    # Solution 1
    def boundaryOfBinaryTree(self, root):
        def leaf(node):
            if node:
                if not node.left and not node.right:
                    self.ans.append(node.val)
                leaf(node.left)
                leaf(node.right)

        def leftBuond(node):
            if node:
                if not node.left and not node.right:
                    return
                self.ans.append(node.val)
                if node.left:
                    leftBuond(node.left)
                else:
                    leftBuond(node.right)

        def rightBuond(node):
            if node:
                if not node.left and not node.right:
                    return
                if node.right:
                    rightBuond(node.right)
                else:
                    rightBuond(node.left)
                self.ans.append(node.val)

        if not root: return []
        self.ans = [root.val]
        leftBuond(root.left)
        leaf(root.left)
        leaf(root.right)
        rightBuond(root.right)
        return self.ans

    # Solution 2
    # def boundaryOfBinaryTree(self, root):
    #     def dfs(node,isl,isr):
    #         if node:
    #             isleaf=not node.left and not node.right
    #             if isleaf or isl:
    #                 self.ans.append(node.val)
    #             dfs(node.left,isl,isr and not node.right)
    #             dfs(node.right,isl and not node.left,isr)
    #             if isr and not isleaf:
    #                 self.ans.append(node.val)
    #
    #     if not root: return []
    #     self.ans=[root.val]
    #     dfs(root.left,True,False)
    #     dfs(root.right,False,True)
    #     return self.ans