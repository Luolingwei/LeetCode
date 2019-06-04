
# B全部在某个word中的条件是B中每个字符出现的最高频率能被word cover住.
# 所以用Counter的并集操作统计字符在每个B中word出现的最高频率. 并与A中的每一个word进行比较.

import collections

class Solution:
    def wordSubsets(self, A, B):
        ans=[]
        freqB=collections.Counter()
        for word in B:
            freqB|=collections.Counter(word)
        for word in A:
            dicA=collections.Counter(word)
            if all(freqB[char]<=dicA[char] for char in freqB):
                ans.append(word)
        return ans

a=Solution()
print(a.wordSubsets(["amazon","apple","facebook","google","leetcode"],["e","o"]))
print(a.wordSubsets(["amazon","apple","facebook","google","leetcode"],["l","e"]))
print(a.wordSubsets(["amazon","apple","facebook","google","leetcode"],["e","oo"]))
print(a.wordSubsets(["amazon","apple","facebook","google","leetcode"],["eo","lo"]))
print(a.wordSubsets(["amazon","apple","facebook","google","leetcode"],["ec","oc","ceo"]))