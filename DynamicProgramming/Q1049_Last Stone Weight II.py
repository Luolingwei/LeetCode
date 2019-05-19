
# 思路: 问题等价于将stone分成两堆，求两堆stone总和的最小difference，考虑求出stones集合可以达到的weight集合，用sum减各个stone得到补集的weight，计算最小差距即可。

class Solution:
    def lastStoneWeightII(self, stones):
        sumW=sum(stones)
        weight={0}
        for stone in stones:
            weight|={stone+i for i in weight}
        return min(abs(sumW-i-i) for i in weight)

a=Solution()
print(a.lastStoneWeightII([2,7,4,1,8,1]))

