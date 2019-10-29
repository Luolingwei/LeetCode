
# 思路: 求每个节点的相对level(左右的max+1)，叶子节点level为0，level决定了该节点第几次被减掉，也就是其在ans中的位置

class Solution:
    def findLeaves(self, root):
        self.ans=[]
        def dfs(node):
            if not node: return -1
            leftL,rightL=dfs(node.left),dfs(node.right)
            curL=max(leftL,rightL)+1
            if len(self.ans)<curL+1:
                self.ans.append([])
            self.ans[curL].append(node.val)
            return curL
        dfs(root)
        return self.ans