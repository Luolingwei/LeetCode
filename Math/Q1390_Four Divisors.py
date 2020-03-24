
# 思路: 对每一个num计算divisor，计算方法为从1扫到根号n，找到能整除的divisor
# 如果个数正好为4，把divisorSum加起来即可

class Solution:
    def sumFourDivisors(self, nums):
        def count(n):
            res = 0
            divisorSum = 0
            for i in range(1,int(n**0.5)+1):
                if int(n/i)*i==n:
                    res+=2 if n//i!=i else 1
                    divisorSum+=(n//i+i)
            return res,divisorSum
        ans = 0
        for n in nums:
            countd,sumd = count(n)
            if countd == 4:
                ans+=sumd
        return ans


