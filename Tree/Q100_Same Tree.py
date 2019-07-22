# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Solution 1 recursive 40 ms
    # def isSameTree(self, p,q):
    #     if p and q:
    #         return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    #     elif not p and not q:
    #         return True
    #     else:
    #         return False

    # Solution 2 iterative 36 ms
    def isSameTree(self, p,q):
        stack=[(p,q)]
        while stack:
            l,r=stack.pop()
            if l and r:
                if l.val!=r.val: return False
                stack.append((l.left,r.left))
                stack.append((l.right,r.right))
            elif not l and not r:
                continue
            else:
                return False
        return True