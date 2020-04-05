
# 思路1: 直接将数字用二进制表示进行操作
# 思路2: 对string进行操作, 从后往前扫描, 除以2为往右移1位, 加1为在尾部加1, 如果尾部为1那么为奇数，否则为偶数
# 如果当前数字s[i]+carry=0, 需要1步操作(除以2), carry置为0
# 如果当前数字s[i]+carry=1, 需要2步操作(加1, 除以2), carry置为1
# 如果当前数字s[i]+carry=2, 需要1步操作(除以2), carry置为1
# 扫描到头部时停止，如果carry=1, 则还需要1步(除以2)完成

class Solution:
    # def numSteps(self, s: str):
    #     n = int(s,2)
    #     ans = 0
    #     while n!=1:
    #         n = n+1 if n&1 else n>>1
    #         ans += 1
    #     return ans

    def numSteps(self, s: str):
        carry = 0
        ans = 0
        i = len(s)-1
        while i>0:
            curN = carry + int(s[i])
            if curN == 0:
                ans += 1
                carry = 0
            elif curN == 1:
                ans += 2
                carry = 1
            else:
                ans += 1
                carry = 1
            i-=1
        return ans + carry

a=Solution()
print(a.numSteps("1101"))
print(a.numSteps("10"))
print(a.numSteps("1"))