class Solution:
    def wordBreak(self, s, wordDict):
        dp=[[""]]+[[] for _ in range(len(s))]
        for i in range(1,len(s)+1):
            for j in range(i):
                if dp[j]!=[]:
                    if s[j:i] in wordDict:
                        dp[i]+=[char+' '+s[j:i] if char else s[j:i] for char in dp[j]]
        return dp[-1]

a=Solution()
print(a.wordBreak("catsanddog",["cat", "cats", "and", "sand", "dog"]))
print(a.wordBreak("pineapplepenapple",["apple", "pen", "applepen", "pine", "pineapple"]))