# Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
# Output: [true,false,true,true,false]
# Explanation:
# "FooBar" can be generated like this "F" + "oo" + "B" + "ar".
# "FootBall" can be generated like this "F" + "oot" + "B" + "all".
# "FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".

# 思路: valid的条件是1.pattern在word中 2.pattern和word的大写字母序列相同

class Solution:
    def camelMatch(self, queries, pattern):
        def check(word):
            it=iter(word)
            return all(c in it for c in pattern)
        def findupper(word):
            return [c for c in word if c.isupper()]
        upperP=findupper(pattern)
        return [check(word) and findupper(word)==upperP for word in queries]

a=Solution()
print(a.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"],"FB"))