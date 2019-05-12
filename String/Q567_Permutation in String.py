# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").

# 思路: 移动窗口法，将s1中的字符串表示target（[0,26]的ord表示，方便进行字符串相等的对比），然后在s1中以len(s1)作为窗口长度滑动，更新窗口，check窗口是否与target相等.

class Solution:
    def checkInclusion(self, s1, s2):
        A=[ord(char)-ord('a') for char in s1]
        B=[ord(char)-ord('a') for char in s2]
        window,target=[0]*26,[0]*26
        for n in A:
            target[n]+=1
        for i in range(len(B)):
            window[B[i]]+=1
            if i>=len(s1):
                window[B[i-len(s1)]]-=1
            if window==target:
                return True
        return False

a=Solution()
print(a.checkInclusion('ab','eidbaooo'))
print(a.checkInclusion('ab','eidboaoo'))
print(a.checkInclusion('abc','bbbca'))