# Input: [ [3,4], [2,3], [1,2] ]
#
# Output: [-1, 0, 1]
#
# Explanation: There is no satisfied "right" interval for [3,4].
# For [2,3], the interval [3,4] has minimum-"right" start point;
# For [1,2], the interval [2,3] has minimum-"right" start point.

# Input: [ [1,4], [2,3], [3,4] ]
#
# Output: [-1, 2, -1]
#
# Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
# For [2,3], the interval [3,4] has minimum-"right" start point.

# 思路：先构造[start,index]的数组，按start从小到大排序，问题就变成寻找大于end的最小start，用bisect寻找，然后取出该[start,index]，并返回index
#注: sorted默认按照[a,b]中第一个数排序，bisect默认按照[a,b]的第一个数进行对比排序。

import bisect
class Solution:
    def findRightInterval(self, intervals):
        starts=sorted([[interval[0],i] for i,interval in enumerate(intervals)])+[[float('inf'),-1]]
        return [starts[bisect.bisect(starts,[interval[1]])][1] for interval in intervals]

a=Solution()
print(a.findRightInterval([ [3,4], [2,3], [1,2] ]))
print(a.findRightInterval([ [1,4], [2,3], [3,4] ]))