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
    #     N,res=len(S),0
    #     for i in range(N-k+1):
    #         if len(set(S[i:i+k]))==k-1:
    #             res+=1
    #     return res


a=Solution()
print(a.count("abc",2))
print(a.count("aba",2))
print(a.count("aa",1))