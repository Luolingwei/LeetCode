'''
let window size from N to 1, do a sliding window, as soon as we find repeated s in a size, just return
'''

class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        N=len(s)
        for L in range(N,0,-1):
            window=s[:L]
            memo={s[:L]}
            for j in range(L,N):
                window=window[1:]+s[j]
                if window in memo:
                    return L
                else:
                    memo.add(window)
        return 0