
# 思路: 按substring统计frequency即可

class Solution:
    def beautySum(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            memo = [0]*26
            for j in range(i,len(s)):
                memo[ord(s[j])-97] += 1
                diff = max(memo) - min([x for x in memo if x>0])
                res += diff
        return res


a=Solution()
print(a.beautySum("aabcb"))
print(a.beautySum("aabcbaa"))