class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[[]]
        for number in nums:
            for element in list(ans):
                ans.append([number]+element)
        return ans

a=Solution()
print(a.subsets([1,2,3]))