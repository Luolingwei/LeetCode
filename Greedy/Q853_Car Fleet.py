# Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
# Output: 3
# Explanation:
# The cars starting at 10 and 8 become a fleet, meeting each other at 12.
# The car starting at 0 doesn't catch up to any other car, so it is a fleet by itself.
# The cars starting at 5 and 3 become a fleet, meeting each other at 6.
# Note that no other cars meet these fleets before the destination, so the answer is 3.

# 思路: 按时间和位置进行排序，由于时间是下降的，所以每新来一个pair，判断其位置是否在最前面，如果是则形成一个新的fleet.否则会被合并到其他fleet中
# 注意ans中的pos是升序排列的（单调栈），所以只需要比较末尾的pos.

class Solution:
    def carFleet(self, target, position, speed):
        pairs=[(pos,(target-pos)/v) for pos,v in zip(position,speed)]
        ans=[]
        for new_pair in sorted(pairs,key=lambda x:(-x[1],-x[0])):
            if not ans or new_pair[0]>ans[-1][0]:
                ans.append(new_pair)
        return len(ans)

a=Solution()
print(a.carFleet(10,[0,4,2],[2,1,3]))
print(a.carFleet(12,[10,8,0,5,3],[2,4,1,1,3]))
print(a.carFleet(12,[],[]))
print(a.carFleet(10,[4,6],[3,2]))