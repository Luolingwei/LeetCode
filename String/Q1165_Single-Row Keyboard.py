# Input: keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba"
# Output: 4
# Explanation: The index moves from 0 to 2 to write 'c' then to 1 to write 'b' then to 0 again to write 'a'.
# Total time = 2 + 1 + 1 = 4.

# 思路: 构造board中index和char的HashTable

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        dic={c:i for i,c in enumerate(keyboard)}
        return sum(abs(dic[word[i]]-dic[word[i-1]]) for i in range(1,len(word)))+dic[word[0]]

a=Solution()
print(a.calculateTime("abcdefghijklmnopqrstuvwxyz","cba"))
print(a.calculateTime("pqrstuvwxyzabcdefghijklmno","leetcode"))