# Input: "abab"
# Output: True
# Explanation: It's the substring "ab" twice.
#
# Input: "aba"
# Output: False
#
# Input: "abcabcabcabc"
# Output: True
# Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

class Solution:
    def repeatedSubstringPattern(self, s):
        length=len(s)
        for sublength in range(1,length//2+1):
            if length%sublength==0:
                if s[:sublength]*(length//sublength)==s:
                    return True
        return False

a=Solution()
print(a.repeatedSubstringPattern('abab'))
print(a.repeatedSubstringPattern('aba'))
print(a.repeatedSubstringPattern('abcabcabcabc'))
print(a.repeatedSubstringPattern('aa'))