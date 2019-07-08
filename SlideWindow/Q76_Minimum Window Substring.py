# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"

# 思路: Sliding window
# 1. 用missing 记录还需要的字母个数，当missing=0的时候，得到右边界j，注意这里用Counter类型的need判断是否真正需要，因为可能T中有多个重复字母.
# 2. 得到i后，缩小左边界i(need[c]<0)，找出真正的最小范围[i:j]，用min_i,min_j更新最小范围.
# 3. 将左边界右移一个，继续寻找下一个window..

import collections
class Solution:
    def minWindow(self, s, t):
        missing,need=len(t),collections.Counter(t)
        i,min_i,min_j=0,float('-inf'),float('inf')
        for j,char in enumerate(s):
            missing-=need[char]>0
            need[char]-=1
            if not missing:
                while need[s[i]]<0:need[s[i]]+=1;i+=1
                if j-i<min_j-min_i:min_i,min_j=i,j
                need[s[i]]+=1;i+=1;missing+=1
        return s[min_i:min_j+1] if min_j!=float('inf') else ""

a=Solution()
print(a.minWindow("ADOBECODEBANC","ABC"))
print(a.minWindow("ABCDR","XDF"))