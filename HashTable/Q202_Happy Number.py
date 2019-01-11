class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen=[]
        while n!=1:
            n=sum(int(char)**2 for char in str(n))
            if n in seen:
                return False
            else:
                seen.append(n)
        return True

a=Solution()
print(a.isHappy(19))