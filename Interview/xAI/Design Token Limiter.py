from typing import List, Optional

class Policy:
    def __init__(self, capacity, refillAmount, refillInterval, remainTokens, refillTime):
        self.capacity = int(capacity)
        self.refillAmount = int(refillAmount)
        self.refillInterval = int(refillInterval)
        self.remainTokens = remainTokens
        self.refillTime = refillTime

class TokenLimiter:
    def __init__(self, policyInput: List[List[str]]):
        self.policies = {}
        self.refillAmount = {}
        self.refillInterval = {}
        for userName, capacity, refillAmount, refillInterval in policyInput:
            self.policies[userName] = Policy(capacity, refillAmount, refillInterval, 0, 0)

    def allowRequest(self, userName: str, tokens: int, timestamp: int) -> bool:
        if userName not in self.policies.keys(): return False

        policy = self.policies[userName]
        print(policy)

        # If it's user's first request, fill the buck in full.
        if policy.refillTime == 0:
            policy.refillTime = timestamp
            policy.remainTokens = policy.capacity

        # Refill tokens
        timeGap = timestamp - policy.refillTime
        if timeGap >= policy.refillInterval:
            numIntervals = timeGap // policy.refillInterval 
            addedTokens = numIntervals * policy.refillAmount
            policy.remainTokens = min(policy.capacity, policy.remainTokens + addedTokens)
            policy.refillTime += numIntervals * policy.refillInterval
        
        # Caculate the token usage
        if policy.remainTokens >= tokens:
            policy.remainTokens -= tokens
            return True
        else:
            return False
