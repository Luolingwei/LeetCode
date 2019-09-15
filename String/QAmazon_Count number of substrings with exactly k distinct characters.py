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

# 思路: 从以每个字母开头进行考虑，计算distinct正好为k的子串数量，累加起来

class Solution:
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

a=Solution()
print(a.count("abc",2))
print(a.count("aba",2))
print(a.count("aa",1))