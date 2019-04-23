# Input: "bcabc"
# Output: "abc"

# Input: "cbacdcbc"
# Output: "acdb"

# 思路: 每次来新元素才有可能改变现有的排序,如bcd 来了一个b（已存在）,如果把b提前是等效的，原来的顺序已经排好
# 所以比较新元素与前一个元素的大小，如果比尾部元素小，而且尾部元素在后面还有(idx储存元素最后出现的位置)，则将尾部元素出栈，达到c a 变a c的效果

class Solution:
    def removeDuplicateLetters(self, s):
        idx={char:index for index,char in enumerate(s)}
        result=''
        for index, char in enumerate(s):
            if char not in result:
                while char<result[-1:] and idx[result[-1]]>index:
                    result=result[:-1]
                result+=char
        return result


a=Solution()
print(a.removeDuplicateLetters('bcabc'))
print(a.removeDuplicateLetters('cbacdcbc'))
print(a.removeDuplicateLetters('bcab'))
print(a.removeDuplicateLetters('bababa'))