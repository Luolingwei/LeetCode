
# Solution 1: 用memo寻找周期，如果碰到memo中已经有的cells,N对周期取余
# Solution 2: 14为周期进行计算

class Solution:
    # def prisonAfterNDays(self, cells, N):
    #     memo = {}
    #     while N:
    #         memo[str(cells)] = N
    #         N -= 1
    #         cells = [0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in range(1, 7)] + [0]
    #         if str(cells) in memo:
    #             N %= memo[str(cells)] - N
    #     return cells

    def prisonAfterNDays(self, cells, N):
        N=(N-1)%14+1
        while N:
            N-=1
            cells=[0]+[cells[i-1]^cells[i+1]^1 for i in range(1,7)]+[0]
        return cells


a=Solution()
print(a.prisonAfterNDays([1,0,0,1,0,0,1,0],1000000000))