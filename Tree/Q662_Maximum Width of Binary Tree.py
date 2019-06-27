# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 每下降一层, 左边的pos=pos*2，右边的pos=pos*2+1

class Solution:
    def widthOfBinaryTree(self, root):
        level,ans=[(root,0)],1
        while level:
            new_level=[]
            for parent,pos in level:
                if parent.left:
                    new_level.append((parent.left,pos*2))
                if parent.right:
                    new_level.append((parent.right,pos*2+1))
            if len(new_level)>=2: ans=max(ans,new_level[-1][1]-new_level[0][1]+1)
            level=new_level
        return ans