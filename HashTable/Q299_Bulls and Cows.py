import operator
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A=sum(map(operator.eq,guess,secret))
        both=sum(min(guess.count(char),secret.count(char))for char in set(guess))
        return str(A)+'A'+str(both-A)+'B'

a=Solution()
print(a.getHint("1807","7810"))
print(a.getHint("1123","0111"))