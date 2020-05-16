from collections import defaultdict

# 思路: 简化为计算到达所有目标的总路径长度, dfs从底层None返回
# 如果没有apple返回-1
# 如果children有apple(>=0), 累加apple+1(收上来路径长度+1)
# 如果children没有apple, 没有apple返回-1, 有apple返回0(0而不设置1是为了路径长度的计算)

class Solution:
    def minTime(self, n: int, edges, hasApple) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        def dfs(root):
            if root == None:
                return -1
            s = 0
            for children in graph[root]:
                curapple = dfs(children)
                if curapple >= 0:
                    s += (curapple + 1)
            if s > 0: return s
            else: return 0 if hasApple[root] else -1

        return max(0, 2 * dfs(0))

a=Solution()
print(a.minTime(7,[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],[False,False,True,False,True,True,False]))