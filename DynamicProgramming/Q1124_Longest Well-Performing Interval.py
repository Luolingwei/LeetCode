# Input: hours = [9,9,6,0,6,6,9]
# Output: 3
# Explanation: The longest well-performing interval is [9,9,6].

# 思路: 类似dp,计算以每个数字结尾的最长interval
# 每来一个数字，如果score>0，那么ans=i，如果score<=0: 那么需要在前面寻找score-1的最靠前位置，ans=max(ans,i-idx[score-1])
# 只需要check score-1的原因是此题的socre是以1,-1为步长变化的，-9一定在-7之后出现，所以score-2,score-3的位置一定更靠后.

class Solution:
    def longestWPI(self, hours):
        s,ans,memo=0,0,{}
        for i,h in enumerate(hours):
            s+=1 if h>8 else -1
            memo.setdefault(s,i)
            if s>0:
                ans=i+1
            elif s-1 in memo:
                ans=max(ans,i-memo[s-1])
        return ans

a=Solution()
print(a.longestWPI([8,8,8,8,9,9,9,9,9]))
print(a.longestWPI([9,9,6,0,6,6,9]))
print(a.longestWPI([6,6,9]))