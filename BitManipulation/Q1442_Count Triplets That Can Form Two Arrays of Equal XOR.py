
# 思路1: dp, 先计算preS, 然后找所有的index组合, O(N^3)
# 思路2: a=b即, a^b==0, 即arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1] ^ arr[j]...arr[k]=0，找出所有xor为0的数组片段即可, 随意分割即为2个相等的段, O(N^2)
# 思路3: 问题已经简化成给定一个数组, 算所有相等元素之间的距离之和, 每次遇到一个出现过的数字, 增加的距离为 之前出现的次数*(i-1)-(之前所有的idx之和), 因为新idx与preidx的距离 = 新idx - 旧idx


class Solution:
    # Solution 1 O(N^3)
    # def countTriplets(self, arr) -> int:
    #     N = len(arr)
    #     dp = [arr[0]] + [0]*(N-1)
    #     ans = 0
    #     for i in range(1,N):
    #         dp[i] = arr[i]^dp[i-1]
    #     for i in range(N):
    #         for j in range(i+1,N):
    #             for k in range(j,N):
    #                 a = dp[j-1]^dp[i-1] if i>=1 else dp[j-1]
    #                 b = dp[k]^dp[j-1]
    #                 if a==b: ans += 1
    #     return ans

    # Solution 2 O(N^2)
    # def countTriplets(self, arr) -> int:
    #     arr = [0] + arr
    #     N = len(arr)
    #     ans = 0
    #     for i in range(1, N):
    #         arr[i] = arr[i] ^ arr[i - 1]
    #     for i in range(N):
    #         for j in range(i + 1, N):
    #             if arr[j] == arr[i]:
    #                 ans += j - i - 1
    #     return ans

    # Solution 3 O(N)
    def countTriplets(self, arr) -> int:
        ans, curbit = 0 , 0
        memo = {0: [-1,1]} # total idx, count idx
        for i,n in enumerate(arr):
            curbit^=n
            if curbit in memo:
                pretotal, precount = memo[curbit]
                ans += precount*(i-1)-pretotal
                memo[curbit] = [pretotal+i,precount+1]
            else:
                memo[curbit] = [i,1]
        return ans


a=Solution()
print(a.countTriplets([2,3]))
print(a.countTriplets([2,3,1,6,7]))
print(a.countTriplets([1,1,1,1,1]))