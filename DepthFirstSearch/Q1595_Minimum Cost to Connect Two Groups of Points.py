from functools import lru_cache

# 思路: 题目意思是在矩阵中选取元素, 并保证每行每列都能被cover, 求最小的总和
# dfs穷举cover所有行(或列)的情况, 用bit mask记录同时被cover的列, 行cover完之后对被漏掉的列取最小的行元素即可

class Solution:

    # 写法1, 全局变量记录, dfs无cache, TLE
    # def connectTwoGroups(self, cost):
    #     self.res = float('inf')
    #     m,n = len(cost),len(cost[0])
    #     min_cols = [min(cost[i][j] for i in range(m)) for j in range(n)]
    #     def dfs(i, visited, curC):
    #         if i>=m:
    #             for j in range(n):
    #                 if not (1<<j)&visited:
    #                     curC += min_cols[j]
    #             self.res = min(self.res, curC)
    #             return
    #         for j in range(n):
    #             dfs(i+1, visited|1<<j, curC+cost[i][j])
    #     dfs(0,0,0)
    #     return self.res

    # 写法2, 去掉curC变量, dfs返回达到最终状态还需要的cost, 对dfs进行cache
    def connectTwoGroups(self, cost):
        m,n = len(cost),len(cost[0])
        min_cols = [min(cost[i][j] for i in range(m)) for j in range(n)]
        @lru_cache(None)
        def dfs(i, visited):
            res = 0 if i>=m else float('inf')
            if i>=m:
                for j in range(n):
                    if not (1<<j)&visited:
                        res += min_cols[j]
                return res
            else:
                for j in range(n):
                    res = min(res, cost[i][j] + dfs(i+1, visited|1<<j))
                return res
        dfs(0,0)
        return dfs(0,0)


a=Solution()
print(a.connectTwoGroups([[15, 96], [36, 2]]))
print(a.connectTwoGroups([[1, 3, 5], [4, 1, 1], [1, 5, 3]]))
print(a.connectTwoGroups([[99,44,34,99,67,59,97,62,82],[77,57,37,2,74,28,80,11,100],[35,14,55,92,7,50,68,31,11],[96,68,32,96,55,26,29,0,45],[25,11,62,87,48,78,68,32,54],[20,34,94,38,7,74,66,3,45],[46,76,73,90,21,32,88,89,60],[75,34,20,69,91,8,69,73,54],[34,45,28,5,69,53,72,1,34],[18,63,89,29,66,11,33,90,54]]))