# Input: trips = [[2,1,5],[3,3,7]], capacity = 4
# Output: false

# 思路: 记录每个时间点的人数变化，正数表示上人，负数表示下人，如果时间点相同先下后上.

class Solution:
    def carPooling(self, trips, capacity):
        changes=sorted([x for n,i,j in trips for x in [(i,n),(j,-n)]])
        for _,change in changes:
            capacity-=change
            if capacity<0:
                return False
        return True

a=Solution()
print(a.carPooling([[2,1,5],[3,3,7]],4))
print(a.carPooling([[2,1,5],[2,5,7]],2))