# Input: [1,2,3,3,4,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences :
# 1, 2, 3
# 3, 4, 5

# 思路: 每次取一个数组中的数i，如果能加到当前的数组末尾，则加，修改end.
# 如果不能加，则在数组中取i+1,i+2构成新的数组
# 如果两种方法都不行，返回False.

import collections
class Solution:
    def isPossible(self, nums):
        left=collections.Counter(nums)
        end=collections.Counter()
        for i in nums:
            if not left[i]: continue
            left[i]-=1
            if end[i-1]>0:
                end[i-1]-=1
                end[i]+=1
            elif left[i+1] and left[i+2]:
                left[i+1]-=1
                left[i+2]-=1
                end[i+2]+=1
            else:
                return False
        return True

a=Solution()
print(a.isPossible([1,2,3,3,4,5]))
print(a.isPossible([1,2,3,4,5,5,6,7]))