# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
#   "cats and dog",
#   "cat sand dog"
# ]

# 思路: 用dfs搜索，每次切割在dic中的单词，直到字符串切割完
# 用dp减少搜索次数，每次切割之前判断字符串s能否被切割成dic中的单词(和word break I相同)

class Solution:
    def wordBreak(self,s,wordDict):
        ans,dic=[],set(wordDict)
        def dfs(path,s):
            if not s:
                ans.append(path[:-1])
            if self.check(s,dic):
                for i in range(len(s)+1):
                    if s[:i] in dic:
                        dfs(path+s[:i]+' ',s[i:])
        dfs('',s)
        return ans

    def check(self, s,wordDict):
        dp=[True]+[False]*len(s)
        for i in range(1,len(s)+1):
            for j in range(i):
                if dp[j]==True:
                    if s[j:i] in wordDict:
                        dp[i]=True
        return dp[-1]

a=Solution()
print(a.wordBreak("catsanddog",["cat", "cats", "and", "sand", "dog"]))
print(a.wordBreak("pineapplepenapple",["apple", "pen", "applepen", "pine", "pineapple"]))