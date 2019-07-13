# row 1: 0
# row 2: 01
# row 3: 0110
# row 4: 01101001

# 思路: 下一行的数与上一行对应位置的数相同(奇数位)或相反(偶数位)
# ^1取相反，^0取相同

class Solution:
    def kthGrammar(self, N, K):
        if N==1 and K==1:
            return 0
        return self.kthGrammar(N-1,(K+1)//2)^K%2^1

a=Solution()
print(a.kthGrammar(1,1))
print(a.kthGrammar(2,1))
print(a.kthGrammar(2,2))
print(a.kthGrammar(4,5))