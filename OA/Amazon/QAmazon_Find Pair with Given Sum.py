
# 和movies on flight的区别在于这里要求两个数加起来正好等于target-30，所以可以不用sort, 用HashMap记录n到index的映射, O(n)解决

class Solution:
    def find(self,nums,target):
        target=target-30
        memo,maxN,ans={},float('-inf'),[]
        for i,n in enumerate(nums):
            if target-n in memo:
                pair=[memo[target-n],i]
                if max(pair)>maxN:
                    maxN=max(pair)
                    ans=pair
            else:
                memo[n]=i
        return ans

a=Solution()
print(a.find([1, 10, 25, 35, 60],90))
print(a.find([20, 50, 40, 25, 30, 10],90))
print(a.find([20, 50, 40, 25, 30, 10],800))