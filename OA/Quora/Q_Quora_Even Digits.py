class Solution:
    def count(self,A):
        def check(n):
            while n:
                n,reminder=divmod(n,10)
                if reminder%2==0: return True
            return False
        return sum(check(i) for i in A)

a=Solution()
print(a.count([12, 3, 5, 3456]))