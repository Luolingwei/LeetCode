
# 思路: 根据Start从小到大排序, 检查end是否落在curEnd之内即可

class Solution:
    def removeCoveredIntervals(self, intervals):
        intervals.sort(key = lambda x: (x[0], -x[1]))
        curEnd = -1
        duplicate = 0
        for i,j in intervals:
            if j<=curEnd:
                duplicate+=1
            else:
                curEnd = j
        return len(intervals)-duplicate


a=Solution()
print(a.removeCoveredIntervals([[1,4],[3,6],[2,8]]))
print(a.removeCoveredIntervals([[1,4],[2,3]]))
print(a.removeCoveredIntervals([[0,10],[5,12]]))
print(a.removeCoveredIntervals([[3,10],[4,10],[5,11]]))