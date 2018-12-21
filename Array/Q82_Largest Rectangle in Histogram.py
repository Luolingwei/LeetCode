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

a=Solution()
print(a.largestRectangleArea([2,1,5,6,2,3]))