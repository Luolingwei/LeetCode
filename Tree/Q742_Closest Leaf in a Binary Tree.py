
# 思路: 先dfs用map构建逆向路径, 并记录起始点
# 然后从起始点bfs向外, 返回第一个到达的叶子节点

class Solution:
    def findClosestLeaf(self, root, k: int) -> int:
        edges = {}
        self.start = None

        def dfs(node, pre):
            if not node: return
            if node.val == k: self.start = node
            edges[node] = pre
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        bfs, visited = [self.start], {self.start.val}
        while bfs:
            new_bfs = []
            for node in bfs:
                if not node.left and not node.right: return node.val
                for next_node in (node.left, node.right, edges[node]):
                    if next_node and next_node.val not in visited:
                        new_bfs.append(next_node)
                        visited.add(next_node.val)
            bfs = new_bfs
        return -1