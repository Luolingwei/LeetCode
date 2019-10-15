class Solution:
    def find(self,nums):
        # only record leftmost frequency
        memo={0:-1}
        count,ans=0,0
        for i,n in enumerate(nums):
            count+=(1 if n else -1)
            if count in memo:
                ans=max(ans,i-memo[count])
            else:
                memo[count]=i
        return ans

a=Solution()
print(a.find([0,1]))
print(a.find([0,1,0]))
print(a.find([0,1,0,0,0,1,0,1]))