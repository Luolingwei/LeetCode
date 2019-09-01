# Input: s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
# Output: [true,false,false,true,true]
# Explanation:
# queries[0] : substring = "d", is palidrome.
# queries[1] : substring = "bc", is not palidrome.
# queries[2] : substring = "abcd", is not palidrome after replacing only 1 character.
# queries[3] : substring = "abcd", could be changed to "abba" which is palidrome. Also this can be changed to "baab" first rearrange it "bacd" then replace "cd" with "ab".
# queries[4] : substring = "abcda", could be changed to "abcba" which is palidrome.

# 思路: 因为可以无限次数的调整顺序，所以只需要计算每个query里面的奇数个数的字母即可, odds//2<=最大replace数k即可

class Solution:
    def canMakePaliQueries(self, s, queries):
        chars,Schars=[0]*26,[[0]*26]
        res=[False]*len(queries)
        for c in s:
            chars[ord(c)-ord('a')]+=1
            Schars.append(chars[:])
        for i,q in enumerate(queries):
            l,r,k=q[0],q[1],q[2]
            odds=sum((b-a)&1 for b,a in zip(Schars[r+1],Schars[l]))
            res[i]=odds//2<=k
        return res

a=Solution()
print(a.canMakePaliQueries("abcda",[[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]))