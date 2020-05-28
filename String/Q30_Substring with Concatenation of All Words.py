
# 思路: 起始index从左到右移动, 比较排序过后的所有words
# 完全一样即是符合条件的start index

class Solution:
    def findSubstring(self, s, words):
        if not words: return []
        words = sorted(words)
        memo = set(words)
        N, L = len(words), len(words[0])
        res = []
        for i in range(len(s)-N*L+1):
            if s[i:i+L] in memo:
                curwords = sorted(s[i+x:i+x+L] for x in range(0,N*L,L))
                if curwords == words:
                    res.append(i)
        return res


a=Solution()
print(a.findSubstring("barfoothefoobarman",["foo","bar"]))