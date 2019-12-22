
# 思路: 出现次数最多的符合条件的substring只需要考虑minsize，因为如果有更大的size的substring,其中的小的substring也出现了同样的次数

import collections
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        N=len(s)
        count=collections.Counter()
        freq=collections.Counter(s[:minSize])
        window=s[:minSize]
        distinct=len(freq)
        if distinct<=maxLetters: count[window]+=1
        for i in range(minSize,N):
            if not freq[s[i]]:
                distinct+=1
            freq[s[i]]+=1
            window+=s[i]
            window=window[1:]
            freq[s[i-minSize]]-=1
            if not freq[s[i-minSize]]:
                distinct-=1
            if distinct<=maxLetters: count[window]+=1
        return max(count.values() or [0])

a=Solution()
print(a.maxFreq("aababcaab",2,3,4))
print(a.maxFreq("aaaa",1,3,3))
print(a.maxFreq("aabcabcab",2,2,3))
print(a.maxFreq("abcde",2,3,3))