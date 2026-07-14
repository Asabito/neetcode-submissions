class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash, t_hash = {}, {}
        for value in s:
            s_hash[value] = s_hash.get(value, 0) + 1
        for value in t:
            t_hash[value] = t_hash.get(value, 0) + 1
        return s_hash == t_hash
            