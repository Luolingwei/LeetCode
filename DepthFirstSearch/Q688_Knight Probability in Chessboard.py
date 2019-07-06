# Input: 3, 2, 0, 0
# Output: 0.0625
# Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
# From each of those positions, there are also two moves that will keep the knight on the board.
# The total probability the knight stays on the board is 0.0625.

# 思路1: bfs:每次计算八个方向的点，还在范围内的加入points中，迭代一次，依次迭代K次，看还剩多少个点，即多少种可行的路径, 概率=剩余个数/8**K
# 思路2: dfs.k次move之后还在范围内的概率=1/8*Sum(当前点move后的8个点 k-1次move之后的概率)

class Solution:
    # Solution 1 bfs without memory, TLE
    # def knightProbability(self, N, K, r, c):
    #     candidates=[(r,c)]
    #     def cal(points):
    #         if not points: return []
    #         new_points=[]
    #         for dx,dy in [(2,1),(2,-1),(-2,1),(-2,-1),(1,-2),(-1,-2),(1,2),(-1,2)]:
    #             for x,y in points:
    #                 if 0<=x+dx<N and 0<=y+dy<N:
    #                     new_points.append((x+dx,y+dy))
    #         return new_points
    #     for _ in range(K):
    #         candidates=cal(candidates)
    #     return len(candidates)/float(8**K)

    # Solution 2 dfs with memory
    def knightProbability(self, N, K, r, c):
        memo={}
        def dfs(x,y,k):
            if not (0<=x<N and 0<=y<N): return 0
            if k==0: return 1
            if (x,y,k) not in memo:
                memo[x,y,k]=0.125*sum(dfs(x+i,y+j,k-1)+dfs(x+j,y+i,k-1) for i in (1,-1) for j in (2,-2))
            return memo[(x,y,k)]
        return dfs(r,c,K)

a=Solution()
print(a.knightProbability(3,2,0,0))