
# 思路: dfs搜索所有可能情况, 每一个数字可能排在k个不同的桶中, 一共有k^n种情况
# 优化1: 当前最大sum大于res的时候, 停止搜索
# 优化2: 将数字放入k个桶时，如果之前有相同的桶放过了, 跳过这个桶

class Solution:
    def minimumTimeRequired(self, jobs, k):
        memo = [0]*k
        self.res = float('inf')
        def dfs(curidx, curmax):
            if curmax>=self.res: return
            if curidx==len(jobs):
                self.res = min(self.res, curmax)
                return
            visited = set()
            for i in range(k):
                if memo[i] in visited: continue
                visited.add(memo[i])
                memo[i]+=jobs[curidx]
                dfs(curidx+1, max(curmax,memo[i]))
                memo[i]-=jobs[curidx]
        dfs(0, 0)
        return self.res


a=Solution()
print(a.minimumTimeRequired([3,2,3],3))
print(a.minimumTimeRequired([1,2,4,7,8],2))
print(a.minimumTimeRequired([46,13,54,51,38,49,54,67,26,78,33],10))