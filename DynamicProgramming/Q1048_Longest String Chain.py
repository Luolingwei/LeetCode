# Input: ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: one of the longest word chain is "a","ba","bda","bdca".

# 思路: dp, 将word以长度排序，用dic存储以之前所有word结尾的chain的最长长度，dp[word]=max(dp.get(word,1), dp.get(word减一个字母,0)+1)

class Solution:
    def longestStrChain(self, words):
        dp={}
        for word in sorted(words,key=len):
            for i in range(len(word)):
                dp[word]=max(dp.get(word,1),dp.get(word[:i]+word[i+1:],0)+1)
        return max(dp.values() or [1])

a=Solution()
print(a.longestStrChain([]))
print(a.longestStrChain(["a","b","ba","bca","bda","bdca"]))
print(a.longestStrChain(["a","b","ba","bca","bda","beua"]))
print(a.longestStrChain(["qyssedya","pabouk","mjwdrbqwp","vylodpmwp","nfyqeowa","pu","paboukc","qssedya","lopmw","nfyqowa","vlodpmw","mwdrqwp","opmw","qsda","neo","qyssedhyac","pmw","lodpmw","mjwdrqwp","eo","nfqwa","pabuk","nfyqwa","qssdya","qsdya","qyssedhya","pabu","nqwa","pabqoukc","pbu","mw","vlodpmwp","x","xr"]))