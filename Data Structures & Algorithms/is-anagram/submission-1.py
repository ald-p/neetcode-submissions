class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {} # {'c': 2, 'a': 2}
        t_map = {}

        for s_char in s:
            if s_char in s_map:
                s_map[s_char] += 1
            else:
                s_map[s_char] = 1

        for t_char in t:
            if t_char in t_map:
                t_map[t_char] += 1
            else:
                t_map[t_char] = 1

        return s_map == t_map




        