
# 思路: 对于某个s, 考虑最后一个加入的数字, 其长度最多为k的长度(因为k<=10^9,所以长度最多为10)
# 从j往前数L个为i, 如果i到j组成的数字符合条件, dp[j]+=dp[i-1]
# 返回dp[-1]即可

class Solution:
    # O(10n)
    def numberOfArrays(self, s: str, k: int) -> int:
        N, L = len(s), len(str(k))
        mod = 10**9+7
        dp = [0]*N
        for j in range(N):
            for i in range(j,max(-1,j-L-1),-1):
                num = s[i:j+1]
                if num[0]!='0' and int(num)<=k:
                    dp[j]=(dp[j]+(dp[i-1] if i>0 else 1))%mod
        return dp[-1]%mod


a=Solution()
print(a.numberOfArrays("1000",10000))
print(a.numberOfArrays("1000",10))
print(a.numberOfArrays("1317",2000))
print(a.numberOfArrays("2020",30))
print(a.numberOfArrays("1234567890",90))