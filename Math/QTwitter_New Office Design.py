
# 思路: 计算每两个pos之间的最大height即可

class Solution:
    def maxHeight(self,tablePositions, tableHeights):
        def helper(p1,p2,h1,h2):
            if p2-p1==1: return 0
            shorter,taller=min(h1,h2),max(h1,h2)
            gap=p2-p1-1
            if shorter+gap<=taller+1: # shorter可以一直累加
                return shorter+gap
            else:
                gap-=(taller-shorter) # 将shorter和taller累加到一样高后平均增加
                return taller+(gap+1)//2
        L=len(tablePositions)
        return max(helper(tablePositions[i-1],tablePositions[i],tableHeights[i-1],tableHeights[i]) for i in range(1,L))

a=Solution()
print(a.maxHeight([1,3,7],[4,3,3]))