# Input: abc, k = 2
# Output: 2
# Possible substrings are {"ab", "bc"}
#
# Input: aba, k = 2
# Output: 3
# Possible substrings are {"ab", "ba", "aba"}
#
# Input: aa, k = 1
# Output: 3
# Possible substrings are {"a", "a", "aa"}

# 思路: 从以每个字母开头进行i卡

import collections
class Solution:

    # 1: 长度不固定，计算distinct 字母=k的子串个数
    def count(self,S,k):
        N,res=len(S),0
        for i in range(N):
            distinct=0
            memo_c=[0]*26
            for j in range(i,N):
                if memo_c[ord(S[j])-97]==0:
                    distinct+=1
                    memo_c[ord(S[j])-97]=1
                if distinct>=k:
                    if distinct==k: res+=1
                    else: break
        return res

    # 2: 长度固定，长度=k，distinct 字母=k-1
    # def count(self,S,k):
    #     N,window=len(S),collections.Counter(S[:k])
    #     distinct,ans=len(window.keys()),0
    #     if distinct==k-1: ans+=1
    #     for i in range(k,N):
    #         if S[i] not in window:
    #             distinct+=1
    #         window[S[i]]+=1
    #         window[S[i-k]]-=1
    #         if not window[S[i-k]]:
    #             distinct-=1
    #         if distinct==k-1:
    #             ans+=1
    #     return ans


a=Solution()
print(a.count("aabc",2))
print(a.count("aba",2))
print(a.count("aa",2))