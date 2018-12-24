class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack=[]
        ans=0
        for height in heights+[0]:
            count=0
            while stack and height<stack[-1][0]:
                y,ycount=stack.pop()
                count+=ycount
                ans=max(ans,count*y)
            stack+=[[height,count+1]]
        return ans

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix==[]:
            return 0
        max_area=0
        temp=[0 for _ in range(len(matrix[0]))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                temp[j]=(0 if matrix[i][j]=='0' else temp[j]+1)
            max_area=max(max_area,self.largestRectangleArea(temp))
        return max_area

a=Solution()
print(a.maximalRectangle([
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]))
print(a.maximalRectangle(["1"]))




