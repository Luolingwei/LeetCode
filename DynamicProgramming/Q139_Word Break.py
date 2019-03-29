class Solution:
    def wordBreak(self, s,wordDict):
        dp=[True]+[False]*len(s)
        for i in range(1,len(s)+1):
            for j in range(i):
                if dp[j]==True:
                    if s[j:i] in wordDict:
                        dp[i]=True
        return dp[-1]

a=Solution()
print(a.wordBreak("leetcode",["leet","code"]))
print(a.wordBreak("applepenapple",["apple", "pen"]))
print(a.wordBreak("catsandog",["cats","dog","sand","and","cat"]))