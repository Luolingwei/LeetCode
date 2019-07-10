# Input: N = 10
# Output: 9

# Input: N = 1234
# Output: 1234

# Input: N = 332
# Output: 299

# 思路: 如果从前往后考虑的话，遇到下降的数字将前面的数字减1，后面置为9，这样可能导致前面的又变成下降数组，如332
# 从后往前考虑，每遇到下降的数对，将后面的置为9，前面的减1，然后继续往前搜索，是否有下降的数对
# 记录最后一个下降数对idx，将前面的数减1，并将idx后面的都置为9即可

class Solution:
    def monotoneIncreasingDigits(self, N):
        strs,idx=list(str(N)),-1
        for i in range(len(strs)-1,0,-1):
            if int(strs[i])<int(strs[i-1]):
                strs[i],idx='9',i
                strs[i-1]=str(int(strs[i-1])-1)
        return int(''.join(strs[:idx]+['9'*(len(strs)-idx)])) if idx!=-1 else N

a=Solution()
print(a.monotoneIncreasingDigits(3243))
print(a.monotoneIncreasingDigits(1234))
print(a.monotoneIncreasingDigits(10))
print(a.monotoneIncreasingDigits(332))
print(a.monotoneIncreasingDigits(342))