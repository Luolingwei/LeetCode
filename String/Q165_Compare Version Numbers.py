class Solution:
    '''
    treat the version number to real number
    1 001->1, by int(001) we can do this
    2 1.0.0.0->1 cut from tail, cut off all zeros

    finally, compare 2 versions by list directly
    '''
    def compareVersion(self, version1, version2):
        def helper(v):
            nums = list(map(int, v.split('.')))
            # we may get [1,1,0,0]
            idx = len(nums) - 1
            while idx >= 0 and nums[idx] == 0:
                idx -= 1
            return nums[:idx + 1]

        n1, n2 = helper(version1), helper(version2)
        if n1 > n2:
            return 1
        elif n1 < n2:
            return -1
        else:
            return 0

a=Solution()
print(a.compareVersion("0.1","1.1"))
print(a.compareVersion("1","0"))
print(a.compareVersion("1.01","1.001"))