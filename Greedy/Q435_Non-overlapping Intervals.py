# Input: [ [1,2], [2,3], [3,4], [1,3] ]
#
# Output: 1
#
# Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.

# Input: [ [1,2], [1,2], [1,2] ]
#
# Output: 2
#
# Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.

# Input: [ [1,2], [2,3] ]
#
# Output: 0
#
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

# 思路：以尾部元素排序，每加入一个interval，如果在第二个start小于当前end，则remove，此时不更新end。如果出现新的start大于等于end，则更新end。以end排序是为了让end增加的尽可能慢，移除的次数尽量少。

class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x:x[1])
        count,end=0,float('-inf')
        for interval in intervals:
            if interval[0]>=end:
                end=interval[1]
            else:
                count+=1
        return count

a=Solution()
print(a.eraseOverlapIntervals([ [1,2], [2,3], [3,4], [1,3] ]))
print(a.eraseOverlapIntervals([ [1,2], [1,2], [1,2] ]))
print(a.eraseOverlapIntervals([ [1,2], [2,3] ]))