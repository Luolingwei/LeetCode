
# 思路: 先将整个string翻转过来, 然后对各个word进行翻转

class Solution:
    def reverseWords(self, s):
        def flip(i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i, j = i + 1, j - 1

        N = len(s)
        flip(0, N - 1)
        l = -1
        for r in range(N):
            if s[r] == " ":
                flip(l + 1, r - 1)
                l = r
        flip(l + 1, N - 1)
        return s


a=Solution()
print(a.reverseWords(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]))