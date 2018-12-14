class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l=len(height)
        left_max=right_max=water=0
        left=0
        right=l-1
        while left<right:
            if height[left]<height[right]:
                if height[left]>left_max:
                    left_max=height[left]
                else:
                    water+=left_max-height[left]
                left+=1
            else:
                if height[right]>right_max:
                    right_max=height[right]
                else:
                    water+=right_max-height[right]
                right-=1
        return water

a = Solution()
print(a.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(a.trap([0,1,0,1,0,2,0,1,0,1,0]))
print(a.trap([5,4,1,2]))



