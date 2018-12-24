class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left=longest=0
        dic={}
        for i in range(len(s)):
            if s[i] not in dic or left>dic[s[i]]:
                dic[s[i]]=i
                longest=max(longest,i-left+1)
            else:
                left = dic[s[i]]+1
                dic[s[i]] = i
        return longest

a=Solution()
print(a.lengthOfLongestSubstring("tmmzuxt"))
