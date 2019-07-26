# Input: "ABC"
# Output: 10
# Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
# Evey substring is composed with only unique letters.
# Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10

# 思路: 问题转化为以每个字母为unique char的子串的数量总和(不去重)
# 先将字符串转成数字表示，然后对26个字母计算index的位置，计算每个位置的字母可以形成的unique string的个数
# 用Counter先记录每个字母的index集.，避免重复遍历S

import collections
class Solution:
    # Solution 1 332 ms
    # def uniqueLetterString(self, S):
    #     S,ans,N=[ord(c)-ord('a') for c in S.lower()],0,len(S)
    #     for c in range(26):
    #         indexs=[i for i in range(N) if S[i]==c]
    #         for i in range(len(indexs)):
    #             pre=indexs[i]-(indexs[i-1] if i>0 else -1)
    #             after=(indexs[i+1] if i<len(indexs)-1 else N)-indexs[i]
    #             ans+=pre*after
    #     return ans%(10**9+7)

    # Solution 2 92 ms
    def uniqueLetterString(self, S):
        c,N,ans=collections.defaultdict(list),len(S),0
        for i,char in enumerate(S):
            c[char].append(i)
        for idx in c.values():
            idx=[-1]+idx+[N]
            ans+=sum((idx[i]-idx[i-1])*(idx[i+1]-idx[i]) for i in range(1,len(idx)-1))
        return ans%(10**9+7)

a=Solution()
print(a.uniqueLetterString("ABC"))
print(a.uniqueLetterString("ABA"))