
# 思路: 因为所有数都是正数, 找到前两大的数字即可

import heapq
class Solution:

    # def maxProduct(self, nums):
    #     nums = [-n for n in nums]
    #     heapq.heapify(nums)
    #     return (-heapq.heappop(nums) - 1) * (-heapq.heappop(nums) - 1)

    def maxProduct(self, nums):
        maxnum = [0,0]
        for n in nums:
            if n>maxnum[0]:
                maxnum = [n,maxnum[0]]
            elif n>maxnum[1]:
                maxnum[1] = n
        return (maxnum[0]-1)*(maxnum[1]-1)


a=Solution()
print(a.maxProduct([3,4,5,2]))
print(a.maxProduct([1,5,4,5]))
print(a.maxProduct([3,7]))