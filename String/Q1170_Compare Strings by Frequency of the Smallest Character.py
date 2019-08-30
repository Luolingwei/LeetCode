# Input: queries = ["cbd"], words = ["zaaaz"]
# Output: [1]
# Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").
#
# Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
# Output: [1,2]
# Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").

# 思路: 分别构建words和queries的数组，然后用bisect寻找比queries里面大的

import bisect
class Solution:
    def numSmallerByFrequency(self, queries, words):
        dic=sorted(w.count(min(w)) for w in words)
        L=len(dic)
        return [L-bisect.bisect_right(dic,q.count(min(q))) for q in queries]

a=Solution()
print(a.numSmallerByFrequency(["cbd"],["zaaaz"]))
print(a.numSmallerByFrequency(["bbb","cc"],["a","aa","aaa","aaaa"]))