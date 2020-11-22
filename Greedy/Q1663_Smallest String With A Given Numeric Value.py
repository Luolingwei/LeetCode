
# 思路: 尽量先排a, 一直到剩下的k > 剩下全部排z的能接受的分数

# 思路2: 先全部填上a, 最多能填 n-1//25个z, 剩下的全部给中间的single_char

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = ""
        while k>0:
            left = 26*(n-1)
            if k-1<left:
                res += "a"
                n-=1
                k-=1
            else:
                res += chr(97+(k-1)-left)
                n-=1
                break
        return res+'z'*n


    def getSmallestString2(self, n: int, k: int) -> str:
        res = ""
        k-=n
        z_num, single_num = divmod(k,25)
        res += (n-1-z_num)*"a"
        res += chr(97+single_num)
        res += z_num*"z"
        return res


a=Solution()
print(a.getSmallestString(3,27))
print(a.getSmallestString(5,73))
print(a.getSmallestString2(3,27))
print(a.getSmallestString2(5,73))