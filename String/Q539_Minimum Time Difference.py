# Input: ["23:59","00:00"]
# Output: 1

# 思路: 将time转换为minute单位，然后进行排序，取相邻最小interval，最后加上首尾interval进行对比.

class Solution:
    def findMinDifference(self, timePoints):
        time=sorted([int(s[:2])*60+int(s[-2:]) for s in timePoints])
        MinSapn=float('inf')
        for i in range(len(time)-1):
            MinSapn=min(MinSapn,time[i+1]-time[i])
        EndsSpan=time[0]+1440-time[-1]
        return min(EndsSpan,MinSapn)

a=Solution()
print(a.findMinDifference(["23:59","00:00"]))