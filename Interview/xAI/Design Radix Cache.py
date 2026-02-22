from typing import List, Optional

class RadixCache:
    def __init__(self, ):
        self.root = {}

    def insert(self, sequence: List[int]) -> None:
        node = self.root
        for n in sequence:
            if n not in node: node[n] = {}
            node = node[n]
        node['$'] = None

    def exists(self, sequence: List[int]) -> bool:
        node = self.root
        for n in sequence:
            if n in node:
                node = node[n]
            else:
                return False
        return '$' in node
