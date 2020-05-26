
# 思路1: 将所有数根据mod3的余数分为0,1,2, 并从小到大排序
# 如果总和mod3=1, 去掉1个1或者2个2
# 如果总和mod3=2, 去掉1个2或者2个1
# 如果总和mod3=2, 全部包含
# 从大到小排序即可

# 思路2: dp记录mod为0,1,2的最大数
# 首先将数字从大到小排列
# 每拿到一个数字, 根据其mod余数更新0,1,2的最大值
# 每次都有2种选择, 选这个数字或者不选, 取max即可

class Solution:
    # def largestMultipleOfThree(self, digits):
    #     s = sum(digits)%3
    #     n0 = sorted([n for n in digits if n%3==0])
    #     n1 = sorted([n for n in digits if n%3==1])
    #     n2 = sorted([n for n in digits if n%3==2])
    #     if s==1:
    #         if n1: res = n1[1:]+n0+n2
    #         else: res = n2[2:]+n0
    #     elif s==2:
    #         if n2: res = n2[1:]+n0+n1
    #         else: res = n1[2:]+n0
    #     else:
    #         res = digits
    #     res = sorted(map(str,res),reverse=True)
    #     if not res: return ""
    #     return str(int(''.join(res)))


    def largestMultipleOfThree(self, digits):
        digits.sort(reverse=True)
        memo = [0, 0, 0]
        for d in digits:
            n = d % 3
            memo[n], memo[(n + 1) % 3], memo[(n + 2) % 3] = max(memo[n], memo[0] * 10 + d), \
                                                            max(memo[(n + 1) % 3], memo[1] * 10 + d if memo[1] else 0), \
                                                            max( memo[(n + 2) % 3], memo[2] * 10 + d if memo[2] else 0)
        if memo[0] == 0 and 0 not in digits: return ""
        return str(memo[0])


a=Solution()
print(a.largestMultipleOfThree([8,1,9]))
print(a.largestMultipleOfThree([8,6,7,1,0]))
print(a.largestMultipleOfThree([1]))
print(a.largestMultipleOfThree([0,0,0,0,0,0]))