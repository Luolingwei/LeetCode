
# 思路: 每个节点返回是否unique, 以及unique的值
# 从空节点开始返回 None,True
# 一个节点valid的条件是，左右都unique且他们的unique值与当前节点相同

class Solution:
    def countUnivalSubtrees(self, root):
        self.res = 0
        def dfs(node):
            if node==None:
                return None,True
            lnum,lstatus = dfs(node.left)
            rnum,rstatus = dfs(node.right)
            if lstatus and rstatus:
                if len(set(filter(lambda x:x!=None,[lnum,rnum,node.val])))==1:
                    self.res+=1
                    return node.val,True
            return node.val,False
        dfs(root)
        return self.res