# Input: str1 = "abac", str2 = "cab"
# Output: "cabac"
# Explanation:
# str1 = "abac" is a substring of "cabac" because we can delete the first "c".
# str2 = "cab" is a substring of "cabac" because we can delete the last "ac".
# The answer provided is the shortest such string that satisfies these properties.

# 先求出Longest Common String, 然后构造公共的总String

class Solution:
    def shortestCommonSupersequence(self, str1, str2):
        def LCS(A,B):
            m,n=len(A),len(B)
            dp=[['']*(n+1) for _ in range(m+1)]
            for i in range(m):
                for j in range(n):
                    if A[i]==B[j]:
                        dp[i+1][j+1]=dp[i][j]+A[i]
                    else:
                        dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j],key=len)
            return dp[-1][-1]
        ans,i,j='',0,0
        for char in LCS(str1,str2):
            while str1[i]!=char:
                ans+=str1[i]
                i+=1
            while str2[j]!=char:
                ans+=str2[j]
                j+=1
            ans+=char
            i,j=i+1,j+1
        return ans+str1[i:]+str2[j:]


a=Solution()
print(a.shortestCommonSupersequence("abac","cab"))