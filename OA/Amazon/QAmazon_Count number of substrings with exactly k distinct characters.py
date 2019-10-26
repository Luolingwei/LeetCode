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

# 思路1: 用Counter计数window中的各字母个数, 动态计算distinct
# 思路2: 由于是k size k distinct，说明所有字母不同，类似Q3解法

import collections
class Solution:

    # 1: 长度不固定，计算distinct 字母=k的子串个数
    # def count(self,S,k):
    #     N,res=len(S),0
    #     for i in range(N):
    #         distinct=0
    #         memo_c=[0]*26
    #         for j in range(i,N):
    #             if memo_c[ord(S[j])-97]==0:
    #                 distinct+=1
    #                 memo_c[ord(S[j])-97]=1
    #             if distinct>=k:
    #                 if distinct==k: res+=1
    #                 else: break
    #     return res

    # 2: 长度固定，长度=k，distinct 字母=k
    # def count(self,S,k):
    #     N,window=len(S),collections.Counter(S[:k])
    #     distinct,ans=len(window),set()
    #     if distinct==k: ans.add(S[:k])
    #     for i in range(k,N):
    #         if not window[S[i]]:
    #             distinct+=1
    #         window[S[i]]+=1
    #         window[S[i-k]]-=1
    #         if not window[S[i-k]]:
    #             distinct-=1
    #         if distinct==k:
    #             ans.add(S[i-k+1:i+1])
    #     return list(ans)

    # 3 类似Q3 substring without repeating char
    def count(self,S,k):
        left,N=0,len(S)
        memo,ans={},set()
        for i,c in enumerate(S):
            if c in memo and memo[c]>=left:
                left=memo[c]+1
            memo[c]=i
            if i-left+1==k:
                ans.add(S[left:i+1])
                left+=1
        return list(ans)

a=Solution()
print(a.count("aabc",2))
print(a.count("aba",2))
print(a.count("aa",2))
print(a.count("abcabc",3))
print(a.count("abacab",3))
print(a.count("awaglknagawunagwkwagl",4))