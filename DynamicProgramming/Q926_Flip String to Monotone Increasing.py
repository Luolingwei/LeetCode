# Input: "00110"
# Output: 1
# Explanation: We flip the last digit to get 00111.

# 思路: i从开头到末尾，记录前面的0的个数，计算前面的1（length-pre0）+后面的0(sum0-pre0)，更新ans.

class Solution:
    def minFlipsMonoIncr(self, S):
        S='$'+S
        preZero,sumZero,ans=0,S.count('0'),float('inf')
        for i in range(len(S)):
            if S[i]=='0': preZero+=1
            ans=min(ans,i+sumZero-2*preZero)
        return ans

a=Solution()
print(a.minFlipsMonoIncr("00110"))
print(a.minFlipsMonoIncr("010110"))
print(a.minFlipsMonoIncr("00011000"))
print(a.minFlipsMonoIncr('0000'))
print(a.minFlipsMonoIncr('11011'))