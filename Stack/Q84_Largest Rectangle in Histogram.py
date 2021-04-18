
# 思路: 单调栈, 对于一个新h, 如果他小于栈顶的h,那么以栈顶为最小高度的长方形右边界确定, 左边界为栈顶元素坐标
# res = max(res, h*r-l-1)

class Solution:
    def largestRectangleArea(self, heights) -> int:
        heights += [0]
        stack=[]
        res = 0
        for i in range(len(heights)):
            while stack and heights[i]<heights[stack[-1]]:
                h = heights[stack.pop()]
                r = i
                l = stack[-1] if stack else -1
                res = max(res, h*(r-l-1))
            stack.append(i)
        return res

a=Solution()
print(a.largestRectangleArea([2,1,5,6,2,3]))
print(a.largestRectangleArea([2,4]))