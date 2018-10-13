class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        self.max = 0
        l = len(height)
        i = 0
        j=l-1

        while i!=j:
            if self.computeArea(height,i,j)>self.max:
                self.max=self.computeArea(height,i,j)
            if height[i]>height[j]:
                j=j-1
            else:
                i=i+1
        return self.max

    def computeArea(self,height,i,j):
        return min(height[i], height[j]) * abs(i - j)

a = Solution()
print(a.maxArea([8, 1, 1, 1, 8]))