
# 思路: 记录每个部分的字母个数并进行对比，可以用stack也可以用两个pointers记录长度

class Solution:
    # Solution 1 stack
    # def expressiveWords(self, S, words):
    #     def check(word):
    #         i, stack2 = 0, []
    #         for c2 in word + '$':
    #             if not stack2:
    #                 stack2.append([c2, 1])
    #             elif c2 != stack2[-1][0]:
    #                 n1, n2, char1, char2 = stack[i][1], stack2[-1][1], stack[i][0], stack2[-1][0]
    #                 if char1 != char2 or n2 > n1 or (n1 < 3 and n1 != n2):
    #                     return False
    #                 stack2.append([c2, 1])
    #                 i += 1
    #             else:
    #                 stack2[-1][1] += 1
    #         return i == len(stack)
    #
    #     stack, ans = [], 0
    #     for c in S:
    #         if not stack or c != stack[-1][0]:
    #             stack.append([c, 1])
    #         else:
    #             stack[-1][1] += 1
    #     return sum(check(word) for word in words)

    # Solution 2 Pointers
    def expressiveWords(self, S, words):
        def check(word):
            i,j,i2,j2,m,n=0,0,0,0,len(S),len(word)
            while i<m and j<n:
                if S[i]!=word[j]: return False
                while i<m and S[i]==S[i2]: i+=1
                while j<n and word[j]==word[j2]: j+=1
                if j-j2>i-i2 or (i-i2<3 and j-j2!=i-i2):
                    return False
                i2,j2=i,j
            return i==m and j==n
        return sum(check(word) for word in words)

a=Solution()
print(a.expressiveWords("heeellooo",["hello", "hi", "helo"]))
print(a.expressiveWords("abcd",["abc"]))