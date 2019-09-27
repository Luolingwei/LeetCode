
# 思路: 用"%.2f"让整除的结果后面加上两个0

class Solution:
    def Weekly(self,prices):
        curS=sum(prices[:7])
        ans=["%.2f"%(curS/7)]
        for i in range(7,len(prices)):
            curS+=prices[i]
            curS-=prices[i-7]
            ans.append("%.2f"%(curS/7))
        return ans

a=Solution()
print(a.Weekly([1,1,1,1,1,1,1,7,7,7,7,7,7,7]))