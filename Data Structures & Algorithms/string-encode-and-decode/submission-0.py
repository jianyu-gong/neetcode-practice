class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []

        for s in strs:
            result.append(f"{len(s)}#{s}")

        return ''.join(result)

    def decode(self, s: str) -> List[str]:

        result, i = [], 0

        while i < len(s):
            j = i + 1

            while s[j] != '#':
                j += 1

            length = int(s[i:j])

            string = s[j + 1: j + 1 + length]
            result.append(string)

            i = j + 1 + length

        return result