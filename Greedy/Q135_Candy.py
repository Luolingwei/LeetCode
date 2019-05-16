# Input: [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
#
# Input: [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
#              The third child gets 1 candy because it satisfies the above two conditions.

# 思路: 想成一条上下起伏的线，从下到上都一定是从1开始...一直到顶，顶端元素的值等于max(左右的长度)+1

class Solution:
    def candy(self, ratings):
        l=len(ratings)
        res=[1]*len(ratings)
        for i in range(1,l):
            if ratings[i]>ratings[i-1]:
                res[i]=res[i-1]+1
        for j in range(l-2,-1,-1):
            if ratings[j]>ratings[j+1]:
                res[j]=max(res[j],res[j+1]+1)  #max用来处理peek的情况，让peek取两边的max
        return sum(res)

a=Solution()
print(a.candy([1,3,4,5,8,4,2,1,9]))
print(a.candy([1,2,3,3,4]))
print(a.candy([1,1,3,3,1]))