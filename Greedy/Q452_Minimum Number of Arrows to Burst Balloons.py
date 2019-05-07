# Input:
# [[10,16], [2,8], [1,6], [7,12]]
#
# Output:
# 2
#
# Explanation:
# One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).

# 思路: 以尾部元素排序，每加入一个point，如果在第二个start小于当前end，则一并消除，此时不更新end。如果出现新的start大于end，则需要count+1，并更新end。

class Solution:
    def findMinArrowShots(self, points):
        points.sort(key=lambda x:x[1])
        ans,end=0,float('-inf')
        for point in points:
            if point[0]>end:
                ans+=1
                end=point[1]
        return ans

a=Solution()
print(a.findMinArrowShots([[10,16], [2,8], [1,6], [7,12]]))