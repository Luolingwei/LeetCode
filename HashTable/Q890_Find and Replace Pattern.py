# Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# Output: ["mee","aqq"]
# Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}.
# "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
# since a and b map to the same letter.

# 思路: check两个字符串pattern是否相等的简单方法: len(set(word))==len(set(zip(pattern,word)))==target

class Solution:
    def findAndReplacePattern(self, words, pattern):
        target=len(set(pattern))
        def check(word):
            return len(set(word))==len(set(zip(pattern,word)))==target
        return list(filter(check,words))

a=Solution()
print(a.findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"],'abb'))