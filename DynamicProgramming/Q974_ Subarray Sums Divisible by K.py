# Input: A = [4,5,0,-2,-3,1], K = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by K = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

# 思路: 用dic记录余数出现的次数，遇到相同的reminder,ans+=dic[reminder],dic[reminder]+=1
# 注意这种divisible by k问题都是记录当前余数，与之前相等的余数去计算.

import collections
class Solution:
    def subarraysDivByK(self, A, K):
        dic=collections.defaultdict(int)
        dic[0],reminder,ans=1,0,0
        for num in A:
            reminder=(reminder+num)%K
            ans+=dic[reminder]
            dic[reminder]+=1
        return ans

a=Solution()
print(a.subarraysDivByK([4,5,0,-2,-3,1],5))