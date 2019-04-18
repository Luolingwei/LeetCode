# Input: nums is [1, 1, 1, 1, 1], S is 3.
# Output: 5
# Explanation:
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
#
# There are 5 ways to assign symbols to make the sum of nums be target 3.

class Solution:
    def findTargetSumWays(self, nums, S):
        dic={nums[0]:1,-nums[0]:1} if nums[0]!=0 else {0:2}
        for n in nums[1:]:
            temp={}
            for key in dic.keys():
                temp[key+n]=dic[key]+temp.get(key+n,0)
                temp[key-n]=dic[key]+temp.get(key-n,0)
            dic=temp
        return dic.get(S,0)

a=Solution()
print(a.findTargetSumWays([1, 1, 1, 1, 1],3))
print(a.findTargetSumWays([1, 2, 5, 2, 1],3))
print(a.findTargetSumWays([1,1,1,0],1))
print(a.findTargetSumWays([0,0,0,0,0,0,0,0,1],1))