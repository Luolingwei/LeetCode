
# 思路1: brute force, 先遍历出所有的1, 然后对每个点求到所有1的距离, 取最小值
# O(mn*mn)

# 思路2: 将所有的1分成横坐标和纵坐标考虑, 最合适的x/y一定会是最中间的
# 即每1对x/y尾部减头部, 加起来就是最小的距离, res = 最小x距离+最小y距离
# worst case: O(mnlog(mn))
# 可以两次遍历让所有的i, j都有序排列，将时间复杂度降低为O(mn)

class Solution:
    # def minTotalDistance(self, grid):
    #     m, n = len(grid), len(grid[0])
    #     people, mindist = [], float('inf')
    #     for i in range(m):
    #         for j in range(n):
    #             if grid[i][j]:
    #                 people.append((i, j))
    #
    #     for i in range(m):
    #         for j in range(n):
    #             curdist = sum([abs(i - x) + abs(j - y) for x, y in people])
    #             mindist = min(mindist, curdist)
    #
    #     return mindist

    # def minTotalDistance(self, grid) -> int:
    #     def getdist(nums):
    #         dist = 0
    #         nums.sort()
    #         i, j = 0, len(nums) - 1
    #         while i < j:
    #             dist += nums[j] - nums[i]
    #             i, j = i + 1, j - 1
    #         return dist
    #
    #     m, n = len(grid), len(grid[0])
    #     ilist, jlist = [], []
    #     for i in range(m):
    #         for j in range(n):
    #             if grid[i][j]:
    #                 ilist.append(i)
    #                 jlist.append(j)
    #
    #     return getdist(ilist) + getdist(jlist)

    def minTotalDistance(self, grid) -> int:
        def getdist(nums):
            dist = 0
            nums.sort()
            i, j = 0, len(nums) - 1
            while i < j:
                dist += nums[j] - nums[i]
                i, j = i + 1, j - 1
            return dist

        m, n = len(grid), len(grid[0])
        ilist, jlist = [], []
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    ilist.append(i)

        for j in range(n):
            for i in range(m):
                if grid[i][j]:
                    jlist.append(j)

        return getdist(ilist) + getdist(jlist)


a=Solution()
print(a.minTotalDistance([[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]))