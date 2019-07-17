# Input: "abc"
# Output: 7
# Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".

# 思路: dp, 每来一个字母，以该字母结尾的数量=前一轮以其他字母结尾的所有子串数量+1
# 每一轮迭代，如果是重复字母，之前的子串数量会被覆盖，因为之前的子串与当前结尾的子串会重复,这样达到了去重的目的.

class Solution:
    def distinctSubseqII(self, S):
        end=[0]*26
        for c in S:
            end[ord(c)-ord('a')]=sum(end)+1
        return sum(end)%(10**9+7)

a=Solution()
print(a.distinctSubseqII("abc"))
print(a.distinctSubseqII("abab"))