class Solution:
    def maxProfit (self,n):
        P,B=[0,10,9,8,7,6,5,4,3,2,1],3
        R=[0]*(n+1)
        babies=[[] for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,i+1):
                if R[i-j]+j*P[j]-B>R[i]:
                    R[i]=R[i-j]+j*P[j]-B
                    babies[i]=babies[i-j]+[j]
        return len(babies[n]),babies[n],R[n]

a=Solution()
print(a.maxProfit(3))