class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}

        for c in s:
            if c not in hash_map:
                hash_map[c] = 1
            else:
                hash_map[c] += 1

        for c in t:
            if c not in hash_map:
                return False

            else:
                hash_map[c] = hash_map[c] - 1

        # print(hash_map)

        for k in hash_map:
            if hash_map[k] != 0:
                return False

        return True