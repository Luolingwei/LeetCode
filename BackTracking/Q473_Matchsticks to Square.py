# Input: [1,1,2,2,2]
# Output: true
#
# Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.

# Input: [3,3,3,3,4]
# Output: false
#
# Explanation: You cannot find a way to form a square with all the matchsticks.

# 思路: backtracking，设置pos从0开始，将数字赋给4个子target，如果能solve，则返回True，否则backtracking。终止条件为pos走到len(nums)，即所有num都被赋给target，此时4个子target都为0，返回True.

class Solution:
    def makesquare(self, nums):
        if len(nums)<4 or sum(nums)%4!=0: return False
        T=sum(nums)//4
        nums.sort(reverse=True)
        if nums[0]>T: return False
        target=[T]*4
        def dfs(pos):
            if pos==len(nums):return True
            for i in range(4):
                if target[i]>=nums[pos]:
                    target[i]-=nums[pos]
                    if 0<target[i]<nums[-1]:
                        target[i]+=nums[pos]
                        continue
                    if dfs(pos+1): return True
                    target[i]+=nums[pos]
            return False
        return dfs(0)

a=Solution()
print(a.makesquare([1,1,2,2,2]))
print(a.makesquare([3,3,3,3,4]))