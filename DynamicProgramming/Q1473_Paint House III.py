from functools import lru_cache

# 思路1: dfs, 搜索所有符合条件的情况, 取最小的cost, TLE

# 思路2: 转为top-down dp, dp(pos,precolor,nb), 表示从当前pos完成需要的cost
# 之前的color是precolor, 之前形成的neighbor数量是nb

class Solution:

    # def minCost(self, houses, cost, m: int, n: int, target: int) -> int:
    #     h = houses[:]
    #     self.res = float('inf')
    #     def dfs(h,curnb,curcost,pos):
    #         if curnb>target:
    #             return
    #         if pos>=len(h):
    #             if curnb==target and pos==len(h):
    #                 self.res = min(self.res,curcost)
    #             return
    #         if h[pos]==0:
    #             for color in range(1,n+1):
    #                 temp = h[pos]
    #                 h[pos] = color
    #                 dfs(h,curnb+(color!=h[pos-1] if pos>0 else 1),curcost+cost[pos][color-1],pos+1)
    #                 h[pos] = temp
    #         else:
    #             dfs(h,curnb+(h[pos]!=h[pos-1] if pos>0 else 1),curcost,pos+1)
    #     dfs(h,0,0,0)
    #     return self.res if self.res!=float('inf') else -1


    def minCost(self, houses, cost, m: int, n: int, target: int) -> int:
        @lru_cache(None)
        def dp(pos,precolor,nb):
            if nb>target:
                return float('inf')
            if pos==m:
                return 0 if nb==target else float('inf')
            if houses[pos]>0:
                return dp(pos+1,houses[pos],nb+(houses[pos]!=precolor))
            res = float('inf')
            for i in range(1,n+1):
                res = min(res,cost[pos][i-1]+dp(pos+1,i,nb+(i!=precolor)))
            return res
        ans = dp(0,None,0)
        return ans if ans!=float('inf') else -1



a=Solution()
print(a.minCost([0,0,0,0,0],[[1,10],[10,1],[10,1],[1,10],[5,1]],5,2,3))
print(a.minCost([0,2,1,2,0],[[1,10],[10,1],[10,1],[1,10],[5,1]],5,2,3))