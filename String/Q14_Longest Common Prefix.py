class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #solution1
        # if not strs: return ""
        # common=strs[0]
        # for str in strs[1:]:
        #     idx=0
        #     while idx<min(len(common),len(str)):
        #         if common[idx]==str[idx]:
        #             idx+=1
        #         else:
        #             break
        #     if idx==0:
        #         return ""
        #     else:
        #         common=common[:idx]
        # return common

        #solution2
        if not strs: return ''
        s1 = min(strs)
        s2 = max(strs)
        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]
        return s1

a=Solution()
print(a.longestCommonPrefix(["flower","flow","flight"]))
print(a.longestCommonPrefix(["dog","racecar","car"]))
print(a.longestCommonPrefix(["dog"]))
print(a.longestCommonPrefix([]))