# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

# 思路: 用字典存储同一个group的单词.

import collections
class Solution:
    # Solution 1 sort+hash O(knlogn)
    # def groupAnagrams(self, strs):
    #     memo=collections.defaultdict(list)
    #     for char in strs:
    #         key=''.join(sorted(char))
    #         memo[key].append(char)
    #     return list(memo.values())

    # Solution 1 hash O(kn)
    def groupAnagrams(self, strs):
        memo=collections.defaultdict(list)
        for word in strs:
            dic=[0]*26
            for c in word:
                dic[ord(c)-97]+=1
            memo[str(dic)].append(word)
        return list(memo.values())

a=Solution()
print(a.groupAnagrams(["eat", "tea", "tan", "eat", "nat", "tan"]))