# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
#
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

# 思路1: expand from enter，累加每个center的回文数量
# 思路2: dp[i][j]表示以i,j开头结尾的是否是回文，如果s[i]!=s[j]:dp[i][j]=0 如果s[i]==s[j]:dp[i][j]=dp[i+1][j-1]

class Solution:
    # solution 1 expand from center  132 ms
    def countSubstrings(self, s):
        self.ans,L=0,len(s)
        def checker(i,j):
            while i>=0 and j<L:
                if s[i]==s[j]:self.ans+=1
                else:break
                i,j=i-1,j+1
        for center in range(L):
            checker(center,center),checker(center,center+1)
        return self.ans

    # solution 2 dp  320 ms
    # def countSubstrings(self, s):
    #     L=len(s)
    #     dp=[[1]*L for _ in range(L)]
    #     for gap in range(1,L):
    #         for left in range(L-gap):
    #             right=left+gap
    #             if s[left]==s[right]: dp[left][right]=dp[left+1][right-1]
    #             else: dp[left][right]=0
    #     return sum(dp[i][j] for i in range(L) for j in range(i,L))

a=Solution()
print(a.countSubstrings("aaa"))
print(a.countSubstrings("aba"))
print(a.countSubstrings("abc"))
print(a.countSubstrings("abhcjkdemoxdiasjdmeaopdiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"))