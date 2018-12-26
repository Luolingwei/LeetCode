class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic={}
        ans=[]
        for char in strs:
            var=''.join(sorted(char))
            if var not in dic.keys():
                dic[var]=[char]
            else:
                dic[var].append(char)
        for key, value in dic.items():
            ans.append(value)
        return ans

a=Solution()
print(a.groupAnagrams(["eat", "tea", "tan", "eat", "nat", "tan"]))