class Solution:
    # solution 1 brute force 48 ms
    # def distributeCandies(self, candies: int, n: int):
    #     ans=[0]*n
    #     i=1
    #     while candies>0:
    #         ans[(i-1)%n]+=min(i,candies)
    #         candies-=i
    #         i+=1
    #     return ans

    # solution 2 math 48 ms
    def distributeCandies(self, candies: int, n: int):
        base,m,j=n*(n+1)//2,0,0
        while candies>base:
            candies-=base
            base+=n*n
            m+=1
        ans=[i*m+m*(m-1)*n//2 for i in range(1,n+1)]
        while candies:
            plus=min(candies,j+1+m*n)
            ans[j]+=plus
            candies-=plus
            j+=1
        return ans

a=Solution()
print(a.distributeCandies(10,3))
print(a.distributeCandies(7,4))