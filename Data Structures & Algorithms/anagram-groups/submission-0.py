class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = {}

        for s in strs:
            sorted_string = ''.join(sorted(s))

            if sorted_string in hash_table:
                hash_table[sorted_string].append(s)

            else:
                hash_table[sorted_string] = [s]

        result = []
        for h in hash_table:
            result.append(hash_table[h])

        return result

