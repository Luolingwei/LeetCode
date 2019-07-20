# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]

# 思路: 将新interval用bisect按start插入，然后merge整个intervals

import bisect
class Solution:
    def insert(self, intervals, newInterval):
        bisect.insort(intervals,newInterval)
        merged=[]
        for start,end in intervals:
            if not merged or start>merged[-1][1]:
                merged.append([start,end])
            else:
                merged[-1][1]=max(merged[-1][1],end)
        return merged

a=Solution()
print(a.insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))