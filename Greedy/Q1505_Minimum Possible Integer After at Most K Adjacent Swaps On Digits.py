
# 思路: greedy, 每次试图将最小的数字移动到最前面, 从0-9搜索, 如果找到了可以移动的数字那么花费idx个swap进行移动
# k用完即返回num, 如果 k >= (L*L-1)/2, 可以reverse string, 任何组合都可以, 直接返回sorted即可

class Solution:
    def minInteger(self, num: str, k: int) -> str:
        if k==0: return num
        if k>=len(num)*(len(num)-1)/2:
            return ''.join(sorted(num))
        for d in range(10):
            idx = num.find(str(d))
            if 0<=idx<=k:
                return str(d)+self.minInteger(num[:idx]+num[idx+1:],k-idx)

a=Solution()
print(a.minInteger("3421",1))
print(a.minInteger("4321",1))