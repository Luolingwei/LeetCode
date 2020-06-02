from collections import Counter

# 思路1: 设定左边开始的index, 右边开始遍历, 一直到找到abc都包含的位置, O(n^2)
# 思路2: 为了不每次都从左边设定的index开始重新计算, 用sliding window, r往右一直到找到abc都包含, res+=N-r
# 然后把l往右移1步, 一直到出现0再把r往右移去寻找

class Solution:

    # def numberOfSubstrings(self, s: str) -> int:
    #     N = len(s)
    #     res = 0
    #     for i in range(N):
    #         curState = [0,0,0]
    #         for j in range(i,N):
    #             curState[ord(s[j])-97]+=1
    #             if 0 not in curState:
    #                 res += N-j
    #                 break
    #     return res

    def numberOfSubstrings(self, s: str) -> int:
        N = len(s)
        res = 0
        window = Counter({'a': 0, 'b': 0, 'c': 0})
        l = 0
        for r in range(N):
            window[s[r]] += 1
            while 0 not in window.values():
                res += N - r
                window[s[l]] -= 1
                l += 1
        return res

a=Solution()
print(a.numberOfSubstrings("abcabc"))
print(a.numberOfSubstrings("aaacb"))
print(a.numberOfSubstrings("abc"))