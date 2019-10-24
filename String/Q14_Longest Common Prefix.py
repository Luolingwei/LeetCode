class Solution:
    # solution1 Trie O(M*N) M为word的平均长度,N为word的个数
    # def longestCommonPrefix(self, strs):
    #     self.root={}
    #     def insert(word):
    #         node=self.root
    #         for c in word:
    #             node=node.setdefault(c,{})
    #         node['$']=None
    #     for word in strs:
    #         insert(word)
    #     node,ans=self.root,""
    #     while node and len(node)==1:
    #         char=list(node.keys())[0]
    #         ans+=char
    #         node=node[char]
    #     if ans and ans[-1]=='$': ans=ans[:-1]
    #     return ans

    # solution2 O(N)
    # def longestCommonPrefix(self, strs):
    #     if not strs: return ""
    #     s1,s2=min(strs),max(strs)
    #     for i,c in enumerate(s1):
    #         if s1[i]!=s2[i]:
    #             return s1[:i]
    #     return s1

    # Solution 3 fast if words are mixed and have no common prefix, do not need to check all word. return early, worst O(M*N)
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        common=strs[0]
        for word in strs[1:]:
            if not common: return ""
            if len(word)<len(common):
                common,word=word,common
            while word[:len(common)]!=common:
                common=common[:-1]
        return common

a=Solution()
print(a.longestCommonPrefix(["flower","flow","flight"]))
print(a.longestCommonPrefix(["dog","racecar","car"]))
print(a.longestCommonPrefix(["dog"]))
print(a.longestCommonPrefix(["",'b']))