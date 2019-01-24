class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans,dic=[],{}
        for num in nums1:
            dic[num]=dic.get(num,0)+1
        for num in nums2:
            if dic.get(num):
                ans.append(num)
                dic[num]-=1
        return ans

a=Solution()
print(a.intersect([4,9,5],[9,4,9,8,4]))
print(a.intersect([1,2,2,1],[2,2]))
print(a.intersect([1,2,1],[2,2]))