# Input: N = 2, K = 1
# Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]

# Input: N = 3, K = 7
# Output: [181,292,707,818,929]
# Explanation: Note that 070 is not a valid number, because it has leading zeroes.

# 思路1; dfs: 从第一位往后，直到len==N，注意K==0和N==1的特殊情况
# 思路2: bfs: 每次加上一位，一共加N-1次，初始为[0,1,2,3,4,5,6,7,8,9]

class Solution:
    # Solution 1 dfs 56 ms
    # def numsSameConsecDiff(self, N, K):
    #     if N==1: return list(range(10))
    #     ans=[]
    #     def dfs(i,path):
    #         if len(path)==N:
    #             ans.append(path)
    #             return
    #         for j in {i+K,i-K}:
    #             if 0<=j<10:
    #                 dfs(j,path+[j])
    #     for i in range(1,10):
    #         dfs(i,[i])
    #     return [int(''.join(map(str,path))) for path in ans]

    # Solution 2 bfs 48 ms
    def numsSameConsecDiff(self, N, K):
        queue=[i for i in range(10)]
        for _ in range(N-1):
            queue=[i*10+j for i in queue for j in {i%10+K,i%10-K} if i and 0<=j<10]
        return queue

a=Solution()
print(a.numsSameConsecDiff(2,1))
print(a.numsSameConsecDiff(3,7))
print(a.numsSameConsecDiff(2,0))
print(a.numsSameConsecDiff(1,1))