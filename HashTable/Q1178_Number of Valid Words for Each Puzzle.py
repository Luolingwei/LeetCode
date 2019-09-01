# Input:
# words = ["aaaa","asas","able","ability","actt","actor","access"],
# puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
# Output: [1,1,3,2,4,0]
# Explanation:
# 1 valid word for "aboveyz" : "aaaa"
# 1 valid word for "abrodyz" : "aaaa"
# 3 valid words for "abslute" : "aaaa", "asas", "able"
# 2 valid words for "absoryz" : "aaaa", "asas"
# 4 valid words for "actresz" : "aaaa", "asas", "actt", "access"
# There're no valid words for "gaswxyz" cause none of the words in the list contains letter 'g'.

# 思路: 首先建立words的Counter，记录每种word的个数（用bit表示word）
# 对于每个puzzle，要使得word包含第一个字母且字母都在puzzle中，计算所有包含第一个字母的combinations，去Counter中取words即可

import collections
class Solution:
    # Solution 1 using frozenset 864 ms (可变set不可作为dic的key)
    # def findNumOfValidWords(self, words, puzzles):
    #     count=collections.Counter(frozenset(w) for w in words)
    #     res=[]
    #     for p in puzzles:
    #         subs=[p[0]]
    #         for c in set(p[1:]):
    #             subs+=[sub+c for sub in subs]
    #         res.append(sum(count[frozenset(sub)] for sub in subs))
    #     return res

    # Solution 2 using bit 620 ms
    def findNumOfValidWords(self, words, puzzles):
        count=collections.Counter()
        for w in words:
            bits=0
            for c in w:
                bits|=1<<(ord(c)-97)
            count[bits]+=1
        res=[]
        for p in puzzles:
            subs=[1<<(ord(p[0])-97)]
            for c in set(p[1:]):
                subs+=[sub|1<<(ord(c)-97) for sub in subs]
            res.append(sum(count[sub] for sub in subs))
        return res

a=Solution()
print(a.findNumOfValidWords(["aaaa","asas","able","ability","actt","actor","access"],["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]))