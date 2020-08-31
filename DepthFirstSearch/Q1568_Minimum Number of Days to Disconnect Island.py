from copy import deepcopy

# 思路: 最多需要remove 2个1就可以形成孤岛, 所以只需要考虑0/1的情况
# 0的情况为一开始island个数不为1, 1的情况可以尝试remove每个1的格子, 如果形成了多于1个的island, 那么返回1

class Solution:
    def minDays(self, grid):
        def dfs(nums, i, j):
            if 0 <= i < m and 0 <= j < n and nums[i][j] == 1:
                nums[i][j] = 0
                dfs(nums, i + 1, j)
                dfs(nums, i - 1, j)
                dfs(nums, i, j + 1)
                dfs(nums, i, j - 1)

        def find_island(nums):
            ret = 0
            for i in range(m):
                for j in range(n):
                    if nums[i][j] == 1:
                        dfs(nums, i, j)
                        ret += 1
            return ret

        m, n = len(grid), len(grid[0])
        nums = deepcopy(grid)
        island_n = find_island(nums)
        if island_n != 1: return 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    temp = deepcopy(grid)
                    temp[i][j] = 0
                    if find_island(temp)!=1:
                        return 1
        return 2


a=Solution()
print(a.minDays([[0,1,1,0],[0,1,1,0],[0,0,0,0]]))
print(a.minDays([[1,1,0,1,1],[1,1,1,1,1],[1,1,0,1,1],[1,1,1,1,1]]))
print(a.minDays([[1,1,0,1,1],[1,1,1,1,1],[1,1,0,1,1],[1,1,0,1,1]]))

