
# dfs计算字数的count和sum，从null返回，用参数记录每个节点subtree的最大average，一直更新到root

class Solution:
    # Solution without global var
    def subtree(self,root):
        def dfs(node):
            if not node:
                return 0,0,float('-inf'),None
            curS,curC,curMax,curNode=node.val,1,float('-inf'),None
            for c in node.children:
                subS,subC,subMax,subNode=dfs(c)
                curS+=subS
                curC+=subC
                if subMax>curMax:
                    curMax=subMax
                    curNode=subNode
            if curC>1 and curS/curC>curMax:
                curMax=curS/curC
                curNode=node
            return curS,curC,curMax,curNode
        return dfs(root)[3]