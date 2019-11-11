class Solution:
    # Solution 1 dp
    # def wordBreak(self, s,wordDict):
    #     dp=[True]+[False]*len(s)
    #     for i in range(1,len(s)+1):
    #         for j in range(i):
    #             if dp[j]==True:
    #                 if s[j:i] in wordDict:
    #                     dp[i]=True
    #     return dp[-1]

    # Solution 2 dfs
    def wordBreak(self, s,wordDict):
        dic=set(wordDict)
        def dfs(word,memo):
            if word in memo:
                return memo[word]
            if word in dic:
                memo[word]=1
                return True
            for i in range(1,len(word)):
                if word[:i] in dic and dfs(word[i:],memo):
                    memo[word]=1
                    return True
            memo[word]=0
            return False
        return dfs(s,{})


a=Solution()
print(a.wordBreak("leetcode",["leet","code"]))
print(a.wordBreak("applepenapple",["apple", "pen"]))
print(a.wordBreak("catsandog",["cats","dog","sand","and","cat"]))