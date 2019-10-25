class Solution:
    def pathSum(self,root,target):
        if not root: return 0
        self.ans=0
        def dfs(node,curS):
            if node:
                curS+=node.val
                if curS==target: self.ans+=1
                dfs(node.left,curS)
                dfs(node.right,curS)
        dfs(root,0)
        return self.ans