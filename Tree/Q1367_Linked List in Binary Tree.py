
# 思路: 从某一个节点开始, 记录p的位置进行dfs check, 如果p到达末尾, 说明有匹配路径
# 对树的所有节点作为开始节点进行check

class Solution:
    def isSubPath(self, head, root):
        def check(node,p):
            if not p: return True
            if not node:
                return False
            if node.val==p.val:
                if check(node.left,p.next) or check(node.right,p.next):
                    return True
            return False
        if not root: return False
        return check(root,head) or self.isSubPath(head,root.left) or self.isSubPath(head,root.right)