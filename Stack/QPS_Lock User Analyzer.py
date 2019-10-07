class Solution:
    def analyze(self,strings):
        stack,memo=[],set()
        for i,s in enumerate(strings):
            commond,number=s.split()
            if commond=="ACQUIRE":
                if number in memo:
                    return i+1
                else:
                    memo.add(number)
                    stack.append(number)
            else:
                if not stack:
                    return i+1
                number2=stack.pop()
                memo.remove(number2)
                if number!=number2:
                    return i+1
        return len(strings)+1 if stack else 0

a=Solution()
print(a.analyze([]))
print(a.analyze(["ACQUIRE 364"]))
print(a.analyze(["RELEASE 364"]))
print(a.analyze(["ACQUIRE 364","ACQUIRE 84","RELEASE 84","RELEASE 364"]))
print(a.analyze(["ACQUIRE 364","ACQUIRE 84","RELEASE 364","RELEASE 84"]))
print(a.analyze(["ACQUIRE 123","ACQUIRE 364","ACQUIRE 84", "RELEASE 84","RELEASE 364","ACQUIRE 456"]))
print(a.analyze(["ACQUIRE 123","ACQUIRE 364","ACQUIRE 84", "RELEASE 84","RELEASE 364","ACQUIRE 789","RELEASE 456","RELEASE 123"]))