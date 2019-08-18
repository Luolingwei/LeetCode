# Input: [1,7,0,7,-8,null,null]
# Output: 2
# Explanation:
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.

# 思路: bfs求各层的sum，取最大sum的level

class Solution:
    def maxLevelSum(self, root):
        bfs,curL,S,ans=[root],1,root.val,1
        while bfs:
            bfs=[node for p in bfs for node in (p.left,p.right) if node]
            curL+=1
            curS=sum(node.val for node in bfs)
            if curS>S:
                ans,S=curL,curS
        return ans