class Solution:
    # Solution 1 recursive dfs bottom-up
    def longestConsecutive(self, root):
        self.ans=0
        def dfs(node):
            if not node: return 0
            left_L,right_L=dfs(node.left),dfs(node.right)
            curL=1
            if node.left and node.left.val-node.val==1:
                curL=max(left_L+1,curL)
            if node.right and node.right.val-node.val==1:
                curL=max(right_L+1,curL)
            self.ans=max(self.ans,curL)
            return curL
        dfs(root)
        return self.ans

    # Solution 2 iterative stack top-down
    # def longestConsecutive(self, root):
    #     if not root: return 0
    #     stack=[(root,1)]
    #     ans=0
    #     while stack:
    #         node,count=stack.pop()
    #         ans=max(ans,count)
    #         if node.left:
    #             stack.append((node.left,count+1) if node.val+1==node.left.val else (node.left,1))
    #         if node.right:
    #             stack.append((node.right,count+1) if node.val+1==node.right.val else (node.right,1))
    #     return ans