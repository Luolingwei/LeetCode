class Solution:
    def distributeCandies(self, candies):
        return min(len(candies)//2,len(set(candies)))

a=Solution()
print(a.distributeCandies([1,1,2,2,3,3]))
print(a.distributeCandies([1,1,2,3]))


