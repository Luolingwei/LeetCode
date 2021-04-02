
# 思路: 每一层下去更新截止当成的heights分布, 求这个heights能构成的最大矩形即可

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

    def maximalRectangle(self, matrix):
        m, n = len(matrix), len(matrix and matrix[0])
        if m==0 or n==0: return 0
        heights = [0]*n
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=="1": heights[j]+=1
                else: heights[j] = 0
            res = max(res, self.largestRectangleArea(heights[:]))
        return res


a=Solution()
print(a.maximalRectangle([
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]))
print(a.maximalRectangle(["1"]))