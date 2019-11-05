
# 根据开头分为letters和digits, letters按照后面的字符串排序，最后合并起来

class Solution:
    def reorderLogFiles(self, logs):
        letters,digits=[],[]
        for s in logs:
            strs=s.split()
            if strs[1][0].isalpha():
                letters.append((s[len(strs[0])+1:],s))
            else:
                digits.append(s)
        letters=[s for _,s in sorted(letters)]
        return letters+digits