class Solution:
    #solution1 dfs
    # def triangle(self, path):
    #     if path[0] + path[1] > path[2] and abs(path[0] - path[1]) < path[2]:
    #         return True
    #     else:
    #         return False
    # def dfs(self, nums, start, path, res):
    #     if len(path) == 3:
    #         if self.triangle(path):
    #             res[0] += 1
    #             return
    #         else:
    #             return
    #     for i in range(start, len(nums)):
    #         self.dfs(nums, i + 1, path + [nums[i]], res)
    # def triangleNumber(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     res = [0]
    #     self.dfs(nums, 0, [], res)
    #     return res[0]

    #solution2
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count=0
        for i3 in range(len(nums)-1,1,-1):
            left,right=0,i3-1
            while left<right:
                if nums[left]+nums[right]>nums[i3]:
                    count+=right-left
                    right-=1
                else:
                    left+=1
        return count


a=Solution()
print(a.triangleNumber([2,2,3,4]))
print(a.triangleNumber([2,2,3,4]))