
# 思路: 最开始有a,e,i,o,u5个字母
# 每一轮, a可以变成a,e,i,o,u结尾的字符串, e可以变成e,i,o,u, i可以变成i,o,u....
# memo[1,2,3,4,5]表示以当前轮以a,e,i,o,u结尾的字符串个数
# 所以new_memo[1] = memo[1], new_memo[2] = memo[1] + memo[2]...
# 对memo每轮进行累加即可, 最后取sum

class Solution:
    def countVowelStrings(self, n: int) -> int:
        memo = [0] + [1]*5
        for _ in range(n-1):
            for i in range(1,6):
                memo[i] += memo[i-1]
        return sum(memo)


a = Solution()
print(a.countVowelStrings(1))
print(a.countVowelStrings(2))
print(a.countVowelStrings(33))