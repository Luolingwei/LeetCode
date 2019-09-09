# Input: distance = [1,2,3,4], start = 0, destination = 3
# Output: 4
# Explanation: Distance between 0 and 3 is 6 or 4, minimum is 4.

# 思路: 分为start到destination和剩下的,两个部分相互比较即可

class Solution:
    def distanceBetweenBusStops(self, distance, start: int, destination: int):
        s,sub1=sum(distance),sum(distance[min(start,destination):max(start,destination)])
        return min(sub1,s-sub1)

a=Solution()
print(a.distanceBetweenBusStops([1,2,3,4],0,3))
print(a.distanceBetweenBusStops([7,10,1,12,11,14,5,0],7,2))