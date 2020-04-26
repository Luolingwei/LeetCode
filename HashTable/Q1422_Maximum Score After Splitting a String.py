from collections import Counter

# 思路: 先用HashTable记录全局数量即可

class Solution:
    def maxScore(self, s: str) -> int:
        memo = Counter(s)
        left0=0
        left1=0
        ans = 0
        for l in range(len(s)-1):
            if s[l]=='0':
                left0+=1
            else:
                left1+=1
            curScore = left0 + memo['1']-left1
            ans = max(ans,curScore)
        return ans

a=Solution()
print(a.maxScore("011101"))
print(a.maxScore("1111"))