class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        memory =[[0]*i for i in range(1,len(triangle)+1)]
        for i in range(len(triangle)):
            for j in range(len(triangle[i])):
                # 边缘像素
                if i==0:
                    memory[i][j]=triangle[i][j]
                elif j==0:
                    memory[i][j]=memory[i-1][j]+triangle[i][j]
                elif j==len(triangle[i])-1:
                    memory[i][j]=memory[i-1][j-1]+triangle[i][j]
                #非边缘像素
                else:
                    memory[i][j]=min(memory[i-1][j-1],memory[i-1][j])+triangle[i][j]
        return min(memory[-1])

a=Solution()
print(a.minimumTotal([
     [-1],
    [2,3],
   [1,-1,-3]
]))