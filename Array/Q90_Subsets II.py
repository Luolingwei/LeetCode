class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        for number in nums:
            for element in list(ans):
                addone=sorted([number] + element)
                if addone not in ans:
                    ans.append(addone)
        return sorted(ans)

a = Solution()
print(a.subsetsWithDup([4,4,4,1,4]))