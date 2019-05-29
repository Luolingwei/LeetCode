class Solution:
    # Solution 1
    # def checkSubarraySum(self, nums, k):
    #     s=[0]*(len(nums)+1)
    #     for i in range(len(nums)+1): s[i]=s[i-1]+nums[i-1]
    #     for length in range(2,len(s)):
    #         for left in range(len(s)-length):
    #             if not k:
    #                 if s[left+length]-s[left]==0:return True
    #             else:
    #                 if (s[left+length]-s[left])%k==0:return True
    #     return False

    # Solution 2 用dic记录不同长度连续数组的余数
    def checkSubarraySum(self, nums, k):
        S,reminder={0:-1},0
        for i,num in enumerate(nums):
            if k:
                reminder=(reminder+num)%k
            else:
                reminder+=num
            if reminder in S:
                if i-S[reminder]>=2:
                    return True
            else: #保持尽量靠前位置的余数, 有相同余数出现时不要覆盖之前的pos
                S[reminder]=i
        return False


a=Solution()
print(a.checkSubarraySum([23, 2, 4, 6, 7],6))
print(a.checkSubarraySum([23, 2, 6, 4, 7],6))
print(a.checkSubarraySum([23, 2, 6, 4, 7],0))
print(a.checkSubarraySum([0,0],0))