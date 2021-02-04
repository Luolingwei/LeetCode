
# 思路: 计算preSum和最少/最多吃的个数, 如果最少的不会吃过target个数, 最多的能吃到target个数, 那么就能吃到

class Solution:
    def canEat(self, candiesCount, queries):
        for i in range(1,len(candiesCount)): candiesCount[i]+=candiesCount[i-1]
        return [d<candiesCount[t] and (t==0 or candiesCount[t-1]<(d+1)*c) for t, d, c in queries]

a=Solution()
print(a.canEat([7,4,5,3,8], [[0,2,2],[4,2,4],[2,13,1000000000]]))
print(a.canEat([5,2,6,4,1], [[3,1,2],[4,10,3],[3,10,100],[4,100,30],[1,3,1]]))