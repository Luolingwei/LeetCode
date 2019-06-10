# Input: "ecbacba"
# Output: "eacb"

# 思路:每次来新元素才有可能改变现有的排序,如bcd 来了一个b（已存在）,如果把b提前是等效的，原来的顺序已经排好(b后面比b大，否则会之前就替换掉了)
# # 所以比较新元素与前一个元素的大小，如果比尾部元素小，而且尾部元素在后面还有(idx储存元素最后出现的位置)，则将尾部元素出栈，达到c a 变a c的效果

class Solution:
    def smallestSubsequence(self, s):
        last={char:i for i,char in enumerate(s)}
        ans=''
        for i,char in enumerate(s):
            if char not in ans:
                while char<ans[-1:] and last[ans[-1:]]>i:
                    ans=ans[:-1]
                ans+=char
        return ans


a=Solution()
print(a.smallestSubsequence('ecbacba'))
print(a.smallestSubsequence('cabac'))
print(a.smallestSubsequence('bcabc'))
print(a.smallestSubsequence('cbacdcbc'))
print(a.smallestSubsequence('bcab'))
print(a.smallestSubsequence('bababa'))