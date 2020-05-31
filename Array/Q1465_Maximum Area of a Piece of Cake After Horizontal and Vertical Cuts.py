
# 思路: 切割之后找到最大的x gap和最大的y gap即可

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts, verticalCuts):
        hs = [0] + sorted(horizontalCuts) + [h]
        ws = [0] + sorted(verticalCuts) + [w]
        return max(hs[i]-hs[i-1] for i in range(1,len(hs)))*max(ws[i]-ws[i-1] for i in range(1,len(ws)))%(10**9+7)

a=Solution()
print(a.maxArea(5,4,[3,1],[1]))
print(a.maxArea(5,4,[3],[3]))