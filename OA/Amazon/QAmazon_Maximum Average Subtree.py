
# dfs计算字数的count和sum，从null返回

class Solution:
    def subtree(self,root):
        self.max,self.ans=float('-inf'),None
        def dfs(node):
            if node:
                if not node:
                    return 0,0
                curS,curC=node.val,1
                for c in node.children:
                    subS,subC=dfs(c)
                    curS+=subS
                    curC+=subC
                if curC>1 and curS/curC>self.max: self.ans=node
                return curS,curC
        dfs(root)
        return self.ans