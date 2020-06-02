
# 思路: Greedy, 先构建Fib数列, 从大往小找, 找到<=k的数, 减掉

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        n,res = 0,0
        nums = [1,1]
        while n<=k:
            n = nums[-1]+nums[-2]
            nums.append(n)
        i = len(nums)-1
        while k:
            while nums[i]>k:
                i-=1
            k-=nums[i]
            res+=1
        return res


a=Solution()
print(a.findMinFibonacciNumbers(7))
print(a.findMinFibonacciNumbers(10))