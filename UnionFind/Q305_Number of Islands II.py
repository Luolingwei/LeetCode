
# 思路1: 每次添加一个点island+1, 然后减去它周围的island个数, 将它和周围的island都标记为同一label

# 思路2: union find, 每次将新增点和周围点进行union, 每次union相当于将当前点与周围island合并减少的island即union成功的次数

class Solution:
    # def numIslands2(self, m, n, positions):
    #     def mark(i, j, label):
    #         if 0 <= i < m and 0 <= j < n and 0<grid[i][j]<label:
    #             grid[i][j] = label
    #             mark(i + 1, j, label)
    #             mark(i - 1, j, label)
    #             mark(i, j + 1, label)
    #             mark(i, j - 1, label)
    #
    #     grid = [[0] * n for _ in range(m)]
    #     label, island = 1, 0
    #     res = []
    #     for x, y in positions:
    #         if grid[x][y] > 0:
    #             res.append(island)
    #             continue
    #         island += 1
    #         neighbors = [(i, j) for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)] if 0 <= i < m and 0 <= j < n]
    #         island -= len({grid[i][j] for i, j in neighbors if grid[i][j] > 0})
    #         grid[x][y] = 1
    #         mark(x, y, label)
    #         res.append(island)
    #         label += 1
    #     return res

    def numIslands2(self, m, n, positions):
        def find(x):
            while x in uf:
                # path compress
                while uf[x] in uf:
                    uf[x] = uf[uf[x]]
                x = uf[x]
            return x
        def union(x,y):
            px,py = find(x), find(y)
            if px==py: return False
            uf[px] = py
            return True

        uf, visited, res = {}, set(), []
        island = 0
        for x, y in positions:
            if (x,y) not in visited:
                visited.add((x,y))
                island+=1
                for newx,newy in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                    if (newx,newy) in visited and union((x,y),(newx,newy)):
                        island-=1
            res.append(island)
        return res

a=Solution()
print(a.numIslands2(3,3,[[0,0], [0,1], [1,2], [2,1]]))
print(a.numIslands2(3,3,[[0,0], [0,1], [1,2], [2,1], [1,1]]))