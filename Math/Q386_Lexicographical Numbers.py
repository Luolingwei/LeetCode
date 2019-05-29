
# 思路: 1: 将位数用0补齐，然后进行比较 2. 转为str直接比较ASCII码

class Solution:
    # def lexicalOrder(self, n):
    #     l=len(str(n))
    #     return sorted([i for i in range(1,n+1)], key=lambda num:num*10**(l-len(str(num))))

    def lexicalOrder(self, n):
        return sorted(range(1,n+1),key=str)

a=Solution()
print(a.lexicalOrder(11))