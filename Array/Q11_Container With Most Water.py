class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        i = j = 0
        max = 0
        l = len(height)
        while i < l:
            while j < l:
                if (min(height[i], height[j]) * abs(i - j)) > max:
                    max = min(height[i], height[j]) * abs(i - j)
                j = j + 1
            i = i + 1
            j = 0
        return max


a = Solution()
print(a.maxArea([8, 1, 1, 1, 8]))