class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return '/n'
        return '/n'.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == '/n':
            return []
        return s.split('/n')
