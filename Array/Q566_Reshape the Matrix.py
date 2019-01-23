class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        r_pre,c_pre=len(nums),len(nums[0])
        if r_pre*c_pre != r*c or r_pre==r and c_pre==c:
            return nums
        elements=[j for i in range(r_pre) for j in nums[i]]
        return [elements[i:i+c] for i in range(0,r*c,c)]

a=Solution()
print(a.matrixReshape([[1,2],[3,4]],1,4))
print(a.matrixReshape([[1,2],[3,4],[5,6]],2,3))