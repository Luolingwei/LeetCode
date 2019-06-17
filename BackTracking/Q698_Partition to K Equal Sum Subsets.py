# Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# Output: True
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

# 思路: 与Q473火柴题类似，构造k个target，分别进行dfs减，如果最后所有数字能进入k个桶，return True.
# 注意需要backtracking 和 从大到小sort数组(减少dfs次数).

class Solution:
    def canPartitionKSubsets(self, nums, k):
        s,N=sum(nums),len(nums)
        if s%k!=0: return False
        target=s//k
        targets=[target]*k
        nums.sort(reverse=True) #先填大数，减少dfs次数
        if nums[0]>target: return False
        def dfs(pos):
            if pos==N: return True
            for i in range(k):
                if targets[i]>=nums[pos]:
                    targets[i]-=nums[pos]
                    if 0<targets[i]<nums[-1]:  #判断当前剩余空间是否小于最小数，如果是，则直接backtracking
                        targets[i]+=nums[pos]
                        continue
                    if dfs(pos+1):
                        return True
                    targets[i]+=nums[pos]
            return False
        return dfs(0)

a=Solution()
print(a.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1],4))