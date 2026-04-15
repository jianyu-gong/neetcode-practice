class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = {}

        for c in t:
            t_count[c] = t_count.get(c, 0) + 1

        need = len(t_count)
        res = ""
        # print(f'{t_count=}')

        for i in range(len(s)):
            cur = 0
            count = {}

            for j in range(i, len(s)):
                count[s[j]] = count.get(s[j], 0) + 1

                if count[s[j]] == t_count.get(s[j], 0):
                    cur += 1

                # print(f'{cur=}. {need=}')
                if cur == need:
                    substring = s[i:j+1]
                    # print(f'{substring=}')

                    if len(res) ==0 or len(substring) < len(res):
                        res = substring
                        # print(f'{res=}')

                    break
            # print(f'{count=}, {cur=}')
        return res        