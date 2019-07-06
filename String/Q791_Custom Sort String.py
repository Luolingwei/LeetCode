# Example :
# Input:
# S = "cba"
# T = "abcd"
# Output: "cbad"
# Explanation:
# "a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a".
# Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.

# 思路: 将T分为在S中和不在S中，在的话在Yes中记录个数，不在放进No，然后按S中的顺序构建新String (Yes+No)

import collections
class Solution:
    # Solution 1 memory 32 ms
    def customSortString(self, S, T):
        memo,Yes,No=set(S),collections.defaultdict(int),[]
        for char in T:
            if char in memo:
                Yes[char]+=1
            else:
                No.append(char)
        return ''.join([c*Yes[c] for c in S]+No)

    # Solution 2 Counter 44 ms
    # def customSortString(self, S, T):
    #     C,memo=collections.Counter(T),set(S)
    #     return ''.join([char*C[char] for char in S])+''.join(char*C[char] for char in C if char not in memo)

a=Solution()
print(a.customSortString('cbax','abcdbdddc'))