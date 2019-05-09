# Input: 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

# 思路: 1111^1010=0101 异或（^）:不同的位变成1，相同的变成0。
# 先生成 1111，即n-1，然后按位异或。

class Solution:
    def findComplement(self, num):
        n=1
        while n<=num:
            n<<=1
        return (n-1)^num