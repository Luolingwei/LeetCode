import heapq

# 搜索全部node, 维护一个size为k的heap, 存储和target差值最小的node值
# O(nlogk)

class Solution:
    def closestKValues(self, root, target, k):
        q = []
        def inorder(node):
            if not node: return
            inorder(node.left)
            heapq.heappush(q,(-abs(node.val-target),node.val))
            if len(q)>k:
                heapq.heappop(q)
            inorder(node.right)
        inorder(root)
        return [n[1] for n in q]