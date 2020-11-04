from collections import deque

# 思路1 : level-order traversal, 判断每一层是否如何条件
# 思路2 : 一遍遍历, 一边添加一边判断,level by level

class Solution:
    def isEvenOddTree1(self, root):
        level = [root]
        n = 0
        while level:
            if n%2==0:
                if any([node.val%2==0 for node in level]) or any([level[i+1].val-level[i].val<=0 for i in range(len(level)-1)]):
                    return False
            else:
                if any([node.val%2==1 for node in level]) or any([level[i+1].val-level[i].val>=0 for i in range(len(level)-1)]):
                    return False
            level = [node for parent in level for node in (parent.left,parent.right) if node]
            n += 1
        return True

    def isEvenOddTree2(self, root):
        level = deque([root])
        even = True
        while level:
            curSize = len(level)
            preVal = float('-inf') if even else float('inf')
            while curSize:
                node = level.popleft()
                if even and (node.val<=preVal or node.val%2==0): return False
                if not even and (node.val>=preVal or node.val%2!=0): return False
                preVal = node.val
                if node.left: level.append(node.left)
                if node.right: level.append(node.right)
                curSize -= 1
            even = not even
        return True