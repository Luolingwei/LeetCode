# Input: text = "ababa"
# Output: 3
#
# Input: text = "aaabaaa"
# Output: 6

# 思路: 一共有两种情况，1.最长的字符串extend 1 2. 两个字符串连起来

from collections import Counter
import itertools
class Solution:
    def maxRepOpt1(self, text):
        A=[[key,len(list(s))] for key,s in itertools.groupby(text)]
        dic=Counter(text)
        # 先考虑只extend 1的情况
        ans=max(min(dic[c],n+1) for c,n in A)
        # 然后考虑字符串连起来的情况
        for i in range(1,len(A)-1):
            if A[i-1][0]==A[i+1][0] and A[i][1]==1:
                ans=max(ans,min(dic[A[i-1][0]],A[i-1][1]+A[i+1][1]+1))
        return ans

a=Solution()
print(a.maxRepOpt1('aaaabbaaaa'))
print(a.maxRepOpt1('aaaabaaaa'))