class Solution:
    def heightChecker(self, heights):
        return sum(i!=j for i,j in zip(heights,sorted(heights)))

a=Solution()
print(a.heightChecker([1,1,4,2,1,3]))
print(a.heightChecker([2,1]))