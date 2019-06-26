# Example :
# Input:
# S = "abcde"
# words = ["a", "bb", "acd", "ace"]
# Output: 3
# Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".

# 思路: 用iter进行subsequence的check，用set()记录已经check过的字符串，避免重复check.

class Solution:
    def numMatchingSubseq(self, S, words):
        ans,right,false=0,set(),set()
        for word in words:
            if word in right:
                ans+=1
                continue
            elif word in false:
                continue
            it=iter(S)
            if all(char in it for char in word):
                ans+=1
                right.add(word)
            else:
                false.add(word)
        return ans

a=Solution()
print(a.numMatchingSubseq("abcde",["a", "bb", "acd", "ace"]))