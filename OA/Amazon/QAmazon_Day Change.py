# Input: [0,1,1,0],1
# Output: [1, 1, 1, 1]
#
# Input: [0,1,1,0],2
# Output: [1, 0, 0, 1]

# 思路: 用memo记录历史，找出循环

class Solution:
    def Change(self,nums,N):
        nums=[0]+nums+[0]
        memo={}
        while N:
            N-=1
            nums=[0]+[nums[i-1]^nums[i+1]^1 for i in range(1,9)]+[0]
            if str(nums) in memo:
                N%=memo[str(nums)]-N
        return nums[1:9]

a=Solution()
print(a.Change([0,1,0,1,1,0,0,1],7))