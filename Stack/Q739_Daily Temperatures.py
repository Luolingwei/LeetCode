# T = [73, 74, 75, 71, 69, 72, 76, 73]
# Out= [1, 1, 4, 2, 1, 1, 0, 0]

# 思路: 用stack记录, 每来一个大数，pop出尾部数字的index, 更新ans

class Solution:
    def dailyTemperatures(self, T):
        stack,ans=[],[0]*len(T)
        for i,num in enumerate(T):
            while stack and num>T[stack[-1]]:
                idx=stack.pop()
                ans[idx]=i-idx
            stack.append(i)
        return ans

a=Solution()
print(a.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))