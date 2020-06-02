

# 两种方法, 一种直接返回数量, 一种遍历并用全局变量记录

class Solution:

    # def goodNodes(self, root):
    #     def dfs(node,curmax):
    #         if not node: return 0
    #         nextmax = max(curmax,node.val)
    #         return (curmax<=node.val)+dfs(node.left,nextmax)+dfs(node.right,nextmax)
    #     return dfs(root,float('-inf'))


    def goodNodes(self, root):
        self.res = 0
        def dfs(node,curmax):
            if not node: return
            if curmax<=node.val:
                self.res+=1
            nextmax = max(curmax,node.val)
            dfs(node.left,nextmax)
            dfs(node.right,nextmax)
        dfs(root,float('-inf'))
        return self.res