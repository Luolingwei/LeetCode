# Input: n = 5
# Output: 12
# Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.

# 思路: 先计算质数个数，然后用排列组合计算组合数即可.
# 计算质数: 从2开始到n**0.5，每个质因子分别乘i,i+1,i+2(i以前的不用重复考虑)，得到合数，并在A中抹去

import math
class Solution:
    def numPrimeArrangements(self, n):
        def countprime(n):
            A=[1]*(n+1)
            A[0],A[1]=0,0
            for i in range(2,int(n**0.5)+1):
                if A[i]:
                    A[i*i:n+1:i]=[0]*len(A[i*i:n+1:i])
            return sum(A)
        primes=countprime(n)
        return (math.factorial(primes)*math.factorial(n-primes))%(10**9+7)

a=Solution()
print(a.numPrimeArrangements(7))
print(a.numPrimeArrangements(5))
print(a.numPrimeArrangements(100))