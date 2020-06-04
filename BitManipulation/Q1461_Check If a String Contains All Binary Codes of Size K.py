
# set存储所有unique的二进制转化的数字, 判断是否等于2^k

class Solution:

    # one-line
    # def hasAllCodes(self, s: str, k: int) -> bool:
    #     return len(set(int(s[i:i+k]) for i in range(len(s)-k+1)))==2**k

    # sliding window
    def hasAllCodes(self, s: str, k: int) -> bool:
        codes = {int(s[:k])}
        N = len(s)
        window = ""
        for j in range(N):
            window += s[j]
            if j>=k:
                window = window[1:]
                codes.add(int(window))
        return len(codes)==2**k


a=Solution()
print(a.hasAllCodes("00110110",2))