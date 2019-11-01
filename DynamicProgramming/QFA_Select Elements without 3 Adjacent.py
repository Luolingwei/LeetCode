class Solution:
    def pickK5(self,nums):
        N=len(nums)
        M=[float('-inf')]*N
        def dp(i):
            if M[i]==float('-inf'):
                if i==0: M[i]=max(nums[0],0)
                elif i==1: M[i]=max(max(nums[0],nums[1],nums[0]+nums[1]),0)
                elif i==2: M[i]=max(max(nums[0],nums[1],nums[2],nums[0]+nums[1],nums[0]+nums[2],nums[1]+nums[2]),0)
                else:
                    M[i]=max(nums[i]+nums[i-1]+dp(i-3),nums[i]+dp(i-2),dp(i-1))
            return M[i]
        maxN=max(nums)
        if maxN<=0: return maxN
        return dp(N-1)

a=Solution()
print(a.pickK5([1,2,3]))
print(a.pickK5([1,6,4,-5,3,2]))
print(a.pickK5([-1,-6,-4,-5,3,2]))
print(a.pickK5([-1,-6]))
print(a.pickK5([-1,1,-6,-7]))