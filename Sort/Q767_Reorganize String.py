# Input: S = "aab"
# Output: "aba"

# 思路: 与Q1054相同，利用奇偶index，将字母按频率从小到大排列后叉开.

import collections
class Solution:
    def reorganizeString(self, S):
        Count,N=collections.Counter(S),len(S)
        maxL=max(Count.values())
        if N-maxL<maxL-1: return ''
        array=sorted(S,key=lambda x:(Count[x],x))
        array[::2],array[1::2]=array[N//2:],array[:N//2]
        return ''.join(array)

a=Solution()
print(a.reorganizeString("aab"))
print(a.reorganizeString("aaab"))
print(a.reorganizeString("aaaeabbddbbcccdeffa"))
print(a.reorganizeString("aaaabbbb"))
print(a.reorganizeString("vvvloii"))