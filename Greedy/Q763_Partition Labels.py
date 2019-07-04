# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

# 思路: 用last记录最后位置，每遇到一个字母，更新当前右范围，如果走出了这个范围，那么前面的为一个part.

class Solution:
    def partitionLabels(self, S):
        curR,l,ans=0,0,[]
        last={char:i for i,char in enumerate(S)}
        for i in range(len(S)):
            if i>curR:
                ans.append(i-l)
                l=i
            curR=max(last[S[i]],curR)
        return ans+[len(S)-l]

a=Solution()
print(a.partitionLabels("ababcbacadefegdehijhklij"))
print(a.partitionLabels("abcdefgh"))
print(a.partitionLabels('a'))