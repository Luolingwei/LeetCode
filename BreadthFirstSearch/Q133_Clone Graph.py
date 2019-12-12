from collections import deque

class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution:
    '''
    start from node, do a bfs search to copy all nodes in graph, use a dic named memo to record all visited nodes.
    if nextnode in memo, directly append memo[nextnode], else append nextnode to memo, and add it to bfs queue
    '''
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        memo={node:Node(node.val,[])}
        bfs=deque([node])
        while bfs:
            curnode=bfs.popleft()
            for nextnode in curnode.neighbors:
                if nextnode not in memo:
                    memo[nextnode]=Node(nextnode.val,[])
                    bfs.append(nextnode)
                memo[curnode].neighbors.append(memo[nextnode])
        return memo[node]