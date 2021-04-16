# Input: s = "bedbathandbeyand", dict = ["bed", "bath", "bat", "and", "hand", "bey", "beyand"]
# Output: ["bed", "bath", "and", "beyand"] or ["bed", "bat", "hand", "beyand"]

# 思路: bfs, 每次对path加上一个word(dict中的任意一个), 直到输出target s.

class Solution:
    # dp 每个word只能用一次
    # def findMin(self,s,dict):
    #     dp={"":[]}
    #     for word in dict:
    #         for strs in list(dp.keys()):
    #             if s[len(strs):len(strs)+len(word)]==word:
    #                 new_strs=strs+word
    #                 if new_strs not in dp or len(dp[new_strs])>len(dp[strs])+1:
    #                     dp[new_strs]=dp[strs]+[word]
    #     return dp[s]

    # bfs
    def findMin(self,s,dict):
        bfs={"":[]}
        while bfs:
            new_bfs={}
            for strs in bfs:
                if strs==s: return bfs[strs]
                for word in dict:
                    if s[len(strs):len(strs)+len(word)]==word:
                        new_bfs[strs+word]=bfs[strs]+[word]
            bfs=new_bfs
        return []


a=Solution()
print(a.findMin("bedbathandbeyand",["bed", "bath", "bat", "and", "hand", "bey", "beyand"]))
print(a.findMin("catsandog",["cats", "dog", "sand", "and", "cat"]))
print(a.findMin("aaaaa",["aa","a"]))
print(a.findMin("aaaaaaaa",["a","aa","aaa","aaaa","aaaaa","aaaaaa"]))