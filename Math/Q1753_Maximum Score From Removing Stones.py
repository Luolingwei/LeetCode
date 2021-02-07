class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        MAX, total = max(a,b,c), a+b+c
        gap = 2*MAX - total
        if gap>0: return (total - gap)//2
        return total//2


a=Solution()
print(a.maximumScore(2,4,6))
print(a.maximumScore(2,4,100))
print(a.maximumScore(4,4,6))
print(a.maximumScore(1,8,8))

