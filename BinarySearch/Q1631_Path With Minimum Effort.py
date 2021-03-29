
# 思路1: dfs从左上角到右下角遍历所有可能的路径, 同时记录最大的diff, 到达右下角时更新global diff
# 思路2: 对于一个确定的max diff, bfs确定是否能到右下角, binary search寻找最小的max diff

class Solution:
    def minimumEffortPath1(self, heights) -> int:
        m, n = len(heights), len(heights[0])
        self.res = float('inf')
        def dfs(x, y, visited, preH, diff):
            if 0<=x<m and 0<=y<n and (x,y) not in visited:
                visited.add((x,y))
                newdiff = max(diff, abs(preH-heights[x][y]))
                if x==m-1 and y==n-1:
                    self.res = min(self.res, newdiff)
                dfs(x+1,y,visited, heights[x][y], newdiff)
                dfs(x-1,y,visited, heights[x][y], newdiff)
                dfs(x,y+1,visited, heights[x][y], newdiff)
                dfs(x,y-1,visited, heights[x][y], newdiff)
                visited.remove((x,y))
        dfs(0,0,set(),heights[0][0],0)
        return self.res


    def minimumEffortPath2(self, heights) -> int:
        l, r = 0, max(max(row) for row in heights)
        while l < r:
            mid = (l + r) // 2
            if not self.bfs(heights, mid):
                l = mid + 1
            else:
                r = mid
        return l

    def bfs(self, heights, max_diff):
        q = [(0, 0)]
        m, n = len(heights), len(heights[0])
        visited = set((0, 0))
        while q:
            newq = []

            for x, y in q:
                if (x, y) == (m - 1, n - 1): return True
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    newx, newy = x + dx, y + dy
                    if 0 <= newx < m and 0 <= newy < n and (newx, newy) not in visited and abs(
                            heights[newx][newy] - heights[x][y]) <= max_diff:
                        newq.append((newx, newy))
                        visited.add((newx, newy))
            q = newq
        return False


a=Solution()
print(a.minimumEffortPath1([[1,2,2],[3,8,2],[5,3,5]]))
print(a.minimumEffortPath1([[1,2,3],[3,8,4],[5,3,5]]))
print(a.minimumEffortPath1([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]))

print(a.minimumEffortPath2([[1,2,2],[3,8,2],[5,3,5]]))
print(a.minimumEffortPath2([[1,2,3],[3,8,4],[5,3,5]]))
print(a.minimumEffortPath2([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]))