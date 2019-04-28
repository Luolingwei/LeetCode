# Input: [1,2,3]
# Output: [1,2] (of course, [1,3] will also be ok)

# Input: [1,2,4,8]
# Output: [1,2,4,8]

# 思路: 将数组从小到大排序，每来一个新的数，将其加到可以加的最长的数组末尾 (这个更新后的数组作为新数组添加到dp中)，（可以加的条件是这个num可以整除数组尾部数字）.最后返回dp中的最长数组即可

class Solution:
    def largestDivisibleSubset(self, nums):
        dp=[[]]
        for n in sorted(nums):
            dp.append(max((s for s in dp if not s or n%s[-1]==0),key=len)+[n])
        return max(dp,key=len)

a=Solution()
print(a.largestDivisibleSubset([1,4,6]))
print(a.largestDivisibleSubset([1,2,4,8]))