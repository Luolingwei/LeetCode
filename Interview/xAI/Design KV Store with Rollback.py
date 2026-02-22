from typing import List, Optional

class KeyValueStore:
    def __init__(self, ):
        self.memo = {}

    def set(self, key: str, value: str) -> None:
        self.memo[key] = value

    def get(self, key: str) -> str:
        return self.memo.get(key, "Not Exist")

    def unset(self, key: str) -> None:
        self.memo.pop(key, None)
