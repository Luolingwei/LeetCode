class Solution:
    def pathSum(self, root, sum):
        self.ans=0
        memo={0:1}
        def dfs(node,curS):
            if node:
                curS+=node.val
                self.ans+=memo.get(curS-sum,0)
                memo[curS]=memo.get(curS,0)+1
                dfs(node.left,curS)
                dfs(node.right,curS)
                memo[curS]-=1
        dfs(root,0)
        return self.ans