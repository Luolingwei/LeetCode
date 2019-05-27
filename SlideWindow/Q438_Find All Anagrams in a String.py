import collections
class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        p_count=collections.Counter(p)
        window=collections.Counter(s[:len(p)])
        ans=[]
        for i in range(len(s)-len(p)+1):
            if p_count==window:
                ans.append(i)
            if i==len(s)-len(p):
                break
            window[s[i]]-=1
            if window[s[i]]==0:
                del window[s[i]]
            window[s[i+len(p)]]+=1
        return ans

a=Solution()
print(a.findAnagrams("cbaebabacd","abc"))