
# 思路: 考虑一个l和r, 要想增大容纳水的体积, 移动高的那个是不行的, 因为最高高度限制了, 宽度变短, 只有可能变小
# 所以每次移动短的边, 使水的体积尽可能增大

class Solution:
    def maxArea(self, height):
        res = 0
        i,j = 0, len(height)-1
        while i<j:
            res = max(res,(j-i)*min(height[j],height[i]))
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return res

a = Solution()
print(a.maxArea([1,8,6,2,5,4,8,3,7]))
print(a.maxArea([8, 1, 1, 1, 8]))